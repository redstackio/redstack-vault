---
id: p-download-internal-content
tags:
  - exfiltration
  - download
  - s3
  - concrete-cms
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
  - '[[Data from Local System]]'
updated_at: '2025-12-14T04:39:02.519Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Download Fetched Internal Content

## Summary

This procedure retrieves the SSRF-fetched internal content from Concrete CMS storage, allowing attackers to exfiltrate private network data via the legitimate download interface.

## Description

After SSRF exploitation, the CMS saves the fetched content (e.g., internal HTML/PHP output) as a file in its library, potentially synced to S3. Attackers can then download it directly from the dashboard, bypassing network restrictions. This step completes the pivoting chain by providing offline access to sensitive info for further analysis or attacks.

## Requirements

1. Successful prior SSRF fetch with content saved
2. Access to CMS file manager
3. Permissions to download files

## Defense

Defensive measures and detection strategies:

- Audit file uploads for anomalous content (e.g., scan for code snippets)
- Limit download permissions and monitor bulk exports
- Integrate storage (S3) logging to track unusual file saves

## Objectives

1. Access the stored internal data
2. Exfiltrate for external analysis
3. Use data to plan further internal exploits

## Instructions

### Step 1: Locate Saved File

**Context**: Find the uploaded file in the CMS library.

Navigate to Files > File Manager and search for the recently added file (e.g., named after the URL hash).

### Step 2: Initiate Download

**Context**: Retrieve the content securely via the interface.

Click the download button on the file entry. If S3-integrated, it pulls from cloud storage.

**Expected Output**: File downloaded to local machine containing internal page source.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Exfiltration]]
- [[download]]
