---
id: proc-uuid-1
tags:
  - graphql
  - magic-link
  - initial-access
type: procedure
tools:
  - '[[tools/Android-SDK]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/send-verification-email-graphql]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.321Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request-Verification-Email-via-GraphQL

## Summary

This procedure uses a GraphQL mutation to request a verification email for the Arrive app's magic link login, triggering the generation of a deeplink containing the login token. It serves as the initial step in phishing or proactive exploitation scenarios where the attacker has access to the target's email.

## Description

The Arrive app relies on magic links sent via email for passwordless login. By sending the SendVerificationEmail mutation to the GraphQL endpoint at arrive-server.shopifycloud.com, an email is dispatched with a deeplink to https://qvay.app.link/... including token parameters. This is exploitable if combined with deeplink interception, as the link lacks proper App Links verification. Prerequisites include the target's email address and network access to the API.

## Requirements

1. Target user's email address
2. Internet connectivity to arrive-server.shopifycloud.com
3. Optional: Access to device email via Android SDK for automation

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on verification email requests
- Monitor for anomalous GraphQL mutations from mobile User-Agents
- Educate users on verifying email senders

## Objectives

1. Trigger magic link email generation
2. Prepare for deeplink interception
3. Enable token extraction in subsequent steps

## Instructions

### Step 1: Prepare GraphQL Request

**Context**: Construct the mutation payload with the target email to initiate the login flow.

**Command** ([[commands/send-verification-email-graphql]]):
```bash
curl -X POST https://arrive-server.shopifycloud.com/graphql \
  -H "Content-Type: application/json" \
  -H "User-Agent: Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 5X Build/OPM7.181105.004)" \
  -d '{"operationName":"SendVerificationEmail","variables":{"email":"target@example.com"},"query":"mutation SendVerificationEmail($email: String!) { sendVerificationEmail(email: $email) { userErrors { field message __typename } __typename } }"}'
```

> This sends the mutation and mimics an Android client. Expected output: {"data":{"sendVerificationEmail":{"__typename":"SendVerificationEmailPayload","userErrors":[]}}} indicating success.

### Step 2: Monitor Email Delivery

**Context**: Check the target's email for the incoming magic link.

No command needed; manually or via app automation open the email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/send-verification-email-graphql]]

## Tools Used

- [[tools/Android-SDK]]

## Tags

- graphql
- magic-link
