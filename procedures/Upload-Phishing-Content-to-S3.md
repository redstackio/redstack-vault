---
tags:
  - phishing-upload
  - s3-public
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:38:49.376Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a30b635b-6f6f-4cab-9e9a-9d1ff967b354
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Phishing-Content-to-S3

## Summary

This procedure uploads a malicious HTML file mimicking a login page to the S3 bucket and sets public permissions to serve phishing content.

## Description

The index.html contains a form that posts credentials to an attacker-controlled endpoint. Public read policy exposes it via the subdomain, tricking users into submitting data.

## Requirements

1. Configured S3 bucket with hosting
2. Phishing HTML file prepared
3. AWS permissions for upload and policy

## Defense

Defensive measures and detection strategies:

- Enforce S3 block public access
- Scan uploads for malicious content
- Monitor for anomalous traffic to subdomains

## Objectives

1. Deploy fake login page
2. Enable public access
3. Capture user inputs

## Instructions

### Step 1: Prepare and Upload File

**Context**: Create phishing HTML and upload.

Create index.html with Bime login form that exfils to attacker's server, then:
In Console: Upload > index.html.

> File added to bucket root.

### Step 2: Set Public Policy

**Context**: Allow anonymous read.

In Permissions: Bucket policy > Edit > Add JSON for public read on objects.

```json
{"Version":"2012-10-17","Statement":[{"Sid":"PublicRead","Effect":"Allow","Principal":"*","Action":"s3:GetObject","Resource":"arn:aws:s3:::a2.bime.io/*"}]}
```

> Policy applied.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phishing-upload]]
- [[s3-public]]
