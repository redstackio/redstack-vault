---
tags:
  - ssrf
  - ghost-cms
  - hosting
type: procedure
tools:
  - '[[tools/Python-SimpleHTTPServer]]'
  - '[[tools/ngrok]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python-simplehttpserver-host]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:53:38.709Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8cd9e85f-051f-4f48-8c15-2de248fda873
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-Malicious-HTML-Using-SimpleHTTPServer

## Summary

This procedure hosts the malicious HTML page locally using Python's SimpleHTTPServer or exposes it publicly via ngrok, allowing the Ghost oEmbed endpoint to fetch it.

## Description

Python SimpleHTTPServer serves static files on port 8000 for local testing. For remote Ghost instances, ngrok creates a tunnel to make the page publicly accessible without direct exposure.

## Requirements

1. Python 2.x installed (for SimpleHTTPServer)
2. Malicious HTML file (poc.html) in current directory
3. ngrok account/token for tunneling (optional)

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected HTTP servers on non-standard ports
- Block traffic to tunneling services like ngrok
- Inspect outbound fetches from application servers

## Objectives

1. Serve HTML for oEmbed fetch
2. Obtain accessible URL for exploitation
3. Ensure stability during testing

## Instructions

### Step 1: Start Local Server

**Context**: Host the HTML locally.

**Command** ([[commands/python-simplehttpserver-host]]):
```bash
python -m SimpleHTTPServer 8000
```

> Output: Serving HTTP on 0.0.0.0 port 8000 ... http://localhost:8000/poc.html is now accessible.

### Step 2: Expose via Tunnel (Optional)

**Context**: Make it public for remote targets.

Download and run ngrok http 8000 to get a public URL like https://abc123.ngrok.io/poc.html.

> Public URL ready for use in oEmbed request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/python-simplehttpserver-host]]

## Tools Used

- [[tools/Python-SimpleHTTPServer]]
- [[tools/ngrok]]

## Tags

- ssrf
- ghost-cms
- hosting
