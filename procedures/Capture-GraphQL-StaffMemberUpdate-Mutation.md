---
id: proc-capture-graphql-mutation-001
name: Capture-GraphQL-StaffMemberUpdate-Mutation
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.624Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - graphql
  - network-intercept
commands: []
platforms:
  - Web
tools:
  - '[[tools/Browser-Developer-Tools]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Capture-GraphQL-StaffMemberUpdate-Mutation

## Summary

This procedure captures the StaffMemberUpdate GraphQL mutation request from Shopify's POS interface using browser developer tools, providing the payload needed for email modification.

## Description

By simulating a staff profile save in the POS interface, the GraphQL mutation to https://pos-channel.shopifycloud.com/graphql-proxy/admin is triggered. Intercepting this via network tools reveals the mutation structure, including variables for email updates, which can then be replayed with alterations. This targets stores with Google Apps enabled where no Google link exists.

## Requirements

1. Target profile loaded in POS staff management
2. Browser with open developer tools (e.g., Chrome DevTools)
3. Basic understanding of HTTP requests and CURL

## Defense

Defensive measures and detection strategies:

- Rate-limit GraphQL mutations on staff updates
- Log all StaffMemberUpdate requests with IP and user context
- Use request signing or CSRF tokens to prevent replay attacks

## Objectives

1. Obtain the exact GraphQL payload for StaffMemberUpdate
2. Export as CURL for offline modification
3. Ensure no authentication tokens are invalidated during capture

## Instructions

### Step 1: Open Network Inspection

**Context**: Prepare to monitor outgoing requests from the POS interface.

In the browser, open Developer Tools (F12) and navigate to the Network tab. Filter for XHR/Fetch requests.

### Step 2: Trigger Profile Save

**Context**: Initiate the mutation by attempting to save the staff profile.

With the target profile open, make a minor change (e.g., add a space to a non-critical field) and click "Save" to send the GraphQL request.

### Step 3: Copy CURL Request

**Context**: Export the intercepted mutation for modification.

Locate the POST request to /graphql-proxy/admin, right-click it, and select "Copy as cURL" to clipboard.

**Expected Output**: Full CURL command including headers, variables, and the mutation query.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- graphql
- mutation-capture
- shopify
