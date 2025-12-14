---
id: uuid-modify-idor
tags:
  - idor
  - parameter-tampering
  - authorization-bypass
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
updated_at: '2025-12-14T17:28:59.259Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Modify-Request-for-Arbitrary-Team-ID

## Summary

Alter the API request URI and body to target the members endpoint with an unauthorized teamId, exploiting IDOR to access restricted data.

## Description

Change from getTeamLastUpdateTs to members endpoint, set limit=0 for full results, orderBy=login, and inject arbitrary teamId while retaining auth params. This bypasses team-specific authorization.

## Requirements

1. Extracted login and uki
2. Known arbitrary team ID (e.g., from prior recon or guessing)
3. Burp Repeater tab open

## Defense

Defensive measures and detection strategies:

- Implement strict authorization checks on teamId against user teams
- Validate input parameters server-side
- Log and alert on mismatched teamId/user associations

## Objectives

1. Craft IDOR payload
2. Preserve authentication
3. Target unauthorized resources

## Instructions

### Step 1: Update URI

**Context**: Switch to exploitable endpoint.

**Instructions**: In Repeater, change Raw URI to https://ws1.dashlane.com/1/teamPlans/members.

### Step 2: Edit Body Parameters

**Context**: Inject arbitrary teamId.

**Instructions**: Set body to URL-encoded: limit=0&login=<your_login>&orderBy=login&teamId=<arbitrary_id>&uki=<your_uki>. Use [[commands/curl-dashlane-team-members]] for equivalent testing.

> Ensure no syntax errors in encoding.

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

- idor
- tampering
