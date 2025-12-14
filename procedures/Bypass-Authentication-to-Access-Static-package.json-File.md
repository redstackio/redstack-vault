---
id: proc-001
tags:
  - access-control
  - information-disclosure
  - package-json
  - node-js
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-package-json]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:17.675Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Bypass-Authentication-to-Access-Static-package.json-File

## Summary

This procedure exploits improper access control in a web application where static files like package.json are served publicly without authentication, while the main endpoints are protected. It allows attackers to retrieve sensitive application metadata, such as dependencies and versions, aiding in reconnaissance for further vulnerabilities.

## Description

In scenarios like the Ping Identity staging application, the main endpoint (https://apps-staging.pingone.com/) enforces authentication and returns a 403 Forbidden error for unauthorized users. However, static assets such as /package.json are not protected, enabling direct access via browser or HTTP requests. This exposure reveals Node.js package details, including library versions that may be exploitable. The procedure targets such misconfigurations in staging or production environments, providing a low-effort way to gather host information without credentials.

## Requirements

1. Network access to the target web application URL
2. Basic HTTP client (browser or curl)
3. Knowledge of common static file paths like /package.json

## Defense

Defensive measures and detection strategies:

- Implement uniform access controls for all static and dynamic assets using web application firewalls (WAF) or server configurations (e.g., Nginx location blocks)
- Monitor access logs for anomalous requests to static files and alert on high-volume or unusual path accesses
- Use robots.txt or authentication middleware for non-public files in staging environments

## Objectives

1. Retrieve unauthorized application configuration data
2. Identify vulnerable dependencies for chained attacks
3. Perform reconnaissance without triggering main app protections

## Instructions

### Step 1: Verify Main Endpoint Protection

**Context**: Confirm that the primary application endpoint requires authentication to establish the access control discrepancy.

**Command** ([[commands/curl-basic-request]]):
```bash
curl -I https://apps-staging.pingone.com/
```

> This command sends a HEAD request to the main endpoint. Expected output includes HTTP 403 Forbidden, indicating protection is in place.

### Step 2: Access the Exposed package.json File

**Context**: Directly request the static file to bypass authentication and retrieve sensitive information.

**Command** ([[commands/curl-fetch-package-json]]):
```bash
curl https://apps-staging.pingone.com/package.json
```

> This fetches the package.json content. Successful execution returns a JSON object with application details, such as name, version, and dependencies. Parse the output to identify exploitable libraries (e.g., outdated versions of express or other Node.js packages).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-fetch-package-json]]
- [[commands/curl-basic-request]]

## Tools Used

- None

## Tags

- [[access-control]]
- [[information-disclosure]]
- [[package-json]]
- [[node-js]]
