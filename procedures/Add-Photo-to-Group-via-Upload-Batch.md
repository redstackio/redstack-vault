---
tags:
  - idor
  - exploitation
  - flickr
  - group-upload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.212Z'
sub_techniques: []
id: bebb8be7-fcea-4930-9a03-59593bbc642e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Photo-to-Group-via-Upload-Batch

## Summary

This procedure exploits Flickr's upload batch feature to add a third-party non-public photo to a group by directly referencing its ID, bypassing ownership and approval checks due to IDOR.

## Description

Flickr's group upload batch allows administrators to process multiple photos at once, but lacks verification that referenced photo IDs belong to the uploader. By crafting a batch with arbitrary IDs, attackers can inject private photos into public or member-visible groups. This requires group admin access and a discovered photo ID; outcomes include unauthorized photo association, exposing content to group members. The attack relies on the platform's direct object reference without permission validation.

## Requirements

1. Flickr account with admin rights to a target group
2. Discovered photo ID from prior reconnaissance
3. Access to the group's upload interface

## Defense

Defensive measures and detection strategies:

- Add ownership validation in batch processing APIs
- Require explicit owner consent for group additions
- Log and alert on cross-user photo references in batches

## Objectives

1. Inject non-owned photo into group pool
2. Bypass privacy restrictions via batch
3. Enable group-based exposure

## Instructions

### Step 1: Initiate Group Upload Batch

**Context**: Start the batch upload process in the group settings.

Log in to Flickr, go to the target group, and select the 'Upload to Group' option. Choose batch mode and prepare a list or interface for multiple entries.

### Step 2: Inject Photo ID

**Context**: Include the target ID in the batch to force addition.

In the batch input field or file, append the non-public photo ID (e.g., as a standalone entry or in a CSV-like format if supported). Submit the batch; the system processes it without checking ownership, adding the photo to the group.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[exploitation]]
