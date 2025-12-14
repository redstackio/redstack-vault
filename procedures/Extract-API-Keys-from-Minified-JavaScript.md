---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: Extract-API-Keys-from-Minified-JavaScript
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:48.529Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials In Files]]'
tags:
  - credential-access
  - parsing
  - api-keys
platforms:
  - Web
tools:
  - '[[tools/JSONParserOnline]]'
commands: []
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---

# Extract-API-Keys-from-Minified-JavaScript

## Summary

This procedure parses a minified JavaScript file to extract hardcoded sensitive API keys, such as those for Aviary and YouTube services.

## Description

Given a downloaded or viewed minified JS file like main.c1965c58f39a0f4aadc3.js, the attacker uses text search or online parsing tools to identify and extract cleartext credentials embedded within the code. This targets web applications where secrets are improperly stored client-side. The outcome is the disclosure of authentication keys, enabling unauthorized API access. Prerequisites include the JS file and a parsing tool.

## Requirements

1. Downloaded JS file or direct access to its contents
2. Online or local tool for JSON/string parsing
3. Basic regex knowledge for key pattern matching

## Defense

Defensive measures and detection strategies:

- Never hardcode secrets in client-side code; use environment variables or secure vaults
- Implement code scanning in CI/CD to detect exposed keys
- Rotate keys immediately upon exposure detection

## Objectives

1. Parse the file to reveal embedded credentials
2. Extract specific API keys like aviaryApiKey and youtubeApiKey
3. Assess potential for unauthorized service access

## Instructions

### Step 1: Load File into Parser

**Context**: Upload or paste the JS contents into an online tool for analysis.

Use [[tools/JSONParserOnline]] to view the file: Visit the tool site and input the minified code.

> The tool beautifies or searches the content, making strings visible.

### Step 2: Search for Key Patterns

**Context**: Look for API key indicators within the parsed output.

Search for terms like 'aviaryApiKey' or 'youtubeApiKey' using the tool's search function.

> Expected output: Cleartext keys extracted, e.g., aviaryApiKey: 'actual_key_value'.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/JSONParserOnline]]

## Tags

- [[credential-access]]
- [[parsing]]
