---
id: proc-uuid-1
tags:
  - reconnaissance
  - web-access
  - http-request
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:55.991Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Software]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Access-Web-Login-Endpoint

## Summary

This procedure involves sending an HTTP request to a web application's login endpoint to retrieve the response, which may contain leaked server information in headers. It is commonly used in reconnaissance to map the target's technology stack without authentication.

## Description

In scenarios like testing jenkins.brew.sh, accessing the login page (e.g., /login) via a simple GET request exposes default server configurations. The nginx server, if not hardened, includes its version in the 'Server' header, allowing attackers to identify potential exploits for that version. This step requires no privileges and serves as the entry point for header inspection.

## Requirements

1. Network access to the target URL (e.g., public internet connectivity)
2. HTTP client tool like curl or a web browser
3. Target endpoint publicly accessible without authentication

## Defense

Defensive measures and detection strategies:

- Configure nginx with 'server_tokens off;' in the http block to hide version details
- Implement Web Application Firewall (WAF) to monitor and block anomalous header requests
- Log all HTTP requests to the login endpoint and alert on repeated unauthenticated accesses

## Objectives

1. Trigger the HTTP response from the login page
2. Establish a baseline for header analysis
3. Confirm the endpoint's availability and response behavior

## Instructions

### Step 1: Send HTTP HEAD or GET Request

**Context**: Use curl to fetch headers from the login endpoint, minimizing payload transfer with -I flag for HEAD request.

**Command** ([[commands/curl-fetch-headers]]):
```bash
curl -I https://jenkins.brew.sh/login
```

> This command sends a HEAD request and outputs all response headers. Expected output includes status code (e.g., 200 OK) and headers like Content-Type, but critically the Server header.

### Step 2: Verify Response Accessibility

**Context**: If using a browser, navigate directly; confirm the page loads without errors.

**Command** ([[commands/curl-fetch-headers]]):
```bash
curl -s https://jenkins.brew.sh/login > /dev/null && echo "Accessible"
```

> Silent check (-s) to verify the endpoint responds without downloading the full body. Success: No errors, page accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques

- [[Software]]

## Commands Used

- [[commands/curl-fetch-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- [[Reconnaissance]]
- [[web]]
- [[http]]
