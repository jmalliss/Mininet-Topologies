from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch
from mininet.link import TCLink

class RingTopo( Topo ):
	"RingTopology ;9 switches and 4 hosts"

	def build( self ):
		# Create hosts.
		h1 = self.addHost( 'h1' )
		h2 = self.addHost( 'h2' )
		h3 = self.addHost( 'h3' )
		h4 = self.addHost( 'h4' )
		# Create switches
		s1 = self.addSwitch( 's1', protocols='OpenFlow13' )
		s2 = self.addSwitch( 's2', protocols='OpenFlow13' )
		s3 = self.addSwitch( 's3', protocols='OpenFlow13' )
		s4 = self.addSwitch( 's4', protocols='OpenFlow13' )
		s5 = self.addSwitch( 's5', protocols='OpenFlow13' )
		s6 = self.addSwitch( 's6', protocols='OpenFlow13' )
		s7 = self.addSwitch( 's7', protocols='OpenFlow13' )
		s8 = self.addSwitch( 's8', protocols='OpenFlow13' )
		s9 = self.addSwitch( 's9', protocols='OpenFlow13' )
		#Add links between the swithc and each host
		self.addLink(s1,s2,cls=TCLink,bw=20)
		self.addLink(s2,s3,cls=TCLink,bw=20)
		self.addLink(s1,s4,cls=TCLink,bw=20)
		self.addLink(s2,s5,cls=TCLink,bw=20)
		self.addLink(s3,s6,cls=TCLink,bw=20)
		self.addLink(s4,s5,cls=TCLink,bw=20)
		self.addLink(s5,s6,cls=TCLink,bw=20)
		self.addLink(s4,s7,cls=TCLink,bw=20)
		self.addLink(s5,s8,cls=TCLink,bw=20)
		self.addLink(s6,s9,cls=TCLink,bw=20)
		self.addLink(s7,s8,cls=TCLink,bw=20)
		self.addLink(s8,s9,cls=TCLink,bw=20)
		self.addLink(s1,h1,cls=TCLink,bw=20)
		self.addLink(s3,h2,cls=TCLink,bw=20)
		self.addLink(s7,h3,cls=TCLink,bw=20)
		self.addLink(s9,h4,cls=TCLink,bw=20)

def runRing():
	"Bootstrap a Mininet network using the Ring Topology"

	# Create an instance of our topology
	topo = RingTopo()

	# Create a network based on the topology using OVS and controlled by
	# a remote controller.
	net = Mininet(topo=topo, controller=lambda name: RemoteController( name, ip='192.168.56.1' ), switch=OVSSwitch, autoSetMacs=True )

	# Actually start the network
	net.start()

	#Drop the user into a CLI so user can run commands.
	CLI( net )

	#After the user exits the CLI, shutdown the network.
	net.stop()

if __name__ == '__main__':
	# This runs if the file is executed directly
	setLogLevel( 'info' )
	runRing()

# Allows the file to be imported using 'mn --custom <filename> --topo minimal
topos = {
	'minimal': RingTopo
}
