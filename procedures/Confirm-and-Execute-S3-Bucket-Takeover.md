---
id: proc-uuid-4
tags:
  - s3-takeover
  - bucket-squatting
type: procedure
tools:
  - '[[tools/can-i-take-over-xyz]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-create-bucket]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.832Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-and-Execute-S3-Bucket-Takeover

## Summary

This procedure validates and performs takeover of orphaned S3 buckets by creating identically named buckets, redirecting subdomain traffic for malicious use like phishing.

## Description

Using known techniques from resources like can-i-take-over-xyz, attackers claim deleted bucket names since S3 allows global unique naming. For Khan Academy, this hijacks event subdomains to spoof content. Target is AWS S3; prerequisites are verified dangling pointers; outcomes include full subdomain control.

## Requirements

1. AWS account for bucket creation
2. Confirmed non-existent bucket names
3. Access to upload static content

## Defense

Defensive measures and detection strategies:

- Reserve critical bucket names preemptively
- Monitor DNS for traffic to new S3 origins
- Implement website monitoring for subdomain changes

## Objectives

1. Reference takeover guides for confirmation
2. Create and configure squatted bucket
3. Deploy phishing payload

## Instructions

### Step 1: Consult Takeover Resources

**Context**: Review S3-specific takeover methods.

Use [[tools/can-i-take-over-xyz]] GitHub repo to confirm steps: search for 'S3' to see that creating the bucket name claims the CNAME.

### Step 2: Create the Bucket

**Context**: Use AWS tools to squat the name.

**Command** ([[commands/aws-s3-create-bucket]]):
```bash
 aws s3 mb s3://healthyhackathon.khanacademy.org --region us-east-1
```

> Success if bucket created without name conflict; DNS now points to your content. Configure public access and upload index.html with fake event page.

### Step 3: Verify Control

**Context**: Test subdomain resolution to new content.

Curl the subdomain to ensure it serves attacker-hosted files.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-create-bucket]]

## Tools Used

- [[tools/can-i-take-over-xyz]]

## Tags

- [[s3-takeover]]
- [[bucket-squatting]]
