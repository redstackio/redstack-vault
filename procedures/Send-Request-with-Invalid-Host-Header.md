---
id: proc-irccloud-host-send-7357
tags:
  - host-header-injection
  - open-redirect
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-host-header]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.256Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Request-with-Invalid-Host-Header

## Summary

This procedure exploits the lack of Host header validation on irccloud.com by sending an HTTP request with an arbitrary Host value, resulting in an open redirect to the specified domain. It demonstrates the core vulnerability enabling potential phishing or cache poisoning.

## Description

In the IRCCloud application, the server processes HTTP requests without verifying the Host header against the intended domain (irccloud.com). An attacker crafts a request where the Host header is set to a malicious domain, causing the server to redirect users to that domain. This can be chained with web-cache poisoning to serve malicious redirects to legitimate users via shared caches. The attack requires no authentication and works over standard HTTP.

## Requirements

1. Network access to irccloud.com (ports 80/443)
2. Tool capable of custom HTTP header manipulation (e.g., curl)
3. Control over a domain for testing the redirect target

## Defense

Defensive measures and detection strategies:

- Implement strict Host header validation to match only irccloud.com
- Use absolute URLs in redirects to prevent relative or external domain resolution
- Monitor server logs for anomalous Host headers and unexpected redirects

## Objectives

1. Trigger an open redirect to an attacker-controlled domain
2. Validate the vulnerability for further exploitation like cache poisoning
3. Assess impact on user traffic redirection

## Instructions

### Step 1: Craft and Send the Malicious Request

**Context**: Prepare an HTTP GET request to irccloud.com but override the Host header to point to an arbitrary domain, observing the server's redirect response.

**Command** ([[commands/curl-send-host-header]]):
```bash
curl -H "Host: evil.com" http://irccloud.com/ -v
```

> This command sends a GET request with the Host header set to 'evil.com'. The verbose (-v) flag shows headers, including any Location header in the response indicating a redirect to http://evil.com/. Successful execution confirms the server trusts the injected Host without validation.

### Step 2: Analyze Response for Redirect

**Context**: Inspect the HTTP response to confirm the open redirect behavior and note the lack of error handling.

**Command** ([[commands/curl-send-host-header]]):
```bash
curl -H "Host: attacker.com" http://irccloud.com/ -i
```

> The -i flag includes response headers. Look for a 302 or 301 status with Location: http://attacker.com/. This step verifies the redirect is unvalidated and applicable to various endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-send-host-header]]

## Tools Used


## Tags

- [[host-header-injection]]
- [[open-redirect]]
