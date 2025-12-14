---
id: proc-uuid-2
tags:
  - ssrf
  - php
  - codeigniter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.374Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-SSRF-in-Json-Status-Function

## Summary

This procedure focuses on pinpointing the SSRF vulnerability in the json_status function of the Campaign controller by analyzing its code and testing basic invocations, confirming acceptance of arbitrary URLs including protocols like gopher:// without validation.

## Description

The json_status function in Campaign.php (line 1048) is defined as public function json_status($status, $real_url = null, $component = null), where $real_url is processed without sanitization, allowing SSRF to localhost or internal services. In a public-facing PHP app on AWS, this enables blind SSRF for reconnaissance. Prerequisites: Source code access and ability to send HTTP requests. Outcomes: Verified SSRF vector for payload crafting.

## Requirements

1. Source code of Campaign.php
2. Ability to send GET requests to the target endpoint
3. Basic understanding of URL encoding

## Defense

Defensive measures and detection strategies:

- Validate and whitelist URLs in functions handling remote fetches, blocking internal IPs and non-HTTP protocols.
- Use web application firewalls (WAF) like ModSecurity to detect gopher:// or localhost patterns.
- Log and monitor requests to controller endpoints for anomalous parameters.

## Objectives

1. Confirm unvalidated $real_url parameter.
2. Test basic SSRF to localhost.
3. Prepare for advanced payload exploitation.

## Instructions

### Step 1: Analyze Function Code

**Context**: Review the function definition to understand input handling.

No command; inspect line 1048 in Campaign.php.

> Note lack of validation on $real_url, allowing arbitrary input.

### Step 2: Test Basic SSRF

**Context**: Send a simple request to trigger SSRF to localhost.

Use curl or browser: curl "https://labs.data.gov/dashboard/Campaign/json_status/gopher%3A%2F%2F127.0.0.1/"

> Expected: Server processes the gopher URL, confirming SSRF (may return 200 OK or error).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[vulnerability-identification]]
