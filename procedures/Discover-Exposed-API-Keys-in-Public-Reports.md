---
id: proc-discover-exposed-api-keys-001
name: Discover Exposed API Keys in Public Reports
tags:
  - credential-harvesting
  - public-disclosure
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:11.110Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Discover Exposed API Keys in Public Reports

## Summary

This procedure involves searching and reviewing public vulnerability disclosure platforms like HackerOne to identify API keys that were exposed in prior reports but not revoked, enabling potential credential access for unauthorized use.

## Description

In scenarios like the Stripo Inc. report, attackers review disclosed reports for sensitive credentials such as API keys. If the organization fails to revoke the key post-disclosure, it remains active, allowing access to API functionalities including data retrieval or manipulation. This targets web-based services and relies on public information availability. Expected outcomes include obtaining a usable credential without direct system compromise.

## Requirements

1. Internet access to search engines and HackerOne
2. Knowledge of target organization and vulnerability keywords (e.g., 'API key disclosure')
3. Basic text parsing skills to extract keys from report content

## Defense

Defensive measures and detection strategies:

- Immediately revoke any disclosed credentials upon report publication
- Monitor API logs for anomalous access patterns from known exposed keys
- Implement key rotation policies and usage alerts

## Objectives

1. Harvest active API keys from public sources
2. Identify non-revoked credentials for exploitation
3. Enable initial access to target APIs

## Instructions

### Step 1: Search for Relevant Reports

**Context**: Use search engines to find public reports containing potential credential disclosures.

Search query: "site:hackerone.com Stripo API key disclosure"

> This yields reports like #1709815. Review the narrative for key exposure.

### Step 2: Extract and Document the Key

**Context**: Parse the report content to isolate the API key.

Manually copy the key from the report text (e.g., a Bearer token string).

> Expected output: A string like 'sk_live_abc123...' ready for testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unprotected Storage of Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[credential-harvesting]]
- [[public-disclosure]]
