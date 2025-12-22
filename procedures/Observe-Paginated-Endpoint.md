---
id: proc-uuid-4
tags:
  - shopify
  - endpoint-discovery
type: procedure
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:52.129Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-Paginated-Endpoint

## Summary

As an admin, interact with the Activity Feed to identify the paginated API endpoint used for loading additional data.

## Description

While viewing activities, trigger pagination to capture the backend request to /admin/dashboard/activity_feed. Note parameters like activity_pages and activity_filter for replication in bypass attempts.

## Requirements

1. Admin session (User X)
2. Browser developer tools (e.g., Network tab)
3. Knowledge of HTTP requests

## Defense

Defensive measures and detection strategies:

- Obfuscate internal API endpoints
- Log all API calls with user context

## Objectives

1. Discover vulnerable endpoint
2. Document request parameters
3. Prepare for unauthorized access

## Instructions

### Step 1: Open Developer Tools

**Context**: Monitor network traffic.

In browser, open DevTools and go to Network tab while logged in as admin.

> Expected: Tools ready to capture requests.

### Step 2: Load Activities and Paginate

**Context**: Trigger API calls.

Visit /admin/activity and click 'Load more' or scroll.

> Expected: Requests to /admin/dashboard/activity_feed?activity_pages=1&activity_filter=all captured.

### Step 3: Note Endpoint Details

**Context**: Analyze the request.

Inspect the URL, method (GET), and parameters.

> Expected: Full endpoint path and query params recorded.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- api-discovery
