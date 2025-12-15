---
id: 6384e689-87ed-4df7-91f5-0c96247fafa8
name: Test-FetLife-Endpoint-JSON-Behavior
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:34.925Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Information Repositories]]'
tags:
  - authorization-bypass
  - json-api
  - fetlife
  - recon
commands:
  - '[[commands/curl-test-fetlife-endpoint-json]]'
platforms:
  - Web
tools:
  - '[[tools/curl]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---

# Test-FetLife-Endpoint-JSON-Behavior

## Summary

This procedure tests the response behavior of FetLife's API endpoints for pictures, videos, and posts by requesting JSON format via the Accept header, revealing an authorization bypass where private resources are accessible without checks, unlike HTML responses.

## Description

In the FetLife web application, endpoints like /users/{user-id}/pictures/{pic-id} enforce privacy controls in HTML but fail to do so in JSON responses. This procedure involves sending HTTP GET requests with Accept: application/json to identify the discrepancy, allowing attackers to confirm the vulnerability before exploiting it for private content access. Prerequisites include knowledge of a target user ID and resource ID, typically obtained through prior reconnaissance or enumeration.

## Requirements

1. Network access to https://fetlife.com
2. curl tool installed
3. Basic understanding of HTTP headers and JSON responses

## Defense

Defensive measures and detection strategies:

- Implement consistent authorization checks across all response formats (JSON, HTML)
- Monitor API endpoints for unusual Accept header usage or JSON requests from non-API clients
- Rate-limit requests to user resource endpoints and log access to private content

## Objectives

1. Verify lack of authorization in JSON responses for private resources
2. Confirm vulnerability existence without triggering alerts
3. Gather baseline for further exploitation

## Instructions

### Step 1: Send Test Request to Picture Endpoint

**Context**: Probe the endpoint to observe JSON response without auth enforcement.

**Command** ([[commands/curl-test-fetlife-endpoint-json]]):
```bash
curl https://fetlife.com/users/{user-id}/pictures/{pic-id} -H "Accept: application/json" --user-agent "not cur1"
```

> This command sends a GET request forcing JSON output. Expected output is a JSON object with resource details if private, indicating bypass. Replace {user-id} and {pic-id} with known values.

### Step 2: Validate Response

**Context**: Check for absence of auth errors compared to HTML request.

**Command** ([[commands/curl-test-fetlife-endpoint-json]]):
```bash
curl https://fetlife.com/users/{user-id}/pictures/{pic-id} --user-agent "not cur1"
```

> Compare to default HTML request, which should redirect or deny access to private content.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-fetlife-endpoint-json]]

## Tools Used

- [[tools/curl]]

## Tags

- [[authorization-bypass]]
- [[json-api]]
- [[fetlife]]
- [[recon]]
