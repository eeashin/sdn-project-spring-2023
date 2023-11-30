#!/usr/bin/env bash


function create_ns() {
echo "Creating the namespace $ns"
ip netns add $ns
}

function create_ovs_bridge() {
echo "Creating the OVS bridge $br"
ovs-vsctl add-br $br
ovs-vsctl set bridge $br protocols=OpenFlow10,OpenFlow12,OpenFlow13
}

#attach_ns_to_ovs red br-1 veth-red veth-red-br 2 10.0.0.2
# ns, br, veth1, veth2, ofport, ip
function attach_ns_to_ovs() {  
echo "Attaching the namespace $ns to the OVS $br"
ip link add $3 type veth peer name $4
ip link set $3 netns $1
ovs-vsctl add-port $2 $4 -- set Interface $4 ofport_request=$5
ip netns exec $1 ip addr add $6/24 dev $3
ip netns exec $1 ip link set dev $3 up
ip link set $4 up
}

# br-1 br-2 br-ovs1 br-ovs2 1
function attach_ovs_to_ovs() {
echo "Attaching the OVS $1 to the OVS $2"
ip link add name $3 type veth peer name $4
ip link set $3 up
ip link set $4 up
ovs-vsctl add-port $1 $3 -- set Interface $3 ofport_request=$5
ovs-vsctl add-port $2 $4 -- set Interface $4 ofport_request=$5
}

function attach_ovs_to_sdn() {
echo "Attaching the OVS bridge to the ONOS controller"
ovs-vsctl set-controller $1 tcp:$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -q  --filter ancestor=onosproject/onos)):6653
}


create_ns ns1
create_ns ns2

create_ovs_bridge br1
create_ovs_bridge br2

attach_ovs_to_ovs br-1 br-2 br-ovs1 br-ovs2 1
attach_ns_to_ovs red br-1 veth-red veth-red-br 2 10.0.0.2
attach_ns_to_ovs blue br-2 veth-blue veth-blue-br 2 10.0.0.3

attach_ovs_to_sdn br-1
attach_ovs_to_sdn br-2

ip netns exec red ping -c 1 10.0.0.3
ip netns exec blue ping -c 1 10.0.0.2

