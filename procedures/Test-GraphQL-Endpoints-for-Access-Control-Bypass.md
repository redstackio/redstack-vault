---
id: proc-885539-test-endpoints
tags:
  - graphql
  - access-control
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:00.373Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test GraphQL Endpoints for Access Control Bypass

## Summary

This procedure tests enumerated GraphQL endpoints by sending POST requests to identify those allowing execution of persisted queries without proper authorization, specifically the ListMembers query that bypasses private list privacy checks.

## Description

Targeting https://api.twitter.com/graphql, this involves crafting requests with extracted queryIds and variables to probe for improper access controls. The ListMembers query (iUmNRKLdkKVH4WyBNw9x2A) executes regardless of list visibility, disclosing members without verifying user access. Use Burp Suite for interception and Firefox for manual validation in an authenticated session. Expected outcome is unauthorized data retrieval, highlighting the vulnerability in Twitter's API implementation.

## Requirements

1. Authenticated Twitter session (cookies or API token).
2. List of queryIds from prior enumeration.
3. Proxy setup for request modification.

## Defense

Defensive measures and detection strategies:

- Enforce strict access controls on all GraphQL queries based on user permissions.
- Log and rate-limit anomalous query patterns or unauthorized endpoint access.
- Use introspection disabling and persisted query validation.

## Objectives

1. Confirm executable persisted queries.
2. Identify bypass of privacy checks in ListMembers.
3. Gather evidence of data leakage.

## Instructions

### Step 1: Craft and Send Test Requests

**Context**: Use Burp Suite to intercept and modify POST requests to /graphql.

Send a request with body: {"queryId":"iUmNRKLdkKVH4WyBNw9x2A","variables":{"listId":"test-id","count":20}}.

**Expected Output**: JSON response with list members if bypass succeeds; no auth error.

### Step 2: Validate in Browser

**Context**: Use Firefox developer tools to execute queries manually.

Open console and send fetch('/graphql/...') with the same payload.

**Expected Output**: Successful retrieval of private list data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Firefox]]

## Tags

- [[access-control]]
- [[bypass]]
