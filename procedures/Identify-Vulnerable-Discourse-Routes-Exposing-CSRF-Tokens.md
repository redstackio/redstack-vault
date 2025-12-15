---
tags:
  - reconnaissance
  - web-cache-deception
  - csrf
type: procedure
tools:
  - '[[tools/CloudFlare-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-u-x-css]]'
  - '[[commands/curl-get-u-my-preferences-css]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:24.444Z'
sub_techniques: []
id: b5bd04a9-8756-4d76-8068-a9609dc18355
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Discourse Routes Exposing CSRF Tokens

## Summary

This procedure identifies Discourse routes that return user-specific data including CSRF tokens and usernames without proper cache-control headers, setting the stage for Web Cache Deception attacks when proxied through CloudFlare.

## Description

Discourse user routes like /u/my/preferences and /u/x (404) embed <meta name="csrf-token"> in HTML and set X-Discourse-Username in headers. These lack no-cache directives, allowing caching when extensions like .css are appended, as CloudFlare treats .css as static. This reconnaissance confirms the vulnerability in the target environment.

## Requirements

1. Access to a Discourse instance behind CloudFlare
2. Browser or curl for HTTP requests
3. Authentication to the target (for /u/my routes)

## Defense

Defensive measures and detection strategies:

- Add Cache-Control: no-cache, no-store, must-revalidate to user-specific routes
- Configure CloudFlare to bypass cache for dynamic paths or user routes
- Monitor for unusual .css requests to user paths in logs

## Objectives

1. Confirm exposure of CSRF tokens and usernames
2. Verify absence of cache prevention headers
3. Identify routes for later exploitation

## Instructions

### Step 1: Request Non-Existent User Route

**Context**: Test 404 page for token leakage.

**Command** ([[commands/curl-get-u-x-css]]):
```bash
curl -H "Host: try.discourse.org" "https://try.discourse.org/u/x.css"
```

> Requests /u/x.css; expects 404 with CSRF meta and X-Discourse-Username header.

### Step 2: Request User Preferences Route

**Context**: Test authenticated route for data exposure.

**Command** ([[commands/curl-get-u-my-preferences-css]]):
```bash
curl "https://try.discourse.org/u/my/preferences.css"
```

> Authenticated request to /u/my/preferences.css; expects 200 with user data and no-cache headers absent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-u-x-css]]
- [[commands/curl-get-u-my-preferences-css]]

## Tools Used

- [[tools/CloudFlare-Proxy]]

## Tags

- [[Reconnaissance]]
- [[web-cache-deception]]
- [[csrf]]
