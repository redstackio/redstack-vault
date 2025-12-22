---
id: proc-credential-leak-observe-001
tags:
  - leak
  - observation
type: procedure
tools:
  - '[[tools/Burp-Suite-Repeater]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:31:19.384Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Observe-Credential-Leak-on-External-Domain

## Summary

This procedure monitors an attacker-controlled domain to capture and decode the leaked HTTP Basic authentication credentials forwarded by Burp Repeater during redirection.

## Description

After the follow-redirection action, the external domain (e.g., evil.com) receives a request with the preserved Authorization header containing base64-encoded credentials. This step involves logging the request on the controlled site and decoding the header to verify the leak. Prerequisites: Attacker domain set up with logging (e.g., via access logs or a simple logger script). Expected outcome: Visible credentials that could be misused for accessing authenticated resources.

## Requirements

1. Attacker-controlled web server (e.g., evil.com) with request logging
2. Tools for decoding base64 (built-in or online)
3. Prior execution of the redirection follow in Burp

## Defense

Defensive measures and detection strategies:

- Implement header inspection proxies to block unauthorized auth headers
- Use certificate pinning or HSTS to prevent MITM on external redirects
- Monitor for anomalous requests to external domains from security tools

## Objectives

1. Capture the incoming request with leaked header
2. Decode and verify the credentials
3. Assess potential impact of the disclosure

## Instructions

### Step 1: Set Up Logging on External Domain

**Context**: Prepare the attacker site to record incoming requests.

No command (setup). Configure server access logs or deploy a PHP logger to dump headers.

> For example, use Apache's mod_log_config to log the Authorization header.

### Step 2: Analyze the Leaked Request

**Context**: Inspect logs after the Burp request arrives.

No command (analysis). Look for: Authorization: Basic dXNlcjpwYXNz in logs.

> Decode base64 (e.g., via echo 'dXNlcjpwYXNz' | base64 -d outputs user:pass). Confirm leak and evaluate reuse potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Repeater]]

## Tags

- leak
- observation
