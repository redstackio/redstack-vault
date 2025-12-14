---
tags:
  - libreoffice
  - processing
  - execution
  - unoconv
type: procedure
tools:
  - '[[tools/LibreOffice]]'
  - '[[tools/unoconv]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Cloud (AWS)
techniques:
  - '[[T1203.001]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8548bb0c-8fdc-4708-8eb7-b417c3f8564c
created_at: '2025-12-14T03:46:14.546Z'
updated_at: '2025-12-14T03:46:14.546Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1203.001]]'
---
# Trigger-LibreOffice-Thumbnail-Processing

## Summary

This procedure relies on Slack's automatic backend processing of uploaded Office files using LibreOffice and unoconv, executing the embedded LFI exploit during thumbnail generation.

## Description

Upon upload, Slack queues files for preview, invoking LibreOffice via unoconv to convert and generate thumbnails. The CVE-2019-17400 vulnerability in this pipeline allows the malicious file structure to enable local file access. This step is passive from the attacker's perspective, occurring server-side in an AWS container. Expected results include exploit activation without further input.

## Requirements

1. Successful file upload to Slack
2. Backend configured with vulnerable LibreOffice/unoconv
3. AWS container environment for processing

## Defense

Defensive measures and detection strategies:

- Isolate processing containers with minimal filesystem access
- Apply patches for CVE-2019-17400 immediately
- Log and alert on LibreOffice conversion errors or unusual file accesses

## Objectives

1. Activate vulnerability during conversion
2. Ensure exploit executes in isolated environment
3. Capture any output from file access attempts

## Instructions

### Step 1: Monitor Upload Queue

**Context**: After upload, Slack automatically processes the file for preview.

No direct action needed; processing triggers on backend receipt.

### Step 2: Invoke LibreOffice Conversion

**Context**: Backend uses unoconv to call LibreOffice for thumbnail creation.

The malicious structure exploits weaknesses in file parsing, leading to LFI.

### Step 3: Verify Processing Trigger

**Context**: Check Slack UI for preview status or errors indicating execution.

Backend logs would show LibreOffice invocation if accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[T1203.001]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/LibreOffice]]
- [[tools/unoconv]]

## Tags

- [[tools/LibreOffice]]
- [[tools/unoconv]]
