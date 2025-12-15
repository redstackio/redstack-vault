---
id: proc-003
tags:
  - waiting
  - processing
  - support-ticket
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
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:29:36.896Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Account Access Removal]]'
---
# Monitor-Support-Processing

## Summary

This procedure involves passively waiting for the NordVPN support team to process the submitted deletion ticket, during which the lack of checks allows the action to proceed to completion.

## Description

After submission, the ticket enters the support queue. The team processes requests based on email matching without additional verification, leading to database deletion for the impersonated account. This step highlights the time-based nature of the exploit, typically requiring 2-4 hours, and targets the email support system's integration with the account database.

## Requirements

1. Submitted ticket from previous procedure
2. Patience for processing delay
3. Optional: Attacker email to monitor any responses (though not required)

## Defense

Defensive measures and detection strategies:

- Implement automated delays or queues with AI-assisted anomaly detection for deletion requests
- Train support staff to always verify identity beyond email for destructive actions
- Use ticketing system alerts for high-risk requests like deletions from new or unauthenticated sources

## Objectives

1. Allow support to action the ticket without intervention
2. Exploit the verification gap in processing
3. Transition to confirmation of impact

## Instructions

### Step 1: Initiate Waiting Period

**Context**: Begin the passive monitoring phase post-submission.

No command required; time-based action:

Wait 2-4 hours for support to review and process the ticket.

> During this time, the team matches the request to the victim's email and executes deletion if no flags are raised.

### Step 2: Optional Response Check

**Context**: If provided, check for any support acknowledgments, though none are typically sent to attackers.

No command required; browser check:

Refresh any confirmation page or check spam for responses (rare).

> Success is inferred by lack of rejection; proceed to verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Account Access Removal]] Account Access Removal

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[waiting]]
- [[processing]]
- [[support-ticket]]
