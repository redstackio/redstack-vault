---
id: proc-construct-clickjacking-poc
tags:
  - clickjacking
  - poc
  - html
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.717Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Construct-Clickjacking-POC-HTML

## Summary

This procedure creates a simple HTML proof-of-concept (PoC) page that embeds a vulnerable target site in an iframe, demonstrating the ability to frame the site for clickjacking attacks without X-Frame-Options restrictions.

## Description

Targeted at sites like WordPress-based WordCamp.org, this builds a malicious page that loads the target in an iframe, allowing attackers to overlay transparent elements for user deception. The scenario involves local file creation; prerequisites are a text editor and browser access. Outcomes include a testable PoC that visually confirms framing, leading to impacts like unauthorized actions or phishing.

## Requirements

1. Text editor (e.g., vim, notepad)
2. Knowledge of basic HTML structure
3. Confirmed vulnerable target from prior header check

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options header to block framing
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict embedding domains
- Scan for PoC-like HTML files in testing environments

## Objectives

1. Generate an embeddable iframe for the target URL
2. Set up a basic page to host the iframe
3. Prepare for browser-based validation of the exploit

## Instructions

### Step 1: Create HTML File

**Context**: Write the HTML code to include an iframe sourcing the vulnerable site.

No command; manually create file:

```html
<html lang='en-US'>
<head>
<meta charset='UTF-8'>
<title>Clickjacking POC</title>
</head>
<body>
<h3>This site is vulnerable to clickjacking</h3>
<iframe src='https://central.wordcamp.org/' frameborder='2px' height='500px' width='500px'></iframe>
</body>
</html>
```

> Save as clickjacking-poc.html. This uses standard iframe attributes; the missing header allows loading.

### Step 2: Verify File Syntax

**Context**: Ensure the HTML is well-formed before testing.

Open in a text editor and check for syntax errors; no automated command needed.

> Expected: Valid HTML with iframe element pointing to target.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[poc-construction]]
