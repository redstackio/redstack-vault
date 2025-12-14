---
tags:
  - lateral-movement
  - interface-exploration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.688Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 67616899-ee21-4c0f-8bd0-8c657efebe94
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Switch-to-Alternative-Dashboard-Interface

## Summary

This procedure involves navigating to an alternative dashboard endpoint (`███/home`) that offers similar but enhanced functionality, allowing further exploitation of access controls.

## Description

The application has multiple dashboard views; switching exposes more features without additional authentication. This builds on initial access, targeting web navigation; outcomes include access to advanced UI elements for deeper data exposure.

## Requirements

1. Valid session from primary dashboard
2. Knowledge of the alternative URL `███/home`
3. Web browser

## Defense

Defensive measures and detection strategies:

- Unify dashboard endpoints with consistent RBAC.
- Log URL navigations and block unauthorized paths.
- Redirect or restrict alternative interfaces to admins.

## Objectives

1. Access enhanced dashboard features.
2. Expand attack surface.
3. Identify additional vulnerabilities.

## Instructions

### Step 1: Navigate to Alternative Endpoint

**Context**: Leave the primary dashboard for the variant.

From the current page, enter or click to `███/home` in the browser.

> The alternative interface loads with a slightly different layout.

### Step 2: Verify Functionality

**Context**: Confirm expanded options.

Explore the new UI, noting additional buttons like 'Add Content'.

> More functionality available compared to primary view.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[lateral-movement]]
- [[interface-exploration]]
