---
id: proc-uuid-3
tags:
  - phabricator
  - json-manipulation
  - spoofing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:11.076Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Manipulate JSON Payload for Feed Spoofing

## Summary

Craft a modified JSON payload for the feed.publish API by substituting spoofed PHIDs, enabling impersonation or false access implications without code execution.

## Description

The 'data' parameter in feed.publish accepts JSON with 'authorPHID', 'tokenPHID', and 'objectPHID'. Replace 'authorPHID' with a target user's PHID to spoof them, set 'objectPHID' to a restricted item's PHID to imply access, and retain a valid 'tokenPHID' (e.g., 'PHID-TOKN-medal-4' for a medal award story). This exploits the API's pre-policy design, allowing arbitrary manipulation. Prerequisites include obtained PHIDs; outcomes are payloads ready for submission, potentially creating misleading stories like "User X awarded token to restricted project Y".

## Requirements

1. Collected PHIDs from prior reconnaissance
2. JSON editor or scripting for payload construction
3. Understanding of Phabricator feed story types

## Defense

Defensive measures and detection strategies:

- Add server-side PHID ownership and access verification before publication
- Sanitize and validate all JSON inputs against user permissions
- Alert on feed stories referencing objects outside user scope

## Objectives

1. Create impersonation-capable payload
2. Include restricted object references
3. Ensure payload syntactic validity for API acceptance

## Instructions

### Step 1: Build Base Payload

**Context**: Start with a template JSON for 'PhabricatorTokenGivenFeedStory' type.

**Instructions**: Use a text editor to construct: {"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted"}. Validate with jsonlint or similar.

> Expected: No syntax errors; fields match API expectations.

### Step 2: Customize for Spoofing

**Context**: Insert specific PHIDs to target impersonation or IDOR simulation.

**Instructions**: Substitute values: authorPHID from user extraction, objectPHID from restricted reference. Test encode in URL for API submission.

> Success if payload implies false actions, e.g., spoofed user awarding to hidden project.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phabricator
- json-manipulation
- spoofing
