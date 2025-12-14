---
tags:
  - ssrf
  - gitlab
  - localhost
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-import-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.614Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1195658f-45c2-4e3b-9cd8-22dfc6c6b1ce
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Specify-Malicious-Localhost-URL-for-SSRF

## Summary

This procedure submits a localhost or internal URL through GitLab's 'Repo by URL' import to trigger SSRF, forcing the server to request local services without authentication.

## Description

The lack of URL validation in GitLab's import feature allows specification of addresses like 'localhost:port' or internal IPs, bypassing external-only restrictions. This targets services bound to the local interface on ports below 1024 (except 22, 80, 443). In a self-hosted GitLab environment, this can expose internal metadata or databases. Prerequisites: Access to the import form. Outcomes: Server initiates unauthorized internal requests.

## Requirements

1. Active GitLab session from previous procedure
2. Knowledge of target internal port/service (e.g., localhost:8080)
3. API token or UI access for submission

## Defense

Defensive measures and detection strategies:

- Validate URLs to restrict to public domains and block private IPs/localhost
- Log all import requests and alert on suspicious URLs
- Deploy network segmentation to isolate internal services

## Objectives

1. Inject SSRF payload via URL parameter
2. Trigger server-side request to local endpoint
3. Observe initial response or error indicating success

## Instructions

### Step 1: Prepare Malicious URL

**Context**: Craft a URL targeting an internal service, such as a debug endpoint.

No command; define URL like `http://localhost:1690/debug/vars`.

> This exploits the feature's fetch mechanism without client-side checks.

### Step 2: Submit Import Request

**Context**: Send the URL via UI or API to initiate SSRF.

**Command** ([[commands/curl-send-import-request]]):
```bash
curl -X POST 'https://gitlab.example.com/api/v4/projects/import' \
  -H 'Private-Token: your_token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=http://localhost:8080/internal' \
  -d 'namespace_id=1'
```

> GitLab fetches the URL server-side; success if no validation error, potential internal access logged.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-import-request]]

## Tools Used


## Tags

- ssrf
- localhost
