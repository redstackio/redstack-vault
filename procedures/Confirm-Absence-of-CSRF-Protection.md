---
tags:
  - csrf
  - web-security
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:18.579Z'
sub_techniques: []
id: 636ea5dd-1650-4296-8598-f0b3e757a67d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Confirm Absence of CSRF Protection

## Summary

This procedure verifies the lack of CSRF tokens in a POST endpoint, enabling cross-origin form submissions that can escalate self-XSS to victim-targeted attacks.

## Description

The /index.php endpoint in Joomla processes POST requests without validating CSRF tokens, allowing external sites to submit forms on behalf of users. This is critical for chaining with XSS. Target: Web apps with AJAX endpoints. Outcome: Successful unauthorized submission from another origin.

## Requirements

1. Target endpoint accessible via HTTP POST.
2. Ability to craft requests from a different origin (e.g., local file).
3. Browser for cross-origin testing.

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens in all state-changing POST requests.
- Use SameSite cookies and CORS policies to restrict origins.
- Log and alert on cross-origin requests.

## Objectives

1. Test for token requirement in legitimate requests.
2. Attempt cross-origin submission.
3. Confirm processing without authentication barriers.

## Instructions

### Step 1: Inspect Legitimate Form

**Context**: Check the original form for token fields.

Load the registration page in [[tools/Firefox]] and inspect the HTML source for hidden CSRF inputs.

### Step 2: Test Cross-Origin POST

**Context**: Submit from an external context without token.

Create a simple HTML file with a form targeting /index.php and submit. Example:

```html
<form action="https://target/index.php" method="POST">
  <input type="hidden" name="task" value="azrul_ajax">
  <input type="hidden" name="option" value="community">
  <input type="hidden" name="func" value="register,ajaxCheckEmail">
  <input type="hidden" name="arg2" value='["test","email@example.com"]'>
  <input type="submit">
</form>
<script>document.forms[0].submit();</script>
```

> Save and open in browser. Expected: Request processes without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- csrf
