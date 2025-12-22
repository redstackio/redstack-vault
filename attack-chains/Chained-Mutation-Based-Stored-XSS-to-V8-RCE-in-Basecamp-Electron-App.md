---
tags:
  - xss
  - rce
  - electron
  - v8
  - rop
  - memory-corruption
  - trix-editor
  - basecamp
type: attack_chain
tools:
  - '[[tools/Trix-Editor]]'
  - '[[tools/Windbg]]'
  - '[[tools/AWS-EC2]]'
  - '[[tools/VirtualBox]]'
  - '[[tools/DOMPurify]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/copy-payload-html]]'
  - '[[commands/decoded-mathml-xss]]'
  - '[[commands/rop-stage1-write-calc]]'
  - '[[commands/rop-stage2-resolve-winexec]]'
  - '[[commands/rop-stage3-prepare-params]]'
  - '[[commands/rop-stage4-call-winexec]]'
  - '[[commands/adjust-rop-gadget-server2022]]'
verified: false
platforms:
  - Web
  - Windows
  - macOS
  - Electron
submitted: true
complexity: high
procedures:
  - '[[procedures/Craft-XSS-Payload-HTML-for-Trix-Editor]]'
  - '[[procedures/Copy-Payload-Text-for-Pasting]]'
  - '[[procedures/Paste-into-Basecamp-Trix-Editor-to-Trigger-XSS]]'
  - '[[procedures/Trigger-V8-Exploit-via-Iframe-Button]]'
  - '[[procedures/Adjust-ROP-Chain-for-Target-OS]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
description: >-
  A multi-stage attack exploiting a mutation-based stored XSS in Trix Editor to
  execute JavaScript, chained with V8 memory corruption in the Electron-based
  Basecamp Desktop App for remote code execution on Windows systems.
skill_level: advanced
impact_level: critical
id: 2cc1dd3b-b2ed-4898-96f5-529d3246e4fd
created_at: '2025-12-13T23:55:06.774Z'
updated_at: '2025-12-13T23:55:06.774Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
---
# Chained Mutation-Based Stored XSS to V8 RCE in Basecamp Electron App

Multi-stage attack chain exploiting a sanitizer bypass in Trix Editor (v2.1.8) via mutated MathML for stored XSS, chained with V8 memory corruption in the Electron-based Basecamp Desktop App to achieve remote code execution, such as launching calc.exe on Windows.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | Critical |

## Attack Flow Visualization

```mermaid
graph LR
    A[Payload Crafting] --> B[Copy-Paste XSS Trigger]
    B --> C[JavaScript Execution]
    C --> D[V8 Memory Corruption]
    D --> E[RCE via ROP Chain]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Trix-Editor]]
- [[tools/Windbg]]
- [[tools/AWS-EC2]]
- [[tools/VirtualBox]]

### Target Environment

- Basecamp Desktop App (Electron-based, vulnerable V8 version)
- Trix Editor v2.1.8
- Windows/macOS host with Basecamp installed
- No specific ports required; local app execution

### Initial Access Requirements

- Access to Basecamp Desktop App session (user-level)
- Ability to paste content into Trix Editor fields
- Debugging tools for ROP offset adjustment

## Detailed Attack Procedures

### Step 1: Payload Crafting
procedure: [[procedures/Craft-XSS-Payload-HTML-for-Trix-Editor]]

**Objective**: Create an HTML file with a mutated MathML payload to bypass Trix Editor sanitizer via copy-paste.

**Instructions**: Generate an HTML file using [[commands/copy-payload-html]] to embed the payload in a div with data-trix-attachment. Save as payload.html and open in a browser.

```html
<div data-trix-attachment="{\"contentType\":\"text/html5\",\"content\":\"<math><mtext><table><mglyph><style><img src=x onerror=alert()>XSSPOC</style>XSSPOC</mglyph></table></mtext></math>"}>copy me</div>
```

**Expected Output**: Browser displays 'copy me' text selectable for copying, with hidden payload.

**Success Indicators**:
- HTML file renders without errors
- Payload text is copyable

### Step 2: Copy Payload
procedure: [[procedures/Copy-Payload-Text-for-Pasting]]

**Objective**: Copy the encoded payload text to clipboard for pasting into Trix Editor.

**Instructions**: Select and copy the 'copy me' text from the HTML file opened in browser. The clipboard now holds the mutated payload using [[commands/decoded-mathml-xss]] structure.

**Expected Output**: Clipboard contains encoded MathML with img onerror handler.

**Success Indicators**:
- Text copied successfully
- No visible errors in browser console

### Step 3: Trigger XSS
procedure: [[procedures/Paste-into-Basecamp-Trix-Editor-to-Trigger-XSS]]

**Objective**: Paste the payload into Basecamp's Trix Editor to mutate and execute JavaScript, bypassing sanitizer.

**Instructions**: Open Basecamp Desktop App, navigate to a Trix Editor field (e.g., message composer), and paste the copied text. The mutation evades sanitization, executing [[commands/decoded-mathml-xss]] to load an external script or alert.

**Expected Output**: Alert() popup or external script loads, confirming XSS.

**Success Indicators**:
- JavaScript executes (alert or network request)
- No sanitization blocks the paste

### Step 4: V8 Exploitation
procedure: [[procedures/Trigger-V8-Exploit-via-Iframe-Button]]

**Objective**: Use the XSS to embed an iframe and trigger V8 memory corruption for ROP chain execution.

**Instructions**: The XSS payload embeds an iframe with a 'Click me' button calling pwn(). Click it to execute ROP stages: [[commands/rop-stage1-write-calc]], [[commands/rop-stage2-resolve-winexec]], [[commands/rop-stage3-prepare-params]], [[commands/rop-stage4-call-winexec]]. Use Windbg to monitor.

**Expected Output**: calc.exe launches on Windows.

**Success Indicators**:
- Memory corruption triggers
- Calculator opens

### Step 5: ROP Adjustment
procedure: [[procedures/Adjust-ROP-Chain-for-Target-OS]]

**Objective**: Fine-tune ROP offsets for specific Windows builds using debugging.

**Instructions**: Use [[tools/Windbg]] on a target VM (e.g., via [[tools/AWS-EC2]] or [[tools/VirtualBox]]) to find offsets like kernel32!WinExec (0x68820). Apply [[commands/adjust-rop-gadget-server2022]] for Windows Server 2022.

**Expected Output**: Updated ROP chain with correct offsets.

**Success Indicators**:
- Offsets verified in Windbg
- Exploit works on target build

## Attack Chain Summary

### Key Achievements

1. Bypassed Trix sanitizer with MathML mutation for stored XSS
2. Chained XSS to V8 exploit for memory corruption
3. Achieved RCE launching calc.exe via ROP on Windows

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01*
