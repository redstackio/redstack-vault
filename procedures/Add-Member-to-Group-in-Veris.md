---
tags:
  - web
  - setup
  - group-association
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:15:31.463Z'
sub_techniques: []
id: 325ae362-480e-4b72-be50-1a50693da347
validated: true
---
# Add-Member-to-Group-in-Veris

## Summary

This procedure adds an existing member to a group in the Veris application, enabling asset linkages that facilitate stored XSS payload delivery in the members view.

## Description

As part of the XSS attack preparation, this step connects the created member to an existing group, ensuring the member's details page will reference associated assets. Performed via the groups management UI at https://sandbox.veris.in/portal/groups/. No malicious input here; outcome is updated group membership for chaining.

## Requirements

1. Existing member from prior step
2. At least one group in the system
3. Authenticated access to groups section

## Defense

Defensive measures and detection strategies:

- Audit group membership changes with alerts for bulk additions
- Restrict group modifications to admin roles
- Monitor for unusual patterns in member-group associations

## Objectives

1. Link member to group for asset visibility
2. Validate group management access
3. Set up for asset creation step

## Instructions

### Step 1: Navigate and Add Member

**Context**: Select a group and append the target member to its roster.

No command; UI action:

- Visit https://sandbox.veris.in/portal/groups/
- Choose an existing group (e.g., first available)
- Click 'Add Member' or edit option
- Search/select the member (e.g., 'Test Member')
- Confirm and save

> Expected: Member listed in group; no errors. This prepares the chain without execution.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[setup]]
