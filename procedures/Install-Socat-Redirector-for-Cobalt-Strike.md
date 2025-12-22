---
id: 295b7b83-8f2e-443e-8c4f-4b12414d2b0c
name: Install-Socat-Redirector-for-Cobalt-Strike
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.281498+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Command and Control]]'
techniques:
  - '[[Connection Proxy]]'
  - '[[Protocol Tunneling]]'
sub_techniques: []
tags:
  - '[[tags/Cobalt Strike]]'
  - '[[tags/Infrastructure]]'
  - '[[tags/Redirectors]]'
  - socat
commands:
  - '[[commands/apt-install-socat]]'
  - '[[commands/socat-forward-traffic-to-team-server]]'
platforms:
  - Linux
tools:
  - '[[tools/Socat]]'
validated: true
---

# Install-Socat-Redirector-for-Cobalt-Strike

## Summary

This procedure installs and configures Socat on a Linux-based redirector server to forward incoming traffic to a Cobalt Strike team server, enabling attackers to mask command and control (C2) communications and evade detection by routing traffic through an intermediary host.

## Description

In red team operations, redirectors are used to obscure the origin of C2 traffic from defenders. Socat, a versatile networking tool, acts as a simple TCP proxy by listening on a specified port (e.g., 80 for HTTP-like traffic) and relaying connections to the Cobalt Strike team server. This setup allows beacons or implants to connect to the redirector, which then forwards the traffic transparently. The technique aligns with proxying and protocol tunneling to blend malicious traffic with legitimate network activity. Prerequisites include root access on the redirector and knowledge of the team server's IP and port. Successful implementation maintains persistent C2 without direct exposure of the team server.

## Requirements

1. Root or sudo access on a Linux redirector server (e.g., Ubuntu/Debian).
2. Network connectivity between the redirector and Cobalt Strike team server.
3. Knowledge of the team server's IP address and listening port (default HTTP/S profile uses 80 or 443).
4. Socat package availability via apt (or equivalent package manager).

## Defense

- Monitor for unusual outbound connections from redirector-like hosts to known C2 IPs or ports.
- Implement network segmentation to isolate potential redirectors and block unauthorized forwarding.
- Use application-layer proxies or deep packet inspection to detect anomalous traffic patterns, such as high-volume TCP relays on port 80.
- Deploy endpoint detection rules for Socat processes spawning with fork options on non-standard hosts.

## Objectives

1. Install Socat on the redirector to enable traffic forwarding capabilities.
2. Configure a persistent TCP listener that proxies connections to the Cobalt Strike team server.
3. Establish a hidden C2 channel for maintaining access to compromised hosts.
4. Verify the redirector setup by testing connectivity from a simulated beacon.

## Instructions

### Step 1: Install Socat

**Context**: Socat must be installed on the redirector server to provide the networking relay functionality. This step ensures the tool is available for configuration.

**Command** ([[commands/apt-install-socat]]):
```bash
sudo apt update && sudo apt install socat
```

> This command updates the package list and installs Socat. Run it as root or with sudo privileges. Expected output includes confirmation of installation, such as "socat is already the newest version" if pre-installed, or download progress followed by "Setting up socat".

### Step 2: Configure Traffic Forwarding

**Context**: Once installed, configure Socat to listen on a port (e.g., 80) and forward all incoming TCP connections to the Cobalt Strike team server. The 'fork' option handles multiple concurrent connections, simulating a basic web server.

**Command** ([[commands/socat-forward-traffic-to-team-server]]):
```bash
socat TCP4-LISTEN:80,fork TCP4:$_TEAM_SERVER_IP:$_TEAM_SERVER_PORT
```

> Replace $_TEAM_SERVER_IP with the IP of your Cobalt Strike team server (e.g., 192.168.1.100) and $_TEAM_SERVER_PORT with the listener port (e.g., 80). Run this in a terminal or as a background process (e.g., via nohup or systemd). Expected output is minimal—Socat runs silently in the foreground, logging connections if verbose mode is enabled (add -v flag). Success is indicated by no errors and the process remaining active (check with ps aux | grep socat).

### Step 3: Verify the Redirector

**Context**: Test the setup by simulating a connection from a client (e.g., a beacon or curl) to ensure traffic is forwarded correctly without exposing the team server.

**Instructions**: From another host, attempt a connection to the redirector on port 80 (e.g., using telnet or curl http://redirector_ip). Monitor the team server logs for incoming connections. If using Cobalt Strike's HTTP listener, ensure the profile matches the forwarded protocol.

**Expected Output**: Client connects to redirector; team server receives the proxied request. No direct connection to team server IP should be observable from external tools like nmap.
