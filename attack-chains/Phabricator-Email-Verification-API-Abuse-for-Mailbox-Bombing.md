---
tags:
  - email-bombing
  - dos
  - rate-limiting-bypass
  - phabricator
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Unverified-User-Account-in-Phabricator]]'
  - '[[procedures/Spam-Email-Verification-Requests-Using-PoC]]'
step_count: 2
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.247Z'
description: >-
  Abuse of Phabricator's email verification endpoint to perform unlimited resend
  requests, enabling email bombing and potential denial-of-service on target
  mailboxes.
id: 98f78dc2-de64-471f-b1fe-12ef4f50e19b
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
---

# Phabricator Email Verification API Abuse for Mailbox Bombing

Multi-stage attack chain demonstrating a complete attack workflow exploiting the lack of rate limiting in Phabricator's email verification system to bomb a target mailbox with verification emails.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Register Unverified Account] --> B[Spam Verification Requests]
    B --> C[Mailbox Overload DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for registration
- Text editor for creating HTML PoC

### Target Environment

- Phabricator instance (e.g., https://admin.phacility.com)
- Required services/ports: Web (HTTPS/443), Email service
- Network access requirements: Direct internet access to Phabricator

### Initial Access Requirements

- No prior credentials needed; registration is open
- Target email address for bombing
- Optional: Local Phabricator install for testing with auth.require-email-verification set to false

## Detailed Attack Procedures

### Step 1: Register Unverified User Account
procedure: [[procedures/Register-Unverified-User-Account-in-Phabricator]]

**Objective**: Create a new user account using the target's email address without requiring verification, triggering an initial verification email and setting up for repeated resends.

**Instructions**: Navigate to the Phabricator registration page and provide the target's email address along with arbitrary username and password. If the instance requires email verification for login (auth.require-email-verification=true), log in may be blocked, but the resend endpoint remains accessible post-registration.

**Expected Output**: Account created successfully; initial verification email sent to the target mailbox.

**Success Indicators**:
- Confirmation email received in target mailbox
- User account visible in Phabricator dashboard

### Step 2: Spam Email Verification Requests
procedure: [[procedures/Spam-Email-Verification-Requests-Using-PoC]]

**Objective**: Exploit the lack of rate limiting on the email verification resend endpoint to flood the target mailbox with repeated verification emails, causing denial-of-service.

**Instructions**: After registration, obtain the verification token from the initial email or dashboard. Create and load a custom HTML page with JavaScript to automate POST requests to the verification endpoint every 2 seconds. Increase the loop count to amplify the spam volume.

**Expected Output**: Multiple verification emails arriving in the target mailbox at rapid intervals.

**Success Indicators**:
- Target mailbox overwhelmed with emails (e.g., 100+ in minutes)
- No errors or throttling from the API

## Attack Chain Summary

### Key Achievements

1. Successful registration with arbitrary target email
2. Unlimited resend of verification emails via API abuse
3. Achieved denial-of-service on target email service through volume overload

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
