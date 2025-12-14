---
tags:
  - information-disclosure
  - auth-bypass
  - credentials-leak
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:25:12.615Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: dda30ae8-1d87-48fa-a5cb-0d12ac386145
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# Access-Vulnerable-Endpoint-to-Disclose-Environment-Variables

## Summary

This procedure exploits a misconfigured web endpoint to bypass authentication and disclose all environment variables, revealing sensitive credentials for servers, databases, mail services, Twitter API (client_id and client_secret), and Facebook API (client_id and client_secret).

## Description

The vulnerability stems from flawed authorization handling in the web application, where appending a semicolon (;) to the endpoint URL causes the server to ignore the 401 authentication error and return the full environment dump. This provides attackers with complete access to backend services, enabling further exploitation like unauthorized database access or API abuse. The procedure targets public-facing web applications and requires no prior authentication.

## Requirements

1. Direct network access to the target domain over HTTPS
2. A web browser or command-line tool like curl for URL manipulation
3. Knowledge of the vulnerable endpoint path (e.g., /admin/config or similar)

## Defense

Defensive measures and detection strategies:

- Implement proper authentication middleware that validates requests before processing
- Sanitize and parse URL parameters to prevent bypass tricks like semicolon injection
- Monitor access logs for anomalous 200 responses on authenticated endpoints and unusual query appendages
- Use environment variable managers like Docker secrets or AWS SSM to avoid exposing vars in responses

## Objectives

1. Bypass 401 error to access protected endpoint
2. Extract sensitive credentials from environment variables
3. Gain control over associated services (databases, mail, social APIs)

## Instructions

### Step 1: Prepare and Access the Endpoint

**Context**: Identify the vulnerable endpoint and append ';' to trigger the bypass, exploiting a server-side parsing issue.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl "https://www.target.com/vulnerable-endpoint;" -v
```

> This command sends a GET request to the modified URL, verbose output (-v) shows headers and confirms the bypass from 401 to 200. Expected output includes a dump of environment variables like SERVER_PASSWORD=abc123, DATABASE_URL=postgresql://user:pass@host/db, TWITTER_CLIENT_ID=xyz789.

### Step 2: Parse and Validate Disclosure

**Context**: Review the response for sensitive data and verify usability of extracted credentials.

**Command** ([[commands/curl-access-endpoint]] with output save):
```bash
curl "https://www.target.com/vulnerable-endpoint;" -o env_dump.txt
cat env_dump.txt | grep -E '(password|secret|key|credential)'
```

> Filters the response for key terms to quickly identify credentials. Success is indicated by matching patterns revealing access tokens or passwords.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-endpoint]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[auth-bypass]]
- [[credentials-leak]]
