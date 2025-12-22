---
tags:
  - request-submission
  - attachment-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.260Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: f4f128bd-a89a-4948-8a57-d21b07f5838f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Submit Request with Attachment

## Summary

This procedure finalizes the exploit by submitting the DoD request form with the malicious file attached, completing the upload chain.

## Description

Upon submission, the file becomes part of the support ticket. In production, this could lead to staff downloading/opening the file, enabling RCE. Files were deleted post-report, but the attachment confirms the vulnerability. The endpoint is `███SubmitRequest/Index.cfm?fwa=wizardform`.

## Requirements

1. Form filled and file uploaded
2. Valid session on the form
3. No submission errors

## Defense

Defensive measures and detection strategies:

- Quarantine uploaded files for manual review
- Alert on suspicious file types in logs
- Disable auto-processing of attachments

## Objectives

1. Deliver the malicious file via legitimate channel
2. Confirm attachment persistence
3. Achieve potential impact through processing

## Instructions

### Step 1: Review and Submit

**Context**: Ensure attachment is included before finalizing.

Review the form and click 'Submit'.

> Expected output: Success message; request created with attachment.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[submission]]
- [[web]]
