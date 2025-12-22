---
id: proc-uuid-2
tags:
  - ui-navigation
  - discovery
  - mobile
  - uber
  - promo-codes
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:42.827Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access Promotion Code Redemption Feature in Uber App

## Summary

This procedure details navigating the Uber iOS app's user interface to reach the promo code redemption section immediately after registration, setting the stage for brute force attempts on the unprotected endpoint.

## Description

Post-registration, the Uber app allows direct access to the promotion code application feature without requiring prior rides or payments. This vulnerability in the app's design enables attackers to test codes right away. The procedure involves standard UI interactions to locate the input field, where API calls to the redemption endpoint occur. Outcomes include readiness for rapid submissions, with no built-in delays or limits observed.

## Requirements

1. Active new Uber account from previous step
2. Uber iOS app open on dashboard
3. Basic familiarity with app navigation

## Defense

Defensive measures and detection strategies:

- Require minimum account activity (e.g., first ride) before promo access
- Log and alert on rapid UI navigations post-signup
- Implement session-based rate limits on feature access

## Objectives

1. Locate and activate the promo code input interface
2. Confirm endpoint accessibility without restrictions
3. Prepare for code submission testing

## Instructions

### Step 1: Navigate to Account Section

**Context**: From the main dashboard, access settings or payments to find promo options.

No specific command; interact via UI:

- Tap the profile icon or menu.
- Select "Payments" or "Promotions" tab.

> Expected output: Sub-menu with promo code option visible.

### Step 2: Open Redemption Input

**Context**: Initiate the code application process.

No specific command; interact via UI:

- Tap "Add Promo Code" or similar button.
- Input field for code appears.

> Expected output: Text field ready for entry, submit button active.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ui-navigation
- discovery
- mobile
