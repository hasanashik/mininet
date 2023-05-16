#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController

class MyTopo( Topo ):
	"Simple topology example."

	def build(self):
		# Add hosts and switches
		leftHost = self.addHost( 'h1' )
		rightHost = self.addHost( 'h2' )
		switch_one = self.addSwitch( 's1', protocols=["OpenFlow13"] )
		switch_two = self.addSwitch( 's2', protocols=["OpenFlow13"] )
		switch_three = self.addSwitch( 's3', protocols=["OpenFlow13"] )
		switch_four = self.addSwitch( 's4', protocols=["OpenFlow13"] )
		switch_five = self.addSwitch( 's5', protocols=["OpenFlow13"] )
		switch_six = self.addSwitch( 's6', protocols=["OpenFlow13"] )
		switch_seven = self.addSwitch( 's7', protocols=["OpenFlow13"] )
		switch_eight = self.addSwitch( 's8', protocols=["OpenFlow13"] )
		switch_nine = self.addSwitch( 's9', protocols=["OpenFlow13"] )
		switch_ten = self.addSwitch( 's10', protocols=["OpenFlow13"] )
		switch_eleven = self.addSwitch( 's11', protocols=["OpenFlow13"] )
		switch_twelve = self.addSwitch( 's12', protocols=["OpenFlow13"] )
		switch_thirteen = self.addSwitch( 's13', protocols=["OpenFlow13"] )
		switch_fourteen = self.addSwitch( 's14', protocols=["OpenFlow13"] )
		switch_fifteen = self.addSwitch( 's15', protocols=["OpenFlow13"] )
		switch_sixteen = self.addSwitch( 's16', protocols=["OpenFlow13"] )
		switch_seventeen = self.addSwitch( 's17', protocols=["OpenFlow13"] )
		switch_eighteen = self.addSwitch( 's18', protocols=["OpenFlow13"] )
		switch_nineteen = self.addSwitch( 's19', protocols=["OpenFlow13"] )
		switch_twenty = self.addSwitch( 's20', protocols=["OpenFlow13"] )
		switch_twentyone = self.addSwitch( 's21', protocols=["OpenFlow13"] )
		switch_twentytwo = self.addSwitch( 's22', protocols=["OpenFlow13"] )
		switch_twentythree = self.addSwitch( 's23', protocols=["OpenFlow13"] )
		switch_twentyfour = self.addSwitch( 's24', protocols=["OpenFlow13"] )
		switch_twentyfive = self.addSwitch( 's25', protocols=["OpenFlow13"] )
		switch_twentysix = self.addSwitch( 's26', protocols=["OpenFlow13"] )
		switch_twentyseven = self.addSwitch( 's27', protocols=["OpenFlow13"] )
		switch_twentyeight = self.addSwitch( 's28', protocols=["OpenFlow13"] )
		switch_twentynine = self.addSwitch( 's29', protocols=["OpenFlow13"] )
		switch_thirty = self.addSwitch( 's30', protocols=["OpenFlow13"] )
		switch_thirtyone = self.addSwitch( 's31', protocols=["OpenFlow13"] )
		switch_thirtytwo = self.addSwitch( 's32', protocols=["OpenFlow13"] )
		switch_thirtythree = self.addSwitch( 's33', protocols=["OpenFlow13"] )


		# Add links
		self.addLink( leftHost, switch_one, cls=TCLink,bw=10 )
		self.addLink( switch_one, switch_two, cls=TCLink,bw=10  )
		self.addLink( switch_two, switch_three, cls=TCLink,bw=10  )
		self.addLink( switch_two, switch_thirtythree, cls=TCLink,bw=10  )
		self.addLink( switch_three, switch_four, cls=TCLink,bw=10  )
		self.addLink( switch_four, switch_five, cls=TCLink,bw=10  )
		self.addLink( switch_four, switch_nine, cls=TCLink,bw=10  )
		self.addLink( switch_five, switch_six, cls=TCLink,bw=10  )
		self.addLink( switch_six, switch_seven, cls=TCLink,bw=10  )
		self.addLink( switch_seven, switch_eight, cls=TCLink,bw=10  )
		self.addLink( switch_nine, switch_ten, cls=TCLink,bw=10  )
		self.addLink( switch_ten, switch_eleven, cls=TCLink,bw=10  )
		self.addLink( switch_eleven, switch_twelve, cls=TCLink,bw=10  )
		self.addLink( switch_twelve, switch_thirteen, cls=TCLink,bw=10  )
		self.addLink( switch_twelve, switch_fourteen, cls=TCLink,bw=10  )
		self.addLink( switch_fourteen, switch_fifteen, cls=TCLink,bw=10  )
		self.addLink( switch_twelve, switch_sixteen, cls=TCLink,bw=10  )
		self.addLink( switch_sixteen, switch_seventeen, cls=TCLink,bw=10  )
		self.addLink( switch_sixteen, switch_thirty, cls=TCLink,bw=10  )
		self.addLink( switch_seventeen, switch_eighteen, cls=TCLink,bw=10  )
		self.addLink( switch_eighteen, switch_nineteen, cls=TCLink,bw=10  )
		self.addLink( switch_nineteen, switch_twenty, cls=TCLink,bw=10  )
		self.addLink( switch_twenty, switch_twentyone, cls=TCLink,bw=10  )
		self.addLink( switch_twentyone, switch_twentytwo, cls=TCLink,bw=10  )
		self.addLink( switch_twentytwo, switch_twentythree, cls=TCLink,bw=10  )
		self.addLink( switch_twentythree, switch_twentyfour, cls=TCLink,bw=10  )
		self.addLink( switch_twentythree, switch_twentyfive, cls=TCLink,bw=10  )
		self.addLink( switch_twentyfive, switch_twentysix, cls=TCLink,bw=10  )
		self.addLink( switch_twentyfive, switch_twentyseven, cls=TCLink,bw=10  )
		self.addLink( switch_twentyseven, switch_twentyeight, cls=TCLink,bw=10  )
		self.addLink( switch_twentyeight, switch_twentynine, cls=TCLink,bw=10  )
		self.addLink( switch_twentynine, switch_thirty, cls=TCLink,bw=10  )
		self.addLink( switch_thirty, switch_thirtyone, cls=TCLink,bw=10  )
		self.addLink( switch_thirtyone, switch_thirtytwo, cls=TCLink,bw=10  )
		self.addLink( switch_thirtytwo, switch_thirtythree, cls=TCLink,bw=10  )
		self.addLink( switch_twentysix, rightHost, cls=TCLink,bw=10  )

topos = { 'mytopo': ( lambda: MyTopo() ) }
