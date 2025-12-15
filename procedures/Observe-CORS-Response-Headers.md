---
id: proc-uuid-2
name: Observe-CORS-Response-Headers
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.178Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - cors
  - analysis
  - web
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Observe-CORS-Response-Headers

## Summary

This procedure inspects the HTTP response headers from the API to confirm a CORS misconfiguration, specifically checking for echoed Origin and credential allowance.

## Description

Following the request to Semrush's API, analyze the response for Access-Control-Allow-Origin matching the arbitrary Origin and Access-Control-Allow-Credentials: true. This indicates the server does not validate origins, allowing malicious sites to access responses cross-origin.

## Requirements

1. Successful request from previous procedure
2. Access to response headers via browser dev tools, curl -v, or proxy

## Defense

Defensive measures and detection strategies:

- Log and alert on mismatched or suspicious Origin headers
- Enforce CORS policies with null or specific origins only
- Use Content-Security-Policy to restrict cross-origin fetches

## Objectives

1. Validate permissive CORS policy
2. Confirm vulnerability for exploitation
3. Document headers for reporting

## Instructions

### Step 1: Inspect Response Headers

**Context**: Review the full response from the crafted request.

No command; use tools like curl -v or browser network tab.

> Look for: Access-Control-Allow-Origin: https://itqayzlbkshw.com and Access-Control-Allow-Credentials: true. Success if present.

### Step 2: Confirm Misconfiguration

**Context**: Ensure the policy disables same-origin enforcement.

> If headers allow arbitrary origin with credentials, the misconfiguration is confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cors]]
- [[analysis]]
