---
id: 2f51a7c6-1393-4c55-b07e-b431cacfc321
name: Trigger-Server-Error-for-Path-Disclosure
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.350Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - info-disclosure
  - web
  - error-handling
commands:
  - '[[commands/curl-access-endpoint]]'
platforms:
  - Web
  - AWS
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Trigger-Server-Error-for-Path-Disclosure

## Summary

This procedure accesses a web endpoint on a misconfigured server to trigger an error response that leaks internal file paths, exploiting poor error handling on re-allocated cloud instances.

## Description

When a web server on a re-allocated EC2 instance lacks proper error configuration, simple HTTP requests can cause 500 errors revealing paths like /var/www/. The attack scenario targets public-facing web apps with outdated setups. Prerequisites include a resolved IP from DNS. Outcomes are low-severity info disclosure, aiding reconnaissance without deeper access.

## Requirements

1. Resolved IP from DNS step
2. HTTP client (e.g., curl)
3. No authentication; assumes open endpoint

## Defense

Defensive measures and detection strategies:

- Configure web servers (e.g., Apache/Nginx) to suppress path details in errors
- Rotate or remove DNS for deallocated instances promptly
- Log and monitor anomalous HTTP requests to old endpoints

## Objectives

1. Elicit server error exposing internal paths
2. Confirm misconfiguration on re-allocated instance
3. Gather info for potential escalation (though low impact here)

## Instructions

### Step 1: Send HTTP Request to Endpoint

**Context**: Issue a GET request to the root or any path on the subdomain to provoke a server error due to misconfiguration.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl -v http://27.prd.vine.co/
```

> The -v flag provides verbose output, including headers and response body. Successful execution shows error HTML/PHP/whatever with embedded paths; inspect for strings like 'No such file or directory: /path/to/internal/dir'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-access-endpoint]]

## Tools Used


## Tags

- [[info-disclosure]]
- [[web]]
- [[error-handling]]
