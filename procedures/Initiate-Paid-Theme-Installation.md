---
id: proc-shopify-initiate-paid-install
tags:
  - shopify
  - theme-trial
  - installation
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
updated_at: '2025-12-14T17:30:35.801Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Paid-Theme-Installation

## Summary

This procedure starts the trial installation of a paid theme on themes.shopify.com, creating a brief window where a temporary theme ID is generated before full installation and payment validation complete.

## Description

The attack relies on the installation process exposing a temporary theme entity via GraphQL before enforcing purchase checks. By clicking 'Try theme' on a paid theme page (e.g., Mr. Parker), the process begins, and switching back to the admin panel allows monitoring the progress spinner, signaling the race window is open.

## Requirements

1. Open tab with admin/themes and dev tools
2. Access to themes.shopify.com
3. Captured publish request from prior step

## Defense

Defensive measures and detection strategies:

- Delay theme ID exposure until installation verifies payment
- Monitor concurrent admin and theme store sessions

## Objectives

1. Trigger paid theme download and temporary ID creation
2. Observe installation state in admin for timing
3. Open race condition window for publish exploit

## Instructions

### Step 1: Navigate to Paid Theme

**Context**: Select a target paid theme.

Open a new tab to https://themes.shopify.com/, search and visit a paid theme like https://themes.shopify.com/themes/mr-parker.

### Step 2: Start Trial

**Context**: Initiate the vulnerable process.

Click the "Try theme" button to begin installation; act quickly as the window is short.

### Step 3: Monitor in Admin

**Context**: Switch to observe progress.

Return to the admin/themes tab, refresh the page, and look for the installing theme with a spinner in the Theme library.

**Expected Output**: Spinner animation indicating ongoing installation.

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

- paid-theme
- race-window
