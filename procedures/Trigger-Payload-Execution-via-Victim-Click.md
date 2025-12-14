---
tags:
  - xss
  - phishing
  - execution-trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.470Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 17bef297-db7f-4c41-a6ba-5f1c8dd16db9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
  - '[[JavaScript]]'
---
# Trigger-Payload-Execution-via-Victim-Click

## Summary

This procedure simulates victim interaction by having them click a phishing link to the injected URL, triggering the XSS payload to execute and exfiltrate data to the attacker's server.

## Description

Once the malicious URL is visited, the browser decodes the callback, injects the SVG into the page, and fires the onload event, causing a redirect that appends document.domain to the attacker's URI. The referer header reveals the Glassdoor origin. This relies on social engineering for delivery. Expected outcome: Data exfiltration without direct attacker interaction.

## Requirements

1. Crafted malicious URL from prior steps
2. Phishing delivery method (e.g., email, SMS)
3. Attacker server to receive and log requests

## Defense

Defensive measures and detection strategies:

- Educate users on phishing link avoidance
- Implement browser-based protections like XSS auditors
- Monitor network traffic for unexpected redirects to external domains
- Use referer policy to strip sensitive info from headers

## Objectives

1. Execute JavaScript in the victim's authenticated session
2. Exfiltrate domain information via GET request
3. Confirm attack success through server logs

## Instructions

### Step 1: Distribute the Malicious Link

**Context**: Deliver the URL to the target victim via phishing.

Craft a convincing message, e.g., "Check out this job listing on Glassdoor: [malicious URL]".

> Send via email or messaging. Expected output: Victim receives and clicks the link.

### Step 2: Monitor Exfiltration

**Context**: Observe the payload execution on the victim's side.

On the attacker server (e.g., interact.sh), watch for incoming GET requests.

> Expected request: URI `/glassdoor.com`, referer `https://www.glassdoor.com/job-listing/spotlight?...`. This confirms domain exfiltration and origin.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Phishing]]
