---
id: proc-uuid-2
tags:
  - cache-poisoning
  - dos
  - verification
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-verify-cache]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:56.241Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Verify-Cache-Poisoning-Effect

## Summary

This procedure confirms the success of cache poisoning by sending a legitimate request to the target resource and observing the cached 403 Forbidden response served by Cloudflare, demonstrating the DoS impact.

## Description

After poisoning the cache, a follow-up request without the invalid header should retrieve the legitimate file from Azure, but instead receives the cached error due to Cloudflare's improper handling. This verifies the vulnerability and shows how users are denied access to essential files like wallet hashes until cache TTL expires.

## Requirements

1. Successful execution of cache poisoning procedure
2. Network access to the same target subdomain
3. Tool for sending plain HTTP GET requests (e.g., curl)

## Defense

Defensive measures and detection strategies:

- Enable cache bypass for error responses in CDN rules
- Use custom headers or cookies to differentiate malicious from legitimate requests
- Log and alert on cache hit rates for error statuses

## Objectives

1. Confirm the cache serves the poisoned 403 to clean requests
2. Validate DoS on legitimate file access
3. Measure the persistence of the poisoning effect

## Instructions

### Step 1: Send Legitimate Verification Request

**Context**: Issue a standard GET request to the poisoned path without any Authorization header to check if Cloudflare serves the cached error.

**Command** ([[commands/curl-verify-cache]]):
```bash
curl -X GET "https://downloads.exodus.com/releases/hashes-exodus-21.2.12.txt?cachebuster=hackerone" -v
```

> This command performs a clean request. Expected output is HTTP/1.1 403 Forbidden from cache, with CF-Cache-Status: HIT, confirming poisoning instead of the expected 200 OK with file content.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-cache]]

## Tools Used


## Tags

- [[cache-poisoning]]
- [[dos]]
- [[verification]]
