---
tags:
  - windows
  - registry
  - path-traversal
  - crlf-injection
  - symlink
  - lpe
  - dos
type: attack_chain
tools:
  - '[[tools/regedit]]'
  - '[[tools/create-symlink]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
  - '[[Defense Evasion]]'
commands:
  - '[[commands/create-symlink-redirection]]'
platforms:
  - Windows
complexity: medium
procedures:
  - '[[procedures/setup-test-environment-for-steam-registry-path-traversal]]'
  - '[[procedures/verify-path-traversal-vulnerability-in-steam-service]]'
  - '[[procedures/inject-crlf-sequences-into-installpath-registry-value]]'
  - >-
    [[procedures/create-symlinks-to-redirect-steam-log-writes-to-arbitrary-files]]
step_count: 4
techniques:
  - '[[Modify Registry]]'
  - '[[Windows Service]]'
  - '[[Endpoint Denial of Service]]'
description: >-
  Multi-stage attack exploiting improper validation of the Steam Client's
  InstallPath registry value to achieve path traversal, CRLF injection, and
  symlink-based redirection for arbitrary file writes as NT AUTHORITY\SYSTEM,
  enabling DoS, network redirection, and privilege escalation.
skill_level: intermediate
impact_level: high
id: 7f0062ca-eda1-4ec3-a93d-28fe2baf4789
created_at: '2025-12-14T17:26:49.004Z'
updated_at: '2025-12-14T17:26:49.004Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Modify Registry]]'
  - '[[Windows Service]]'
  - '[[Endpoint Denial of Service]]'
---
# Arbitrary File Write as SYSTEM via Steam Client InstallPath Path Traversal and Symlink Redirection

Multi-stage attack chain demonstrating exploitation of the Steam Windows Client's registry handling to achieve arbitrary file creation or appending as NT AUTHORITY\SYSTEM through path traversal, CRLF injection, and NTFS symlink redirection. This leads to denial-of-service via system file corruption, network redirection by modifying the hosts file, horizontal privilege escalation via user startup scripts, and potential vertical escalation via appending to privileged scripts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Verify Path Traversal]
    B --> C[Inject CRLF for Content Control]
    C --> D[Redirect Logs via Symlinks]
    D --> E[Arbitrary File Write as SYSTEM]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/regedit]]
- [[tools/create-symlink]]

### Target Environment

- Windows OS (tested on Windows 10/11)
- Steam Client installed (version 5.31.28.21 or similar)
- Steam Client Service (runs as NT AUTHORITY\SYSTEM)
- Local user account with write access to user directories
- No admin rights required for symlink creation (uses object-directory symlinks)

### Initial Access Requirements

- Local user access to the target Windows machine
- Ability to stop/start Steam Client Service
- No network access needed; fully local exploitation

## Detailed Attack Procedures

### Step 1: Setup Test Environment
procedure: [[procedures/setup-test-environment-for-steam-registry-path-traversal]]

**Objective**: Prepare a controlled directory and modify the InstallPath registry to include traversal sequences for testing Steam service behavior.

**Instructions**: Close the Steam application and stop the Steam Client Service if running. Create a test folder at `C:\test` and copy `Steam.exe` and `steamservice.dll` from the original installation (`C:\Program Files (x86)\Steam`) to `C:\test`. Create an empty `logs` subfolder in `C:\test`. Use [[tools/regedit]] to set the `InstallPath` value at `HKLM\Software\wow6432node\valve\steam` to `C:\test\1..` (binary edit if needed for precision).

```reg
# Using regedit: Navigate to HKLM\Software\wow6432node\valve\steam, right-click InstallPath > Modify > Enter 'C:\test\1..' in Value data
```

**Expected Output**: Registry value updated successfully; test folder ready with copied binaries and empty logs directory.

**Success Indicators**:
- Steam files copied without errors
- Registry modification succeeds (Users group has full control on this key)
- Service can be stopped/started manually

### Step 2: Verify Path Traversal
procedure: [[procedures/verify-path-traversal-vulnerability-in-steam-service]]

**Objective**: Confirm path traversal by observing how the Steam service logs the unnormalized path in error messages.

**Instructions**: Start the Steam Client Service. After it fails (due to invalid path), check `C:\test\logs` for `service_log.txt` containing an error like "ERROR: SteamService: Invalid file signature C:\test\1..\bin\SteamService.dll". Note Windows normalization to `C:\test` but log retains original. Delete the log file afterward.

```powershell
# Manual service start: sc start Steam Client Service
# Check logs: dir C:\test\logs
# View log: type C:\test\logs\service_log.txt
```

**Expected Output**: Log file created with unnormalized path in error message.

**Success Indicators**:
- Service starts and generates log with traversal path
- Path normalized for execution but preserved in log
- No crashes or unexpected behavior

### Step 3: Inject CRLF for Content Control
procedure: [[procedures/inject-crlf-sequences-into-installpath-registry-value]]

**Objective**: Exploit binary registry editing to inject CRLF sequences, allowing control over log content appended by the service.

**Instructions**: Using [[tools/regedit]], edit the binary data of `InstallPath` to insert CRLF (0D 0A hex) characters, e.g., append custom text like "\r\nCustom injected line\r\n". Start the Steam Client Service; it uses the normalized path but logs include the injected content. Delete `service_log.txt` after verification.

```reg
# In regedit: Right-click InstallPath > Modify Binary Data > Insert bytes for CRLF (0D 0A) and ASCII for custom text
```

**Expected Output**: Log file contains service errors plus injected custom lines (semi-controlled, excluding first/last lines).

**Success Indicators**:
- Custom text appears in log
- Service processes path without crashing
- CRLF injection confirmed via log inspection

### Step 4: Redirect Writes via Symlinks
procedure: [[procedures/create-symlinks-to-redirect-steam-log-writes-to-arbitrary-files]]

**Objective**: Use NTFS reparse points and object-directory symlinks to redirect log writes to arbitrary targets, achieving file creation/appending as SYSTEM.

**Instructions**: Ensure `C:\test\logs` is empty and writable. Use [[commands/create-symlink-redirection]] to create a reparse point for `C:\test\logs` to `\RPC Control\` and symlink `\RPC Control\service_log.txt` to the target (e.g., `C:\Windows\System32\drivers\etc\hosts` for network redirection). Start the Steam Client Service to trigger the write.

```cmd
CreateSymlink.exe C:\test\logs\service_log.txt C:\target\file.txt
```

**Expected Output**: Symlink created; target file appended with log content including CRLF-injected lines upon service start.

**Success Indicators**:
- Symlink creation succeeds without admin
- Target file modified with SYSTEM privileges
- No access denied errors

## Attack Chain Summary

### Key Achievements

1. Confirmed path traversal and CRLF injection in Steam registry handling
2. Redirected SYSTEM-privileged writes to arbitrary files using symlinks
3. Enabled DoS (e.g., corrupt SAM file), network redirection (hosts append), and EoP (startup script append)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Modify Registry]] Modify Registry
- [[Windows Service]] Create or Modify System Process (Configuration File)
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

---
*Last updated: 2023-10-01*
