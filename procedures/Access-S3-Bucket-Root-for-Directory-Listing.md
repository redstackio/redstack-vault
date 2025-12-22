---
id: proc-uuid-005
tags:
  - s3
  - directory-listing
  - disclosure
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Cloud (AWS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:25:18.268Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Access-S3-Bucket-Root-for-Directory-Listing

## Summary

This procedure directly accesses the root of the public S3 bucket to exploit directory listing, allowing enumeration and download of all private images.

## Description

Due to public read permissions and enabled directory listing on `ping-api-production.s3.us-west-2.amazonaws.com`, navigating to the root URL lists all objects without authentication. This exposes images from other stores, enabling data theft. The attack relies on the extracted bucket name from prior steps.

## Requirements

1. Extracted S3 bucket URL from previous inspection
2. Web browser for direct access
3. No AWS credentials needed (public access)

## Defense

Defensive measures and detection strategies:

- Disable public access and directory listing on S3 buckets
- Enable AWS CloudTrail logging for bucket access
- Use bucket policies to restrict anonymous reads
- Monitor for unusual GET requests to root

## Objectives

1. Trigger directory listing at bucket root
2. View and download unauthorized images
3. Confirm scope of disclosure

## Instructions

### Step 1: Construct Root URL

**Context**: Use extracted bucket info.

From the image URL, derive the root: `https://ping-api-production.s3.us-west-2.amazonaws.com/`.

> Expected: Valid bucket endpoint.

### Step 2: Navigate and Browse

**Context**: Exploit public permissions.

Enter the root URL in [[tools/Web-Browser]] and load the page.

> Expected: XML or HTML listing of objects, including images from other users.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage Object

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- s3-access
- public-exposure
