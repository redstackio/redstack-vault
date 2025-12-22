---
id: 54533bb8-1ded-4be7-9583-cc3f20306412
name: Web-SOCKS-Pivoting-with-Pivotnacci
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.606427+00:00'
updated_at: '2023-04-10T20:25:18.043696+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
sub_techniques:
  - '[[sub-techniques/Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]'
tags:
  - '[[tags/Network Pivoting Techniques]]'
  - '[[tags/Web SOCKS - pivotnacci]]'
commands:
  - '[[commands/pip-install-pivotnacci]]'
  - '[[commands/pivotnacci-run-with-password]]'
  - '[[commands/pivotnacci-run-with-polling-interval]]'
platforms:
  - Linux
tools:
  - '[[tools/pivotnacci]]'
validated: true
---

# Web-SOCKS-Pivoting-with-Pivotnacci

## Summary

Web SOCKS Pivoting with Pivotnacci is a technique used for lateral movement within a network. This procedure involves using a compromised web server as a pivot point to redirect network traffic through a SOCKS proxy, allowing attackers to bypass network security controls and access systems not directly reachable from the initial entry point.

## Description

This procedure details how to set up and use Pivotnacci to create a SOCKS proxy via an HTTP agent on a compromised web server. Pivotnacci polls the HTTP agent (e.g., a PHP agent on the target server) to tunnel traffic, enabling multi-hop proxying for further network exploration or exploitation. It is particularly useful in web application compromises where direct shell access is limited, but HTTP callbacks are possible. The technique modifies network routing effectively through the proxy, making traffic appear to originate from the legitimate web server, which complicates detection.

## Requirements

1. A compromised web server with an HTTP agent (e.g., PHP webshell) capable of handling polling requests.
2. Attacker machine with Python 3 and pip installed.
3. Network access to the compromised web server from the attacker side.
4. Administrative or shell access on the attacker machine to run proxy tools.

## Defense

Defensive measures and detection strategies:

- Deploy network segmentation to limit lateral movement and isolate compromised hosts.
- Monitor network traffic for anomalies such as unusual outbound connections from web servers or patterns indicative of proxying (e.g., high-frequency polling to external IPs).
- Implement strong authentication, web application firewalls (WAFs), and runtime application self-protection (RASP) to prevent initial web server compromise.
- Log and analyze HTTP request patterns on web servers for suspicious polling or agent-like behaviors.

## Objectives

1. Establish a SOCKS proxy through a compromised web server for pivoting.
2. Bypass firewalls and access internal network segments.
3. Maintain stealthy command and control via HTTP callbacks.

## Instructions

### Step 1: Install Pivotnacci

**Context**: Install the Pivotnacci Python package on the attacker machine to enable SOCKS proxy creation via HTTP agents. This step ensures the tool is available for subsequent proxy setup.

**Command** ([[commands/pip-install-pivotnacci]]):
```bash
pip3 install pivotnacci
```

> This command fetches and installs the Pivotnacci package from PyPI. It requires internet access and may prompt for confirmation if dependencies are needed. Verify installation by running `pivotnacci --help` afterward.

### Step 2: Run Pivotnacci with Password Authentication

**Context**: Launch the Pivotnacci proxy using an HTTP agent URL and secure it with a password. The password authenticates callbacks from the agent, preventing unauthorized use. This step creates the initial SOCKS tunnel.

**Command** ([[commands/pivotnacci-run-with-password]]):
```bash
pivotnacci https://domain.com/agent.php --password "s3cr3t"
```

> Replace `https://domain.com/agent.php` with the actual URL of the HTTP agent on the compromised server. The proxy will start listening locally (default port 1080) and begin polling the agent. Expected behavior includes confirmation of the connection and proxy readiness.

### Step 3: Configure Polling Interval if Needed

**Context**: Adjust the polling frequency for the HTTP agent to balance stealth and responsiveness. A longer interval reduces detectability but may slow down the proxy. Use this after basic setup or to optimize performance.

**Command** ([[commands/pivotnacci-run-with-polling-interval]]):
```bash
pivotnacci https://domain.com/agent.php --polling-interval 2000
```

> The `--polling-interval` is in milliseconds (2000ms = 2 seconds). Run this as a separate invocation or integrate with password option. Monitor for stable polling without errors in agent responses.
