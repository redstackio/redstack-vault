---
tags:
  - mongodb
  - api
  - error-trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-mongodb-error]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:18.142Z'
sub_techniques: []
id: d293929e-3065-4ed9-aa12-a4242c53796a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger MongoDB Error in Semrush API

## Summary

This procedure involves sending malformed inputs to the Semrush API's site audit endpoint to provoke a MongoDB backend error, revealing potential injection points for further exploitation like XSS.

## Description

The Semrush API endpoint /reports/v1/projects/:id/siteaudit/page/list processes the 'url' parameter, which can trigger database errors if invalid. These errors expose unsanitized reflections, setting the stage for reflected XSS. This is typically done during reconnaissance of API vulnerabilities in web applications using MongoDB.

## Requirements

1. Access to a valid Semrush project ID
2. API authentication token if required
3. Tool for HTTP requests (e.g., curl or Burp Suite)

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization before database queries
- Use error handling that logs internally without exposing details to responses
- Deploy WAF rules to detect error-triggering patterns

## Objectives

1. Provoke and observe MongoDB error in API response
2. Identify reflection opportunities for injection attacks
3. Confirm backend technology stack

## Instructions

### Step 1: Prepare the Request

**Context**: Replace placeholders with actual project ID and auth token to target the endpoint.

**Command** ([[commands/curl-trigger-mongodb-error]]):
```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=invalid_input" -H "Authorization: Bearer YOUR_API_TOKEN"
```

> This sends a GET request with an invalid 'url' to trigger the error. Expected output includes a MongoDB-specific error message in the JSON response body.

### Step 2: Analyze Response

**Context**: Inspect the response for error details confirming MongoDB usage.

No specific command; use response parsing tools or manual inspection.

> Look for phrases like "MongoError" or stack traces mentioning MongoDB.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-mongodb-error]]

## Tools Used


## Tags

- [[mongodb]]
- [[api]]
- [[error-trigger]]
