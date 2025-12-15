---
tags:
  - csrf
  - web
  - interception
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: da56b5e3-b005-4587-8b10-b502fc40aba5
created_at: '2025-12-14T17:27:22.593Z'
updated_at: '2025-12-14T17:27:22.593Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-HTTP-Requests-to-Identify-CSRF-Token-Storage

## Summary

This procedure involves capturing HTTP requests to a web application's edit endpoint to identify how CSRF tokens are set and stored, revealing improper cookie-based handling in the Gratipay application.

## Description

In web applications using CSRF protections, tokens are typically passed in forms or headers. Here, intercepting traffic to the statement edit endpoint (e.g., /~username/statement.json) shows the token being set via Set-Cookie, exposing it to cookie interception risks. This step is foundational for analyzing token mishandling and potential bypasses. Prerequisites include a valid session and proxy setup; outcomes include visibility into response headers.

## Requirements

1. Web browser or proxy tool for traffic interception
2. Authenticated access to the target application
3. Knowledge of the edit endpoint URL

## Defense

Defensive measures and detection strategies:

- Implement strict cookie attributes (HttpOnly, Secure) for session cookies, but isolate CSRF tokens
- Monitor for anomalous proxy traffic or use WAF to detect interception attempts
- Use token-per-request generation to limit exposure

## Objectives

1. Capture request/response to edit endpoint
2. Identify CSRF token in Set-Cookie header
3. Document storage mechanism for risk assessment

## Instructions

### Step 1: Setup Interception

**Context**: Configure a tool to monitor HTTPS traffic to the target site.

Open browser developer tools (Network tab) or use a proxy like Burp Suite. Ensure HTTPS decryption if needed.

### Step 2: Trigger Edit Request

**Context**: Perform an action that hits the edit endpoint to capture the response.

Navigate to the user's statement edit page on Gratipay.com and submit a change, or simulate via POST to https://gratipay.com/~username/statement.json.

**Expected Output**: Response headers including Set-Cookie: csrftoken=some_token_value.

### Step 3: Extract Token Details

**Context**: Analyze the captured data for token handling.

Inspect the cookie value and note its visibility alongside other cookies.

**Expected Output**: Token like zxRdWnGq3I5bMcXDRUWuWWXjxdsO1JtZ observed in cookie.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[interception]]
