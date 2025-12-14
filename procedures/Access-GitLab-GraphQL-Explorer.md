---
tags:
  - graphql
  - gitlab
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.093Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7b4144d2-e102-4293-bffd-80cdb8bc8da4
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-GitLab-GraphQL-Explorer

## Summary

This procedure outlines how to access GitLab's public GraphQL Explorer, a web-based interface for testing GraphQL queries without authentication, serving as the entry point for information disclosure attacks.

## Description

The GitLab GraphQL Explorer is publicly accessible at https://gitlab.com/-/graphql-explorer, allowing unauthenticated users to execute queries against the API. In the context of this vulnerability, it exposes private fields like user emails due to missing access controls. This step requires only a web browser and internet access, with no prior authentication needed. Expected outcomes include loading the interactive query editor, enabling further API exploration.

## Requirements

1. Web browser with JavaScript enabled
2. Internet connectivity to reach gitlab.com
3. No GitLab account or credentials required

## Defense

Defensive measures and detection strategies:

- Restrict GraphQL Explorer to authenticated users only
- Implement rate limiting on public API endpoints
- Monitor for anomalous GraphQL queries in access logs

## Objectives

1. Gain entry to the GraphQL interface for query execution
2. Confirm public accessibility without barriers
3. Prepare for sensitive data retrieval

## Instructions

### Step 1: Navigate to Explorer

**Context**: Directly access the public endpoint to load the interface.

No command required; use browser navigation.

> Open your web browser and go to https://gitlab.com/-/graphql-explorer. The page should load the GraphQL Explorer UI, including a query editor on the left and response pane on the right.

### Step 2: Confirm Accessibility

**Context**: Verify no authentication prompt appears, confirming unauthenticated access.

No command required.

> Interact with the interface by clicking the 'Execute Query' button with a simple test query like '{ __schema { types { name } } }'. A successful response indicates the endpoint is open.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- graphql
- gitlab
- web-access
