---
id: 749ca2e7-fb31-4903-9945-b2d96998a199
name: Windows - Network Enumeration for Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.706305+00:00'
updated_at: '2023-04-10T20:37:53.200792+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
tags:
- '[[Network Enumeration]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[ARP Table and IPv4 Neighbor Table]]'
- '[[Find Domain Shares]]'
- '[[Get IPv4 Route Information]]'
- '[[List all active network connections and their associated processes]]'
- '[[View IPv4 Route Table]]'
---

# Windows - Network Enumeration for Privilege Escalation

## Summary

Network enumeration is a crucial step in the privilege escalation process. By gathering information about the network, an attacker can identify potential targets for further exploitation. This procedure involves using various Windows commands to gather information about the network, including the n

## Description

# Description

Network enumeration is a crucial step in the privilege escalation process. By gathering information about the network, an attacker can identify potential targets for further exploitation. This procedure involves using various Windows commands to gather information about the network, including the network interfaces, IP configuration, routing table, ARP table, current connections list, and network shares. This information can be used to identify vulnerable systems and services that can be exploited to gain higher privileges. Successful execution of this procedure can lead to complete compromise of the network and its systems.

Technical Explanation: This procedure involves executing various Windows commands to gather network information. The commands used are: Network Interface and IP Configuration, IPv4 Routing Table, ARP Table, Current Connections List, List Network Shares, and SNMP Configuration Check. These commands provide information about the network interfaces, IP configuration, routing table, ARP table, current connections, network shares, and SNMP configuration. The attacker can use this information to identify potential targets for further exploitation.

Business Value: This procedure can help organizations identify vulnerabilities in their network and take appropriate measures to mitigate them. By understanding how attackers can enumerate their network, organizations can take steps to secure their systems and prevent unauthorized access.

 

## Requirements

1. Access to a Windows system on the network

1. Permissions to execute Windows commands

 

## Defense

1. Implement network segmentation to prevent lateral movement

1. Regularly update and patch systems to prevent exploitation of known vulnerabilities

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Identify potential targets for further exploitation

1. Gain higher privileges

 

# Instructions

1. This command will display a list of all network interfaces, their descriptions and assigned IPv4 addresses, as well as the DNS server addresses currently in use.

 



**Code**: [[ipconfig /all
Get-NetIPConfiguration | ft Interfac]]



> The 'ipconfig /all' command displays detailed information about all network interfaces, including their MAC addresses, IP addresses, subnet masks, DHCP status, and more. The 'Get-NetIPConfiguration' command is a PowerShell cmdlet that displays information about the IP configuration of all network adapters, including their interface aliases, descriptions, and IPv4 addresses. Lastly, the 'Get-DnsClientServerAddress' command displays the DNS server addresses currently in use for the IPv4 address family.

2. To view the current IPv4 routing table, run the following command in PowerShell:

 



**Code**: [[route print
Get-NetRoute -AddressFamily IPv4 | ft ]]



> This command displays the current IPv4 routing table, which shows the available routes for network traffic. The output includes the destination prefix, the next hop IP address, the route metric, and the interface index. This information can be useful for troubleshooting network connectivity issues or for configuring static routes.



**Command** ([[View IPv4 Route Table]]):

```bash
route print
```





**Command** ([[Get IPv4 Route Information]]):

```bash
Get-NetRoute -AddressFamily IPv4 | ft DestinationPrefix,NextHop,RouteMetric,ifIndex
```



3. To list the ARP table, run the following command:

 



**Code**: [[arp -A
Get-NetNeighbor -AddressFamily IPv4 | ft if]]



> This command will display the Address Resolution Protocol (ARP) table, which is a list of mappings between IP addresses and physical addresses (MAC addresses) on a network. The 'arp -A' command displays the ARP table in Windows, while 'Get-NetNeighbor -AddressFamily IPv4 | ft ifIndex,IPAddress,LinkLayerAddress,State' displays the ARP table in PowerShell. The output includes the interface index, IP address, MAC address, and state of each device on the network.



**Command** ([[ARP Table and IPv4 Neighbor Table]]):

```bash
arp -A
Get-NetNeighbor -AddressFamily IPv4 | ft ifIndex,IPAddress,LinkLayerAddress,State
```



4. This command is used to display all active TCP and UDP connections on the local computer. It also shows the PID (process identifier) and name of the process that owns the connection. To execute this command, open the Command Prompt and type 'netstat -ano' and press Enter.

 



**Code**: [[netstat -ano]]



> The 'netstat' command is used to display the TCP/IP network protocol statistics and information. The '-a' option displays all active connections and the '-n' option displays addresses and port numbers in numerical form. The '-o' option displays the owning process ID associated with each connection. This command is useful for troubleshooting network connectivity issues and identifying which process is using a particular port.



**Command** ([[List all active network connections and their associated processes]]):

```bash
netstat -ano
```



5. To list all network shares, use the 'net share' command in Command Prompt or the 'Find-DomainShare' cmdlet in PowerShell. The 'net share' command displays a list of all shares on the local machine, while the 'Find-DomainShare' cmdlet can be used to find shares on a remote computer in a specific domain.

 



**Code**: [[net share
powershell Find-DomainShare -ComputerDom]]



> The 'net share' command takes no arguments and simply lists all shares on the local machine. The 'Find-DomainShare' cmdlet requires the '-ComputerDomain' argument to specify the domain to search in, and can also take the '-ShareName' argument to search for a specific share by name. For example, 'Find-DomainShare -ComputerDomain domain.local -ShareName MyShare' would search for a share named 'MyShare' on computers in the 'domain.local' domain.



**Command** ([[Find Domain Shares]]):

```powershell
net share
powershell Find-DomainShare -ComputerDomain domain.local
```



6. To check the configuration of SNMP, run the following command:

 



**Code**: [[reg query HKLM\SYSTEM\CurrentControlSet\Services\S]]



> This command will query the SNMP service registry key in the Windows registry and return the configuration details. It will also recursively list all subkeys and values under the SNMP service key. This is useful for troubleshooting SNMP configuration issues or verifying the current configuration settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Share Discovery|T1135 - Network Share Discovery]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

## Commands Used

- [[ARP Table and IPv4 Neighbor Table]]
- [[Find Domain Shares]]
- [[Get IPv4 Route Information]]
- [[List all active network connections and their associated processes]]
- [[View IPv4 Route Table]]

## Tags

- [[Network Enumeration]]
- [[Windows - Privilege Escalation]]


