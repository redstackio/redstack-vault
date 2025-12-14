---
id: proc-gitlab-trigger-xss-dashboard
tags:
  - xss-trigger
  - csrf-exploitation
  - ssh-compromise
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/javascript-alert-opener-location]]'
  - '[[commands/javascript-csrf-theft-ssh-addition]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:15.909Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Trigger-XSS-via-Metrics-Dashboard-Link

## Summary

This procedure triggers the stored XSS by accessing the Metrics Dashboard in the GitLab admin sidebar, rendering the malicious link and executing the JavaScript payload upon click, leading to session manipulation.

## Description

Once the payload is stored, it appears as a clickable link in the admin sidebar under Monitoring -> Metrics Dashboard. The link uses target='_blank', but the javascript: scheme executes in the new tab, leveraging window.opener to manipulate the original tab's DOM, steal sensitive data like CSRF tokens, and perform actions such as adding SSH keys.

## Requirements

1. Payload injected from previous procedure
2. Another admin session (or self in test) to click the link
3. jQuery loaded in the GitLab page for advanced payload

## Defense

Defensive measures and detection strategies:

- Escape URLs in link rendering (e.g., use Rails' h() helper)
- Disable window.opener access via rel='noopener noreferrer' on links
- Monitor for anomalous POST requests to /profile/keys from admin sessions

## Objectives

1. Render and click the stored payload link
2. Execute JS to access original tab
3. Achieve impact like token theft and account modification

## Instructions

### Step 1: Navigate to Metrics Dashboard

**Context**: Access the sidebar link where the payload renders.

From the admin area, click Monitoring -> Metrics Dashboard.

**Expected Output**: Sidebar shows the Grafana link with the injected URL.

### Step 2: Click the Malicious Link

**Context**: Trigger execution in a new tab.

Click the Metrics Dashboard link (target='_blank').

**Command** (executes implicitly via link):
For basic: [[commands/javascript-alert-opener-location]]

For advanced: [[commands/javascript-csrf-theft-ssh-addition]]

> The browser executes the javascript: payload, accessing window.opener to run code in the original context.

**Expected Output**: Alert (basic) or silent POST request (advanced) adding SSH key.

**Success Indicators**:
- Alert displays original URL
- New SSH key appears in victim's /profile/keys

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-opener-location]]
- [[commands/javascript-csrf-theft-ssh-addition]]

## Tools Used


## Tags

- [[xss-trigger]]
- [[csrf-exploitation]]
- [[ssh-compromise]]

---
