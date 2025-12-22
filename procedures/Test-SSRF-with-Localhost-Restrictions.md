---
id: proc-test-ssrf-localhost-913276
tags:
  - ssrf
  - reconnaissance
  - vulnerability-scan
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-http-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:08:48.332Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Test-SSRF-with-Localhost-Restrictions

## Summary

This procedure tests a web application's icon fetching endpoint for SSRF vulnerabilities by requesting resources from localhost, which typically triggers partial restrictions and reveals the potential for internal request forgery.

## Description

In the context of the Bitwarden icons.bitwarden.net service, this step involves sending a request to fetch an icon from a localhost domain. The application processes the request but returns a 400 Bad Request due to built-in restrictions on direct localhost access. This confirms the endpoint fetches external resources without full validation, setting the stage for bypass techniques. The target environment is a public web service built on .NET Core, accessible without authentication.

## Requirements

1. Network access to the target endpoint (https://icons.bitwarden.net)
2. Tool for making HTTP requests, such as curl or a web browser
3. Basic understanding of HTTP status codes

## Defense

Defensive measures and detection strategies:

- Implement URL validation to block localhost and private IP ranges (e.g., using allowlists for domains)
- Monitor server logs for requests to internal addresses and anomalous 400 responses
- Use web application firewalls (WAF) to detect and block SSRF patterns like localhost in URLs

## Objectives

1. Confirm the endpoint processes user-controlled domains for resource fetching
2. Identify restriction mechanisms on localhost access
3. Establish baseline for SSRF exploitation potential

## Instructions

### Step 1: Send Localhost Request

**Context**: Probe the endpoint to see how it handles internal address requests, expecting a blocked but processed response.

**Command** ([[commands/curl-http-request]]):
```bash
curl -i https://icons.bitwarden.net/localhost/icon.png
```

> This command sends an HTTP GET request to the icon endpoint with 'localhost' as the domain. Expected output includes a 400 Bad Request status, indicating the request was parsed but rejected due to the internal target, confirming SSRF risk without full block.

### Step 2: Analyze Response

**Context**: Review the response headers and body to validate restriction behavior.

No specific command; inspect the curl output for status code and any error messages related to invalid domains.

> Successful execution shows HTTP/1.1 400 Bad Request, proving the application attempts internal resolution.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-http-request]]

## Tools Used


## Tags

- [[ssrf]]
- [[Reconnaissance]]
- [[web]]
