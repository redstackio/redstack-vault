---
id: proc-federate-share-folder
tags:
  - federated-sharing
  - nextcloud
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:23:24.871Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Federate-Share-Malicious-Folder-to-Target

## Summary

This procedure shares the malicious folder from the evil instance to the target Nextcloud using federated sharing, making it available as external storage.

## Description

Leveraging Nextcloud's federated feature, the attacker shares the folder containing blacklisted files. The target accepts the share, exposing the contents without initial local copy.

## Requirements

1. Evil instance with shared folder ready
2. Target instance with federated sharing enabled
3. Valid user credentials on both

## Defense

Defensive measures and detection strategies:

- Review and approve external shares manually
- Block shares from untrusted domains
- Log and alert on new federated shares

## Objectives

1. Propagate malicious folder to target
2. Maintain external storage status
3. Prepare for local copy

## Instructions

### Step 1: Initiate Share from Evil Instance

**Context**: Use sharing UI to federate.

Select 'sharefolder', choose federated share, enter target server URL and remote user.

> Expected output: Share token generated.

### Step 2: Accept Share on Target

**Context**: Receive and accept on target.

In target, go to shares, enter evil server URL and token, accept.

> Expected output: Folder appears as 'External storage' in files.

### Step 3: Verify Contents

**Context**: Check malicious files visible.

Browse the shared folder; .htaccess and attack.php should be listed.

> Expected output: Files viewable but not executable yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- federated-share
