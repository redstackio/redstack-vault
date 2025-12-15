---
tags:
  - dos
  - rails
  - route-enumeration
  - recon
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:37.167Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 48750600-2a19-4a68-89d7-ee702c1eb0f8
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Rails-Routes

## Summary

This procedure involves scanning or reviewing a Ruby on Rails application's routing configuration to identify wildcard routes containing the ':controller' placeholder, which are vulnerable to the Action Pack DoS issue due to flawed caching.

## Description

In vulnerable Rails versions (>=4.0.0 and <5.0.0.beta1), the Action Pack component uses a global cache to map URL controller names to class names. Wildcard routes with ':controller' trigger lookups for any requested controller, even non-existent ones, populating the cache without bounds. This procedure focuses on reconnaissance to confirm such routes exist, typically by examining config/routes.rb or sending probe requests that elicit specific error patterns indicating controller resolution.

## Requirements

1. Access to the Rails application URL (public-facing web app)
2. Ability to read application source if available, or send HTTP requests for inference
3. Basic knowledge of Rails routing syntax

## Defense

Defensive measures and detection strategies:

- Patch to Rails 4.1/4.2 series or upgrade to 5.0+
- Implement rate limiting on route requests
- Monitor for unusual 404 patterns on controller paths
- Use application firewalls to block repetitive invalid requests

## Objectives

1. Confirm presence of vulnerable ':controller' wildcard routes
2. Map out exploitable URL patterns
3. Prepare for targeted DoS exploitation

## Instructions

### Step 1: Review Routing Configuration

**Context**: If source access is available, directly inspect the routes file to locate vulnerable patterns.

Examine config/routes.rb for lines like:

```ruby
match ':controller(/:action(/:id))', :action => /[^/]+/, :id => /[^/]+/, via: :get
```

> This identifies routes that use ':controller' without restrictions, triggering the cache population on any input.

### Step 2: Probe with Test Requests

**Context**: Without source access, send requests to potential wildcard paths and analyze responses for controller lookup indicators.

Send a GET request to a likely non-standard path, such as http://target.com/randomcontroller:

```http
GET /randomcontroller HTTP/1.1
Host: target.com
```

> Look for 404 responses with Rails-specific error details mentioning 'uninitialized constant' or similar, confirming the lookup mechanism is active.

### Step 3: Validate Vulnerability

**Context**: Confirm the route is wildcard-based by testing variations.

Test multiple invalid controllers (e.g., /abc, /xyz) and check if each triggers a unique lookup without immediate rejection.

> Success is indicated by consistent 404s without static file serving, pointing to dynamic controller resolution.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- rails
- route-enumeration
- recon
