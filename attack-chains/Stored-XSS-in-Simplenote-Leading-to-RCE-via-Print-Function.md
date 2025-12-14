---
id: ac-simplenote-xss-rce-001
tags:
  - xss
  - rce
  - electron
  - stored-xss
  - desktop-app
type: attack_chain
tools:
  - '[[tools/Simplenote-Desktop-App]]'
  - '[[tools/String-fromCharCode-Encoder]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Desktop
  - Electron
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Simplenote-Desktop-App]]'
  - '[[procedures/Inject-Stored-XSS-Payload-in-Note]]'
  - '[[procedures/Trigger-XSS-via-Print-Function]]'
  - '[[procedures/Escalate-XSS-to-RCE-with-Encoded-Payload]]'
  - '[[procedures/Execute-RCE-and-Post-Fix-Exploitation]]'
step_count: 5
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:28.415Z'
description: >-
  A multi-stage attack exploiting stored XSS in the Simplenote desktop app to
  achieve remote code execution by injecting malicious payloads that trigger
  during note printing.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
---
# Stored XSS in Simplenote Leading to RCE via Print Function

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in Simplenote 1.1.3 desktop app, escalating to full RCE on the victim's machine via Electron's Node.js bindings during note printing or PDF export. The attack allows injection of malicious HTML/JavaScript into shared notes, executing arbitrary commands like spawning applications when the victim prints the note.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup App] --> B[Inject XSS]
    B --> C[Trigger XSS]
    C --> D[Escalate to RCE]
    D --> E[Execute RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Simplenote-Desktop-App]]
- [[tools/String-fromCharCode-Encoder]]

### Target Environment

- Simplenote desktop app version 1.1.3 (or 1.1.4 for post-fix)
- Electron-based desktop platform (Linux, Windows, macOS)
- Markdown disabled for initial exploit (enabled for post-fix)

### Initial Access Requirements

- Access to create or share notes in Simplenote
- Victim must print or export the malicious note as PDF
- No network credentials required; local app exploitation

## Detailed Attack Procedures

### Step 1: Setup Simplenote Desktop App
procedure: [[procedures/Setup-Simplenote-Desktop-App]]

**Objective**: Install and configure the vulnerable Simplenote app to prepare for payload injection.

**Instructions**: Download and install Simplenote 1.1.3 on the target desktop OS, ensuring Markdown is disabled to allow direct HTML injection.

**Expected Output**: App installed and ready for note creation.

**Success Indicators**:
- App launches without errors
- New note creation functional

### Step 2: Inject Stored XSS Payload in Note
procedure: [[procedures/Inject-Stored-XSS-Payload-in-Note]]

**Objective**: Create a note with a stored XSS payload that injects HTML/JavaScript, persisting for execution on print.

**Instructions**: Open the app, create a new note, and input the initial payload `<details open ontoggle=confirm('XSS')>1</details>` to test XSS. For RCE escalation, use an encoded version detailed in later steps.

**Expected Output**: Payload saved in the note without visible errors.

**Success Indicators**:
- Note saves successfully
- Payload appears in note content

### Step 3: Trigger XSS via Print Function
procedure: [[procedures/Trigger-XSS-via-Print-Function]]

**Objective**: Execute the injected JavaScript by invoking the print function, confirming XSS.

**Instructions**: Select the malicious note, go to File > Print. The payload triggers, displaying a confirm dialog with 'XSS'.

**Expected Output**: JavaScript alert or confirm box appears during print preview.

**Success Indicators**:
- Alert confirms XSS execution
- No app crash

### Step 4: Escalate XSS to RCE with Encoded Payload
procedure: [[procedures/Escalate-XSS-to-RCE-with-Encoded-Payload]]

**Objective**: Replace the basic payload with an encoded Node.js script to bypass filters and access Electron's process APIs for RCE.

**Instructions**: Encode a script using String.fromCharCode to spawn a process, e.g., via `writeln(String.fromCharCode(...))` wrapping Node.js code like `var Process = process.binding('process_wrap').Process; ... proc.spawn({file:'/usr/bin/gnome-calculator', ...});`. Inject into a new note.

**Expected Output**: Encoded payload saved; ready for printing.

**Success Indicators**:
- Payload encodes without truncation
- Note renders with hidden script

### Step 5: Execute RCE and Post-Fix Exploitation
procedure: [[procedures/Execute-RCE-and-Post-Fix-Exploitation]]

**Objective**: Trigger RCE by printing the note, spawning an external process; extend to post-fix version with Markdown.

**Instructions**: Print the note to execute the decoded script, launching gnome-calculator. For 1.1.4 with Markdown enabled, use `<a href="javascript:require('child_process').exec('/usr/bin/gnome-calculator',function(){});">CLICK ME</a>`, enable preview, print, and click the link.

**Expected Output**: Calculator app launches on victim's machine.

**Success Indicators**:
- External process spawns successfully
- Full app compromise potential via shared notes

## Attack Chain Summary

### Key Achievements

1. Confirmed stored XSS in note printing
2. Escalated to RCE using Electron Node.js bindings
3. Bypassed filters with encoding
4. Demonstrated post-fix persistence via Markdown

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
