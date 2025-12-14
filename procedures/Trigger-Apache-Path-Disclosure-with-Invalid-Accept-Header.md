---
tags:
  - information-disclosure
  - path-disclosure
  - apache
  - web
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-invalid-accept-header]]'
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 2cee180c-de88-46d9-9510-ced4a1543fa4
created_at: '2025-12-14T17:26:22.753Z'
updated_at: '2025-12-14T17:26:22.753Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-Apache-Path-Disclosure-with-Invalid-Accept-Header

## Summary

This procedure exploits misconfigured Apache error handling to disclose the full server webroot path by sending an HTTP request with an invalid Accept header to the /index endpoint, resulting in an error response that reveals sensitive file path information for reconnaissance purposes.

## Description

In vulnerable Apache configurations, processing an invalid MIME type in the Accept header during content negotiation can trigger a detailed error message that includes the absolute path to the webroot directory. This occurs when the server attempts to serve a default index file (e.g., index.html) but fails due to the invalid header, leading to a disclosure in the 406 Not Acceptable or 500 Internal Server Error response. The attack targets public-facing web applications like www.rockstargames.com/index and requires no authentication. Expected outcomes include exposure of paths such as /var/www/html, aiding attackers in mapping the server's filesystem for further exploits like brute-forcing filenames or directory traversal. Prerequisites include network access to the target and an HTTP client; the procedure is low-risk for detection as it mimics legitimate traffic.

## Requirements

1. Network access to the target web server (HTTP/HTTPS on port 80/443).
2. HTTP client tool like curl or Burp Suite.
3. Knowledge of the target endpoint (e.g., /index).

## Defense

Defensive measures and detection strategies:

- Configure Apache to suppress detailed error messages using ErrorDocument directives or mod_rewrite to return generic errors.
- Implement web application firewall (WAF) rules to block requests with malformed headers (e.g., invalid MIME types in Accept).
- Monitor server logs for anomalous Accept header values and error responses containing paths; use tools like Fail2Ban or SIEM for alerting.
- Regularly audit server configurations with tools like Apache's mod_security.

## Objectives

1. Gather server filesystem details for reconnaissance.
2. Identify potential entry points for file-based attacks.
3. Assess server configuration weaknesses without exploitation.

## Instructions

### Step 1: Craft and Send Malformed Request

**Context**: Prepare an HTTP GET request to the vulnerable endpoint with an invalid Accept header to trigger the error disclosure.

**Command** ([[commands/curl-invalid-accept-header]]):
```bash
curl -H "Accept: invalid/mime" -v http://www.rockstargames.com/index
```

> This command sends a verbose GET request (-v flag for headers) with Accept: invalid/mime, which Apache cannot match, causing it to error and disclose the path in the response body. Look for phrases like "No matching DirectoryIndex" followed by the full path in the output.

### Step 2: Analyze Response

**Context**: Parse the server response to extract and validate the disclosed path information.

**Command** (Manual inspection or grep):
```bash
curl -H "Accept: invalid/mime" http://www.rockstargames.com/index | grep -i "path\|directory\|webroot"
```

> Grep the response for path-related keywords to isolate the disclosure. Successful output will show an absolute path, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-invalid-accept-header]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[path-disclosure]]
- [[apache]]
- [[web]]
- [[Reconnaissance]]
