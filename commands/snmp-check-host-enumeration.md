---
type: command
executor: bash
data: snmp-check -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
output: >-
  root@kali:~# snmp-check -c public -v 2c
  10.10.10.10                                       

  snmp-check v1.9 - SNMP
  enumerator                                                                   

  Copyright (c) 2005-2015 by Matteo Cantoni
  (www.nothink.org)                                         
                                                                                                      
  [+] Try to connect to 10.10.10.10:161 using SNMPv2c and community
  'public'                          
                                                                                                      
                                                                                                      
  [*] System
  information:                                                                             
                                                                                                      
    Host IP address               : 10.10.10.10                                                       
    Hostname                      : Host                                                     
    Description                   : Linux Sneaky 4.4.0-75-generic #96~14.04.1-Ubuntu SMP Thu Apr 20 11
  :06:56 UTC 2017
  i686                                                                                
    Contact                       : root                                                              
    Location                      : Unknown                                                           
    Uptime snmp                   : 00:18:52.85                                                       
    Uptime system                 : 00:18:48.37                                                       
    System date                   : 2019-9-17 02:15:24.0
created_at: '2019-09-17T00:51:23.956542Z'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - enumeration
  - snmp
verified: true
validated: true
---

# snmp-check-host-enumeration

## Command

```bash
snmp-check -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```

## Description

This command uses the snmp-check tool to perform comprehensive enumeration of an SNMP-enabled host, retrieving categorized information such as system details, network interfaces, processes, and services. It is particularly useful for reconnaissance when the SNMP community string is known, providing a structured overview without needing manual parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c $_COMMUNITY_STRING` | SNMP community string for authentication (e.g., 'public', 'private') | Yes |
| `-v $_VERSION` | SNMP protocol version (1, 2c, or 3) | Yes |
| `$_TARGET_IP` | IP address or hostname of the target device | Yes |

## Examples

### Basic Usage

```bash
snmp-check -c public -v 2c 10.10.10.10
```

### Advanced Usage

```bash
snmp-check -c private -v 1 192.168.1.100 -t 2
```

(Adds a 2-second timeout with `-t 2` for slower networks)

## Expected Output

```
root@kali:~# snmp-check -c public -v 2c 10.10.10.10                                       
snmp-check v1.9 - SNMP enumerator                                                                   
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)                                         
                                                                                                    
[+] Try to connect to 10.10.10.10:161 using SNMPv2c and community 'public'                          
                                                                                                    
                                                                                                    
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

Success is indicated by a successful connection message and populated sections with details like system information, interfaces, or processes. Failure shows connection errors or empty outputs.

## Related

- [[tools/snmp-check]]
- [[commands/snmpwalk-basic-enumeration]]
