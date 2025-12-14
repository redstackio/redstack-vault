---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - uac-bypass
  - privilege-escalation
  - registry-tampering
  - veracrypt
type: attack_chain
tools:
  - '[[tools/add-bat]]'
  - '[[tools/malstaller-bat]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Payload-for-Elevation]]'
  - '[[procedures/Tamper-HKCU-Registry-Keys-for-Protocol-Hijacking]]'
  - '[[procedures/Trigger-UAC-Bypass-via-VeraCryptExpander-Homepage]]'
  - '[[procedures/Set-Booby-Trapped-Browser-as-Default-on-Windows-10]]'
step_count: 4
techniques:
  - '[[Bypass User Account Control]]'
updated_at: '2025-12-14T17:29:44.583Z'
description: >-
  A privilege escalation attack exploiting VeraCryptExpander.exe by tampering
  with HKCU browser protocol handlers to hijack ShellExecute calls from an
  elevated process, allowing arbitrary code execution with admin privileges.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
---
# UAC Bypass via HKCU Registry Tampering in VeraCryptExpander

Multi-stage attack chain demonstrating a UAC bypass in VeraCrypt by exploiting insecure ShellExecute usage in an elevated process, allowing a limited admin to execute arbitrary code with full privileges.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Payload] --> B[Tamper Registry]
    B --> C[Set Default Browser]
    C --> D[Trigger Elevation]
    D --> E[Execute Privileged Actions]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/add-bat]]
- [[tools/malstaller-bat]]

### Target Environment

- Windows 10 or later with VeraCrypt installed
- Limited admin user account (no full admin rights needed for tampering)
- VeraCryptExpander.exe accessible

### Initial Access Requirements

- Local access as limited user
- Ability to write to user desktop and HKCU registry
- No network access required

## Detailed Attack Procedures

### Step 1: Create Malicious Payload
procedure: [[procedures/Create-Malicious-Payload-for-Elevation]]

**Objective**: Prepare a batch script that will execute with elevated privileges to perform malicious actions like binary replacement.

**Instructions**: Create `malstaller.bat` on the desktop. Customize paths for the current user (e.g., replace 'Temp' with actual username). The script copies a fake executable (e.g., putty.exe renamed as VeraCrypt2.exe) to the VeraCrypt installation folder and executes it.

**Expected Output**: Batch file created, ready for hijacking.

**Success Indicators**:
- File exists on desktop
- Script syntax validated (no errors when run manually)

### Step 2: Tamper Registry Keys
procedure: [[procedures/Tamper-HKCU-Registry-Keys-for-Protocol-Hijacking]]

**Objective**: Modify HKCU protocol handlers for browsers to point to the malicious script, enabling hijacking without elevation.

**Instructions**: Customize and run `add.bat` to set registry defaults for protocols like HTTP, HTTPS, ChromeHTML, etc., to `malstaller.bat` with the URL parameter.

Use [[commands/set-registry-protocol-hijack]] for the key modification:

```bash
reg add "HKCU\Software\Classes\http\shell\open\command" /ve /d "C:\Users\Temp\Desktop\malstaller.bat \"%1\"" /f
```

Repeat for other protocols (FirefoxURL, IE.HTTP, etc.).

**Expected Output**: Registry keys updated; no errors from reg add.

**Success Indicators**:
- HKCU keys point to malstaller.bat (verify with reg query)
- No UAC prompt during modification

### Step 3: Set Booby-Trapped Browser as Default
procedure: [[procedures/Set-Booby-Trapped-Browser-as-Default-on-Windows-10]]

**Objective**: Ensure the tampered protocol (e.g., IE) is used by setting it as the default browser on Windows 10.

**Instructions**: After tampering, go to Windows Settings > Apps > Default apps, and set Internet Explorer (or the targeted browser) as default for HTTP/HTTPS.

**Expected Output**: Default browser changed; verify in settings.

**Success Indicators**:
- Targeted browser set as default
- Protocol handlers resolve to tampered keys

### Step 4: Trigger UAC Bypass
procedure: [[procedures/Trigger-UAC-Bypass-via-VeraCryptExpander-Homepage]]

**Objective**: Execute the elevated VeraCryptExpander and trigger ShellExecute to run the hijacked script with admin rights.

**Instructions**: Run VeraCryptExpander.exe (UAC prompts for elevation), then click the 'Homepage' button. This invokes ShellExecute on a URL, hijacking via HKCU to run malstaller.bat elevated.

**Expected Output**: Malstaller.bat executes without additional UAC; fake binary placed and run.

**Success Indicators**:
- Elevated script runs (e.g., file copied to C:\Program Files\VeraCrypt)
- No further prompts; privileges confirmed via whoami /priv

## Attack Chain Summary

### Key Achievements

1. Bypassed UAC using user-modifiable HKCU keys
2. Achieved full admin execution from limited user context
3. Compromised VeraCrypt installation with malware
4. Demonstrated tamper with privileged processes

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Bypass User Account Control]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T12:00:00Z*
