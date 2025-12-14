---
id: proc-linkedin-brute-force
tags:
  - brute-force
  - deletion
  - intruder
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/linkedin-delete-skill-assessment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:25:34.027Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Destruction]]'
---
# Brute-Force-Skill-ID-for-Deletion

## Summary

This procedure uses brute-forcing to identify the correct skill ID in the modified LinkedIn delete request, resulting in the removal of the victim's skill assessment and badge.

## Description

LinkedIn skill IDs are numeric (e.g., 280 for a specific skill), and the endpoint lacks proper checks, allowing trial-and-error. Burp Intruder sends requests at a low frequency (3/sec) to avoid detection. The target is the Voyager API; a 200 response confirms deletion. Verify impact by checking the victim's public profile.

## Requirements

1. Modified request in Burp Intruder with skill ID marked
2. Payload list of numeric IDs (e.g., 1-1000)
3. Valid session cookies and tokens

## Defense

Defensive measures and detection strategies:

- Implement ID validation and rate limiting on delete endpoints
- Anomaly detection for repeated failed deletions per profile
- Require CAPTCHA or secondary auth for bulk operations

## Objectives

1. Enumerate valid skill ID for the victim
2. Execute deletion on match
3. Confirm badge removal from profile

## Instructions

### Step 1: Configure Intruder Payload

**Context**: Set up the brute-force attack on the skill ID parameter.

In Burp Intruder, select 'Numbers' payload type, range 1-1000, step 1.

> Payloads generate; positions confirmed on skill URN.

### Step 2: Set Attack Options

**Context**: Control speed to evade throttling.

Under Options > Request Engine, set threads to 1, delay to 333ms (3 req/sec), total timeout 30s.

> Attack starts; monitor responses in Results table.

### Step 3: Execute and Identify Success

**Context**: Run the attack and filter for successful deletions.

Click 'Start Attack'; look for HTTP 200 or 204 responses differing from 404/403.

Use [[commands/linkedin-delete-skill-assessment]] for manual verification if needed:

```bash
curl -X DELETE "https://www.linkedin.com/voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/urn%3Ali%3Afsd_skillAssessmentAttemptReport%3A(urn%3Ali%3Afsd_profile%3A{victim-uuid}%2Curn%3Ali%3Askill%3A280%2C1)" -H "Authorization: Bearer {token}" -H "Csrf-Token: {csrf}"
```

> 200 response: {"status":200}; 4xx indicates invalid ID.

### Step 4: Verify Deletion

**Context**: Confirm impact on victim's profile.

Refresh victim's public profile; check for missing badge under skills section.

> Badge and assessment result absent if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Data Destruction]]

### Sub-Techniques


## Commands Used

- [[commands/linkedin-delete-skill-assessment]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[deletion]]
- [[intruder]]
