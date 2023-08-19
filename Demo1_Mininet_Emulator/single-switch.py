#!/usr/bin/python
# -*- single switch topo, 13 hosts-*-
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=13):
        switch = self.addSwitch('s1', protocols='OpenFlow13')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo(n=13)
    net = Mininet( topo=topo, controller=None)
    net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6653 )
    net.start()
    dumpNodeConnections(net.hosts)
    CLI(net)
    net.pingAll()
    net.stop()
