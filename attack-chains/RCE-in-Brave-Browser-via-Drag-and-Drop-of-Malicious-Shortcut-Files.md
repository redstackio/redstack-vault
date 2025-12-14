---
id: ac-brave-dnd-rce-001
name: RCE in Brave Browser via Drag-and-Drop of Malicious Shortcut Files
type: attack_chain
description: >-
  Multi-stage attack exploiting Brave browser's drag-and-drop handling of
  shortcut files to bypass origin restrictions, load malicious HTML in
  privileged chrome://brave context, read local files, access private APIs, and
  achieve remote code execution via MITM or local vectors on macOS.
verified: false
submitted: true
step_count: 6
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.808Z'
procedures:
  - '[[procedures/Prepare-macOS-Environment-for-Brave-Exploit]]'
  - '[[procedures/Start-MITM-Server-for-Brave-DnD-Attack]]'
  - '[[procedures/Open-Brave-Browser-for-DnD-Interaction]]'
  - '[[procedures/Drag-and-Drop-Malicious-Shortcut-to-Brave]]'
  - '[[procedures/Exploit-Loaded-Content-in-Privileged-Context]]'
  - '[[procedures/Alternative-DnD-Vector-via-Mail-App]]'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
  - '[[Compromise Client Software Binary]]'
  - '[[Hijack Execution Flow]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
  - '[[Impact]]'
tags:
  - rce
  - browser-exploit
  - drag-and-drop
  - mitm
  - privilege-escalation
  - uxss
  - electron
platforms:
  - macOS
  - Browser
tools:
  - '[[tools/Node.js]]'
  - '[[tools/Mail.app]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
  - '[[Compromise Client Software Binary]]'
  - '[[Hijack Execution Flow]]'
---

# RCE in Brave Browser via Drag-and-Drop of Malicious Shortcut Files

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in Brave browser (version 0.24.0 on macOS) where drag-and-drop of .webloc shortcut files allows navigation to the privileged 'chrome://brave' origin, bypassing Chromium-level patches. This enables loading malicious HTML in Muon's privileged context, leading to local file reads, access to Electron's private APIs (ipcRenderer, ipcMain), arbitrary IPC commands, and remote code execution (RCE) via shell commands or .terminal file execution. The attack requires user interaction (DnD) but can be facilitated remotely via MITM on domains like maps.googleapis.com or locally via reflected XSS/HTML files.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Environment] --> B[Start MITM Server]
    B --> C[Open Brave Browser]
    C --> D[Drag-and-Drop Shortcut]
    D --> E[Exploit Privileged Context]
    E --> F[Alternative Mail.app Vector]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node.js]]
- [[tools/Mail.app]]

### Target Environment

- Target OS/Platform: macOS with Brave browser 0.24.0 (Muon 8.1.6, Chromium-based)
- Required services/ports: httpd service (to stop for MITM), port 80/443 for Node.js server
- Network access requirements: Local admin privileges for /etc/hosts modification; MITM requires interception of HTTPS traffic (e.g., maps.googleapis.com)

### Initial Access Requirements

- Credential requirements: Admin/sudo access on macOS for environment setup
- Network position: Local machine or MITM position (e.g., via compromised network)
- Prior access needed: Physical/local access to drag-and-drop files, or remote delivery of malicious shortcuts/links

## Detailed Attack Procedures

### Step 1: Prepare Environment
procedure: [[procedures/Prepare-macOS-Environment-for-Brave-Exploit]]

**Objective**: Set up macOS environment to enable MITM interception for the DnD exploit.

**Instructions**: Stop the httpd service and modify /etc/hosts to redirect traffic for MITM.

**Expected Output**: httpd stopped, hosts file updated with '127.0.0.1 maps.googleapis.com'.

**Success Indicators**:
- httpd service confirmed stopped via `ps aux | grep httpd`
- Ping to maps.googleapis.com resolves to 127.0.0.1

### Step 2: Start MITM Server
procedure: [[procedures/Start-MITM-Server-for-Brave-DnD-Attack]]

**Objective**: Launch Node.js server to intercept and inject malicious content during DnD navigation.

**Instructions**: Execute [[commands/start-mitm-server]] to run the server with elevated privileges.

```bash
sudo node server.js
```

**Expected Output**: Server logs indicating it's running and ready to proxy requests.

**Success Indicators**:
- Server output shows "MITM server running on port 80/443"
- Test request to maps.googleapis.com is intercepted

### Step 3: Open Brave Browser
procedure: [[procedures/Open-Brave-Browser-for-DnD-Interaction]]

**Objective**: Load a benign page in Brave to prepare for drag-and-drop interaction.

**Instructions**: Launch Brave and navigate to any HTTP/HTTPS page (e.g., google.com) to establish a tab for DnD.

**Expected Output**: Brave browser open with a loaded page.

**Success Indicators**:
- Browser tab active and responsive
- No errors in browser console

### Step 4: Drag and Drop Malicious Shortcut
procedure: [[procedures/Drag-and-Drop-Malicious-Shortcut-to-Brave]]

**Objective**: Use DnD of a crafted .webloc file to navigate to chrome://brave/<local_file>, triggering malicious HTML load via MITM.

**Instructions**: Create a .webloc file pointing to 'chrome://brave/etc/passwd' and drag it to the Brave tab.

**Expected Output**: Navigation to privileged origin, loading intercepted malicious HTML.

**Success Indicators**:
- Alert or page load showing /etc/passwd contents
- Network logs in MITM server confirm injection

### Step 5: Exploit Loaded Content
procedure: [[procedures/Exploit-Loaded-Content-in-Privileged-Context]]

**Objective**: Leverage the privileged context to read files, execute IPC commands, and achieve RCE.

**Instructions**: The loaded HTML uses ipcRenderer to send commands, e.g., read files or launch apps via chrome.shell.openExternal.

**Expected Output**: File contents displayed, Calculator.app launched, or shell commands executed.

**Success Indicators**:
- Local file read successful (e.g., alert with /etc/passwd)
- External app execution (e.g., Calculator opens)
- Persistence via protocol registration

### Step 6: Alternative Vector via Mail.app
procedure: [[procedures/Alternative-DnD-Vector-via-Mail-App]]

**Objective**: Deliver the malicious URL via email and DnD from Mail.app to bypass shortcut file creation.

**Instructions**: Send a mail with 'chrome://brave/etc/passwd' link and drag it directly to Brave.

**Expected Output**: Same navigation and exploit as Step 4.

**Success Indicators**:
- DnD from Mail.app triggers the same privileged load
- Exploit executes without .webloc file

## Attack Chain Summary

### Key Achievements

1. Bypassed chrome:// origin restrictions via DnD of shortcuts handled at Chromium level
2. Loaded malicious HTML in Muon's privileged context for local file reads and API access
3. Achieved RCE through IPC commands, .terminal execution, and shell access, leading to full system compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[JavaScript]] JavaScript
- [[Compromise Client Software Binary]] Compromise Client Software Binary
- [[Hijack Execution Flow]] Hijack Execution Flow

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation
- [[Discovery]] Discovery
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
