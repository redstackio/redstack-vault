---
id: proc-slack-load-external-001
tags:
  - external-resource
  - avatar
  - s3
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:12.496Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Load-External-Image-as-Avatar

## Summary

This procedure triggers the loading of the manipulated external URL in Slack's photo endpoint, displaying and storing the image as an avatar on S3.

## Description

Following URL manipulation, accessing the page causes Slack's backend to fetch the external image, crop it if needed, and save it to AWS S3. This was reported as RFI but confirmed as designed behavior for external file integration, with limited impact to cosmetic changes.

## Requirements

1. Modified URL from prior procedure
2. Browser session active

## Defense

Defensive measures and detection strategies:

- Scan S3 uploads for unexpected external origins
- Rate-limit avatar upload requests

## Objectives

1. Display external image
2. Confirm storage on S3
3. Validate no code execution

## Instructions

### Step 1: Access Modified URL

**Context**: Initiate fetch and display.

No command required; press Enter on the edited URL or refresh the page.

> External image loads in crop tool; may create two S3 files.

### Step 2: Verify Avatar Update

**Context**: Check persistence.

No command required; complete crop and save; view profile.

> External image set as avatar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[external-resource]]
- [[avatar]]
- [[s3]]
