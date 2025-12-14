---
id: proc-1
tags:
  - recon
  - cache
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.051Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Normal-GET-Request-to-Static-Asset

## Summary

This procedure sends a standard GET request to a static JS asset on GitLab's CDN to establish baseline caching behavior with Varnish, confirming the resource is served and cached correctly before attempting poisoning.

## Description

In the context of cache poisoning attacks, this initial step verifies normal operation of the CDN at https://assets.gitlab-static.net/. The request targets a webpack chunk JS file, which is critical for GitLab's frontend. The response includes the full file and Varnish headers, setting the stage for observing deviations in poisoned responses. This is essential in web environments using reverse proxies like Varnish on GCP.

## Requirements

1. Internet access to https://assets.gitlab-static.net/
2. HTTP client capable of sending GET requests (e.g., curl, browser)
3. Knowledge of target asset paths (e.g., webpack bundles)

## Defense

Defensive measures and detection strategies:

- Monitor Varnish logs for unusual cache MISS/HIT patterns on static assets
- Implement header validation to strip or log X-Http-Method-Override on CDN edges

## Objectives

1. Confirm asset delivery and caching mechanism
2. Identify cache headers for later comparison
3. Baseline for poisoning verification

## Instructions

### Step 1: Craft and Send GET Request

**Context**: Target a specific JS file to simulate normal user access and observe caching.

Send the following HTTP request:

```http
GET /assets/webpack/commons-pages.admin.sessions-pages.groups.omniauth_callbacks-pages.ldap.omniauth_callbacks-pages.omn-c3aaf8c4.3f9d44ba.chunk.js HTTP/1.1
Host: assets.gitlab-static.net
```

> This request fetches the JS file. Expected output is the full JavaScript content with Content-Type: application/javascript and Varnish headers like X-Varnish: <id> and Cache-Control: max-age=... indicating caching.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[cache]]
- [[web]]
