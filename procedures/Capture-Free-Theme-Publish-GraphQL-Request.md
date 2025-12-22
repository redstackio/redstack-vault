---
id: proc-shopify-capture-publish-request-927567
tags:
  - shopify
  - graphql
  - request-capture
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:29.092Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Free-Theme-Publish-GraphQL-Request

## Summary

This procedure captures the legitimate GraphQL mutation request for publishing a free theme in Shopify, providing a template for modification to target paid themes and bypass access controls.

## Description

By publishing a free theme through the Shopify admin UI, this step intercepts the underlying XHR POST request to the unversioned GraphQL endpoint (/admin/online-store/admin/api/unversioned/graphql). Using browser dev tools, the request is copied as a JavaScript fetch for replay. This assumes an installed free theme and focuses on the ThemePublishLegacy mutation. It sets up for API tampering without direct impact.

## Requirements

1. Installed free theme in Shopify
2. Browser with Network tab in Developer Tools
3. Active admin session

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens in all GraphQL mutations
- Monitor for duplicated or replayed API requests in logs
- Rate-limit theme publication endpoints

## Objectives

1. Intercept the ThemePublishLegacy mutation payload
2. Export request as executable fetch code
3. Validate free theme publication to confirm capture

## Instructions

### Step 1: Open Developer Tools

**Context**: Prepare to monitor network traffic during publication.

Open browser DevTools > Network tab > Filter by XHR/Fetch.

> Clear existing logs for clarity.

### Step 2: Publish Free Theme

**Context**: Trigger the mutation to capture the request.

In admin, select free theme > Click 'Publish'.

> Request appears in Network tab: POST to GraphQL endpoint.

### Step 3: Copy as Fetch

**Context**: Export the request for modification.

Right-click the request > Copy > Copy as Fetch > Paste into console.

> Result: JavaScript fetch code with variables.id for free theme.

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

- shopify
- graphql
- request-capture
