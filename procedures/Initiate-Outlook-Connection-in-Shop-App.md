---
tags:
  - oauth-initiation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Android
  - iOS
techniques:
  - '[[Network Device Authentication]]'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
id: bdd39939-e11f-436c-a6fa-fcc7be1bc1ee
created_at: '2025-12-14T17:31:31.011Z'
updated_at: '2025-12-14T17:31:31.011Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Network Device Authentication]]'
---
# Initiate-Outlook-Connection-in-Shop-App

## Summary

This procedure starts the OAuth flow within the Shopify Shop App to connect a Microsoft Outlook account, triggering the vulnerable deep link redirect.

## Description

By navigating to the Outlook integration feature, the app initiates an OAuth 2.0 authorization request to Microsoft, which redirects back via the insecure shopapp:// deep link carrying the authorization code.

## Requirements

1. Installed and logged-in Shopify Shop App
2. Victim's interaction to proceed
3. Internet access for OAuth

## Defense

Defensive measures and detection strategies:

- Validate redirect URIs strictly in OAuth configuration
- Log OAuth initiations for anomaly detection
- User prompts for sensitive integrations

## Objectives

1. Trigger the OAuth authorization request
2. Redirect to Microsoft for consent
3. Generate the deep link with auth code

## Instructions

### Step 1: Open Shop App

**Context**: Launch the app and access account settings.

Open the app and sign in or create an account.

**Expected Output**: Dashboard visible.

### Step 2: Navigate to Integrations

**Context**: Start the Outlook connection process.

Go to settings > Integrations > Connect Microsoft Outlook.

**Expected Output**: OAuth prompt appears.

### Step 3: Confirm Initiation

**Context**: Proceed to trigger the redirect.

Tap to begin, opening the browser.

**Expected Output**: Microsoft login page loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Network Device Authentication]] Network Device Authentication

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[oauth-initiation]]
