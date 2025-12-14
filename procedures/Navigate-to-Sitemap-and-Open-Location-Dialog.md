---
id: p-navigate-sitemap-open-location-dialog
tags:
  - navigation
  - concrete-cms
  - sitemap
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
updated_at: '2025-12-14T03:16:20.643Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Sitemap-and-Open-Location-Dialog

## Summary

This procedure guides navigation within Concrete CMS to the Sitemap and opens the Location dialog for a selected page, positioning the attacker to exploit the stored XSS vulnerability in the Additional URLs field.

## Description

Once authenticated, the attacker uses the admin dashboard to access the Sitemap feature, selects any page, and invokes the Location dialog via the context menu. This exposes the vulnerable input field lacking sanitization, allowing subsequent payload injection in the JavaScript-rendered table.

## Requirements

1. Active authenticated session in Concrete CMS.
2. Conversations feature enabled.
3. Browser with JavaScript enabled for dialog rendering.

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to limit Sitemap editing to trusted admins.
- Log all dialog accesses and monitor for anomalous page selections.

## Objectives

1. Access the Sitemap interface.
2. Target a specific page for attribute editing.
3. Open the vulnerable Location dialog.

## Instructions

### Step 1: Access Sitemap from Dashboard

**Context**: Locate the Sitemap section to view page hierarchy.

In the dashboard, click on 'Sitemap' under the Pages menu.

> The Sitemap tree loads, displaying all pages.

### Step 2: Select Page and Open Location Dialog

**Context**: Choose a page and invoke the editing dialog.

Right-click on any page in the Sitemap and select 'Location' from the context menu.

> The Location dialog opens, showing current URL attributes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- navigation
- concrete-cms
- sitemap
