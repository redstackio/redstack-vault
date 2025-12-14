---
id: proc-3
tags:
  - verification
  - cache
  - dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud (GCP)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:56.037Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Verify-Poisoned-Cache-Entry

## Summary

This procedure confirms cache poisoning by requesting the targeted resource with the cache buster parameter and observing the empty response served from Varnish cache.

## Description

After poisoning, this step validates the attack's success in a controlled manner using the query parameter. In the GitLab CDN scenario, it shows how the empty JS response breaks frontend functionality, highlighting the DoS potential in Varnish-cached web assets on GCP.

## Requirements

1. Browser or HTTP client for simple GET
2. The exact URL with cache buster from poisoning step
3. No special privileges needed

## Defense

Defensive measures and detection strategies:

- Implement cache validation checks for static assets (e.g., content-length mismatches)
- Monitor for sudden increases in empty responses from CDN

## Objectives

1. Confirm cached empty response is served
2. Observe impact on resource loading
3. Validate isolation via cache buster

## Instructions

### Step 1: Request Poisoned Variant

**Context**: Simulate a follow-up request to hit the poisoned cache entry.

Access the URL in a browser or send:

```http
GET /assets/webpack/commons-pages.admin.sessions-pages.groups.omniauth_callbacks-pages.ldap.omniauth_callbacks-pages.omn-c3aaf8c4.3f9d44ba.chunk.js?cb=youstin-xyz HTTP/1.1
Host: assets.gitlab-static.net
```

> Expected output: Empty body with cache HIT header, confirming poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[cache]]
- [[dos]]
