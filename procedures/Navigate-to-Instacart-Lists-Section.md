---
id: p-navigate-instacart-lists
tags:
  - navigation
  - web-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:23.495Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Instacart-Lists-Section

## Summary

This procedure describes accessing the 'Lists and Recipes' section in the authenticated Instacart application to reach the shopping list management interface, a prerequisite for exploiting the stored XSS vulnerability.

## Description

After authentication, the lists feature is available via the navigation menu. This section allows users to create and manage shopping lists, where the list name input lacks sanitization, enabling payload injection. The target URL is https://www.instacart.com/store/demo/lists, part of the web platform's frontend.

## Requirements

1. Active authenticated session in Instacart
2. Web browser
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Log navigation patterns to detect unusual access to administrative or feature-specific pages
- Implement role-based access controls to restrict list management
- Use client-side monitoring to flag rapid navigation sequences

## Objectives

1. Load the lists management page
2. Verify access to 'Add List' functionality
3. Position for payload injection

## Instructions

### Step 1: Select Lists Option

**Context**: From the main dashboard, locate and select the lists feature.

In the navigation menu, click 'Lists and Recipes'.

> This directs to the lists page. Expected output: Page loads with existing lists and an 'Add List' button.

### Step 2: Confirm Page Load

**Context**: Ensure the correct interface is accessible.

Verify the URL is https://www.instacart.com/store/demo/lists and the add feature is present.

> Expected output: No 404 or access denied errors; interactive elements visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
- [[web]]
