#!/usr/bin/python
# -*- OVS linear topo, 5 hosts, 5 switches -*-
import os

def create_namespace(name):
    print(f"Creating namespace {name}")
    os.system(f"ip netns add {name}")

def create_ovs_bridge(name):
    print(f"Creating OVS bridge {name}")
    os.system(f"ovs-vsctl add-br {name}")
    os.system(f"ovs-vsctl set bridge {name} protocols=OpenFlow10,OpenFlow12,OpenFlow13")

def attach_namespace_to_ovs(namespace_name, bridge_name, veth_name, peer_name, ofport, ip_address):
    print(f"Attaching namespace {namespace_name} to OVS {bridge_name}")
    os.system(f"ip link add {veth_name} type veth peer name {peer_name}")
    os.system(f"ip link set {veth_name} netns {namespace_name}")
    os.system(f"ovs-vsctl add-port {bridge_name} {peer_name} -- set Interface {peer_name} ofport_request={ofport}")
    os.system(f"ip netns exec {namespace_name} ip addr add {ip_address}/24 dev {veth_name}")
    os.system(f"ip netns exec {namespace_name} ip link set dev {veth_name} up")
    os.system(f"ip link set {peer_name} up")

def attach_ovs_to_ovs(bridge1_name, bridge2_name, veth1_name, veth2_name, ofport):
    print(f"Attaching OVS {bridge1_name} to OVS {bridge2_name}")
    os.system(f"ip link add {veth1_name} type veth peer name {veth2_name}")
    os.system(f"ip link set {veth1_name} up")
    os.system(f"ip link set {veth2_name} up")
    os.system(f"ovs-vsctl add-port {bridge1_name} {veth1_name} -- set Interface {veth1_name} ofport_request={ofport}")
    os.system(f"ovs-vsctl add-port {bridge2_name} {veth2_name} -- set Interface {veth2_name} ofport_request={ofport}")

def attach_ovs_to_sdn(bridge_name, controller_ip):
    print(f"Attaching OVS bridge {bridge_name} to SDN controller")
    os.system(f"ovs-vsctl set-controller {bridge_name} tcp:{controller_ip}:6653")

if __name__ == '__main__':
    
    #create namespaces
    for i in range(1,6):
        create_namespace(f"ns{i}")

    # Create OVS bridges
    for i in range(1,6):
        create_ovs_bridge(f"br{i}")
        attach_ovs_to_sdn(f"br{i}", "172.0.0.1")


    # Attach namespaces to OVS bridges
    for i in range(1,6):
        if i == 1:
            #attach first namespace to first switch
            attach_namespace_to_ovs(f"ns{i}", f"br{i}", f"veth{i}-br", f"veth-br{i}", 1, f"10.0.{i}.2")
        elif i == 5:
            #attach last namespace to last switch
            attach_namespace_to_ovs(f"ns{i}", f"br{i}", f"veth{i}-br", f"veth-br{i}", 1, f"10.0.{i}.2")
            #attach last switch to previous switch
            attach_ovs_to_ovs(f"br{i-1}", f"br{i}", f"veth{i-1}-br", f"veth{i}-br", 1)
        else:
            #attach middle namespaces to current and next switches
            attach_namespace_to_ovs(f"ns{i}", f"br{i}", f"veth{i}-br", f"veth-br{i}", 1, f"10.0.{i}.2")
            attach_namespace_to_ovs(f"ns{i}", f"br{i+1}", f"veth{i}-br", f"veth-br{i+1}", 1, f"10.0.{i+1}.2")
            #attach current switch to previous switch
            attach_ovs_to_ovs(f"br{i-1}", f"br{i}", f"veth{i-1}-br", f"veth{i}-br", 1)

   
    
