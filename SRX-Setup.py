# Libraries to import
import re

# Variables to be used later on
unitNumb = 0
vlanID1 = 4
vlanID2 = 1
firstInterface = 18
secondInterface = 19
aeInterface = "ae0"

# Asking for Gateway Address
nativeVLAN = input("What is the Native VLAN? ")
defaultGW = input("What is the Default Gateway? ") 


# def to print ERROR messages
def error(self):
    print("ERROR: " + defaultGW + " not a valid IP!!")
    exit()


def ipchecker(arg1):
    # Checks for validity of the IP based on the below regex comparison
    gateway = re.match(r"(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2}\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})", arg1)

    # Errors out if it not a valid IP
    if not bool(gateway):
        error(arg1)


ipchecker(defaultGW)

# Commands needed for setting up the " + str(aeInterface)" interface
print("set interfaces xe-0/0/" + str(firstInterface) + " gigether-options 802.3ad " + str(aeInterface))
print("set interfaces xe-0/0/" + str(secondInterface) + " gigether-options 802.3ad " + str(aeInterface))
print("set interfaces " + str(aeInterface) + " flexible-vlan-tagging")
print("set interfaces " + str(aeInterface) + " native-vlan-id " + nativeVLAN)
print("set interfaces " + str(aeInterface) + " aggregated-ether-options link-speed 10g")
print("set interfaces " + str(aeInterface) + " aggregated-ether-options lacp active")

# Not sure why this line is needed, but things didn't work propery without it
print("set chassis aggregated-devices ethernet device-count 44")

# Default route to be added
print("set routing-options static route 0.0.0.0/0 next-hop " + defaultGW)

# While loop to create sub interfaces for each VLAN
while vlanID1 < 9:
    while vlanID2 < 9:    
        print("set interfaces " + str(aeInterface) + " unit " + str(unitNumb) + " description " + str(vlanID1) + "0" + str(vlanID2))
        print("set interfaces " + str(aeInterface) + " unit " + str(unitNumb) + " vlan-id " + str(vlanID1) + "0" + str(vlanID2))
        print("set interfaces " + str(aeInterface) + " unit " + str(unitNumb) + " family inet address 10." + str(vlanID1) + str(vlanID2) + ".0.1/24")
        print("set forwarding-options dhcp-relay relay-option-82 circuit-id use-interface-description device")
        print("set forwarding-options dhcp-relay forward-only")
        print("set forwarding-options dhcp-relay server-group " + str(vlanID1) + "0" + str(vlanID2) + "-serverGroup 10.30.0.2")
        print("set forwarding-options dhcp-relay active-server-group " + str(vlanID1) + "0" + str(vlanID2) + "-serverGroup")
        print("set forwarding-options dhcp-relay group " + str(vlanID1) + "0" + str(vlanID2) + "-serverGroup interface " + str(aeInterface) + "." + str(unitNumb))
        print("set security zones security-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " description " + str(vlanID1) + "0" + str(vlanID2))
        print("set security zones security-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " address-book address VLAN" + str(vlanID1) + "0" + str(vlanID2) + " 10." + str(vlanID1) + str(vlanID2) + ".0.0/24")
        print("set security zones security-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " interfaces " + str(aeInterface) + "." + str(unitNumb) + " host-inbound-traffic system-services snmp")
        print("set security zones security-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " interfaces " + str(aeInterface) + "." + str(unitNumb) + " host-inbound-traffic system-services ping")
        print("set security zones security-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " interfaces " + str(aeInterface) + "." + str(unitNumb) + " host-inbound-traffic system-services traceroute")
        print("set security zones security-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " interfaces " + str(aeInterface) + "." + str(unitNumb) + " host-inbound-traffic system-services dhcp")
        print("set security nat source rule-set VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-NAT from zone VLAN" + str(vlanID1) + "0" + str(vlanID2))
        print("set security nat source rule-set VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-NAT to zone Beanfield")
        print("set security nat source rule-set VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-NAT rule VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-OUT match source-address 10." + str(vlanID1) + str(vlanID2) + ".0.0/24")
        print("set security nat source rule-set VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-NAT rule VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-OUT match destination-address 0.0.0.0/0")
        print("set security nat source rule-set VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-NAT rule VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-OUT match protocol tcp")
        print("set security nat source rule-set VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-NAT rule VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-OUT match protocol udp")
        print("set security nat source rule-set VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-NAT rule VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-OUT match protocol icmp")      
        print("set security nat source rule-set VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-NAT rule VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-OUT then source-nat pool Beanfield")
        print("set security policies from-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " to-zone Beanfield policy VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-Out match source-address VLAN" + str(vlanID1) + "0" + str(vlanID2))
        print("set security policies from-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " to-zone Beanfield policy VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-Out match destination-address any")
        print("set security policies from-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " to-zone Beanfield policy VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-Out match application any")
        print("set security policies from-zone VLAN" + str(vlanID1) + "0" + str(vlanID2) + " to-zone Beanfield policy VLAN" + str(vlanID1) + "0" + str(vlanID2) + "-Out then permit")
        vlanID2 += 1
        unitNumb += 1
    vlanID2 = 1
    vlanID1 += 1 
