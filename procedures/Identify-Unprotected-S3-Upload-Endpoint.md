---
id: proc-uuid-002
tags:
  - api-discovery
  - traffic-analysis
  - s3
type: procedure
tools:
  - '[[tools/Frida]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:20.926Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Unprotected-S3-Upload-Endpoint

## Summary

This procedure involves tracing network traffic from the BCM Messenger app after SSL bypass to identify the open API endpoint responsible for generating presigned S3 upload URLs.

## Description

With SSL pinning bypassed, app interactions (e.g., profile image upload) reveal HTTP requests to an unprotected endpoint at http://47.52.75.65:8080//v1/attachments/s3/upload_certification. This endpoint returns JSON with S3 presigned POST data, including bucket 'bcm-hk', access key, policy, and signature, without requiring authentication. This step uncovers the misconfiguration allowing public access.

## Requirements

1. SSL pinning bypassed via prior procedure
2. Traffic interception tool (e.g., mitmproxy, Burp Suite, or adb logcat)
3. Running instance of BCM Messenger app
4. Access to the API server IP (47.52.75.65:8080)

## Defense

Defensive measures and detection strategies:

- Enforce API authentication (e.g., JWT tokens or API keys) on all endpoints
- Rate-limit and log unauthenticated requests to upload endpoints
- Use WAF rules to block anomalous traffic patterns from mobile apps

## Objectives

1. Locate the vulnerable upload API endpoint
2. Extract initial presigned S3 response structure
3. Confirm lack of access controls

## Instructions

### Step 1: Trigger App Traffic

**Context**: Simulate user actions in the app to generate network requests.

Open the BCM Messenger app, navigate to profile settings, and attempt to upload a certification or image file.

**Expected Output**: App sends POST to the endpoint; capture via proxy.

### Step 2: Analyze Captured Traffic

**Context**: Inspect intercepted requests for the S3 upload endpoint.

Use mitmproxy or similar to filter HTTP POST requests:

```bash
mitmproxy -s script.py  # Where script.py logs S3-related JSON
```

Look for responses containing 'bcm-hk', 'AKIA3NG2JXZC3SY2WNXE', or 's3.ap-east-1.amazonaws.com'.

> The endpoint http://47.52.75.65:8080//v1/attachments/s3/upload_certification responds with JSON: {"downloadUrl": "...", "postUrl": "https://bcm-hk.s3.ap-east-1.amazonaws.com/", "key": "profile/...", "X-Amz-Credential": "...", etc.}

### Step 3: Validate Endpoint Accessibility

**Context**: Test the endpoint directly to confirm it's open.

Send a manual POST request using curl (no auth needed):

```bash
curl -X POST http://47.52.75.65:8080//v1/attachments/s3/upload_certification -d '{}'
```

**Expected Output**: JSON with presigned fields, no 401/403 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Frida]]

## Tags

- api-discovery
- reconnaissance
- s3-upload
