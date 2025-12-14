---
tags:
  - path-traversal-bypass
  - middleware-bypass
type: procedure
tools:
  - '[[tools/Rack-Protection-PathTraversal]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-encoded-backslash-traversal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.379Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 48201e83-9135-4c89-a06c-fd2f7249e71d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Bypass-Path-Traversal-Middleware-with-Encoded-Backslashes

## Summary

This procedure bypasses the optional Rack::Protection::PathTraversal middleware in Rails by using URL-encoded backslashes ('%5c') in traversal paths, allowing the request to reach the vulnerable view resolver and disclose files.

## Description

Rack::Protection::PathTraversal blocks paths with '/' starters but misses '\../' variants. When encoded as '%5c../', it passes the middleware, but Dir.glob in the resolver escapes backslashes (without FNM_NOESCAPE), treating it as '../'. This chains with the traversal vuln for file disclosure. Scenario: Attacker targets a protected Rails app. Prerequisites: Middleware enabled, wildcard route present. Outcome: Successful file read despite protection.

## Requirements

1. Rails app with Rack::Protection::PathTraversal enabled (e.g., in middleware stack)
2. Configured wildcard route
3. HTTP client supporting URL encoding

## Defense

Defensive measures and detection strategies:

- Update to patched Rails versions
- Enhance middleware to decode and check encoded paths
- WAF rules for encoded traversal patterns (%5c, ..)

## Objectives

1. Evade middleware checks using encoded backslashes
2. Achieve traversal and file disclosure
3. Validate bypass effectiveness

## Instructions

### Step 1: Encode the Path with Backslashes

**Context**: Replace '/' with '\' in traversal and URL-encode to '%5c../' to slip past middleware.

**Command** ([[commands/curl-encoded-backslash-traversal]]):
```bash
curl -X GET "http://localhost:3000/help/%5c../%5c../%5c../Gemfile" -v
```

> Middleware doesn't block; resolver processes as '../'. Expected output: 200 with Gemfile contents.

### Step 2: Confirm Bypass

**Context**: Compare with non-encoded to ensure only encoded succeeds under protection.

**Command** (Test non-bypass):
```bash
curl -X GET "http://localhost:3000/help/../../Gemfile" -v
```

> Expected output: Blocked (403/400) if middleware active; encoded version succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-encoded-backslash-traversal]]

## Tools Used

- [[tools/Rack-Protection-PathTraversal]]

## Tags

- path-traversal-bypass
- middleware-bypass
