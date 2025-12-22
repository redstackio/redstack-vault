---
tags:
  - hosting
  - web-server
  - csrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/python-simple-http-server]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.303Z'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques: []
id: 23f23e0e-6556-402a-8aab-a5afb2d623b2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-Malicious-CSRF-Page

## Summary

This procedure hosts the crafted CSRF HTML page on an attacker-controlled server, making it accessible via a URL for delivery to the victim, enabling the cross-site request forgery against UPchieve's vulnerable endpoints.

## Description

Once the malicious HTML is created, it must be served from a domain different from the target (UPchieve) to trigger the cross-site behavior. This exploits the lack of SameSite on session cookies, allowing the victim's browser to send the request with credentials. Simple hosting suffices, as the page only needs to load and submit the form; no advanced server features are required. Use local tools for testing or public hosting for real attacks.

## Requirements

1. Access to a server or machine with Python 3 installed
2. The crafted HTML file (e.g., csrf_poc.html)
3. Firewall/port access for serving (e.g., port 8000)

## Defense

Defensive measures and detection strategies:

- Block or monitor unexpected inbound hosting from unknown domains
- Use web application firewalls to detect anomalous form submissions
- Educate users on phishing links leading to non-official domains

## Objectives

1. Make the CSRF page publicly or targetedly accessible
2. Ensure reliable loading without CORS interference on submission
3. Minimize hosting footprint to avoid detection

## Instructions

### Step 1: Prepare the Hosting Directory

**Context**: Place the HTML file in a directory to serve.

Create a folder (e.g., /path/to/csrf) and copy csrf_poc.html into it.

### Step 2: Start the Web Server

**Context**: Use Python's built-in HTTP server to host the page statically.

Execute [[commands/python-simple-http-server]] from the directory:

```bash
python3 -m http.server 8000
```

> This starts a server on port 8000, serving files at http://localhost:8000/csrf_poc.html. For remote access, use 0.0.0.0 as bind address if needed: python3 -m http.server 8000 --bind 0.0.0.0. Expected output: Serving HTTP on 0.0.0.0 port 8000.

### Step 3: Verify Hosting

**Context**: Confirm the page is accessible and functional.

Visit http://your-ip:8000/csrf_poc.html in a browser (logged into target app) and inspect network tab for the POST submission.

**Expected Output**: Page loads, form submits to target endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/python-simple-http-server]]

## Tools Used


## Tags

- [[hosting]]
- [[web-server]]
- [[csrf]]
