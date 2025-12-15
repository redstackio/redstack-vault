---
tags:
  - recon
  - source-analysis
  - rails
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:23:31.171Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e24c1c53-1f16-487c-bcee-6e6f74a0074e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-Rails-Source-for-IP-Parsing-Discrepancy

## Summary

This procedure involves static analysis of Ruby on Rails source code and documentation to identify discrepancies in IP address parsing between the RemoteIp middleware and Web Console validation, enabling the discovery of whitelist bypass opportunities.

## Description

In the context of auditing Rails 4.0 and 4.1 applications, review the Web Console gem documentation which enables a debugging console restricted to localhost (127.0.0.1 and ::1). Examine the ActionDispatch::RemoteIp middleware source, which uses regex patterns (e.g., ^::1$ for IPv6 localhost) to process X-Forwarded-For and Client-IP headers by stripping trusted proxies. Contrast this with the Web Console's use of the Ruby IPAddr class to validate request.remote_ip against localhost addresses. The differential allows IPv6 variants like '0000::1' to evade regex matching but resolve to ::1 via IPAddr, bypassing restrictions. This analysis was key to discovering CVE-2015-3224.

## Requirements

1. Access to Rails source code repositories (e.g., GitHub)
2. Knowledge of Ruby, regex, and IPv6 addressing
3. Tools for code review (e.g., text editor or IDE)

## Defense

Defensive measures and detection strategies:

- Regularly audit and update Rails applications to patched versions (post-4.1)
- Disable Web Console in production environments
- Implement comprehensive logging of source code access and changes in CI/CD pipelines

## Objectives

1. Identify parser inconsistencies in IP handling
2. Confirm vulnerability applicability to target versions
3. Document bypass vectors for exploitation planning

## Instructions

### Step 1: Review Web Console Documentation

**Context**: Understand the intended IP restrictions for the Web Console.

Consult the official documentation for the web-console gem, noting it is enabled by default in development and test environments and restricts access to localhost IPs.

### Step 2: Examine RemoteIp Middleware Source

**Context**: Analyze how proxy headers are processed to find regex limitations.

Navigate to https://github.com/rails/rails/blob/4-1-stable/actionpack/lib/action_dispatch/middleware/remote_ip.rb#L31-38. Identify regex patterns such as `^::1$` used to match and strip trusted IPv6 localhost proxies from X-Forwarded-For headers.

### Step 3: Compare with Web Console Validation

**Context**: Verify the use of IPAddr and test parsing differences.

Review the Web Console source (e.g., in actionpack/lib/action_dispatch/middleware/remote_ip.rb or console gem code) to confirm it uses `IPAddr.new(request.remote_ip)` for validation. Test locally that '0000::1' parses as ::1 via IPAddr but fails the regex match.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[source-analysis]]
- [[rails]]
