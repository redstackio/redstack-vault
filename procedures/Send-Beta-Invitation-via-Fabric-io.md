---
tags:
  - phishing
  - beta-testing
  - fabric.io
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
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:24:39.670Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c0167293-a7a5-4d0a-b8ce-29ee5ddf2916
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Send-Beta-Invitation-via-Fabric-io

## Summary

This procedure uses the fabric.io beta testing feature to send invitations to target users, prompting them to open the Crashlytics Android app where the previously injected XSS payload will be rendered and executed.

## Description

After creating a malicious app, the attacker leverages fabric.io's built-in beta distribution to invite testers via email. The invitation process integrates with the Crashlytics app, requiring recipients to download or launch it to view details. This step relies on social engineering to ensure victims interact with the app, delivering the payload without direct malware distribution. Expected outcomes include high engagement from legitimate-looking invites, leading to XSS trigger on Android devices.

## Requirements

1. Fabric.io app created with payload (from prior procedure)
2. List of target email addresses
3. Web access to fabric.io dashboard

## Defense

Defensive measures and detection strategies:

- Review beta invitations for suspicious app names or sources before accepting
- Use email filters to flag unexpected developer invites
- Disable auto-download of beta apps in Crashlytics settings
- Audit fabric.io accounts for anomalous activity

## Objectives

1. Deliver the malicious invitation to targets
2. Induce victims to open the Crashlytics app
3. Position for automatic payload execution

## Instructions

### Step 1: Access Beta Testing Section

**Context**: Navigate to the distribution tools for the malicious app.

In the fabric.io dashboard, select your app and go to the 'Beta' or 'Distribute' tab.

### Step 2: Add Testers and Send Invites

**Context**: Configure and dispatch invitations to victims.

Enter target email addresses in the tester list, customize the invitation message if needed (e.g., "Test my new app!"), and click 'Send Invites'. The system will email links that direct to the Crashlytics app for acceptance.

> Invites appear legitimate, referencing the app name (including payload) and prompting app download if missing.

### Step 3: Monitor Invitation Status

**Context**: Verify delivery and potential acceptance.

Check the dashboard for sent status and any acceptance notifications. Follow up via email if needed to encourage opening the app.

**Expected Output**: Invites delivered; dashboard shows pending testers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- social-engineering
- beta-invitation
