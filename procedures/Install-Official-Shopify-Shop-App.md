---
tags:
  - app-installation
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Android
  - iOS
techniques: []
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 98f06a38-f009-4b10-994d-158f2bb18cd0
created_at: '2025-12-14T17:31:31.014Z'
updated_at: '2025-12-14T17:31:31.014Z'
verified: false
validated: true
submitted: true
---
# Install-Official-Shopify-Shop-App

## Summary

This procedure installs the legitimate Shopify Shop App from official stores, setting up the environment for the OAuth flow exploitation.

## Description

The official app must be present to initiate the vulnerable OAuth integration with Microsoft Outlook. Installation from trusted sources ensures the flow triggers correctly, allowing the malicious app to intercept the subsequent deep link.

## Requirements

1. Access to Google Play Store (Android) or App Store (iOS)
2. Device with internet connectivity
3. Sufficient storage space (~100MB)

## Defense

Defensive measures and detection strategies:

- Regularly update apps to patch known vulnerabilities
- Use app store restrictions to prevent sideloading
- Monitor installed apps for anomalies

## Objectives

1. Deploy the official app to enable OAuth initiation
2. Ensure compatibility with the malicious app scheme
3. Prepare for user interaction in the flow

## Instructions

### Step 1: Access App Store

**Context**: Navigate to the official store on the device.

Open Google Play Store or App Store and search for "Shopify Shop".

**Expected Output**: App page loads.

### Step 2: Download and Install

**Context**: Initiate installation of the official app.

Tap "Install" and wait for completion.

**Expected Output**: App icon appears on home screen.

### Step 3: Launch and Verify

**Context**: Confirm the app functions normally.

Open the app and create a test account if needed.

**Expected Output**: App dashboard loads.

## MITRE ATT&CK Mapping

### Tactics

-

### Techniques

-

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[app-installation]]
