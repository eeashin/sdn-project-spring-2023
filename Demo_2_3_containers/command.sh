sudo ip netns delete ns1
sudo ip netns delete blue
sudo ovs-vsctl del-br br-1
sudo ovs-vsctl del-br br-2
sudo ip link delete br-ovs1
sudo ip link delete br-ovs2

# application inside onos runnning


ssh onos@127.0.0.1 -p 8101  
# password : rocks

app activate org.onosproject.hostprovider
app activate org.onosproject.mobility
app activate org.onosproject.lldpprovider
app activate org.onosproject.ofagent
app activate org.onosproject.openflow-base
app activate org.onosproject.openflow
app activate org.onosproject.roadm
app activate org.onosproject.proxyarp 
app activate org.onosproject.fwd


