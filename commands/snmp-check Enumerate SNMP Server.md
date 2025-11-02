---
id: be12360e-df20-4322-8ea9-6691391e3835
name: snmp-check Enumerate SNMP Server
type: command
executor: bash
data: snmp-check -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
output: "root@kali:~# snmp-check -c public -v 2c 10.10.10.10                     \
  \                  \nsnmp-check v1.9 - SNMP enumerator                         \
  \                                          \nCopyright (c) 2005-2015 by Matteo Cantoni\
  \ (www.nothink.org)                                         \n                 \
  \                                                                              \
  \     \n[+] Try to connect to 10.10.10.20:161 using SNMPv2c and community 'public'\
  \                          \n                                                  \
  \                                                  \n                          \
  \                                                                          \n[*]\
  \ System information:                                                          \
  \                   \n                                                         \
  \                                           \n  Host IP address               :\
  \ 10.10.10.10                                                       \n  Hostname\
  \                      : Host                                                  \
  \   \n  Description                   : Linux Sneaky 4.4.0-75-generic #96~14.04.1-Ubuntu\
  \ SMP Thu Apr 20 11\n:06:56 UTC 2017 i686                                      \
  \                                          \n  Contact                       : root\
  \                                                              \n  Location    \
  \                  : Unknown                                                   \
  \        \n  Uptime snmp                   : 00:18:52.85                       \
  \                                \n  Uptime system                 : 00:18:48.37\
  \                                                       \n  System date        \
  \           : 2019-9-17 02:15:24.0 "
created_at: '2019-09-17T00:51:23.956542+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
- '[[snmp-check]]'
---

# snmp-check Enumerate SNMP Server

```bash
snmp-check -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```

## Expected Output

```
root@kali:~# snmp-check -c public -v 2c 10.10.10.10                                       
snmp-check v1.9 - SNMP enumerator                                                                   
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)                                         
                                                                                                    
[+] Try to connect to 10.10.10.20:161 using SNMPv2c and community 'public'                          
                                                                                                    
                                                                                                    
[*] System information:                                                                             
                                                                                                    
  Host IP address               : 10.10.10.10                                                       
  Hostname                      : Host                                                     
  Description                   : Linux Sneaky 4.4.0-75-generic #96~14.04.1-Ubuntu SMP Thu Apr 20 11
:06:56 UTC 2017 i686                                                                                
  Contact                       : root                                                              
  Location                      : Unknown                                                           
  Uptime snmp                   : 00:18:52.85                                                       
  Uptime system                 : 00:18:48.37                                                       
  System date                   : 2019-9-17 02:15:24.0 
```


