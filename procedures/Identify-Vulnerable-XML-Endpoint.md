---
tags:
  - xxe
  - recon
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-discover-endpoint]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d9202499-8fdb-41cf-8c63-7d13e2633563
created_at: '2025-12-13T09:00:33.907Z'
updated_at: '2025-12-13T09:00:33.907Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable XML Endpoint

## Summary

This procedure involves discovering and confirming web endpoints that process XML inputs, potentially vulnerable to XXE injection due to improper entity handling, as seen in the DuckDuckGo x.js case.

## Description

In this procedure, attackers probe public-facing web endpoints to identify those that accept and parse XML data via parameters like 'u'. The goal is to confirm XML processing without sanitation, setting the stage for XXE exploitation. This is based on the reported vulnerability in https://duckduckgo.com/x.js, where external entities were not properly restricted, leading to file leaks.

## Requirements
1. Network access to the target URL
2. Basic HTTP client tool like curl
3. Knowledge of the target endpoint (e.g., via source info or scanning)

## Defense

Defensive measures and detection strategies:
- Implement strict XML parsing with external entity resolution disabled
- Monitor for unusual HTTP requests containing XML payloads

## Objectives
1. Confirm endpoint accessibility and XML processing
2. Identify parameters vulnerable to injection
3. Prepare for payload crafting

## Instructions

### Step 1: Probe Endpoint Accessibility

**Context**: Send a basic request to verify the endpoint responds.

**Command** ([[commands/curl-discover-endpoint]]):
```bash
curl "https://duckduckgo.com/x.js?u=test"
```

> This command tests if the endpoint processes the 'u' parameter and returns a valid response.

### Step 2: Test for XML Parsing

**Context**: Send a simple XML structure to observe parsing behavior.

**Command** ([[commands/curl-discover-endpoint]]):
```bash
curl "https://duckduckgo.com/x.js?u=<?xml version=\"1.0\"?><foo>bar</foo>"
```

> Look for responses indicating XML was parsed, such as echoed content or errors.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/curl-discover-endpoint]]

## Tools Used
- [[tools/curl]]

## Tags
- xxe
- recon
