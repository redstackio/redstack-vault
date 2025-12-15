---
id: proc-shopify-prepare-free-theme
tags:
  - shopify
  - setup
  - theme-install
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.806Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Shopify-Store-with-Free-Theme

## Summary

This procedure sets up a Shopify store by ensuring a default theme is published and installing/publishing a free theme, creating a baseline for monitoring theme changes during the exploit.

## Description

In the context of exploiting Shopify's theme race condition, this initial setup verifies the store's theme management is functional. It involves accessing the admin panel to confirm the default theme and then installing a free theme from the library to use as a reference for capturing publish requests. This step requires authenticated access to a Shopify merchant account and ensures no disruptions in theme publishing before proceeding to the paid theme exploitation.

## Requirements

1. Authenticated access to Shopify admin panel
2. Internet browser like Google Chrome
3. No prior theme issues in the store

## Defense

Defensive measures and detection strategies:

- Monitor admin panel access logs for unusual theme installations
- Implement rate limiting on theme publish actions

## Objectives

1. Establish a published default theme for store functionality
2. Install and publish a free theme to intercept legitimate requests
3. Prepare environment for race condition exploitation

## Instructions

### Step 1: Verify Default Theme

**Context**: Confirm the store has a default theme set as published to avoid any baseline errors.

Navigate to the Shopify admin panel at https://yourshop.myshopify.com/admin/themes and verify the default theme is listed as "Published".

### Step 2: Install Free Theme

**Context**: Add a free theme to the library for publishing actions.

In the admin/themes section, click "Visit Theme Store", search for a free theme, and click "Add" to install it.

### Step 3: Publish Free Theme

**Context**: Set the free theme as the main published theme to generate a publish request.

Select the installed free theme and click "Publish" to make it active.

**Expected Output**: Theme updates to "Published" status in the library.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- shopify
- theme-setup
