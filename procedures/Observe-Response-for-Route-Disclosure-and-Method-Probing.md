---
tags:
  - rails
  - disclosure
  - probing
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-multiple-probes]]'
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:23:27.475Z'
sub_techniques: []
id: 70f4f31c-3c64-466f-95c3-5293ae3d3884
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Observe-Response-for-Route-Disclosure-and-Method-Probing

## Summary

This procedure analyzes HTTP responses from array parameter requests to disclose existence of _url methods/routes via successful redirects or 500 errors with tracebacks, enabling mapping of the application's internal structure.

## Description

Responses differentiate method existence: redirects for valid methods, errors for invalid, often leaking route details in Rails error pages. Targets post-exploitation of vulnerable redirects. Prerequisites: Sent probing requests. Outcomes: List of discoverable routes/methods for further attacks.

## Requirements

1. Responses from prior array requests
2. Ability to parse HTTP responses and errors
3. Scripting for automated probing if manual is inefficient

## Defense

Defensive measures and detection strategies:

- Customize error pages to hide stack traces (config.consider_all_requests_local = false in production)
- Rate-limit requests to redirect endpoints
- WAF rules to block array parameters in URL helpers
- Audit logs for patterns of failed method calls

## Objectives

1. Distinguish valid vs invalid methods from responses
2. Extract route information from errors
3. Identify exploitable methods for deeper access

## Instructions

### Step 1: Inspect Single Response

**Context**: Check verbose output for status and body to determine method status.

**Command** ([[commands/curl-multiple-probes]]):
```bash
curl -v -X GET "http://target.com/vulnerable?user_input[]=user_url" 2>&1 | grep -E "HTTP/|Location|error"
```

> Look for 302 with Location header for success, or 500 with NoMethodError in body for disclosure.

### Step 2: Automate Probing

**Context**: Probe multiple potential method names to map routes systematically.

**Command** ([[commands/curl-multiple-probes]]):
```bash
for method in dashboard_url profile_url secret_url; do curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -X GET "http://target.com/vulnerable?user_input[]=$method"; done
```

> Collects status codes and redirects; 200/302 indicate hits, 500s provide error insights via separate body fetches.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-multiple-probes]]

## Tools Used


## Tags

- disclosure
- error-analysis
- route-enumeration
