---
id: proc-identify-target-app-id
tags:
  - shopify
  - app-id
  - recon
type: procedure
tools: []
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
updated_at: '2025-12-14T17:29:19.737Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-Target-App-ID

## Summary

This procedure retrieves the global ID of a target custom app in Shopify, necessary for targeting it in GraphQL mutations for uninstallation or other operations.

## Description

Shopify apps are referenced by global IDs (e.g., 'gid://shopify/App/6431859') in API calls. This step involves inspecting the admin interface or using queries to enumerate and identify the ID of a custom app installed by developers. It assumes staff-level access and focuses on apps visible in the store's app list. Outcome: Precise ID for exploitation.

## Requirements

1. Authenticated staff session in Shopify admin
2. Target custom app already installed
3. Browser dev tools for inspection

## Defense

Defensive measures and detection strategies:

- Restrict app visibility to authorized roles only
- Log API queries for app enumeration
- Use app installation whitelisting

## Objectives

1. Enumerate installed custom apps
2. Extract global ID for targeting
3. Validate ID format and accessibility

## Instructions

### Step 1: Access Apps Section

**Context**: Log in as staff and view installed apps.

1. Navigate to Apps in the admin sidebar.
2. Locate the target custom app in the list.

**Expected Output**: List of installed apps displayed.

### Step 2: Inspect App Details

**Context**: Use dev tools to find the global ID.

1. Right-click the app and 'Inspect Element'.
2. Search for 'gid://shopify/App/' in network requests or DOM elements.
3. Alternatively, run a GraphQL query for apps if API access allows.

**Expected Output**: ID like 'gid://shopify/App/6431859' copied.

### Step 3: Verify ID

**Context**: Confirm the ID corresponds to the correct app.

1. Note app title or details alongside ID.
2. Test in a safe query if possible.

**Expected Output**: Valid ID confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- app-id
- discovery
