---
id: proc-shopify-access-themes
tags:
  - shopify
  - admin-dashboard
  - navigation
type: procedure
tools: []
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
updated_at: '2025-12-14T17:29:56.867Z'
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
# Access-Shopify-Themes-Section

## Summary

This procedure details navigating to the Themes section in a Shopify store's admin dashboard, a prerequisite for generating preview tokens used in authentication bypass.

## Description

Within Shopify's admin interface, the Themes section under Sales channels > Online Store allows access to preview functionality. This step positions the attacker to click 'View your store' for token generation. It assumes prior login to the store admin and targets development stores. Outcome: Themes page loaded, ready for preview link extraction.

## Requirements

1. Logged-in session to the target development store admin
2. Standard web browser
3. No additional permissions beyond store owner access

## Defense

Defensive measures and detection strategies:

- Enforce session timeouts and multi-factor authentication on admin logins
- Log navigation patterns to sensitive sections like Themes
- Block automated access to admin paths

## Objectives

1. Reach the preview token generation point
2. Maintain admin session integrity
3. Avoid triggering any access controls

## Instructions

### Step 1: Log In to Store Admin

**Context**: Ensure authenticated access to the store dashboard.

Visit <store-name>.myshopify.com/admin and log in.

> Expected output: Admin homepage displayed.

### Step 2: Navigate to Sales Channels

**Context**: Locate the Online Store management area.

Click 'Sales channels' in the left sidebar, then select 'Online Store'.

> Expected output: Online Store settings page.

### Step 3: Enter Themes Section

**Context**: Access the specific area for theme previews.

Click 'Themes' to load the theme management interface.

> Expected output: List of installed themes with 'View your store' option.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[admin-dashboard]]
- [[navigation]]
