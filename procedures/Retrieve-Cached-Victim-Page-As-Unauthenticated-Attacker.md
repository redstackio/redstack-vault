---
id: proc-wcd-retrieve-cache-001
tags:
  - cache-retrieval
  - unauthenticated-access
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-cached-wcd-page]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.254Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-Cached-Victim-Page-As-Unauthenticated-Attacker

## Summary

This procedure fetches the cached 404 page from the WCD attack using an unauthenticated request, obtaining the victim's personalized data without session credentials, exploiting the proxy's misclassification of dynamic content as cacheable CSS.

## Description

After the victim visits, Cloudflare serves the cached response to any unauthenticated requester. Use curl without cookies/headers to simulate this, retrieving HTML that appears as CSS but contains full 404 source with user data. Targets Shopify's help subdomain; outcomes include access to PII and tokens. Prerequisites: Victim has visited; basic HTTP knowledge.

## Requirements

1. Malicious URL with random .css path
2. curl or similar HTTP client
3. No authentication (incognito or clean session)

## Defense

Defensive measures and detection strategies:

- Configure caches to bypass for error codes or authenticated paths
- Vary cache keys by user-agent or session presence
- Monitor cache hit rates on unusual extensions like .css for error content

## Objectives

1. Retrieve the poisoned cache entry
2. Confirm unauthenticated access to victim data
3. Capture response for analysis

## Instructions

### Step 1: Execute Unauthenticated Request

**Context**: Request the URL without auth to hit the cache and get the leaked page.

**Command** ([[commands/curl-fetch-cached-wcd-page]]):
```bash
curl https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css
```

> This outputs the HTML 404 page source; look for user-specific elements in the response body.

### Step 2: Save and Inspect Response

**Context**: Store output for detailed review.

Add `-o cached_page.html` to curl: `curl -o cached_page.html [URL]`.

> Open in text editor; success if it includes dynamic user data not present in fresh unauth 404.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-cached-wcd-page]]

## Tools Used

- [[tools/curl]]

## Tags

- cache-poisoning
- data-retrieval
