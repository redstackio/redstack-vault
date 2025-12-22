---
id: proc-vimeo-direct-download-4
tags:
  - authorization-bypass
  - s3-download
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Amazon S3
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.811Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Direct-Download-URL-with-Track-ID

## Summary

This procedure constructs and accesses the /musicstore/download endpoint using the extracted track_id, exploiting the missing permission check to download paid tracks directly from Amazon S3 without payment.

## Description

The vulnerability lies in the GET endpoint /musicstore/download, which lacks verification of purchase status. By appending ?track_id=[ID]&license_id=4, it redirects to an S3 URL for the track file. This bypasses checkout, allowing unauthorized access to paid content. Target is Vimeo's web app integrated with S3; requires track_id from prior steps.

## Requirements

1. Extracted track_id from cart request.
2. Authenticated session (though not strictly enforced).
3. Browser or curl for GET request.

## Defense

Defensive measures and detection strategies:

- Add server-side permission checks on /musicstore/download to validate purchase.
- Monitor direct accesses to download endpoints and correlate with cart/purchase logs.
- Use signed S3 URLs with expiration and user-specific policies.

## Objectives

1. Bypass payment by direct endpoint access.
2. Retrieve the paid track file from S3.
3. Confirm unauthorized download success.

## Instructions

### Step 1: Construct Download URL

**Context**: Build the vulnerable URL using the track_id.

Replace [track_id] with the extracted value, e.g., https://vimeo.com/musicstore/download?track_id=110947&license_id=4.

> license_id=4 typically corresponds to a free or default license, but works for paid due to the flaw.

### Step 2: Send GET Request and Download

**Context**: Access the URL to trigger the S3 redirect and file download.

Navigate to the URL in the browser or use curl:

```bash
curl -L "https://vimeo.com/musicstore/download?track_id=110947&license_id=4" -o track.mp3
```

> The request redirects to an Amazon S3 URL (e.g., https://s3.amazonaws.com/...), downloading the MP3 without payment verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- curl-download-vimeo-track

## Tools Used


## Tags

- authorization-bypass
- s3-download
