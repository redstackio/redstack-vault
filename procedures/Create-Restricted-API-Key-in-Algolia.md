---
tags:
  - algolia
  - api-key
type: procedure
tools:
  - '[[tools/Algolia-Dashboard]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:10.481Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b67725bf-deba-4f4e-a919-ef336c5c467f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Restricted-API-Key-in-Algolia

## Summary

This procedure generates a restricted API key in the Algolia dashboard, limiting it to specific operations on a single index, setting up the foundation for testing scope enforcement.

## Description

In Algolia, API keys can be scoped to particular indices and permissions. This procedure creates a key with 'addObject' permission only for the 'test' index, simulating a limited-access scenario such as for an invited collaborator. The key is then used to probe for enforcement flaws, potentially leading to broader access within the same application.

## Requirements

1. Active Algolia account with dashboard access
2. Permissions to generate API keys
3. Knowledge of the target application ID (e.g., FTCHS7XZX2)

## Defense

Defensive measures and detection strategies:

- Enforce strict API key scoping and validate index names server-side
- Monitor API key usage logs for anomalous index access patterns
- Use rate limiting and anomaly detection on batch operations

## Objectives

1. Obtain a scoped API key for testing
2. Verify key creation without full admin privileges
3. Prepare for scope bypass validation

## Instructions

### Step 1: Access Algolia Dashboard

**Context**: Log in to the Algolia dashboard to navigate to API key management.

No command required; use the web interface at https://www.algolia.com.

> Log in with your credentials and select the target application.

### Step 2: Generate Restricted Key

**Context**: Create a new key with limited ACL for the 'test' index.

No command; dashboard UI action.

> In the 'API Keys' section, click 'Add API Key', set ACL to 'addObject' on 'test' index only, and generate. Copy the key value.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Algolia-Dashboard]]

## Tags

- [[algolia]]
- [[api-key]]
