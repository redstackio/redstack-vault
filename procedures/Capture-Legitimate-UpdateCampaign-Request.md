---
tags:
  - recon
  - graphql
  - request-capture
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/UpdateCampaign-GraphQL-Mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.293Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a10782ed-4f92-4d4b-ae64-340cfcbc45e0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Legitimate-UpdateCampaign-Request

## Summary

This procedure involves intercepting a legitimate GraphQL UpdateCampaign mutation request on HackerOne's platform to obtain the structure needed for IDOR exploitation, focusing on capturing the base64-encoded campaign_id.

## Description

In the context of testing for IDOR in HackerOne's campaign management, start by editing a campaign you own. Use a proxy or browser tools to capture the POST request to the /graphql endpoint. This reveals the JSON payload with variables like campaign_id, team_id, and dates. The vulnerability stems from insufficient checks on the decoded ID, allowing later manipulation.

## Requirements

1. Authenticated HackerOne session with access to edit a campaign
2. Proxy tool (e.g., Burp Suite) or browser dev tools for interception
3. Basic knowledge of HTTP requests and JSON

## Defense

Defensive measures and detection strategies:

- Implement request logging at the GraphQL endpoint to monitor UpdateCampaign mutations
- Enforce strict authorization checks on decoded GlobalIDs to ensure team ownership

## Objectives

1. Obtain a valid request template for modification
2. Identify the base64-encoded campaign_id structure
3. Prepare for ID tampering without triggering alerts

## Instructions

### Step 1: Edit a Campaign to Trigger Request

**Context**: Navigate to a campaign edit page in a program you control to generate the legitimate mutation.

**Command** ([[commands/UpdateCampaign-GraphQL-Mutation]]):
Use browser dev tools to monitor network requests while submitting the edit form.

```http
POST /graphql HTTP/2
Host: hackerone.com
Cookie: yourcookie
Content-Type: application/json

{"operationName":"UpdateCampaign","variables":{"input":{"campaign_id":"Z2lkOi8vaGFja2Vyb25lL0NhbXBhaWduLzI0NA==",...}},"query":"mutation UpdateCampaign($input: UpdateCampaignInput!) { updateCampaign(input: $input) { was_successful ... } }"}
```

> This captures the full request. Expected output: 200 OK with JSON {'data': {'updateCampaign': {'was_successful': true}}}.

### Step 2: Extract and Save Request

**Context**: Isolate the JSON payload for analysis.

No specific command; copy the request body from the proxy.

> Save as a file for editing. Success if payload includes valid campaign_id.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/UpdateCampaign-GraphQL-Mutation]]

## Tools Used


## Tags

- recon
- graphql
