---
id: 56423ca4-879f-4eb2-a59f-1ee0d019fa76
name: Metasploit Display the Host's ARP Cache
type: command
executor: metasploit
data: arp
output: "meterpreter > arp\n\nARP cache\n=========\n\n    IP address       MAC address\
  \        Interface\n    ----------       -----------        ---------\n    10.0.1.1\
  \         00:21:29:64:d4:4d  11\n    10.0.1.122       08:00:27:23:ff:90  11\n  \
  \  10.0.1.255       ff:ff:ff:ff:ff:ff  11\n    224.0.0.22       00:00:00:00:00:00\
  \  1\n    224.0.0.22       01:00:5e:00:00:16  11\n    224.0.0.252      01:00:5e:00:00:fc\
  \  11\n    239.255.255.250  00:00:00:00:00:00  1\n    239.255.255.250  01:00:5e:7f:ff:fa\
  \  11\n    255.255.255.255  ff:ff:ff:ff:ff:ff  11"
created_at: '2020-07-09T00:22:14.470272+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Display the Host's ARP Cache

```metasploit
arp
```

## Expected Output

```
meterpreter > arp

ARP cache
=========

    IP address       MAC address        Interface
    ----------       -----------        ---------
    10.0.1.1         00:21:29:64:d4:4d  11
    10.0.1.122       08:00:27:23:ff:90  11
    10.0.1.255       ff:ff:ff:ff:ff:ff  11
    224.0.0.22       00:00:00:00:00:00  1
    224.0.0.22       01:00:5e:00:00:16  11
    224.0.0.252      01:00:5e:00:00:fc  11
    239.255.255.250  00:00:00:00:00:00  1
    239.255.255.250  01:00:5e:7f:ff:fa  11
    255.255.255.255  ff:ff:ff:ff:ff:ff  11
```


