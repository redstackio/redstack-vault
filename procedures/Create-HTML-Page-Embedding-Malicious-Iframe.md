---
id: proc-uuid-4
tags:
  - xss
  - html
  - iframe
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:10.455Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-HTML-Page-Embedding-Malicious-Iframe

## Summary

This procedure generates an HTML page that embeds the malicious Zomato widget URL in an iframe, allowing the XSS to execute when the page is loaded by a victim.

## Description

The HTML uses an iframe to load the crafted URL, styled to blend in. In the attack, this page is hosted or sent via phishing. Outcomes: Isolated delivery of the exploit, executing JS in the Zomato context upon load.

## Requirements

1. Text editor (e.g., VS Code)
2. Malicious URL from prior step
3. Local file system or web server for hosting

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options or CSP frame-ancestors to prevent embedding
- Scan for iframe sources pointing to sensitive domains
- Educate users on phishing pages mimicking widgets

## Objectives

1. Embed iframe without visual disruption
2. Ensure cross-origin loading
3. Prepare for victim interaction

## Instructions

### Step 1: Write Basic HTML Structure

**Context**: Create a simple page to host the iframe.

```html
<!DOCTYPE html>
<html><body>
<iframe src="MALICIOUS_URL" style="position:relative;width:100%;height:100%;"></iframe>
</body></html>
```

> Replace MALICIOUS_URL with the full URL; style hides borders.

### Step 2: Save and Test Locally

**Context**: Verify iframe loads the widget.

Save as exploit.html and open in browser.

> Expected: Widget appears; no immediate alert until Zomato context loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[html]]
