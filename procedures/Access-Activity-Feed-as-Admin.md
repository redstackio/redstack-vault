---
id: proc-uuid-2
tags:
  - shopify
  - activity-feed
type: procedure
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:28:52.135Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Access-Activity-Feed-as-Admin

## Summary

Log in as a full admin user to access and view the Shopify Activity Feed, establishing baseline functionality.

## Description

Using admin credentials, navigate to the activity page in Shopify admin to load shop events. This step confirms proper access and observes pagination mechanisms for later exploitation.

## Requirements

1. Admin user credentials (User X)
2. Web browser
3. Valid Shopify session

## Defense

Defensive measures and detection strategies:

- Log all admin panel accesses
- Implement session timeouts

## Objectives

1. Verify admin access to sensitive features
2. Identify pagination endpoints
3. Collect baseline activity data

## Instructions

### Step 1: Log In as Admin

**Context**: Authenticate to gain full access.

Enter credentials for User X at https://yourshop.myshopify.com/admin.

> Expected: Dashboard loads successfully.

### Step 2: Navigate to Activity Feed

**Context**: Load the main activity page.

Go to https://yourshop.myshopify.com/admin/activity.

> Expected: Activity feed displays shop events.

### Step 3: Interact with Pagination

**Context**: Trigger loading of additional data to observe endpoints.

Scroll or click 'Load more' to fetch paginated content.

> Expected: Additional activities load via backend call.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- admin-access
