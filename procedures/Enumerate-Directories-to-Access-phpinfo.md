---
id: proc-uuid-001
tags:
  - directory-enumeration
  - information-disclosure
  - phpinfo
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
  - '[[Vulnerability Scanning]]'
  - '[[Hardware]]'
updated_at: '2025-12-14T17:30:07.351Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Hardware]]'
---
# Enumerate-Directories-to-Access-phpinfo

## Summary

This procedure uses directory enumeration to discover and access an exposed phpinfo() file on a web server, disclosing sensitive configuration details like OS version, PHP settings, loaded extensions, and environment variables without authentication.

## Description

In this attack scenario, an attacker targets a web application on a Linux/PHP stack where debugging files like info.php are left accessible over HTTP. Using a tool like Burp Suite Intruder, directories are fuzzed to identify the file. Accessing it reveals server internals, aiding further reconnaissance or exploit planning. The target environment is a public-facing web server with improper access controls, allowing HTTP access while HTTPS is restricted. Expected outcomes include full server config dump, enabling tailored attacks like extension-based exploits.

## Requirements

1. Network access to the target web server over HTTP
2. Burp Suite with Intruder module configured
3. Wordlist for common directories/files (e.g., including 'info.php')
4. Proxy setup to intercept and modify requests

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to phpinfo() files via .htaccess or server config (e.g., deny /info.php)
- Enforce authentication or IP whitelisting for sensitive paths
- Monitor access logs for enumeration patterns (high 404 rates from single IP)
- Use WAF rules to block directory fuzzing payloads

## Objectives

1. Discover hidden sensitive files through enumeration
2. Access and extract server configuration data
3. Identify access control weaknesses (e.g., HTTP vs HTTPS)

## Instructions

### Step 1: Configure Burp Suite Proxy and Target

**Context**: Set up interception to route traffic through Burp for manipulation.

Intercept the initial request to the target URL (e.g., http://target.com) and forward it to confirm connectivity.

### Step 2: Launch Directory Enumeration with Intruder

**Context**: Use Intruder to fuzz paths and identify responsive directories/files.

Send a GET request to http://target.com/§payload§ to Intruder. Load a wordlist (e.g., common PHP files like info.php, config.php). Set payload positions and launch the attack, sorting by response length or code to spot anomalies.

### Step 3: Analyze Results and Identify /info.php

**Context**: Review outputs to find the exposed file.

Look for 200 OK responses with PHP content signatures. Confirm /info.php by previewing the response body for phpinfo() output.

### Step 4: Access the File and Capture Output

**Context**: Directly retrieve the disclosed information.

Navigate to http://target/info.php in the browser or via Burp Repeater. Document the revealed details: OS (Linux 5.4.17-uggogamesdb), PHP config, extensions (e.g., curl, gd), and env vars. Test HTTPS to note the 403 block.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning
- [[Hardware]] Gather Victim Host Information: Hardware

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Intruder]]

## Tags

- [[directory-enumeration]]
- [[information-disclosure]]
- [[phpinfo]]
- [[Reconnaissance]]
