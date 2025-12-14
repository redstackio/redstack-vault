---
id: proc-001
tags:
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/normal-bugs-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:27:30.213Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Observe-Normal-Bugs-Endpoint-Behavior

## Summary

This procedure observes the standard behavior of the HackerOne /bugs endpoint to understand how it fetches report JSON via XHR, serving as a baseline for identifying manipulation opportunities in subsequent steps.

## Description

In the HackerOne platform, the /bugs endpoint is used to load bug reports for a given subject (team). When a valid integer report_id is provided, it triggers an internal XHR GET request to /reports/{report_id}.json to fetch the report data. This step confirms the normal flow, including authentication via session cookies, and identifies the lack of strict validation on the report_id parameter, which is key for path traversal exploitation. The target environment is a web application built on Ruby on Rails, proxied through nginx and Cloudflare.

## Requirements

1. Authenticated session on HackerOne (valid cookie)
2. Access to browser dev tools or curl for request inspection
3. Valid report_id (e.g., 99698) for the target subject (e.g., anontest5667)

## Defense

Defensive measures and detection strategies:

- Implement request logging for /bugs endpoint to monitor unusual report_id patterns
- Use WAF rules to detect traversal sequences like '../' in parameters
- Enforce CSRF tokens on all state-changing endpoints, even internal ones

## Objectives

1. Confirm normal JSON fetching mechanism
2. Identify internal XHR trigger points
3. Baseline for detecting deviations in manipulated requests

## Instructions

### Step 1: Send Standard GET Request

**Context**: Initiate a normal request to the /bugs endpoint to observe the triggered XHR.

**Command** ([[commands/normal-bugs-request]]):
```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=99698&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

> This command simulates loading the bugs page. In a browser, inspect the Network tab to see the XHR to /reports/99698.json. Expected output includes the bugs page HTML and JSON report data.

### Step 2: Verify XHR Response

**Context**: Confirm the internal fetch succeeds and returns valid JSON.

**Command** (Manual inspection):
```bash
# No direct command; use dev tools or proxy like Burp to capture XHR
```

> Look for 200 OK on /reports/{id}.json with report details. Success confirms the endpoint's reliance on report_id for path construction.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/normal-bugs-request]]

## Tools Used


## Tags

- recon
- web
- hackerone
