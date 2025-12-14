---
id: proc-identify-endpoint-2024
tags:
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:05.441Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Comment-Submission-Endpoint

## Summary

This procedure involves observing network traffic to identify the comment submission endpoint and its JSON payload structure on intensedebate.com, setting the stage for parameter testing.

## Description

In the attack scenario, users submit comments via a web interface, triggering GET requests to /js/commentAction/ with a JSON payload. By inspecting these requests using browser dev tools or a proxy, attackers can map parameters like acctid, src, and blogpostid for subsequent injection tests. This is a reconnaissance step in web application testing, applicable to PHP-based sites with MySQL backends.

## Requirements

1. Access to a browser with developer tools (e.g., Firefox)
2. Ability to interact with the comment form on intensedebate.com
3. Optional: Proxy tool like Burp Suite for request capture

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) to log unusual request patterns
- Use client-side monitoring to detect dev tools usage
- Rate-limit comment submissions to hinder reconnaissance

## Objectives

1. Locate the /js/commentAction/ endpoint
2. Document JSON payload parameters
3. Prepare for vulnerability testing

## Instructions

### Step 1: Submit a Normal Comment

**Context**: Trigger a legitimate comment submission to capture the baseline request.

Navigate to a blog post on intensedebate.com and submit a test comment. Open browser dev tools (Network tab) to inspect the request.

**Expected Output**: GET request to /js/commentAction/?data={JSON payload}.

### Step 2: Analyze Payload Structure

**Context**: Extract and understand the parameters in the JSON.

Look for keys like "acctid", "src", "blogpostid". Note the structure for modification.

**Expected Output**: Clear mapping of injectable fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- web
