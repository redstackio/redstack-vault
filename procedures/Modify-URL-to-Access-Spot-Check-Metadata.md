---
tags:
  - information-disclosure
  - graphql
  - url-manipulation
  - idor
type: procedure
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:30:35.431Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: fb80cf6f-da5c-4da5-80fd-8782b0cbadab
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Modify URL to Access Spot Check Metadata

## Summary

This procedure exploits insufficient authorization in HackerOne's GraphQL backend by altering the Spot Check ID in the URL, triggering the SpotCheckSingleQuery to disclose confidential metadata like hacker counts, budgets, and selection criteria to unauthorized users.

## Description

The vulnerability stems from the backend returning program-owner-level data without proper checks when a hacker accesses a specific Spot Check ID they are invited to. By modifying the URL from the general Spot Checks page to include a targeted ID, the GraphQL query executes with variables {"id":"[spot-check-id]","product_area":"spot_checks","product_feature":"view"}, leaking sensitive information. This requires prior invitation to the Spot Check but compromises operational confidentiality. Expected outcomes include visible metadata in the page response or network tab.

## Requirements

1. Active session from the previous navigation step
2. Knowledge of a valid Spot Check ID (obtainable from invitations or page source)
3. Browser developer tools to inspect GraphQL responses

## Defense

Defensive measures and detection strategies:

- Enforce role-based access controls (RBAC) in GraphQL resolvers for SpotCheckSingleQuery
- Validate user permissions against the specific Spot Check ID before querying
- Monitor for anomalous GraphQL queries from hacker accounts accessing owner metadata

## Objectives

1. Trigger unauthorized data retrieval via URL parameter tampering
2. Extract and view confidential Spot Check details
3. Demonstrate the scope of information disclosure without further privileges

## Instructions

### Step 1: Identify Target Spot Check ID

**Context**: Locate a Spot Check ID you are invited to, typically from email invitations or the Spot Checks list.

No command; inspect the page source or network requests for IDs in the format of GraphQL variables.

> Example ID might appear as a UUID in the interface or prior API calls.

### Step 2: Construct and Load Modified URL

**Context**: Append the ID to the URL to force the single-view query, bypassing list-level restrictions.

Navigate to: https://hackerone.com/organizations/[organization-id]/spot_checks/[spot-check-id]

> Replace [organization-id] with the program's ID and [spot-check-id] with the target ID. Load the page and check the Network tab in developer tools for the GraphQL response.

### Step 3: Inspect Disclosed Data

**Context**: Analyze the response for leaked fields.

In the browser's developer tools, filter for SpotCheckSingleQuery and examine the JSON payload.

> Look for fields like "hackerCount", "budget", and "selectionCriteria" that reveal private details.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- graphql-query
- metadata-leak
- authorization-bypass
