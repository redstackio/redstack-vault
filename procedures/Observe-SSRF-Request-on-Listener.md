---
tags:
  - observe
  - ssrf
  - verification
type: procedure
tools:
  - '[[tools/Perl]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T04:08:55.247Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 9600d87f-4821-489e-aa9f-68be1b92f0db
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Observe SSRF Request on Listener

## Summary

Monitor the internal TCP listener to capture and verify the SSRF request, confirming access to localhost via the bypass.

## Description

After triggering the fetch, the request arrives as GET /PATH_IS_KEPT to port 80 on 127.0.0.1, demonstrating the vulnerability in IconFetchingService.cs lines 301-314 where redirects are followed without IP re-check.

## Requirements

1. Active Perl listener in container
2. Recent credential addition
3. Access to container logs

## Defense

Defensive measures and detection strategies:

- Log all internal HTTP requests
- Alert on requests from icons service to localhost
- Implement IP validation on all outbound fetches

## Objectives

1. Validate SSRF exploitation
2. Extract request details for analysis
3. Extend to scan other internals (e.g., 169.254.169.254 for AWS)

## Instructions

### Step 1: Monitor Listener Output

**Context**: Watch for incoming connections.

In the container shell, observe the Perl script's stdout for data.

> Expected: Prints full HTTP request including method, path, host (localhost), and User-Agent from Bitwarden.

### Step 2: Analyze Captured Request

**Context**: Confirm SSRF elements.

Look for: GET /PATH_IS_KEPT HTTP/1.1 Host: test.local.yourdomain.com (resolved to 0.0.0.0).

> Success: Request body/headers show internal targeting; no external exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Perl]]

## Tags

- observe
- ssrf
- verification
