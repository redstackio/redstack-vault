---
tags:
  - exfiltration
  - download
  - metadata
type: procedure
tools:
  - '[[tools/Uppy]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T04:08:55.562Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: baa9e590-e45a-4ac5-9a3e-f945ea92d60e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Download-Exfiltrated-Internal-Content

## Summary

This procedure retrieves the uploaded file from the Uppy dashboard, which contains the raw response from the SSRF-fetched internal URL, allowing exfiltration of sensitive data like server metadata.

## Description

After SSRF triggers the fetch, the Companion server embeds the internal response (e.g., JSON metadata with instance ID, hostname) into a downloadable file via the Tus endpoint. Downloading this file completes the exfiltration, revealing information for further attacks like RCE or lateral movement. The impact includes access to local networks, file reads, and internal service interactions.

## Requirements

1. Successful URL submission and upload completion
2. Uppy dashboard showing the processed file
3. Browser download permissions enabled
4. Knowledge of target internal data (e.g., AWS IMDSv1)

## Defense

Defensive measures and detection strategies:

- Block file downloads containing internal responses by scanning upload contents
- Disable IMDSv1 and require tokens for metadata (IMDSv2)
- Log and alert on anomalous file uploads with internal data patterns
- Encrypt or restrict access to exfiltrated files in upload pipelines

## Objectives

1. Obtain the file with internal response
2. Analyze exfiltrated data for further exploitation
3. Confirm SSRF success

## Instructions

### Step 1: Initiate Download

**Context**: Use the dashboard to export the uploaded file.

**Instructions**: Click the file in the Uppy interface to trigger download.

> Expected: Browser prompts save; file named with URL hash or similar.

### Step 2: Inspect Content

**Context**: Open the downloaded file to verify internal data.

**Instructions**: Use a text editor or JSON viewer on the file.

> Expected: Content like {"id": "instance-id", "hostname": "server-name", "user-data": "..."}.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Uppy]]

## Tags

- exfiltration
- download
- metadata
