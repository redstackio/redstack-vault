---
id: proc-uuid-5
tags:
  - broken-access-control
  - privilege-escalation
  - shopify
type: procedure
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:52.127Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1068.001]]'
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Bypass-Access-via-Paginated-Endpoint

## Summary

Exploit the lack of permission checks on Shopify's paginated Activity Feed endpoint to allow limited users to view sensitive data.

## Description

The /admin/dashboard/activity_feed endpoint does not enforce 'Home' permissions, unlike the main /admin/activity page. By directly accessing it with limited credentials, attackers can retrieve all shop activities, leading to information disclosure.

## Requirements

1. Limited user session (User Y)
2. Known endpoint URL and parameters
3. Web browser or HTTP client

## Defense

Defensive measures and detection strategies:

- Implement consistent permission checks on all endpoints
- Monitor direct API accesses from limited accounts
- Use API gateways with auth validation

## Objectives

1. Achieve unauthorized data access
2. Escalate privileges via endpoint bypass
3. Disclose sensitive shop events

## Instructions

### Step 1: Log In as Limited User

**Context**: Establish restricted session.

Log in with User Y at https://yourshop.myshopify.com/admin.

> Expected: Limited access granted.

### Step 2: Construct Endpoint URL

**Context**: Build the bypass request.

Use format: https://yourshop.myshopify.com/admin/dashboard/activity_feed?activity_pages=1&activity_filter=all.

> Expected: Valid GET request prepared.

### Step 3: Access Endpoint Directly

**Context**: Send request to vulnerable endpoint.

Navigate to or fetch the constructed URL in browser.

> Expected: JSON or HTML response with full activity data, no permission block.

### Step 4: Iterate Pages

**Context**: Load multiple pages for complete disclosure.

Increment activity_pages parameter (e.g., 2, 3) to fetch more.

> Expected: All historical shop activities visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- [[T1068.001]] Vulnerability in Software Development Lifecycle

## Commands Used


## Tools Used


## Tags

- shopify
- endpoint-bypass
