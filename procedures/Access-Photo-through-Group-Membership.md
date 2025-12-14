---
tags:
  - idor
  - access
  - flickr
  - collection
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.207Z'
sub_techniques: []
id: eb3f5181-b188-4e3a-9702-f97677f84da5
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Photo-through-Group-Membership

## Summary

This procedure grants unauthorized viewing access to a non-public photo by leveraging Flickr group membership after it has been added via IDOR exploitation.

## Description

Once a private photo is added to a group through the vulnerable batch process, group visibility rules override the original privacy settings, allowing any member to view the content. This step involves navigating the group interface to locate and render the photo using its ID or group search. Prerequisites are group membership and prior addition success; expected outcomes include full photo exposure, demonstrating the IDOR's impact on data confidentiality.

## Requirements

1. Membership in the target Flickr group
2. Knowledge of the added photo's ID or group location
3. Standard web access to Flickr

## Defense

Defensive measures and detection strategies:

- Revoke group visibility for non-owned photos
- Audit group additions for unauthorized sources
- Implement per-photo permission inheritance checks

## Objectives

1. View private photo content via group
2. Collect exposed media and metadata
3. Validate IDOR impact

## Instructions

### Step 1: Navigate to Group Pool

**Context**: Locate the added photo within the group's photo collection.

Log in to Flickr, go to the group page, and open the 'Photos' or pool section. Search or browse for the recently added photo using keywords or the ID if searchable.

### Step 2: View and Extract Content

**Context**: Access the full photo details.

Click on the photo thumbnail or direct link (e.g., https://www.flickr.com/groups/[group_id]/pool/[photo_id]). The image and details load due to group permissions, exposing private content.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[Collection]]
