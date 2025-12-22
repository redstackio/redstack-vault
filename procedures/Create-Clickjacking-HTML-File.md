---
tags:
  - clickjacking
  - iframe
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
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:05.161Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: f743a3ad-a339-4af3-bddb-3434cff52868
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Clickjacking-HTML-File

## Summary

This procedure creates a simple HTML file containing an iframe that attempts to embed a target website, used to test for clickjacking vulnerabilities due to missing anti-framing headers like X-Frame-Options.

## Description

In scenarios where a web application lacks the X-Frame-Options header, attackers can embed the site in an iframe on a malicious page. This enables UI redressing attacks, where invisible overlays trick users into clicking on hidden elements, potentially leading to unauthorized actions such as form submissions or data disclosure. This procedure focuses on generating the embedding HTML for demonstration on static pages like those hosted on AWS S3.

## Requirements

1. A text editor such as Notepad or any basic code editor.
2. Knowledge of the target URL vulnerable to embedding, e.g., https://www.legalrobot.com/swag/.
3. Local machine access without network restrictions.

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses to prevent framing.
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict embedding sources.
- Monitor for unusual iframe usage in web traffic logs and scan for header absences using tools like securityheaders.com.

## Objectives

1. Produce a functional HTML snippet that embeds the target site.
2. Set the stage for verifying the vulnerability.
3. Highlight the risk of clickjacking in web applications.

## Instructions

### Step 1: Open Text Editor and Input HTML Code

**Context**: Start by launching a text editor to compose the embedding page. This step builds the core iframe element targeting the vulnerable URL.

No command execution required; manually paste the following HTML:

```html
<html>
<body>
<iframe src="https://www.legalrobot.com/swag/" width="500" height="500"></iframe>
</body>
</html>
```

> This code creates a basic page with a 500x500 iframe sourcing the target static page. Upon success, the iframe will render the content without blocking.

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
- [[iframe-embedding]]
- [[web-vulnerability]]
