---
tags:
  - clickjacking
  - yelp
  - web
  - iframe
type: procedure
tools:
  - '[[tools/Bootstrap]]'
  - '[[tools/jQuery]]'
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
updated_at: '2025-12-14T17:28:04.388Z'
sub_techniques: []
id: ad030d1a-4e2a-4d11-8e62-704bc45ff914
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Yelp-Endpoint-for-ClickJacking

## Summary

This procedure identifies the Yelp business attribute editing endpoint vulnerable to ClickJacking by testing iframe embedding, confirming the absence of frame-busting protections like X-Frame-Options.

## Description

In a web-based attack scenario targeting Yelp, this procedure involves probing the specific endpoint https://www.yelp.com/biz_attribute?biz_id=RIyHYSf3lyJcFb4El9T4tQ to verify it can be loaded in an external iframe. This allows subsequent UI overlay attacks to trick authenticated users into editing business details. Prerequisites include basic web development knowledge and a browser for testing. Expected outcomes include confirmation of the vulnerability, enabling escalation to POC creation.

## Requirements

1. Access to a web browser for iframe testing
2. Knowledge of the target biz_id (e.g., RIyHYSf3lyJcFb4El9T4tQ)
3. Local HTML file creation capability

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on sensitive pages
- Monitor for unusual iframe embeddings via web application firewall (WAF) rules
- Educate users on phishing via fake forms or surveys

## Objectives

1. Confirm the endpoint loads in an external iframe
2. Verify editable business attributes are accessible
3. Establish foundation for UI redressing attack

## Instructions

### Step 1: Create Test HTML Page

**Context**: Build a simple HTML page to attempt embedding the Yelp endpoint in an iframe.

Create a local HTML file with the following structure:

```html
<!DOCTYPE html>
<html>
<head><title>Test Iframe</title></head>
<body>
<iframe src="https://www.yelp.com/biz_attribute?biz_id=RIyHYSf3lyJcFb4El9T4tQ" width="800" height="600"></iframe>
</body>
</html>
```

> Open the file in a browser. If the Yelp page loads without errors, the vulnerability exists.

### Step 2: Inspect for Frame Restrictions

**Context**: Check browser console and network tab for any frame-denial responses.

Load the page and inspect developer tools.

> Expected output: No errors like "Refused to display in a frame". Success if the form for editing name, email, etc., is visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Bootstrap]]
- [[tools/jQuery]]

## Tags

- clickjacking
- yelp
- iframe
