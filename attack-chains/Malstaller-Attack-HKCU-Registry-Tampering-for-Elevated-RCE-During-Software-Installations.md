---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - windows
  - registry
  - privilege-escalation
  - rce
  - uac-bypass
type: attack_chain
tools:
  - '[[tools/Registry-Editor]]'
  - '[[tools/Malstaller-Batch-Script]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Tamper-with-HKCU-Protocol-Handler-Registry-Keys]]'
  - '[[procedures/Create-Malicious-Batch-Script-for-URL-Logging]]'
  - '[[procedures/Trigger-Elevated-Execution-via-Software-Installation]]'
step_count: 3
techniques:
  - '[[Modify Registry]]'
  - '[[Bypass User Account Control]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:23.769Z'
description: >-
  A privilege escalation attack exploiting trust in user-modifiable HKCU
  registry keys to hijack protocol handlers, leading to remote code execution
  with administrator privileges during software installations or
  uninstallations.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Modify Registry]]'
  - '[[Bypass User Account Control]]'
  - '[[Windows Command Shell]]'
---
---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Malstaller Attack: HKCU Registry Tampering for Elevated RCE During Software Installations
type: attack_chain
description: "A privilege escalation attack exploiting trust in user-modifiable HKCU registry keys to hijack protocol handlers, leading to remote code execution with administrator privileges during software installations or uninstallations."
verified: false
submitted: false
step_count: 3
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: ["[[procedures/Tamper-with-HKCU-Protocol-Handler-Registry-Keys]]", "[[procedures/Create-Malicious-Batch-Script-for-URL-Logging]]", "[[procedures/Trigger-Elevated-Execution-via-Software-Installation]]"]
techniques: ["[[Modify Registry]]", "[[Bypass User Account Control]]", "[[Windows Command Shell]]"]
tactics: ["[[Privilege Escalation]]", "[[Execution]]"]
tags: ["windows", "registry", "privilege-escalation", "rce", "uac-bypass"]
platforms: ["Windows"]
tools: ["[[tools/Registry-Editor]]", "[[tools/Malstaller-Batch-Script]]"]
---

# Malstaller Attack: HKCU Registry Tampering for Elevated RCE During Software Installations

Multi-stage attack chain demonstrating a complete attack workflow exploiting Windows installer trust in HKCU registry keys to achieve privilege escalation and RCE.

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
    A[Tamper HKCU Registry Keys] --> B[Create Malicious Script]
    B --> C[Trigger via Elevated Installation]
    C --> D[RCE and Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Registry-Editor]]
- [[tools/Malstaller-Batch-Script]]

### Target Environment

- Windows OS (tested on Windows 10/11)
- Required services/ports: None (local privilege escalation)
- Network access requirements: None

### Initial Access Requirements

- Low-privileged user account on the target system
- Administrator account for triggering elevated processes
- No prior network access needed; local execution

## Detailed Attack Procedures

### Step 1: Tamper with HKCU Registry Keys
procedure: [[procedures/Tamper-with-HKCU-Protocol-Handler-Registry-Keys]]

**Objective**: Modify user-writable HKCU registry keys to redirect HTTP/HTTPS and Firefox protocol handlers to a malicious batch file, setting up the hijack for elevated execution.

**Instructions**: Use [[tools/Registry-Editor]] or [[commands/reg-add-http-redirect]] to alter the specified keys. For example, set the command for HTTPS:

```cmd
reg add "HKEY_CURRENT_USER\Software\Classes\https\shell\open\command" /ve /d "C:\Users\%USERNAME%\Desktop\malstaller.bat %1" /f
```

Repeat for HTTP, FirefoxHTML, and FirefoxURL keys as detailed in the procedure.

**Expected Output**: Registry keys updated to point to malstaller.bat without errors.

**Success Indicators**:
- Registry keys modified successfully (verify with reg query)
- No immediate alerts from antivirus

### Step 2: Create Malicious Batch Script
procedure: [[procedures/Create-Malicious-Batch-Script-for-URL-Logging]]

**Objective**: Deploy a batch script that captures and logs triggered URLs to a protected directory while masking the attack by launching the legitimate browser.

**Instructions**: Create the malstaller.bat file on the desktop using a text editor, incorporating [[commands/capture-url-argument]], [[commands/log-url-to-file]], and [[commands/launch-firefox-masked]]:

```cmd
echo set arg1=%%1 > C:\Users\%USERNAME%\Desktop\malstaller.bat
echo echo %%date%% : %%1 >> C:\mal_log.txt >> C:\Users\%USERNAME%\Desktop\malstaller.bat
echo "C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -osint -url "%%1" >> C:\Users\%USERNAME%\Desktop\malstaller.bat
```

**Expected Output**: Batch file created and ready for execution.

**Success Indicators**:
- File exists on desktop
- Script syntax is valid (test in non-elevated context)

### Step 3: Trigger Elevated Execution
procedure: [[procedures/Trigger-Elevated-Execution-via-Software-Installation]]

**Objective**: Provoke an administrator to perform an elevated action (e.g., install software) that clicks a URL, triggering the hijacked handler with UAC elevation for RCE.

**Instructions**: As a low-priv user, wait for or social-engineer an admin to run an installer (e.g., via native tools like perfmon.exe). When a link like privacy policy is clicked, the tampered handler executes malstaller.bat elevated. Monitor C:\mal_log.txt for logged URLs.

**Expected Output**: Malstaller.bat runs as admin, logs URL to C:\mal_log.txt, and opens Firefox.

**Success Indicators**:
- Log file created in root C:\ with sensitive URL data
- No UAC prompt blocks (due to trusted installer context)
- Elevated write confirmed

## Attack Chain Summary

### Key Achievements

1. Achieved privilege escalation from low-priv to admin without direct UAC prompt
2. Demonstrated RCE via arbitrary batch execution during trusted processes
3. Enabled URL sniffing and system tampering (e.g., AV bypass, file corruption)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Modify Registry]] Modify Registry
- [[Bypass User Account Control]] Bypass User Account Control
- [[Windows Command Shell]] Windows Command Shell

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
