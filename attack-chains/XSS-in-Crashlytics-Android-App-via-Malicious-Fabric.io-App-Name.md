---
tags:
  - xss
  - android
  - crashlytics
  - fabric.io
  - javascript
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-App-with-Payload-Name]]'
  - '[[procedures/Send-Beta-Invitation-via-Fabric-io]]'
  - '[[procedures/Trigger-XSS-on-Tester-Device]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:39.686Z'
description: >-
  A cross-site scripting attack exploiting unsanitized app name rendering in the
  Crashlytics Android app through fabric.io beta invitations, enabling arbitrary
  JavaScript execution on testers' devices.
skill_level: intermediate
impact_level: high
id: 882ab6e0-fadd-4f62-9039-937e2483345b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS in Crashlytics Android App via Malicious Fabric.io App Name

Multi-stage attack chain demonstrating a complete attack workflow exploiting a cross-site scripting vulnerability in the Crashlytics Android app. An attacker creates a test app on fabric.io with a malicious JavaScript payload embedded in the app name. By inviting testers via the beta testing feature, the unsanitized app name is rendered as HTML in the Crashlytics app, executing the payload when the invitation is viewed. This allows arbitrary client-side JavaScript execution, potentially stealing user data or launching Android intents to interact with other apps.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious App] --> B[Send Invitation]
    B --> C[Trigger XSS Execution]
    C --> D[JavaScript Payload Executes]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Fabric.io account (free developer signup)
- Android device or emulator for testing (optional)

### Target Environment

- Fabric.io platform for app creation and beta distribution
- Crashlytics Android app installed on target testers' devices
- No specific ports or services beyond web access to fabric.io

### Initial Access Requirements

- Valid fabric.io developer account
- No prior access to victims needed; relies on social engineering via beta invites
- Network access to fabric.io dashboard

## Detailed Attack Procedures

### Step 1: Create Malicious App
procedure: [[procedures/Create-Malicious-App-with-Payload-Name]]

**Objective**: Register a new app on fabric.io with a malicious JavaScript payload injected into the app name to bypass sanitization during rendering.

**Instructions**: Log into your fabric.io account, navigate to the dashboard, and create a new Android app. In the app name field, enter a payload such as "><img src=x onerror=alert(03)>. Complete the app setup without uploading a real APK, as the vulnerability is in the name rendering, not the app binary. Note the app's unique identifier for the next step.

**Expected Output**: App created successfully on fabric.io, with the malicious name stored.

**Success Indicators**:
- App appears in dashboard with the injected payload in the name field
- No errors during creation; payload not stripped

### Step 2: Send Beta Invitation
procedure: [[procedures/Send-Beta-Invitation-via-Fabric-io]]

**Objective**: Distribute an invitation to target testers, forcing them to interact with the Crashlytics app where the payload will be rendered.

**Instructions**: From the fabric.io dashboard, go to the beta testing section for your malicious app. Add target email addresses as testers and send invitations. The invitation email will prompt recipients to download or open the Crashlytics Android app to accept and view details.

**Expected Output**: Invitations sent; recipients receive emails with links to the beta app details.

**Success Indicators**:
- Confirmation emails sent from fabric.io
- Testers report receiving the invitation

### Step 3: Trigger XSS Execution
procedure: [[procedures/Trigger-XSS-on-Tester-Device]]

**Objective**: Have the victim open the Crashlytics app to view the invitation, causing the unsanitized app name to render as HTML and execute the JavaScript payload.

**Instructions**: Instruct or socially engineer the tester to download/open the Crashlytics app (if not already installed) and navigate to the invitations or beta section. Upon viewing the malicious app's details, the payload executes automatically in the app's rendering context (likely a WebView).

**Expected Output**: JavaScript alert or other payload effects visible on the victim's device, such as an alert box popping up.

**Success Indicators**:
- Payload executes (e.g., alert(03) displays)
- Potential for further actions like intent launches to other apps

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS payload into app metadata without detection
2. Delivery of payload via legitimate beta testing workflow
3. Arbitrary JavaScript execution in a trusted Android app context, enabling data theft or app interactions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
