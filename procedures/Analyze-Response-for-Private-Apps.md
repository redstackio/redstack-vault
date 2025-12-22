---
id: proc-analyze-response-private-apps
tags:
  - analysis
  - disclosure
  - private-apps
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:53.584Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Analyze-Response-for-Private-Apps

## Summary

This procedure examines the GraphQL API response to identify and extract details of private apps, confirming the information disclosure vulnerability.

## Description

After sending the modified query, the response contains an array of app objects. By filtering for "isPrivate": true, attackers can uncover sensitive data like handles and API client IDs from unauthorized stores, enabling potential further attacks such as impersonation or token abuse.

## Requirements

1. Successful response from the modified GraphQL query
2. JSON parsing tool or Burp Suite's response viewer
3. Basic understanding of GraphQL pagination (edges/node structure)

## Defense

Defensive measures and detection strategies:

- Audit API responses for over-exposure of data
- Implement field-level authorization in GraphQL schema
- Alert on queries returning large result sets

## Objectives

1. Parse the JSON response for app details
2. Identify private apps via the isPrivate flag
3. Document exposed sensitive information

## Instructions

### Step 1: Inspect Response in Burp

**Context**: View the full JSON payload from the API.

No command required; in Burp Repeater, switch to the Response tab.

> Look for the 'data' > 'shopApps' > 'edges' array. Expected output: Paginated list of app nodes.

### Step 2: Filter for Private Apps

**Context**: Search and extract unauthorized private app data.

Use Burp's search or export to JSON viewer; grep for "isPrivate":true.

> Confirm multiple private apps from other stores. Expected output: Details like {"id":"gid://...","isPrivate":true,"handle":"private-app","shopifyApiClientId":"..."}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- analysis
- disclosure
- private-apps
