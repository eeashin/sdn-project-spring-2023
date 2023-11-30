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


    Creating namespace ns1
Creating namespace ns2
Creating namespace ns3
Creating namespace ns4
Creating namespace ns5
Creating OVS bridge br1
Attaching OVS bridge br1 to SDN controller
Creating OVS bridge br2
Attaching OVS bridge br2 to SDN controller
Creating OVS bridge br3
Attaching OVS bridge br3 to SDN controller
Creating OVS bridge br4
Attaching OVS bridge br4 to SDN controller
Creating OVS bridge br5
Attaching OVS bridge br5 to SDN controller
Attaching namespace ns1 to OVS br1
Attaching namespace ns2 to OVS br2
Attaching namespace ns2 to OVS br3
RTNETLINK answers: File exists
Attaching OVS br1 to OVS br2
RTNETLINK answers: File exists
Cannot find device "veth1-br"
ovs-vsctl: Error detected while setting up 'veth1-br': could not open network device veth1-br (No such device).  See ovs-vswitchd log for details.
ovs-vsctl: The default log directory is "/var/log/openvswitch".
Attaching namespace ns3 to OVS br3
RTNETLINK answers: File exists
Cannot find device "veth3-br"
ovs-vsctl: cannot create a port named veth-br3 because a port named veth-br3 already exists on bridge br3
Cannot find device "veth3-br"
Cannot find device "veth3-br"
Attaching namespace ns3 to OVS br4
Attaching OVS br2 to OVS br3
RTNETLINK answers: File exists
Cannot find device "veth3-br"
ovs-vsctl: cannot create a port named veth2-br because a port named veth2-br already exists on bridge br2
ovs-vsctl: Error detected while setting up 'veth3-br': could not open network device veth3-br (No such device).  See ovs-vswitchd log for details.
ovs-vsctl: The default log directory is "/var/log/openvswitch".
Attaching namespace ns4 to OVS br4
RTNETLINK answers: File exists
Cannot find device "veth4-br"
ovs-vsctl: cannot create a port named veth-br4 because a port named veth-br4 already exists on bridge br4
Cannot find device "veth4-br"
Cannot find device "veth4-br"
Attaching namespace ns4 to OVS br5
Attaching OVS br3 to OVS br4
ovs-vsctl: cannot create a port named veth3-br because a port named veth3-br already exists on bridge br3
Attaching namespace ns5 to OVS br5
RTNETLINK answers: File exists
Cannot find device "veth5-br"
ovs-vsctl: cannot create a port named veth-br5 because a port named veth-br5 already exists on bridge br5
Cannot find device "veth5-br"
Cannot find device "veth5-br"
Attaching OVS br4 to OVS br5
RTNETLINK answers: File exists
Cannot find device "veth5-br"
ovs-vsctl: cannot create a port named veth4-br because a port named veth4-br already exists on bridge br4
ovs-vsctl: Error detected while setting up 'veth5-br': could not open network device veth5-br (No such device).  See ovs-vswitchd log for details.
ovs-vsctl: The default log directory is "/var/log/openvswitch".