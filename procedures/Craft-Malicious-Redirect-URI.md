---
tags:
  - bypass
  - redirect
  - uri-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-redirect-uri]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:19.961Z'
sub_techniques: []
id: dd45d8ef-5246-49a1-a3f9-b9716bc38f82
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious Redirect URI

## Summary

This procedure constructs a redirect_uri that exploits prefix-based validation in Login.gov by appending an attacker-controlled domain as a subdomain (e.g., agency.gov.example.com), allowing it to pass as legitimate.

## Description

Attackers leverage the validation flaw where hostnames are checked for starting with a registered domain like 'agency.gov' rather than exact equality. By controlling example.com, the URI https://agency.gov.example.com/malicious directs post-auth traffic to the attacker after validation succeeds.

## Requirements

1. Attacker-controlled domain and hosting for callback
2. Knowledge of target registered domains (e.g., agency.gov)
3. HTTP client for testing

## Defense

Defensive measures and detection strategies:

- Enforce exact domain matching and port/protocol restrictions
- Validate URIs against a strict allowlist
- Monitor for subdomain-like anomalies in logs

## Objectives

1. Create a URI that evades validation
2. Verify acceptance by the endpoint
3. Set up for flow initiation

## Instructions

### Step 1: Construct the URI

**Context**: Build the malicious URI using the target's domain prefix and attacker's domain.

**Command** ([[commands/curl-test-redirect-uri]]):
```bash
curl -X GET "https://idp.login.gov/oauth/authorize?client_id=TEST_CLIENT&redirect_uri=https://agency.gov.example.com/malicious&response_type=code&scope=openid" -v
```

> The command tests if the crafted URI is accepted; success if no validation error.

### Step 2: Validate on Attacker Side

**Context**: Ensure the attacker site can receive redirects; set up a simple HTTP server if needed.

**Command** ([[commands/curl-test-redirect-uri]]):
```bash
# On attacker site, but test endpoint acceptance first as above
```

> Confirm redirect would land on controlled endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-redirect-uri]]

## Tools Used


## Tags

- [[bypass]]
- [[redirect]]
