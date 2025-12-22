---
id: 123e4567-e89b-12d3-a456-426614174002
name: Initiate-SSRF-via-Calendar-Subscription
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.969Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - ssrf
  - nextcloud
  - calendar
platforms:
  - Web
commands:
  - '[[commands/nextcloud-calendar-ssrf-proxy]]'
tools:
  - '[[tools/Burp-Suite]]'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Initiate-SSRF-via-Calendar-Subscription

## Summary

This procedure exploits the lack of URL validation in the Nextcloud Calendar app's New Subscription feature to trigger SSRF, causing the server to fetch arbitrary URLs including internal ones.

## Description

The Calendar app's subscription mechanism sends requests to a proxy endpoint without checking for private IPs or localhost. By providing a malicious URL like `http://localhost/secret`, the server performs the HTTP request and returns the response. This targets authenticated users and can lead to data exfiltration. Prerequisites include an active session; outcomes include server-side access to internal resources.

## Requirements

1. Authenticated Nextcloud session
2. Burp Suite for request interception
3. Target URL pointing to internal resource (e.g., localhost)

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed URL domains in subscription features
- Block requests to private IP ranges and localhost
- Log and monitor outbound requests from the application server

## Objectives

1. Trigger SSRF via proxy endpoint
2. Fetch internal resource content
3. Observe unfiltered response

## Instructions

### Step 1: Navigate to Calendar App

**Context**: Access the vulnerable New Subscription feature.

Use web interface: Go to Calendar app > New Subscription.

> Enter malicious URL and submit. Expected output: Request sent to `/index.php/apps/calendar/v1/proxy?url=`.

### Step 2: Send SSRF Request

**Context**: Execute the proxy request with encoded malicious URL.

**Command** ([[commands/nextcloud-calendar-ssrf-proxy]]):
```bash
GET /nextcloud/nextcloud/index.php/apps/calendar/v1/proxy?url=http%3A%2F%2Flocalhost%2Fsecret HTTP/1.1
```

> This sends the request; expected output: Server response with internal file content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/nextcloud-calendar-ssrf-proxy]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[nextcloud]]
- [[calendar]]
