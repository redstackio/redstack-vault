---
id: p2b3c4d5-e6f7-8901-bcde-f23456789012
tags:
  - publication-creation
  - id-extraction
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.346Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-Offline-Publication-and-Extract-sourceDocumentId

## Summary

This procedure creates an offline publication on Publitas and extracts the associated sourceDocumentId, providing a reference ID format for IDOR manipulation.

## Description

Offline publications in Publitas are non-public catalogs generated for internal use. Creating one via the dashboard triggers API calls that assign a unique sourceDocumentId. This ID is used in subsequent requests and can be inspected via browser developer tools or network logs. The procedure assumes an authenticated session and results in a testable publication ID, essential for crafting IDOR payloads targeting other users' content.

## Requirements

1. Active Publitas account
2. Web browser with developer tools
3. Permissions to create publications

## Defense

Defensive measures and detection strategies:

- Log all publication creation events and audit ID assignments
- Restrict ID visibility to prevent extraction

## Objectives

1. Create a sample offline publication
2. Capture the sourceDocumentId for reference
3. Understand ID structure for exploitation

## Instructions

### Step 1: Access Publication Creation

**Context**: Log in and navigate to the publication management section.

From the dashboard, select 'Create New Publication' and choose 'Offline' mode.

### Step 2: Configure and Generate

**Context**: Set up basic publication details to trigger generation.

Fill in minimal required fields (e.g., title, pages) and submit to generate the offline version.

### Step 3: Extract sourceDocumentId

**Context**: Inspect the creation response for the ID.

Open browser dev tools (Network tab), monitor the API call during generation, and copy the sourceDocumentId from the response JSON (e.g., {"sourceDocumentId": "12345"}).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[publication-creation]]
- [[id-extraction]]
