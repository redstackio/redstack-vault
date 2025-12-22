---
id: proc-extract-id
tags:
  - extraction
  - salesforce-id
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
updated_at: '2025-12-14T17:31:43.134Z'
skill_level: beginner
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-ContentDocument-ID-Response

## Summary

Parse the JSON response from the Aura query to extract Salesforce ContentDocument IDs for use in IDOR downloads.

## Description

The response contains an array of file records; extracting the 'Id' field from each item provides direct references to sensitive attachments, enabling targeted unauthorized access.

## Requirements

1. Successful query response JSON
2. Text editor or JSON parser (e.g., jq if scripting)

## Defense

Defensive measures and detection strategies:

- Mask sensitive IDs in API responses
- Enable field-level security on ContentDocument Id
- Log all queries to sensitive objects

## Objectives

1. Identify valid file IDs from response
2. Prepare for IDOR exploitation
3. Scale to multiple files

## Instructions

### Step 1: Inspect Response JSON

**Context**: Locate the items array in the response.

No command; open response in Burp or browser dev tools.

> Look for structure like {"items":[{"Id":"069830000028KJdAAM", ...}]}.

### Step 2: Copy ID Value

**Context**: Extract the specific ID string.

No command; copy the 18-character ID (e.g., 069830000028KJdAAM).

> Verify ID prefix (069 for ContentDocument); repeat for other records.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[extraction]]
