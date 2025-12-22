---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Share Discovery|T1135 - Network Share Discovery]]'
  - >-
    [[techniques/System Network Configuration Discovery|T1016 - System Network
    Configuration Discovery]]
sub_techniques: []
tags:
  - '[[tags/Network Enumeration]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/ipconfig-all]]'
  - '[[commands/get-net-ip-configuration]]'
  - '[[commands/get-dns-client-server-address-ipv4]]'
  - '[[commands/route-print]]'
  - '[[commands/get-net-route-ipv4]]'
  - '[[commands/arp-a]]'
  - '[[commands/get-net-neighbor-ipv4]]'
  - '[[commands/netstat-ano]]'
  - '[[commands/net-share]]'
  - '[[commands/find-domain-share]]'
  - '[[commands/reg-query-snmp]]'
  - '[[commands/get-childitem-snmp-registry]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# windows-network-enumeration-for-privilege-escalation

## Summary

This procedure performs comprehensive network enumeration on a Windows system to gather details about interfaces, IP configurations, routing, ARP mappings, active connections, network shares, and SNMP settings. This information helps identify potential lateral movement paths, misconfigurations, or accessible shares that could contain credentials or tools for privilege escalation during post-exploitation.

## Description

Network enumeration is essential in privilege escalation scenarios on Windows domains, as it reveals the system's position in the network, connected hosts, and shared resources that may be exploitable. Attackers use built-in commands to map the environment without external tools, reducing detection risk. For example, discovering open shares might expose password files or scripts, while connection details can pinpoint domain controllers or high-value targets. This targets user-level access on domain-joined Windows machines (Windows 10/Server 2016+), assuming no advanced restrictions like AppLocker. Successful enumeration provides a topology overview, enabling targeted attacks like share access or SNMP querying for further discovery.

## Requirements

1. Local user-level access to a Windows system (domain or local account).
2. Ability to execute commands in Command Prompt (cmd.exe) or PowerShell.
3. For advanced share enumeration, PowerView module loaded in PowerShell (e.g., via Import-Module PowerView.ps1).
4. No administrative privileges required for most commands, but some outputs may be limited without them.

## Defense

- Enable PowerShell logging and constrained language mode to monitor and restrict script execution.
- Implement Windows Defender Application Control (WDAC) or AppLocker to block unauthorized command usage.
- Use network access control lists (ACLs) and segmentation to limit visibility of shares and SNMP services.
- Monitor for anomalous command executions via Sysmon or EDR tools, focusing on netstat, arp, and reg query patterns.

## Objectives

1. Map network interfaces, IPs, and DNS to understand the system's connectivity.
2. Identify routes and neighbors to discover adjacent hosts for lateral movement.
3. Enumerate active connections and shares to find exploitable resources or credentials.
4. Check SNMP configuration for potential weak community strings enabling remote queries.

## Instructions

### Step 1: Enumerate Network Interfaces and IP Configuration

**Context**: Start by gathering details on all network adapters, their IP addresses, and DNS servers to establish the system's network footprint and potential gateways.

**Command** ([[commands/ipconfig-all]]):
```cmd
ipconfig /all
```

> This displays comprehensive details for each interface, including MAC addresses, DHCP status, and subnet masks. Use it to identify the primary interface and any static configurations that might indicate misconfigs.

**Command** ([[commands/get-net-ip-configuration]]):
```powershell
Get-NetIPConfiguration | ft InterfaceAlias,InterfaceDescription,IPv4Address
```

> This PowerShell cmdlet provides a formatted view of IP settings per interface. Expected output includes alias, description, and IPv4 address, helping spot multiple NICs or VPNs.

**Command** ([[commands/get-dns-client-server-address-ipv4]]):
```powershell
Get-DnsClientServerAddress -AddressFamily IPv4 | ft
```

> Lists DNS servers for IPv4. Success is confirmed by seeing primary/secondary DNS IPs, which could be internal DCs for further targeting.

### Step 2: View IPv4 Routing Table

**Context**: Examine the routing table to understand traffic paths, default gateways, and persistent routes that reveal network topology and potential pivot points.

**Command** ([[commands/route-print]]):
```cmd
route print
```

> Outputs the full routing table in a tabular format. Look for active routes to subnets, which indicate reachable segments for lateral movement.

**Command** ([[commands/get-net-route-ipv4]]):
```powershell
Get-NetRoute -AddressFamily IPv4 | ft DestinationPrefix,NextHop,RouteMetric,ifIndex
```

> PowerShell equivalent with formatted columns for destination, next hop, metric, and interface. Useful for scripting; success shows no errors and populated routes.

### Step 3: List ARP Table and Neighbors

**Context**: Retrieve ARP mappings to identify local network devices by IP-MAC pairs, aiding in host discovery and potential ARP poisoning for escalation.

**Command** ([[commands/arp-a]]):
```cmd
arp -a
```

> Displays the ARP cache. Expected: List of IP to MAC mappings for recently communicated hosts on the local subnet.

**Command** ([[commands/get-net-neighbor-ipv4]]):
```powershell
Get-NetNeighbor -AddressFamily IPv4 | ft ifIndex,IPAddress,LinkLayerAddress,State
```

> Enhanced PowerShell view including state (e.g., Reachable). Helps verify live neighbors for targeting shares or services.

### Step 4: List Active Network Connections

**Context**: Identify ongoing TCP/UDP connections and associated processes to spot listening services, remote hosts, or SMB sessions that could be hijacked.

**Command** ([[commands/netstat-ano]]):
```cmd
netstat -ano
```

> Shows all connections with PIDs. Cross-reference PIDs with Task Manager to find processes like lsass.exe for credential dumping opportunities.

### Step 5: Enumerate Network Shares

**Context**: Discover local and domain shares to locate accessible files, configs, or credentials that enable privilege escalation via readable sensitive data.

**Command** ([[commands/net-share]]):
```cmd
net share
```

> Lists all local shares. Look for ADMIN$ or IPC$ with unusual permissions.

**Command** ([[commands/find-domain-share]]):
```powershell
Find-DomainShare -ComputerDomain domain.local
```

> Requires PowerView; enumerates shares across domain. Replace 'domain.local' with actual domain. Success: List of remote shares, potentially with paths to SYSVOL or user folders.

### Step 6: Check SNMP Configuration

**Context**: Query registry for SNMP settings to find enabled services or community strings that allow unauthenticated remote enumeration, leading to broader discovery.

**Command** ([[commands/reg-query-snmp]]):
```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Services\SNMP /s
```

> Dumps SNMP registry values. Expected: Details on enabled status and communities like 'public'.

**Command** ([[commands/get-childitem-snmp-registry]]):
```powershell
Get-ChildItem -Path HKLM:\SYSTEM\CurrentControlSet\Services\SNMP -Recurse
```

> Recursively lists SNMP keys. Reveals config for potential exploitation if SNMPv1/2 is active with weak auth.
