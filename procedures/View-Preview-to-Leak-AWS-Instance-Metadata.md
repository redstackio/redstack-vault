---
id: proc-infogram-leak-metadata-001
tags:
  - data-leak
  - aws-metadata
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[T1210.001]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:32:10.701Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1210.001]]'
  - '[[Cloud Instance Metadata API]]'
---
# View-Preview-to-Leak-AWS-Instance-Metadata

## Summary

This procedure accesses the dashboard preview of the SSRF-infographic, causing the backend to fetch and embed AWS metadata in the generated image, leaking sensitive internal data.

## Description

The preview process on Infogram's AWS instance resolves the iframe src internally, capturing response in the image. This exposes metadata service data publicly. Prerequisites: SSRF payload stored. Target: Dashboard library view. Outcomes: Visible leak of instance details, potentially credentials.

## Requirements

1. Infogram session
2. SSRF infographic created
3. Ability to inspect preview images

## Defense

Defensive measures and detection strategies:

- Restrict preview rendering to external URLs only, blocking private IPs
- Use network segmentation to isolate metadata services from app servers
- Scan preview images and logs for internal endpoint access

## Objectives

1. Trigger SSRF during preview generation
2. Capture and view leaked metadata
3. Assess further exploitation like credential theft

## Instructions

### Step 1: Access SSRF Infographic in Library

**Context**: Locate the modified project.

Navigate to https://infogram.com/app/#/library and find the new infographic.

> Lists projects; select by title. Expected: Thumbnail preview loads.

### Step 2: Inspect Preview for Leak

**Context**: Observe embedded internal data.

Open the project; examine the preview image for AWS metadata response (e.g., instance-id, IAM roles).

> Image renders iframe content from backend fetch. Expected: Text like 'ami-id: xxx' visible if permissions allow.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[T1210.001]] Exploitation of Remote Services
- [[Cloud Instance Metadata API]] Cloud Instance Metadata

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- exfiltration
- preview-leak
