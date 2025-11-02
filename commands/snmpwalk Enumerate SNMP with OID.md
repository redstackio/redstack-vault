---
id: 341c8486-4185-4958-a7b6-c2a3a1718111
name: snmpwalk Enumerate SNMP with OID
type: command
executor: bash
data: snmpwalk -c $WORDLIST -v $VERSION $TARGET_IP $OID
output: 'root@kali:~# snmpwalk -c public -v 2c 10.10.10.10 1.3.6.1.2.1.4.34.1.3

  IP-MIB::ipAddressIfIndex.ipv4."10.10.10.10" = INTEGER: 2

  IP-MIB::ipAddressIfIndex.ipv4."10.10.10.255" = INTEGER: 2

  IP-MIB::ipAddressIfIndex.ipv4."127.0.0.1" = INTEGER: 1

  IP-MIB::ipAddressIfIndex.ipv6."00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:01"
  = INTEGER: 1

  IP-MIB::ipAddressIfIndex.ipv6."de:ad:be:ef:00:00:00:00:02:50:56:ff:fe:a4:8c:bc"
  = INTEGER: 2

  IP-MIB::ipAddressIfIndex.ipv6."fe:80:00:00:00:00:00:00:02:50:56:ff:fe:a4:8c:bc"
  = INTEGER: 2'
created_at: '2019-10-18T21:24:21.329965+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[snmpwalk]]'
---

# snmpwalk Enumerate SNMP with OID

```bash
snmpwalk -c $WORDLIST -v $VERSION $TARGET_IP $OID
```

## Expected Output

```
root@kali:~# snmpwalk -c public -v 2c 10.10.10.10 1.3.6.1.2.1.4.34.1.3
IP-MIB::ipAddressIfIndex.ipv4."10.10.10.10" = INTEGER: 2
IP-MIB::ipAddressIfIndex.ipv4."10.10.10.255" = INTEGER: 2
IP-MIB::ipAddressIfIndex.ipv4."127.0.0.1" = INTEGER: 1
IP-MIB::ipAddressIfIndex.ipv6."00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:01" = INTEGER: 1
IP-MIB::ipAddressIfIndex.ipv6."de:ad:be:ef:00:00:00:00:02:50:56:ff:fe:a4:8c:bc" = INTEGER: 2
IP-MIB::ipAddressIfIndex.ipv6."fe:80:00:00:00:00:00:00:02:50:56:ff:fe:a4:8c:bc" = INTEGER: 2
```


