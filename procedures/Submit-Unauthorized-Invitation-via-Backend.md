---
id: proc-uuid-3
tags:
  - unauthorized-invite
  - business-logic
  - account-addition
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:57.082Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1078.004]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Submit Unauthorized Invitation via Backend

## Summary

This procedure exploits the lack of rate limit validation on HackerOne's backend invite endpoint to send invitations to unauthorized emails, such as those of other security researchers, potentially adding unintended members to the sandbox organization.

## Description

After accessing the hidden endpoint, the form submission POSTs to the backend without checking the UI rate limit. Entering an email like `0620@wearehackerone.com` and submitting triggers an invitation email, bypassing frontend restrictions. This business logic flaw allows unauthorized expansion of organization membership, risking data exposure or further compromises. Assumes authenticated access and loaded form from prior steps.

## Requirements

1. Loaded invite form from the hidden endpoint.
2. Target email address (e.g., another researcher's HackerOne-associated email).
3. Authenticated browser session.

## Defense

Defensive measures and detection strategies:

- Synchronize rate limits across UI and backend APIs.
- Audit invitation logs for anomalies, such as rapid or external emails.
- Require additional verification for invites (e.g., CAPTCHA or approval workflows).

## Objectives

1. Send invitation without rate limit enforcement.
2. Add unauthorized member to the organization.
3. Demonstrate impact of logic bypass.

## Instructions

### Step 1: Enter Target Email Address

**Context**: Input the email of an unintended recipient to test bypass.

In the form's email field, type an address like `0620@wearehackerone.com`.

### Step 2: Submit the Invitation Form

**Context**: Trigger the backend processing to send the invite.

Click the submit button on the form.

**Expected Output**: Success message indicating invitation sent, or email dispatched to the recipient.

### Step 3: Verify Invitation Delivery

**Context**: Confirm the bypass worked by checking for receipt.

Monitor the recipient's email or organization members list for the new invite/pending member.

**Expected Output**: Recipient receives HackerOne invitation email; member appears as pending if accepted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Sub-Techniques

- [[T1078.004]]

## Commands Used


## Tools Used


## Tags

- [[unauthorized-invite]]
- [[business-logic]]
- [[account-addition]]
