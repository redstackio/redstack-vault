---
id: proc-frontegg-create-key-001
tags:
  - api-key-creation
  - frontegg
  - persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:29.178Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Owner-API-Key

## Summary

This procedure generates an API key with Owner privileges in Frontegg, serving as the target for access control exploitation by lower-privileged users.

## Description

Log in to the Owner account and use the dashboard's API keys section to create a new key assigned to the Owner role. This key represents high-privilege access that should be protected from editing by Admins. The procedure assumes Owner login and focuses on UI-based creation. Expected outcome: A new API key with ID for subsequent targeting.

## Requirements

1. Logged-in Owner account
2. Access to tenant admin panel
3. Browser for UI interaction

## Defense

Defensive measures and detection strategies:

- Restrict API key creation to verified Owner sessions
- Audit all key generations with IP and user logging
- Implement key rotation policies post-creation

## Objectives

1. Produce a high-privilege API key for testing
2. Obtain key ID for exploitation steps
3. Validate UI restrictions on editing

## Instructions

### Step 1: Access API Keys Section

**Context**: Navigate to the management interface.

Log in as Owner and go to the API tokens section in the tenant panel.

**Expected Output**: List of existing keys (empty if new).

### Step 2: Generate New Key

**Context**: Create key with Owner role.

Click to generate a new API key and select Owner role during setup.

**Expected Output**: Key details displayed, including ID and role.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api-key-creation]]
- [[frontegg]]
- [[Persistence]]
