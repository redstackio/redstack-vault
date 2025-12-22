---
type: procedure
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
sub_techniques: []
tags:
  - '[[tags/Network Pivoting Techniques]]'
  - '[[tags/ngrok]]'
commands:
  - '[[commands/download-and-unzip-ngrok-binary]]'
  - '[[commands/authenticate-ngrok-with-authtoken]]'
  - '[[commands/deploy-ngrok-http-forwarding]]'
  - '[[commands/deploy-ngrok-tcp-forwarding]]'
platforms:
  - Linux
tools:
  - '[[tools/ngrok]]'
skill_level: beginner
impact_level: medium
detection_risk: high
verified: true
validated: true
---

# Setup-Ngrok-Port-Forwarding-Tunnel

## Summary

This procedure sets up ngrok to create a secure tunnel from a public endpoint to a locally running service on port 4433, enabling attackers or red teams to bypass firewall restrictions and establish command and control channels or exfiltrate data from behind NAT or firewalls.

## Description

Ngrok is a tunneling tool that exposes local services to the internet via a public URL, making it useful in offensive security for pivoting into restricted networks. In an attack scenario, this allows remote access to internal resources without direct inbound connections. The procedure involves downloading the ngrok binary, authenticating with an account token, and starting either an HTTP or TCP tunnel. This maps to MITRE ATT&CK's Connection Proxy technique, where the tunnel acts as a proxy for C2 communication. Prerequisites include an ngrok account for authentication and a local service running on the target port.

## Requirements

1. Linux environment (e.g., Kali or Ubuntu) with wget and unzip installed.
2. Valid ngrok account and authentication token obtained from ngrok.com.
3. Local service running on port 4433 (e.g., a web server or listener).
4. Internet access on the target machine for downloading and connecting to ngrok's servers.

## Defense

- Monitor network traffic for connections to ngrok domains (e.g., *.ngrok.io) or unusual outbound traffic to tunneling services.
- Implement application whitelisting to block unauthorized binaries like ngrok.
- Use network segmentation and egress filtering to restrict connections to known C2 domains.
- Enable logging for process creation and network connections to detect ngrok execution.

## Objectives

1. Download and prepare the ngrok binary on the target system.
2. Authenticate ngrok to enable tunnel creation.
3. Establish a public tunnel to the local service for remote access or data exfiltration.
4. Verify the tunnel is active and accessible from the internet.

## Instructions

### Step 1: Download and Extract Ngrok Binary

**Context**: Obtain the ngrok executable for Linux to set up the tunneling client. This step ensures the tool is available locally without relying on pre-installed packages.

**Command** ([[commands/download-and-unzip-ngrok-binary]]):
```bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && unzip ngrok-stable-linux-amd64.zip
```

> This downloads the stable Linux AMD64 version and extracts the binary to the current directory. If the download URL is outdated, visit ngrok.com/download for the latest. Expected output includes a progress bar for wget and confirmation of extraction, resulting in an executable `./ngrok` file.

### Step 2: Authenticate Ngrok

**Context**: Link the local ngrok instance to your account to unlock features like reserved domains and avoid rate limits. This is required before creating tunnels.

**Command** ([[commands/authenticate-ngrok-with-authtoken]]):
```bash
./ngrok authtoken $_AUTH_TOKEN
```

> Replace $_AUTH_TOKEN with your actual token from the ngrok dashboard. Expected output is a success message like "Authtoken saved to configuration file...". If invalid, it will error with authentication failure.

### Step 3: Deploy HTTP Tunnel

**Context**: Create an HTTP tunnel to forward traffic from a public ngrok URL to your local HTTP service on port 4433. Use this for web-based C2 or exposing HTTP listeners.

**Command** ([[commands/deploy-ngrok-http-forwarding]]):
```bash
./ngrok http 4433
```

> This starts the tunnel and displays a public URL (e.g., https://abc123.ngrok.io). Expected output includes session status, tunnel details, and the forwarding URL. Press Ctrl+C to stop.

### Step 4: Deploy TCP Tunnel (Alternative)

**Context**: If HTTP forwarding isn't suitable (e.g., for non-HTTP protocols), use TCP tunneling to forward raw TCP traffic to port 4433. This is useful for SSH, databases, or custom listeners.

**Command** ([[commands/deploy-ngrok-tcp-forwarding]]):
```bash
./ngrok tcp 4433
```

> Similar to HTTP, this provides a tcp:// public endpoint. Expected output shows the TCP address (e.g., tcp://0.tcp.ngrok.io:12345). Verify by connecting from a remote machine.

### Step 5: Verify Tunnel Functionality

**Context**: Test the tunnel to ensure external access to the local service, confirming the bypass of firewall restrictions.

**Instructions**: Use curl or a browser to access the provided ngrok URL. For TCP, use telnet or nc to connect to the public endpoint.

> Example for HTTP: `curl https://your-ngrok-url.ngrok.io`. Expected output matches your local service's response. If it fails, check local service status and ngrok logs for errors.
