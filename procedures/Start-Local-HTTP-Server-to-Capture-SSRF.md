---
tags:
  - ssrf
  - capture
  - local-server
type: procedure
tools:
  - '[[tools/Python-SimpleHTTPServer]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/sudo-python-simplehttpserver]]'
platforms:
  - Linux
  - Web
techniques:
  - '[[Network Sniffing]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: b5ee013f-94c4-4284-b92c-8e9c141974aa
created_at: '2025-12-14T04:39:09.663Z'
updated_at: '2025-12-14T04:39:09.663Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Start-Local-HTTP-Server-to-Capture-SSRF

## Summary

This procedure starts a simple HTTP server on localhost port 80 using Python to listen for and log SSRF requests triggered by the Ghost oEmbed exploitation.

## Description

Python's built-in SimpleHTTPServer module creates a basic web server to handle incoming GET requests. Running it with sudo binds to port 80, allowing capture of requests from Ghost's internal fetch to resolved localhost addresses. This confirms the SSRF success and can be used to inspect request details.

## Requirements

1. Python 2/3 installed (uses http.server in Python 3)
2. Root privileges for port 80 binding
3. SSRF-triggering request sent prior or concurrently

## Defense

Defensive measures and detection strategies:

- Block unauthorized local servers on production hosts
- Monitor for ephemeral HTTP servers on low ports

## Objectives

1. Capture proof of SSRF exploitation
2. Log internal request details
3. Validate bypass effectiveness

## Instructions

### Step 1: Launch Local Server

**Context**: Start the server before sending the oEmbed request to catch the incoming SSRF traffic.

**Command** ([[commands/sudo-python-simplehttpserver]]):
```bash
sudo python -m SimpleHTTPServer 80
```

> For Python 3, use `python3 -m http.server 80`. Expected output: "Serving HTTP on 0.0.0.0 port 80 ..." followed by request logs like "127.0.0.1 - - [date] \"GET /index.html HTTP/1.1\" 200 -".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques


## Commands Used

- [[commands/sudo-python-simplehttpserver]]

## Tools Used

- [[tools/Python-SimpleHTTPServer]]

## Tags

- [[ssrf]]
- [[capture]]
- [[local-server]]
