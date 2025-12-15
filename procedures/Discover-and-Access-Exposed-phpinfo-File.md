---
id: proc-uuid-5678
tags:
  - information-disclosure
  - phpinfo
  - directory-enumeration
  - reconnaissance
type: procedure
tools:
  - '[[tools/Burp-Suite-Intruder]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:29:09.594Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Gather Victim Host Information]]'
---
# Discover-and-Access-Exposed-phpinfo-File

## Summary

This procedure outlines the reconnaissance steps to enumerate directories on a target web server using Burp Suite Intruder, identify an exposed phpinfo() file, and access it unauthenticated to disclose sensitive server configuration details such as OS version, PHP settings, loaded extensions, and environment variables. It targets misconfigurations from leftover debugging files in PHP environments, commonly found on public-facing web servers.

## Description

In this attack scenario, an attacker begins by accessing the target domain and uses automated scanning to brute-force directories, uncovering /info.php which executes phpinfo() without protection. This reveals critical intelligence like Linux kernel details (e.g., 3.10.0-1160.80.1.el7.x86_64), PHP configuration (e.g., loaded modules like curl, openssl), and environment variables that could aid in crafting further exploits such as path traversal or extension-based attacks. The procedure assumes a web-based target with no authentication on the endpoint and requires only HTTP access. Expected outcomes include a full dump of server info usable for reconnaissance in broader attack chains.

## Requirements

1. Network access to the target web server (HTTPS on port 443)
2. Burp Suite Professional or Community Edition with Intruder module
3. A directory wordlist (e.g., SecLists or custom list including 'info.php')
4. Web browser for manual verification

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to debugging files like phpinfo() in production environments using .htaccess or server configs (e.g., deny /info.php)
- Implement web application firewalls (WAF) to block directory brute-forcing attempts by rate-limiting or signature-based detection
- Regularly scan for exposed sensitive files using tools like Nuclei or manual audits during deployments
- Monitor access logs for anomalous requests to non-standard paths like /info.php

## Objectives

1. Identify hidden endpoints through active scanning
2. Extract server configuration for vulnerability research
3. Enable follow-on attacks by understanding the tech stack

## Instructions

### Step 1: Access Target Domain

**Context**: Confirm the target is reachable to set up for enumeration.

No specific command; use a browser to visit https://██████████ and verify the page loads.

> This establishes the base URL for subsequent scanning. Expected output: Standard web page response without errors.

### Step 2: Configure and Run Directory Enumeration

**Context**: Use Burp Suite Intruder to fuzz paths and discover sensitive files.

Intercept a GET request to the root (/) using Burp Proxy, right-click and send to Intruder. Set payload position on the path (e.g., §§), load a wordlist with entries like 'info.php', and attack type to 'Sniper'. Launch the attack, filtering for 200 status codes.

> This automates brute-forcing to find /info.php. Expected output: Response lengths and codes indicating valid files, with /info.php showing PHP output snippet.

### Step 3: Access and Review phpinfo Output

**Context**: Manually retrieve and analyze the disclosed information.

Navigate directly to https://████████/info.php in the browser.

> No authentication is prompted, and the full phpinfo() table loads, detailing OS (Linux kernel 3.10.0-1160.80.1.el7.x86_64), PHP version, extensions (e.g., gd, mbstring), and env vars. Save or screenshot for analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Intruder]]

## Tags

- [[information-disclosure]]
- [[phpinfo]]
- [[directory-enumeration]]
- [[Reconnaissance]]
