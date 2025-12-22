---
tags:
  - gdpr
  - email-spoofing
  - account-deletion
  - misconfiguration
type: attack_chain
tools:
  - '[[tools/SendGrid]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Email
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Spoof-GDPR-Deletion-Request]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.291Z'
description: >-
  A misconfiguration in GitLab's GDPR data deletion process allows attackers to
  spoof emails from a victim's address to trigger unauthorized account deletion
  without authentication.
skill_level: intermediate
impact_level: high
id: 3a29b8d2-ba3d-4af0-a6cf-429683ae152f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized GitLab Account Deletion via Spoofed GDPR Email Request

Multi-stage attack chain exploiting a misconfiguration in GitLab's GDPR data deletion workflow, allowing unauthorized account termination via unauthenticated email spoofing.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes active + days for processing |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Spoofed GDPR Request] --> B[Victim Receives Confirmation]
    B --> C[Account Deletion Processed]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/SendGrid]]

### Target Environment

- GitLab SaaS platform
- Access to SMTP service for spoofing
- Victim's email address

### Initial Access Requirements

- No prior credentials needed
- Ability to spoof sender email
- Knowledge of victim's email

## Detailed Attack Procedures

### Step 1: Send Spoofed GDPR Deletion Request
procedure: [[procedures/Spoof-GDPR-Deletion-Request]]

**Objective**: Initiate the deletion process by spoofing an email from the victim's address to GitLab's GDPR endpoint, requesting account removal under GDPR rights.

**Instructions**: Use an SMTP service like SendGrid to craft and send an email with the victim's address as the sender. The email body should reference GDPR Article 17 (right to erasure) and provide the victim's username or email for identification.

**Expected Output**: Email successfully sent; no immediate response from GitLab.

**Success Indicators**:
- Email delivery confirmation from SMTP provider
- No bounce-back errors

### Step 2: Victim Receives Confirmation Email

**Objective**: GitLab's automated system sends a confirmation to the spoofed victim's email, acknowledging the request without requiring further verification.

**Instructions**: Monitor for the confirmation email arriving in the victim's inbox (attacker does not interact here; this is passive).

**Expected Output**: Victim receives an email from GitLab confirming the deletion request and outlining the process timeline.

**Success Indicators**:
- Confirmation email observed in victim's mailbox
- No additional authentication prompted

### Step 3: Account Deletion Occurs

**Objective**: GitLab processes the request after a short period (typically a few days), resulting in permanent account deletion.

**Instructions**: Wait for GitLab's internal processing; no further action required from attacker.

**Expected Output**: Victim's GitLab account is deleted, revoking access to repositories, issues, and data.

**Success Indicators**:
- Victim reports loss of access
- Attempted login fails with account not found

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication in GDPR workflow via email spoofing
2. Triggered automated account deletion without victim consent
3. Demonstrated potential for widespread account disruption in GitLab

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
