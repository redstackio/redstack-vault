---
id: proc-verify-ssrf-logs-001
name: Verify-SSRF-via-Access-Logs
tags:
  - ssrf
  - verification
  - logs
type: procedure
tools:
  - '[[tools/Python-HTTP-Server]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/observe-git-protocol-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.104Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-SSRF-via-Access-Logs

## Summary

This procedure checks the HTTP listener's access logs to confirm the SSRF by identifying the incoming Git protocol request from the GitLab server IP.

## Description

After triggering the import, the listener captures the request, which includes Git-specific paths like /info/refs?service=git-upload-pack. Verification involves matching the source IP to GitLab's and the request details to expected SSRF behavior. This proves the vulnerability and can reveal internal details if targeted accordingly.

## Requirements

1. Running HTTP listener with logging enabled
2. Access to server console or log files
3. Known GitLab IP range for confirmation

## Defense

Defensive measures and detection strategies:

- Block or log unexpected outbound Git fetches
- Use IDS to detect anomalous HTTP requests from app servers
- Regularly audit import logs for suspicious URLs

## Objectives

1. Confirm request receipt from target
2. Analyze request for vulnerability details
3. Document proof for reporting

## Instructions

### Step 1: Monitor Logs for Incoming Request

**Context**: Watch the server output for the SSRF-triggered GET request.

**Command** ([[commands/observe-git-protocol-request]]):
No executable command; observe passive logs.

> Expected log: "<GitLab-IP> - - [timestamp] \"GET /info/refs?service=git-upload-pack HTTP/1.1\" 404 -". The 404 confirms endpoint absence but request success.

### Step 2: Validate Request Details

**Context**: Cross-check IP and parameters to ensure it's SSRF.

**Command**: No command; manual inspection.

> Look for service=git-upload-pack parameter and GitLab User-Agent. Success if IP matches known GitLab range (e.g., 40.84.0.225).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/observe-git-protocol-request]]

## Tools Used

- [[tools/Python-HTTP-Server]]

## Tags

- log-analysis
- ssrf-poc
- git-protocol
