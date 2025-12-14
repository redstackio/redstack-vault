---
tags:
  - information-disclosure
  - data-analysis
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Email Addresses]]'
updated_at: '2025-12-14T17:25:12.924Z'
skill_level: novice
impact_level: medium
detection_risk: low
sub_techniques: []
id: f8e2e25d-1e93-4270-8b6b-f1f883017187
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Email Addresses]]'
---
# Analyze JSON Response

## Summary

This procedure parses and extracts sensitive information from the JSON response obtained from the HackerOne invitation endpoint, focusing on researcher email and private program details.

## Description

After accessing the endpoint, the JSON response contains unprotected fields exposing the researcher's email address and private program metadata, including name, handle, state, profile picture URL, and program URL. This step involves manual or scripted analysis to identify and document the leaked data, highlighting the privacy and confidentiality impacts in a web-based bug bounty context.

## Requirements

1. JSON response from the invitation endpoint
2. Text editor or JSON viewer
3. Basic understanding of JSON structure

## Defense

Defensive measures and detection strategies:

- Censor sensitive fields in API responses for unaccepted invitations (e.g., mask email, remove program details)
- Implement data loss prevention (DLP) scanning on API outputs
- Audit and rotate exposed tokens promptly after incidents

## Objectives

1. Extract email and program details from JSON
2. Assess the scope of disclosed information
3. Document impacts for reporting or exploitation

## Instructions

### Step 1: Save Response

**Context**: Capture the JSON output for inspection.

No command; redirect or copy the curl output to a file, e.g., invitation.json.

> Ensure the file contains the full JSON structure.

### Step 2: Parse and Extract Data

**Context**: Review key fields for sensitive content.

No command required; open invitation.json in a text editor and locate fields:
- 'email': Researcher's email address
- 'team': Object with 'name' (program name), 'handle' (program handle), 'state', 'profile_picture' (URL), 'url' (program URL)

> Expected output: Documented leaks, e.g., Email: researcher@example.com, Program: Private Prog (handle: prog-handle).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Email Addresses]] Gather Victim Identity Information: Email Addresses

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[information-disclosure]]
- [[data-analysis]]
