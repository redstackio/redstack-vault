---
id: proc-404797-capture-photo-ids
tags:
  - request-capture
  - parameter-extraction
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/zomato-photo-deletion-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.457Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture and Extract Photo IDs

## Summary

This procedure intercepts a legitimate photo deletion request in Zomato's manager interface to extract the photo_ids parameter, revealing the format used for IDOR exploitation.

## Description

During testing of restaurant-specific endpoints, a GET request to /php/client_manage_handler is captured when initiating photo deletion. The photo_ids[] parameter (e.g., r_YxNDUOTE4MTYzO) is extracted, prefixed with 'r_' for restaurant photos. This step requires an authenticated manager session and focuses on identifying the IDOR vector without actual deletion. The target is Zomato's PHP-based web app, with outcomes including saved IDs for cross-restaurant use.

## Requirements

1. Active restaurant manager session (from prior setup)
2. Proxy or browser dev tools for request interception
3. Access to a restaurant with uploadable photos

## Defense

Defensive measures and detection strategies:

- Log and monitor all requests to client_manage_handler for anomalous photo_ids
- Implement client-side validation of photo ownership before submission
- Rate-limit deletion requests per res_id to detect bulk or foreign ID attempts

## Objectives

1. Intercept and analyze deletion request structure
2. Extract usable photo_ids for manipulation
3. Understand endpoint parameters like res_id and case

## Instructions

### Step 1: Navigate to Photo Management

**Context**: Position the session to trigger the deletion flow.

Using the first account, go to https://www.zomato.com/clients/manage_photos.php and select a photo to delete.

**Expected Output**: UI prompts deletion; network tab shows pending request.

### Step 2: Intercept and Extract

**Context**: Capture the request before submission to analyze parameters.

Initiate deletion and intercept the GET request using [[commands/zomato-photo-deletion-request]]:

```http
GET /php/client_manage_handler?res_id=REDACTED&photo_ids%5B%5D=r_YxNDUOTE4MTYzO&removable=1&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
X-Requested-With: XMLHttpRequest
Cookie: REDACTED
Connection: close
```

> This command captures the request; extract photo_ids[] (e.g., r_YxNDUOTE4MTYzO) and note res_id.

**Expected Output**: photo_ids saved; optional {"status":"success"} if allowed to proceed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/zomato-photo-deletion-request]]

## Tools Used


## Tags

- interception
- id-extraction
