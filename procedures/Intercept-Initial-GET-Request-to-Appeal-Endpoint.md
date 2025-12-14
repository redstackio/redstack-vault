---
tags:
  - auth-bypass
  - http-intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:31:52.514Z'
sub_techniques: []
id: 2104a38b-8be4-4893-b0c5-c33297fd3f62
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Initial-GET-Request-to-Appeal-Endpoint

## Summary

This procedure captures the initial GET request to the appeal creation endpoint in the DoD application, setting the stage for authentication bypass by identifying the authentication-enforced redirect.

## Description

In the context of the DoD ASP.NET web application, unauthenticated access to /App/createappeal.aspx triggers a 302 redirect to login. Intercepting this request allows subsequent manipulation. This is typically done using a proxy tool in a man-in-the-middle setup, targeting web applications vulnerable to client-side redirect reliance without server-side checks.

## Requirements

1. Proxy tool like Burp Suite installed and running
2. Browser configured to proxy traffic through the tool (e.g., 127.0.0.1:8080)
3. Network access to the target DoD application

## Defense

Defensive measures and detection strategies:

- Implement server-side authentication checks on all sensitive endpoints
- Monitor for anomalous HTTP response codes in proxy logs
- Use Web Application Firewalls (WAF) to detect traffic interception patterns

## Objectives

1. Capture the authentication redirect response
2. Prepare for response tampering
3. Gain unauthorized form access

## Instructions

### Step 1: Configure Proxy and Navigate

**Context**: Set up interception and trigger the request.

Intercept traffic using Burp Suite Proxy. Open the browser and navigate to https://target/app/createappeal.aspx.

**Expected Output**: GET request to /App/createappeal.aspx appears in the proxy history, followed by a 302 response.

### Step 2: Capture and Inspect Request

**Context**: Analyze the request to confirm endpoint and headers.

In Burp Suite, select the request in the Proxy tab and forward it, noting the 302 redirect location (likely to login).

**Expected Output**: Detailed request/response visible, confirming authentication enforcement.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth-bypass]]
- [[http-intercept]]
