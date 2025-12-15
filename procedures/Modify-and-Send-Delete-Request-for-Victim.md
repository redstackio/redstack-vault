---
id: proc-modify-delete-request
tags:
  - idor-exploit
  - request-modification
  - api-abuse
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Stored Data Manipulation]]'
updated_at: '2025-12-14T17:25:47.461Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Stored Data Manipulation]]'
---
# Modify-and-Send-Delete-Request-for-Victim

## Summary

This core exploitation procedure modifies the captured DELETE request in Burp Suite by substituting the victim's ProfileId and ImageId, then sends it to unauthorizedly remove the target's featured image.

## Description

Using the legitimate request as a base, replace the parameters in the URL: /voyager/api/voyagerIdentityDashProfileTreasuryMedia/urn:li:fsd_profileTreasuryMedia:(victim_ImageId,victim_ProfileId)?sectionUrn=urn:li:fsd_profile:victim_ProfileId. The authenticated attacker session allows the API to process the request without ownership checks, exploiting the IDOR. This leads to data manipulation on the victim's profile.

## Requirements

1. Captured request in Burp Repeater
2. Extracted victim IDs
3. Active authenticated session in Burp

## Defense

Defensive measures and detection strategies:

- Enforce ownership validation on API endpoints (e.g., check if ProfileId matches user ID)
- Audit logs for cross-profile API calls and alert on mismatches

## Objectives

1. Bypass authorization via ID substitution
2. Execute unauthorized deletion
3. Confirm API response indicates success

## Instructions

### Step 1: Edit Request Parameters

**Context**: Substitute IDs to target the victim.

In Burp Repeater, update the URL path and query: replace original ImageId and ProfileId with victim's, including in the URN and sectionUrn.

### Step 2: Send Modified Request

**Context**: Replay the request to trigger deletion.

Ensure headers (e.g., CSRF token, auth cookies) are intact, then click 'Send' or 'Forward'.

**Expected Output**: Response code 200/204 with success message; no 403/401 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Stored Data Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor-exploit]]
- [[request-modification]]
- [[api-abuse]]
