---
tags:
  - pii-disclosure
  - email-notification
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:29:44.848Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6aca48b6-77d6-4a97-bf81-0c3e24bcb0db
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Trigger-and-Observe-PII-Disclosure-Email

## Summary

This procedure observes the outcome of the modified GraphQL mutation, where the failure still triggers an email notification disclosing the target user's PII across organizations.

## Description

After sending the tampered UpdateOrganizationUserRole mutation, the backend rejects the request due to organization mismatch but processes the notification logic, sending an email to the admin with the target's first name, last name, and email. This exploits insufficient validation in the notification path. Expected outcome is receipt of unauthorized PII via email.

## Requirements

1. Admin email access for the Shopify Plus account
2. Completion of prior request modification
3. Awareness of potential email delays (up to a few minutes)

## Defense

Defensive measures and detection strategies:

- Ensure notification emails are only sent after full authorization checks
- Audit email logs for PII disclosures to unauthorized recipients
- Implement rate limiting on user role mutations

## Objectives

1. Confirm mutation failure
2. Receive and verify PII in notification email
3. Document the disclosed information for impact assessment

## Instructions

### Step 1: Monitor API Response

**Context**: Check the immediate response from the forwarded request.

Observe the HTTP response in the proxy tool; expect a GraphQL error like invalid user or permission denied.

> Error indicates failure but does not halt notification.

### Step 2: Check Admin Email Inbox

**Context**: Wait for and inspect the triggered notification email.

Refresh email client; look for Shopify notification about role change attempt.

> Email contains target's first name, last name, and email address, confirming disclosure.

### Step 3: Validate Disclosure

**Context**: Confirm the PII belongs to a cross-organization user.

Cross-reference the disclosed details against known information or organization boundaries.

> Unauthorized PII access verified if details match external user.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Data from Information Repositories

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[pii-disclosure]]
- [[email-notification]]
