---
tags:
  - directory-traversal
  - information-disclosure
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-directory-traversal-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:05.926Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 904f5ae0-e891-4448-b895-8730516d2a5b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Test-Directory-Traversal-with-src-Parameter

## Summary

This procedure tests the autoload.php endpoint for directory traversal vulnerabilities by crafting HTTP requests with the 'src' parameter, demonstrating file path disclosure and potential access to sensitive files.

## Description

Targeted at PHP web applications like the php-encryption-master fork, this procedure simulates an attack by sending traversal payloads to the 'src' parameter. Without proper filtering, the server may reveal directory structures or file contents, aiding reconnaissance. Prerequisites include a reachable endpoint; outcomes involve confirming the vulnerability through response analysis.

## Requirements

1. HTTP client (e.g., curl or browser) for sending requests
2. Knowledge of the target URL hosting autoload.php
3. Network access to the web server

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with path normalization and allowlisting
- Monitor server logs for traversal attempts (e.g., '../' patterns)
- Deploy runtime protections like PHP's open_basedir directive

## Objectives

1. Verify directory browsing capability via 'src'
2. Disclose full file paths for impact assessment
3. Identify exploitable files outside the web root

## Instructions

### Step 1: Prepare Test Payloads

**Context**: Define traversal strings to test the parameter.

Create payloads like 'src=../' for directory up and 'src=../../../etc/passwd' for specific file access.

### Step 2: Send Basic Traversal Request

**Context**: Test for directory disclosure.

Execute [[commands/curl-directory-traversal-test]] to send a request:

```bash
curl "http://target/autoload.php?src=../"
```

> This command fetches the parent directory; expect a response with file listings or paths if vulnerable.

### Step 3: Escalate to File Access

**Context**: Attempt to read sensitive files.

Modify the payload to target a known file:

```bash
curl "http://target/autoload.php?src=../../../etc/passwd"
```

> Successful output may include file contents; failure shows errors revealing paths.

### Step 4: Analyze Response

**Context**: Validate the disclosure.

Check for unintended data in the HTTP response body or headers, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-directory-traversal-test]]

## Tools Used


## Tags

- [[directory-traversal]]
- [[web-exploit]]
