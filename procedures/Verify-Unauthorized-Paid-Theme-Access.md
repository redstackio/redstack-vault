---
id: proc-shopify-verify-access
tags:
  - shopify
  - verification
  - access-bypass
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
updated_at: '2025-12-14T17:30:35.795Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Unauthorized-Paid-Theme-Access

## Summary

This procedure confirms the exploit success by checking if the paid theme is published without purchase indicators, enabling unauthorized editing and downloading of theme files.

## Description

After the race-timed publish, the installation completes normally, but the theme is now set as main without trial restrictions. Refreshing the admin/themes page reveals full access, including file editing and ZIP download, leading to potential content theft and financial impact for Shopify.

## Requirements

1. Publish mutation executed successfully
2. Installation process completed
3. Admin/themes page accessible

## Defense

Defensive measures and detection strategies:

- Audit published themes against purchase records
- Flag themes published during installation

## Objectives

1. Confirm theme status as published
2. Test access to restricted features
3. Validate bypass of payment controls

## Instructions

### Step 1: Wait for Completion

**Context**: Allow installation to finish post-publish.

Monitor the spinner until it stops, indicating installation end.

### Step 2: Refresh and Check Status

**Context**: Verify the theme's new state.

Refresh https://yourshop.myshopify.com/admin/themes and locate the paid theme.

### Step 3: Test Access

**Context**: Attempt unauthorized actions.

Click "Customize" or "Download theme" on the paid theme; no trial badge or purchase prompt should appear.

**Expected Output**: Theme marked as "Published", files editable without restrictions.

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

- theme-access
- bypass-verification
