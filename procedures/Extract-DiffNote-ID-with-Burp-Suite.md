---
id: uuid-extract-id-burp
tags:
  - gitlab
  - id-extraction
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:25:53.156Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Extract-DiffNote-ID-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept the deletion of a DiffNote, extracting its global ID, then creates a new DiffNote to obtain an incremental ID for the exploit.

## Description

Delete the existing DiffNote while proxying traffic through Burp Suite to capture the ID in the request (e.g., gid://gitlab/DiffNote/116). Immediately create another DiffNote; IDs are incremental, so the next is 117 or 118. This ID is crucial for the destroySnippet mutation to resolve to a non-snippet object like DiffNote, bypassing type checks in authorized_find!.

## Requirements

1. Burp Suite configured as proxy
2. Existing DiffNote from merge request
3. Maintainer session active

## Defense

Defensive measures and detection strategies:

- Proxy traffic inspection for ID leaks
- Rate-limit DiffNote deletions

## Objectives

1. Capture global ID during deletion
2. Generate new DiffNote for valid ID
3. Obtain ID for mutation input

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception for GitLab requests.

No specific command; in Burp, configure browser proxy to 127.0.0.1:8080.

> Ensure all GitLab traffic routes through Burp.

### Step 2: Delete DiffNote and Extract ID

**Context**: Trigger deletion to intercept ID.

No specific command; in MR discussion, delete the comment (DiffNote).

> In Burp Proxy > HTTP history, find the deletion request and extract ID from payload (e.g., id: "gid://gitlab/DiffNote/116").

### Step 3: Create New DiffNote

**Context**: Generate next incremental ID.

No specific command; add another comment on the diff.

> Note the new ID will be sequential; use Burp if needed to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- gitlab
- id-extraction
- burp-suite
