---
tags:
  - information-disclosure
  - path-disclosure
  - php
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-invalid-language-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:06.152Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 89bedad2-6313-4907-8fa0-4a55cb4105b7
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger Full Path Disclosure via Invalid Language ID

## Summary

This procedure exploits an unhandled PHP exception in the Localize web application's language selection endpoint by supplying an invalid language identifier, resulting in the disclosure of internal server file paths. It is primarily used for reconnaissance to map the target's file system structure.

## Description

The Localize application, built on PHP, processes language IDs in URLs like /projects/{project_id}/languages/{language_id}. When an invalid ID (e.g., '4xX') is provided, the Language.php class throws a fatal exception due to an unknown ID (interpreted as 3083). PHP's default error reporting then outputs a detailed stack trace, revealing absolute server paths such as /srv/data/web/vhosts/www.localize.im/htdocs/classes/Language.php. This information can assist attackers in understanding the server's directory layout, potentially facilitating further exploits like local file inclusion or path traversal, though no such escalations were observed in this case. The attack requires no authentication and can be executed via a simple HTTP request.

## Requirements

1. Network access to the target web application (e.g., https://www.localize.im)
2. A tool or browser capable of making HTTP GET requests
3. Knowledge of a valid project ID (e.g., '3t' from public enumeration)

## Defense

Defensive measures and detection strategies:

- Implement custom error handling in PHP to suppress path details (e.g., set display_errors=Off in production)
- Use a web application firewall (WAF) to block requests with malformed parameters
- Monitor server logs for fatal exceptions and invalid parameter patterns
- Enable PHP's error logging to file instead of stdout

## Objectives

1. Disclose internal server file paths for reconnaissance
2. Map application directory structure
3. Identify potential vectors for advanced attacks

## Instructions

### Step 1: Prepare the Malformed URL

**Context**: Construct the target URL using a known project ID and an invalid language code to trigger the exception.

No command required; use the URL https://www.localize.im/projects/3t/languages/4xX.

### Step 2: Send the Request

**Context**: Execute an HTTP GET request to the malformed endpoint to provoke the PHP error and capture the response.

**Command** ([[commands/curl-access-invalid-language-url]]):
```bash
curl "https://www.localize.im/projects/3t/languages/4xX" -v
```

> This command sends a verbose GET request to the endpoint. The -v flag provides detailed output, including headers and the full response body. Expected output includes a 500 Internal Server Error with a PHP fatal error message exposing the stack trace and file paths.

### Step 3: Analyze the Response

**Context**: Review the error output to extract disclosed paths and assess the server's structure.

No command required; manually inspect the response for lines like "Fatal error: Uncaught exception ... in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Language.php".

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-invalid-language-url]]

## Tools Used


## Tags

- information-disclosure
- path-disclosure
- php
- reconnaissance
