---
id: proc-verify-changes-001
tags:
  - verification
  - impact-assessment
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software Discovery]]'
updated_at: '2025-12-14T17:25:23.588Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Software Discovery]]'
---
# Verify Changes from Victim Account

## Summary

This procedure switches back to the victim account to inspect the scorecard, confirming the success of unauthorized modifications, permission assignments, and any download activities performed by the attacker.

## Description

Post-exploitation validation ensures the IDOR impact by observing persistent changes from the owner's perspective. Log back into the victim session, access the scorecard via legitimate means, and review alterations. In demo.sftool.gov, this reveals edited data, new permissions, and potential audit logs of downloads, highlighting the vulnerability's severity without additional tools.

## Requirements

1. Victim account credentials
2. Known scorecard access path
3. Prior knowledge of original state

## Defense

Defensive measures and detection strategies:

- Enable user notifications for object changes
- Implement immutable audit logs for all modifications
- Alert on permission changes outside owner sessions

## Objectives

1. Confirm data integrity loss
2. Validate unauthorized permission grants
3. Assess exfiltration evidence

## Instructions

### Step 1: Switch Back to Victim

**Context**: Re-authenticate as owner.

No specific command; log out of attacker, then log in with victim credentials.

> Victim dashboard loads.

### Step 2: Access Scorecard Legitimately

**Context**: View from owner's interface.

No specific command; navigate to /tws or scorecard list, select the test scorecard.

> Original URL loads with visible changes.

### Step 3: Inspect Modifications

**Context**: Document impact.

No specific command; review content for edits, check permissions for new entries, and look for download history.

> Altered data, added permissions, and download confirmation indicate success.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Software Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[post-exploit]]
- [[verification]]
- [[access-control]]
