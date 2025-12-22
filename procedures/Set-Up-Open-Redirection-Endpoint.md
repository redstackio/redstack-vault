---
id: proc-open-redirect-setup-001
tags:
  - open-redirection
  - setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.395Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Open-Redirection-Endpoint

## Summary

This procedure sets up a controlled web endpoint that performs open redirections to arbitrary URLs, enabling the simulation of a vulnerable site for testing Burp Suite's redirection handling and credential leakage.

## Description

In the context of demonstrating Burp Suite vulnerabilities, an open redirection flaw is created on a controlled domain (e.g., example.com) using a simple PHP script. This endpoint accepts a 'url' parameter and issues a 302 redirect to the specified location. The setup requires a web server like Apache with PHP support. Once deployed, it allows crafting requests that redirect to attacker-controlled domains, facilitating the observation of credential forwarding in tools like Burp Repeater. Prerequisites include server access and basic web development knowledge; expected outcome is a functional redirect that preserves query parameters but forwards the client to external sites.

## Requirements

1. Web server (e.g., Apache on Linux) with PHP enabled
2. Domain control (e.g., example.com) accessible from the testing environment
3. Network access to deploy and test the endpoint

## Defense

Defensive measures and detection strategies:

- Implement redirect validation to whitelist allowed domains
- Use HTTP response headers like Content-Security-Policy to restrict navigations
- Monitor server logs for unusual redirect patterns or high-volume parameter usage

## Objectives

1. Establish a realistic open redirection vulnerability for testing
2. Ensure the endpoint is reachable and functional
3. Prepare for integration with authentication testing tools

## Instructions

### Step 1: Deploy the Redirection Script

**Context**: Create and upload a PHP file to handle open redirections on the controlled site.

No command required (file-based setup). Create /redirect.php with the following content:

```php
<?php
header('Location: ' . $_GET['url']);
?>
```

> This script reads the 'url' GET parameter and issues a Location header redirect. Upload to the web root of example.com and ensure PHP execution is enabled. Test by accessing http://example.com/redirect.php?url=http://example.com/test, which should redirect internally.

### Step 2: Verify Endpoint Functionality

**Context**: Confirm the open redirection works by sending a test request.

Use a browser or curl to test:

```bash
curl -I http://example.com/redirect.php?url=http://evil.com
```

> Expected output includes HTTP/1.1 302 Found and Location: http://evil.com. This validates the endpoint before proceeding to Burp Suite testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- open-redirection
- setup
