from pysnmp import hlapi

ipaddr = u'10.31.70.107'
port = 161
community_name = 'public'

result = getCmd(SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ipaddr, port)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

result2 = nextCmd(SnmpEngine(),
                  CommunityData(community_name, mpModel=0),
                  UdpTransportTarget((ipaddr, port)),
                  ContextData(),
                  ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
                  lexicographicMode=False)

for i in result:
    print(i[3][0])

print("")

for i in result2:
#i_str=str(i[-1][0])
    print(type(i))