---
tags:
  - recon
  - oauth
  - openid-connect
  - validation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-inspect-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:19.964Z'
sub_techniques: []
id: a8456a78-0c10-4dec-a4b1-eba57125c72c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify OpenID Connect Endpoint and Validation

## Summary

This procedure involves probing the OpenID Connect authorization endpoint to identify and understand the redirect_uri validation mechanism, revealing flaws like prefix-based hostname checking instead of exact matches.

## Description

In the context of Login.gov, attackers examine the /openid_connect/authorize endpoint to test how redirect_uris are validated. The flaw allows URIs like agency.gov.example.com to pass as valid for agency.gov, enabling open redirects. This is typically done via HTTP requests in a browser or tool, observing responses to infer logic without source code access.

## Requirements

1. Network access to Login.gov endpoints
2. Basic knowledge of OAuth/OpenID Connect flows
3. Tools for HTTP inspection (e.g., curl or Burp Suite)

## Defense

Defensive measures and detection strategies:

- Implement exact hostname matching in redirect validation
- Log and monitor anomalous redirect_uris
- Use allowlists for registered redirect domains

## Objectives

1. Confirm endpoint existence and parameter handling
2. Identify validation weakness (prefix vs. exact match)
3. Prepare for crafting bypassing URIs

## Instructions

### Step 1: Probe the Authorization Endpoint

**Context**: Send a GET request to the authorize endpoint with a legitimate redirect_uri to observe behavior.

**Command** ([[commands/curl-inspect-endpoint]]):
```bash
curl -X GET "https://idp.login.gov/oauth/authorize?client_id=TEST_CLIENT&redirect_uri=https://agency.gov/callback&response_type=code&scope=openid" -v
```

> This command initiates the flow and logs verbose output, showing if the URI is accepted. Look for 302 redirects or error responses indicating validation.

### Step 2: Test Invalid URI for Comparison

**Context**: Try an obviously invalid URI to baseline error handling, then test borderline cases like subdomains.

**Command** ([[commands/curl-inspect-endpoint]]):
```bash
curl -X GET "https://idp.login.gov/oauth/authorize?client_id=TEST_CLIENT&redirect_uri=https://invalid.com/callback&response_type=code&scope=openid" -v
```

> Expect a 4xx error for invalid; absence for prefix-matching subdomains confirms the flaw.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inspect-endpoint]]

## Tools Used


## Tags

- [[recon]]
- [[oauth]]
