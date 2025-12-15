---
id: proc-002
tags:
  - impersonation
  - deletion-request
  - broken-access-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:29:36.900Z'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Access Removal]]'
---
# Submit-Impersonated-Account-Deletion-Request

## Summary

This procedure details filling and submitting a support ticket form using a victim's email address to request account deletion, exploiting the system's reliance on email alone without additional verification for inactive accounts.

## Description

Once the support form is open, attackers input the victim's registered email and craft a deletion request, impersonating the owner. The form, accessible without authentication, creates a ticket processed by support staff who fail to confirm ownership via PIN, payment history, or other checks—especially for inactive accounts without purchases. This leads to database-level account removal. The attack targets the web-based email support system integrated with the account database.

## Requirements

1. Victim's email address
2. Access to the open support form from previous procedure
3. Basic knowledge of crafting plausible support requests

## Defense

Defensive measures and detection strategies:

- Enforce strict verification protocols for deletion requests, including multi-factor auth or manual review with callbacks
- Audit support ticket logs for submissions from unauthenticated sessions or suspicious IPs
- Block or flag deletion requests for accounts without recent activity or purchases

## Objectives

1. Create a support ticket impersonating the victim to trigger deletion
2. Bypass access controls relying solely on email matching
3. Achieve unauthorized impact on the victim's account

## Instructions

### Step 1: Input Victim Details

**Context**: Populate the form with impersonated information to mimic a legitimate owner request.

No command required; use form fields:

Enter the victim's email address in the 'From' or email field. In the message body, write: "Please delete my account associated with this email as I no longer need it."

> The form accepts the input without validation, creating the ticket under the victim's email.

### Step 2: Specify Deletion for Inactive Account

**Context**: Enhance plausibility to avoid scrutiny, targeting the weakness for inactive accounts.

No command required; add to message:

Include details like "This is an inactive account without any purchases," to align with the system's lax checks.

> Submission proceeds, queuing the request for support processing.

### Step 3: Submit the Form

**Context**: Finalize the ticket creation as an unauthorized user.

No command required; click submit:

Click the submit button on the form.

> Expect a confirmation message indicating the ticket has been created; no login or auth is enforced.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Access Removal]] Account Access Removal

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[impersonation]]
- [[deletion-request]]
- [[broken-access-control]]
