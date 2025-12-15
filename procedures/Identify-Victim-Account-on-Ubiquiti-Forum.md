---
id: proc-identify-victim-ubnt
tags:
  - account-discovery
  - discovery
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
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:30.074Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-Victim-Account-on-Ubiquiti-Forum

## Summary

This procedure identifies a target victim's user account on community.ubnt.com by extracting their numeric user ID, which is essential for IDOR exploitation in account deletion.

## Description

User profiles on the forum expose numeric IDs in URLs (e.g., /user/John_victim?id=12345), allowing easy discovery. For testing, create a victim account; in real scenarios, enumerate via search or public profiles. This step leverages poor ID obfuscation, enabling targeted attacks without advanced tools.

## Requirements

1. Access to the forum's search or profile browsing features
2. Authenticated session (from attacker account)
3. Browser developer tools to inspect URLs

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove user IDs from public URLs
- Log and monitor profile access patterns for anomalies
- Implement role-based visibility for user details

## Objectives

1. Retrieve the victim's numeric user ID
2. Confirm the account's existence and activity
3. Minimize exposure during enumeration

## Instructions

### Step 1: Search for Victim

**Context**: Locate the victim's profile to expose the ID.

Use the forum's search function at https://community.ubnt.com/index.php?/search/ with the victim's username (e.g., John_victim).

> Click on the profile link; inspect the URL for the ?id= parameter value.

### Step 2: Verify ID

**Context**: Confirm the ID corresponds to the target account.

Navigate directly to https://community.ubnt.com/index.php?/profile/<id> using the extracted numeric ID.

> Profile loads with victim's details, validating the ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-discovery]]
- [[Discovery]]
- [[web]]
