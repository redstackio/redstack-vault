---
tags:
  - data-exfiltration
  - file-download
  - bypass
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.931Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 10ada844-a1a6-4ff6-bb5f-525bc8e6d6a6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Download-Personal-Folder-to-Access-Deleted-File

## Summary

This procedure completes the bypass by downloading a personal folder containing a shortcut to a deleted file, allowing the resolution of the link to retrieve unauthorized content from Lark Technologies' storage.

## Description

Once a shortcut to a deleted file is placed in a personal folder, downloading the folder triggers the shortcut resolution, which fetches the original file content without respecting deletion status. This exploits the file sharing download mechanism in the cloud-based Lark platform. Requires an authenticated session and the prior shortcut setup. Expected outcome: Full access to sensitive deleted data via the downloaded archive.

## Requirements

1. Personal folder with the shortcut to the deleted file
2. Valid user session in Lark
3. Local storage space to save the download

## Defense

Defensive measures and detection strategies:

- Scan downloads for shortcut resolutions to restricted files
- Rate-limit folder downloads and audit for unusual patterns
- Purge deleted file content from backend storage immediately upon deletion

## Objectives

1. Retrieve deleted file content through shortcut indirection
2. Exfiltrate sensitive data bypassing admin controls
3. Validate the vulnerability's impact on data exposure

## Instructions

### Step 1: Select Personal Folder

**Context**: Prepare the folder for download in the Lark UI.

**Actions**:
- Log in to Lark.
- Navigate to the personal folder containing the shortcut.

> Folder displays with the shortcut visible; select it for download.

### Step 2: Initiate Folder Download

**Context**: Trigger the download to resolve the shortcut and access content.

**Actions**:
- Click 'Download' on the folder.
- Wait for the archive to generate and save locally.

> Download succeeds; the ZIP or archive includes the resolved deleted file.

### Step 3: Extract and Verify

**Context**: Confirm access to the unauthorized content.

**Actions**:
- Extract the downloaded folder on local machine.
- Open the shortcut-resolved file to view content.

> File contents are intact, demonstrating successful bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[data-exfiltration]]
- [[file-download]]
- [[bypass]]
