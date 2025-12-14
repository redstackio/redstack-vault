---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - dos
  - resource-exhaustion
  - pagination
  - web
  - sqlalchemy
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/crafted-get-group-dos]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.221Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Pagination-DoS-in-Web-Endpoint

## Summary

This procedure exploits inefficient pagination in web applications using libraries like SQLAlchemy-Paginator, causing the server to load entire large datasets into memory when rendering pagination footers, resulting in delays, errors, and potential DoS for authenticated users with many resources.

## Description

In vulnerable applications, the pagination library's iterator method eagerly executes .all() on the full query during Jinja2 template rendering for the footer, consuming excessive CPU and memory for users with 3000+ items. This was observed in ctf.hacker101.com's /group endpoint, where a crafted GET request with specific headers triggers a 40-50 second delay and 502 error via Cloudflare. Concurrent requests amplify to server crashes. Prerequisites include an authenticated session with a large dataset; the attack targets Python-based web apps with SQL backends.

## Requirements

1. Valid credentials for an account with 3000+ groups or similar resources
2. Access to a web browser or HTTP client (e.g., curl) for sending requests
3. Network connectivity to the target web application

## Defense

Defensive measures and detection strategies:

- Implement efficient pagination (e.g., offset/limit without full loads) or use lazy loading in templates
- Rate limit authenticated requests to paginated endpoints
- Monitor for high memory/CPU spikes correlated with /group-like requests; use tools like New Relic or server logs to detect long-running queries
- Validate and sanitize headers like Accept-Encoding to prevent compression-related issues

## Objectives

1. Cause server-side resource exhaustion leading to delays and errors
2. Demonstrate potential for scalable DoS
3. Highlight risks in pagination implementations for large datasets

## Instructions

### Step 1: Authenticate and Prepare Session

**Context**: Log in to establish a session with an account having a large number of groups to maximize resource load.

**Command** ([[commands/crafted-get-group-dos]]):
Use the site's login mechanism to obtain a session cookie.

> No specific command; perform manual login via browser. Expected output: Valid session cookie for subsequent requests.

### Step 2: Send Crafted Request to Trigger Exhaustion

**Context**: Craft and send a GET request to the vulnerable endpoint with headers that may exacerbate processing, while including the session.

**Command** ([[commands/crafted-get-group-dos]]):
```bash
curl -X GET "https://ctf.hacker101.com/group" \
  -H "User-Agent: Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36" \
  -H "Accept-Encoding: gzip, gzip,deflate,br" \
  -H "Cookie: [valid_session_cookie]" \
  -H "Referer: https://ctf.hacker101.com/group" \
  --max-time 60
```

> This command sends the request and waits up to 60 seconds. Expected output: Delay of 40-50 seconds followed by HTTP 502 Bad Gateway and Cloudflare error page.

### Step 3: Verify and Scale (Controlled)

**Context**: Observe the impact and note DoS potential without full execution.

**Command** ([[commands/crafted-get-group-dos]]):
Repeat the command in multiple terminals or tabs (e.g., 5-10 concurrent) in a test environment only.

> Expected output: Cumulative delays leading to server unresponsiveness. Do not execute on production to avoid harm.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/crafted-get-group-dos]]

## Tools Used

- None

## Tags

- dos
- resource-exhaustion
- pagination
- web
- sqlalchemy
