---
tags:
  - clickjacking
  - poc
  - iframe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.580Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 18986801-3f19-45d2-b590-53df1e9dde92
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Clickjacking-Proof-of-Concept-HTML-File

## Summary

This procedure creates a basic HTML file to test clickjacking by embedding the target site in an iframe, verifying if the site's framing protections are bypassed in Chrome due to an invalid X-Frame-Options header.

## Description

Clickjacking POCs simulate UI redressing attacks by framing sensitive sites. For Periscope.tv, the POC embeds the homepage in an iframe, which loads successfully in Chrome because the 'ALLOW-FROM' header is ignored. This step requires a text editor and local web server; outcomes include confirmation of framability, setting up for impact demonstration. The attack scenario targets authenticated users, but this POC focuses on basic embedding.

## Requirements

1. Text editor (e.g., VS Code)
2. Local web server (e.g., Python http.server)
3. Chrome browser

## Defense

Defensive measures and detection strategies:

- Enforce strict X-Frame-Options or CSP frame-ancestors
- Browser extensions to detect iframes
- Web Application Firewall (WAF) rules for anomalous embedding attempts

## Objectives

1. Construct HTML with iframe targeting the vulnerable site
2. Host and load the POC in Chrome to test framing
3. Validate no blocking occurs

## Instructions

### Step 1: Write HTML File

**Context**: Create a simple HTML document that includes an iframe sourcing the target URL.

**Command** (Manual file creation):

```html
<!DOCTYPE html>
<html>
<head><title>Clickjacking POC</title></head>
<body>
<iframe src="https://www.periscope.tv/" width="800" height="600"></iframe>
</body>
</html>
```

> Save as Clickjacking_Periscope.html. This embeds the site without overlays for initial testing.

### Step 2: Serve and Test

**Context**: Host the file locally and open in Chrome to confirm loading.

**Command** (Using Python server):
```bash
python -m http.server 8000
```

> Navigate to http://localhost:8000/Clickjacking_Periscope.html in Chrome. Expected: Site loads in iframe without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web-exploit]]
