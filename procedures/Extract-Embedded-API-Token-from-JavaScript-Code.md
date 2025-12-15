---
tags:
  - credential-access
  - token-leak
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Credentials In Files]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6f0f2375-4dd2-479b-b073-542ce10c7f4f
created_at: '2025-12-14T17:32:39.185Z'
updated_at: '2025-12-14T17:32:39.185Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-Embedded-API-Token-from-JavaScript-Code

## Summary

This procedure involves reviewing downloaded JavaScript code to identify and extract embedded API tokens, such as the internal token for api.semrush.com used in statistical endpoints.

## Description

Semrush's internal JS files hardcode API tokens in client-side code for convenience, but this exposes them publicly. Analysis reveals the token in configuration objects or API call setups. Prerequisites: downloaded JS files; outcomes: usable token for unauthorized access.

## Requirements

1. Downloaded JS files
2. Text editor (e.g., VS Code) or browser console
3. Regex knowledge for token patterns

## Defense

Defensive measures and detection strategies:

- Obfuscate or externalize secrets from client-side code
- Use server-side proxies for API calls with token validation
- Scan JS files for secrets during code reviews and deployments

## Objectives

1. Locate token in JS code
2. Validate token format and purpose
3. Securely copy for use

## Instructions

### Step 1: Open and Search JS File

**Context**: Scan for API-related strings.

Open the JS file in a text editor and search for "api.semrush.com".

> Look for patterns like const token = 'sk_abc123...' or in fetch() headers.

### Step 2: Extract and Note Token

**Context**: Isolate the credential.

Copy the token string (e.g., a 32+ char alphanumeric key). Note its usage context from surrounding code.

> Expected: Token confirmed as internal API key for stats endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[credential-access]]
- [[token-leak]]
