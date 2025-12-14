---
id: proc-nextcloud-intent-craft-001
tags:
  - sqli
  - intent-crafting
  - android
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.012Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Intent-for-SQL-Injection-Bypass

## Summary

This procedure details crafting an Android intent with an SQL-injected projection to exploit the FileContentProvider in the Nextcloud app, targeting the ocshares table while bypassing URI restrictions.

## Description

Following source code analysis, construct an intent for the content resolver query using the vulnerable URI content://org.nextcloud/file. The projection parameter is manipulated with a payload like "* from ocshares --" to inject SQL, evading the partial restrictions and querying arbitrary SQLite tables in filelist.db. This requires ADB or app-level access to send intents.

## Requirements

1. ADB installed for intent execution on device/emulator
2. Nextcloud app installed and database populated with shares
3. Understanding of Android intents and content URIs

## Defense

Defensive measures and detection strategies:

- Enforce strict projection whitelisting in all content provider cases
- Log and validate all incoming intent projections
- Use Android's ContentProvider security features like path permissions

## Objectives

1. Create a bypass for isCallerNotAllowed check
2. Inject SQL to target specific tables like ocshares
3. Prepare intent for data extraction

## Instructions

### Step 1: Define URI and Projection

**Context**: Set the base URI and craft the injection payload.

No command; manually define: URI = content://org.nextcloud/file, Projection = "* from ocshares --".

> The "--" comments out remaining SQL to prevent errors.

### Step 2: Assemble Intent Structure

**Context**: Build the full intent for content.query().

> Include action as ACTION_QUERY, data as URI, and extras for projection; ensure it matches vulnerable cases (not ROOT_DIRECTORY).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sqli]]
- [[intent-crafting]]
- [[android]]
