---
tags:
  - ip-bypass
  - auth-bypass
  - http-header
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-bypass-rails-ip]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:28.634Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2be57481-6c2e-402a-b0a3-ef9d51e8bde9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-IP-Whitelist-with-Crafted-X-Forwarded-For

## Summary

This procedure crafts and sends an HTTP request with a specially formatted X-Forwarded-For header containing '0000::1' to exploit the IP parsing discrepancy in Rails Web Console, bypassing localhost restrictions and gaining unauthorized access.

## Description

Target Rails 4.0/4.1 apps with Web Console enabled. The RemoteIp middleware fails to recognize '0000::1' via its regex (^::1$), leaving it in the IP chain, but the Web Console's IPAddr validation normalizes it to ::1, treating it as localhost. This grants remote access to the /rails/console endpoint, which is otherwise restricted. Exploitation requires sending the header via a proxy or direct request simulation.

## Requirements

1. Network access to the target Rails app (e.g., http://target:3000)
2. Tool like curl for header manipulation
3. Confirmation of vulnerable version via prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Patch to Rails 4.2+ or disable Web Console
- WAF rules to inspect and block anomalous X-Forwarded-For values (e.g., padded IPv6)
- Log and monitor access to /rails/console with IP validation

## Objectives

1. Spoof origin IP to evade whitelist
2. Access restricted Web Console endpoint
3. Prepare for code execution payload

## Instructions

### Step 1: Prepare the Malicious Header

**Context**: Construct the X-Forwarded-For header with the bypass payload.

Set the header to '0000::1' to exploit the parsing difference.

### Step 2: Send the Request

**Context**: Transmit the request to the Web Console endpoint.

**Command** ([[commands/curl-bypass-rails-ip]]):
```bash
curl -H "X-Forwarded-For: 0000::1" http://target:3000/rails/console
```

> This command sends a GET request to the console path with the crafted header. The middleware processes it incorrectly, allowing access.

### Step 3: Verify Access

**Context**: Check response for successful bypass.

Inspect the HTTP response for the console interface (e.g., HTML form for Ruby input) instead of a 403 Forbidden.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-bypass-rails-ip]]

## Tools Used

- [[tools/curl]]

## Tags

- [[ip-bypass]]
- [[auth-bypass]]
- [[http-header]]
