---
tags:
  - persistence
  - trigger
  - admin-compromise
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.172Z'
sub_techniques: []
id: b291e276-86a7-48e9-829e-e184b32816d6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Wait-for-Admin-to-Access-User-Record

## Summary

This passive procedure waits for an administrator to view the compromised user record in the Informatica admin panel, triggering the stored XSS payload to execute in their browser.

## Description

After injection, the payload remains dormant until an admin accesses the user details via the admin panel endpoint, such as https://█████████/phnx/driver.aspx?routename=Social/UniversalProfile/UserRecordEdit&TargetUser=480514&FromSearch=True#loaded or /admin/OrgUnitList.aspx. Upon rendering, the unsanitized Company field executes the script, capturing session data. This step relies on typical admin workflows like user reviews, with no active attacker intervention needed.

## Requirements

1. Injected payload in a visible user record
2. Patience for admin interaction (may take minutes to days)
3. Monitoring setup from previous steps

## Defense

Defensive measures and detection strategies:

- Role-based access controls to limit admin views
- Anomaly detection on admin panel access patterns
- Sandbox admin sessions or use no-JS views for reviews

## Objectives

1. Trigger payload in high-privilege context
2. Capture admin-specific data
3. Maintain stealth during wait

## Instructions

### Step 1: Deploy and Idle

**Context**: After injection, do nothing; the system handles persistence.

No command required; close the browser if desired.

> The payload is stored server-side and awaits admin query.

### Step 2: Verify Storage (Optional)

**Context**: If possible, log in as the user to confirm payload persistence.

No command required; check profile if editable.

> Expected output: Payload visible in user data (non-executing for regular users).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[Persistence]]
- [[trigger]]
