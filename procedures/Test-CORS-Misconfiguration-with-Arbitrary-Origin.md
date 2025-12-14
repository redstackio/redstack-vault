---
id: proc-uuid-1
name: Test-CORS-Misconfiguration-with-Arbitrary-Origin
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.185Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - cors
  - testing
  - web
commands: []
platforms:
  - Web
tools:
  - '[[tools/XMLHttpRequest-API]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Test-CORS-Misconfiguration-with-Arbitrary-Origin

## Summary

This procedure tests for CORS misconfigurations by sending a crafted HTTP request to an API endpoint with an arbitrary Origin header, verifying if the server echoes it back without validation.

## Description

In the context of Semrush's API, this involves sending a GET request to /organic-traffic-insights/api/rest/1.2/users/{user_id}/projects with a fake Origin like https://itqayzlbkshw.com and authentication cookies. The goal is to check if the response allows cross-origin access with credentials, enabling potential data theft. Prerequisites include access to the endpoint and a valid user session for testing.

## Requirements

1. Network access to https://www.semrush.com
2. Valid authentication cookies for a logged-in Semrush user
3. Browser developer tools or a proxy like Burp Suite for header manipulation

## Defense

Defensive measures and detection strategies:

- Implement strict Origin validation or whitelisting on API endpoints
- Disable Access-Control-Allow-Credentials for non-trusted origins
- Monitor for unusual Origin headers in server logs

## Objectives

1. Confirm if the API trusts arbitrary Origins
2. Identify potential for cross-origin credentialed requests
3. Assess risk of data exfiltration

## Instructions

### Step 1: Craft and Send Request

**Context**: Prepare a GET request to the target endpoint, setting a fake Origin header and including credentials.

**Command** (Use browser console or curl equivalent):

Use [[tools/XMLHttpRequest-API]] or curl to send:

```bash
curl -H "Origin: https://itqayzlbkshw.com" -H "Cookie: auth_token=your_cookie" "https://www.semrush.com/organic-traffic-insights/api/rest/1.2/users/████/projects?_=$(date +%s)" -v
```

> This command sends the request with verbose output (-v) to inspect headers. Expected output includes a 200 response if successful.

### Step 2: Verify Request Acceptance

**Context**: Ensure the request is not blocked by CORS preflight.

No specific command; observe if the request completes without errors.

> Successful execution shows no CORS errors in browser console or curl output.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XMLHttpRequest-API]]

## Tags

- [[cors]]
- [[testing]]
