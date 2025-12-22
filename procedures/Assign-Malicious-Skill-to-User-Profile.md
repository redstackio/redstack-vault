---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - xss
  - profile-injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.792Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Assign-Malicious-Skill-to-User-Profile

## Summary

This procedure authenticates as the target user and creates a pentester profile, selecting the previously injected malicious skill to store the XSS payload in the user's profile data.

## Description

After enabling the pentester flag, log in to the application and navigate to the profile settings. The skill dropdown includes the malicious entry, which is assigned without sanitization, persisting the payload for backend rendering.

## Requirements

1. Enabled pentester flag on user
2. Valid credentials for the 'hacker' user
3. Local app running on port 8080

## Defense

Defensive measures and detection strategies:

- Sanitize skill selections during profile save
- Limit skill options to pre-approved list
- Log profile updates for anomalous content

## Objectives

1. Authenticate and access profile settings
2. Select and assign the malicious skill
3. Persist payload in user profile

## Instructions

### Step 1: Enable Feature Flag

**Context**: If required, set the 'pentester-profile' feature flag in the app config.

No command; edit config or use Rails console.

### Step 2: Authenticate and Create Profile

**Context**: Log in as 'hacker' and navigate to http://localhost:8080/settings/pentests, then choose the malicious skill.

Submit the profile form.

**Expected Output**: Profile created, skill assigned.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[profile-injection]]
