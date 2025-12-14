---
id: proc-trigger-iframe-exploit
tags:
  - execution
  - redirect
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.001]]'
updated_at: '2025-12-13T23:52:33.490Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.001]]'
---
# Trigger-Iframe-Load-for-Redirect-and-Popup

## Summary

This procedure saves or previews the tainted template to load the injected iframe, executing the Firebase JavaScript for open redirects and phishing popups against viewers.

## Description

Upon triggering, the CSP allows the frame-src load due to the *.firebaseapp.com wildcard. The JS then attempts top-level redirects and popups, assuming browser policies permit from my.stripo.email. This impacts template viewers (e.g., via https://viewstripo.email/) and can chain to organization-wide phishing; requires no additional tools beyond the browser.

## Requirements

1. Saved template with injected iframe
2. Browser allowing popups and cross-origin redirects
3. Access to preview or share functionality

## Defense

Defensive measures and detection strategies:

- Tighten CSP to block wildcard sources and enforce frame-ancestors
- Disable JS in previews or sandbox iframes
- Detect anomalous redirects/popups via browser security features or endpoint monitoring

## Objectives

1. Load iframe to execute payload
2. Achieve redirect and popup for phishing
3. Disrupt editor usability if needed

## Instructions

### Step 1: Preview Template

**Context**: Initiate load without full save to test.

Click 'Preview' in Stripo editor.

> Expected: Iframe loads; JS executes if CSP permits.

### Step 2: Save and Share

**Context**: Persist and expose to victims.

Save template; generate share link (e.g., https://viewstripo.email/...).

> Expected: Viewer loads with active iframe exploitation.

### Step 3: Verify Impact

**Context**: Confirm redirect/popup in target browser.

Open share link; observe behavior.

> Expected: Alert, redirect to attacker.com, popup to phish-site.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- execution
- redirect
- phishing
