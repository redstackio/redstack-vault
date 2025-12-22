---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Registry Run Keys / Startup Folder|T1060 - Registry Run Keys /
    Startup Folder]]
tags:
  - registry-hkcu
  - simple-user
  - windows-persistence
commands:
  - '[[commands/sharpersist-add-hkcu-run-persistence-cmd-calc]]'
  - '[[commands/sharpersist-add-hkcu-run-persistence-cmd-calc-with-env]]'
  - '[[commands/sharpersist-add-logonscript-persistence-cmd-calc]]'
  - '[[commands/reg-add-multiple-hkcu-run-keys-for-backdoor]]'
platforms:
  - Windows
tools:
  - '[[tools/sharpersist]]'
validated: true
---

# windows-simple-user-registry-persistence

## Summary

This procedure outlines how to achieve user-level persistence on Windows systems by modifying the HKEY_CURRENT_USER (HKCU) registry to automatically execute a payload or backdoor upon user logon. It covers manual editing, command-line registry modifications, and tool-assisted methods using SharpPersist, ensuring the attacker's code survives reboots without requiring administrative privileges.

## Description

Registry-based persistence via HKCU Run keys is a common technique for maintaining access in post-exploitation scenarios. By adding string values to keys like HKCU\Software\Microsoft\Windows\CurrentVersion\Run, attackers can specify executable paths that Windows launches at logon. This method is stealthy for non-admin users since HKCU is modifiable by the logged-in user. The procedure demonstrates creating such entries pointing to a hypothetical backdoor.exe or using benign payloads like calc.exe for testing. It assumes the payload is already on the system (e.g., dropped via initial access). Success is verified by checking the registry and observing execution after logoff/logon or reboot. This aligns with scenarios where attackers need long-term access for data exfiltration or lateral movement.

## Requirements

1. Local logon access to the target Windows system as a standard (non-admin) user.
2. Write permissions to the HKCU registry hive (default for the current user).
3. A payload executable placed on the system, such as in %APPDATA% or %TEMP% (e.g., backdoor.exe).
4. Optional: SharpPersist tool executable available on the system for automated methods.
5. Command prompt or PowerShell access for reg.exe and SharpPersist execution.

## Defense

- Enable registry auditing via Group Policy (Computer Configuration > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Object Access > Audit Registry) to log changes to Run keys.
- Deploy endpoint detection tools (e.g., Microsoft Defender, CrowdStrike) to alert on modifications to startup registry locations and anomalous process spawns from them.
- Use application control policies (e.g., AppLocker or WDAC) to block execution of unsigned or unknown binaries in user-writable directories like %TEMP%.
- Periodically scan and clean startup items using tools like Autoruns or msconfig, and implement user education on reviewing installed programs.

## Objectives

1. Create automatic execution triggers in the user registry to run payloads on logon.
2. Ensure persistence survives system reboots and user logoffs without admin rights.
3. Provide redundant methods (manual, reg.exe, SharpPersist) for reliable implementation.
4. Verify persistence to confirm backdoor activation for ongoing access.

## Instructions

### Step 1: Manually Add Registry Value for Persistence

**Context**: Use the built-in Registry Editor to create a single string value in the HKCU Run key. This method is straightforward for one-off additions but less automatable; it's ideal when command-line access is limited.

1. Press Windows + R, type `regedit`, and press Enter to open the Registry Editor.
2. Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`.
3. Right-click in the right pane, select New > String Value, and name it `Backdoor`.
4. Double-click the new value, set its data to `C:\Users\%USERNAME%\AppData\Local\Temp\backdoor.exe` (adjust path to your payload), and click OK.
5. Close Registry Editor and log off/on to test (or use `gpupdate /force` for immediate trigger if applicable).

**Expected Output**: The value appears in the Run key with the specified data. Upon logon, the payload executes silently.

> Why this step: Manual editing avoids detection by command-line monitoring tools. Success criteria: Value exists in registry; payload runs post-logon (monitor via Process Explorer).

### Step 2: Add Redundant Persistence Entries Using reg.exe

**Context**: Leverage the native reg.exe utility to add the payload path to multiple HKCU startup keys (Run, RunOnce, RunServices, RunServicesOnce). This provides redundancy if one key is monitored or cleared, ensuring higher persistence success.

**Command** ([[commands/reg-add-multiple-hkcu-run-keys-for-backdoor]]):

```cmd
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices" /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"
```

> This multi-command sequence targets four keys for comprehensive coverage. Each `reg add` operates independently; run them sequentially in an elevated Command Prompt if needed (though HKCU doesn't require elevation). Expected output per line: `The operation completed successfully.`

**Expected Output**: Confirmation messages for each addition. Verify by running `reg query HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v Evil` (repeat for other keys) to see the value and data.

> Why this step: Redundancy maximizes survival against partial cleanup. Decision point: If one key fails (e.g., access denied), skip and proceed—HKCU should allow all. Success criteria: Values present in targeted keys; payload executes on logon.

### Step 3: Add Persistence Using SharpPersist Tool

**Context**: Employ the SharpPersist tool for automated, flexible registry persistence. This step uses a test payload (cmd.exe launching calc.exe) but can be adapted for backdoors. It demonstrates basic Run key addition, with environment variable output, and logon script variant for diversity.

**Command** ([[commands/sharpersist-add-hkcu-run-persistence-cmd-calc]]):

```cmd
SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add
```

> Adds a basic HKCU Run entry to spawn calc.exe on logon.

**Command** ([[commands/sharpersist-add-hkcu-run-persistence-cmd-calc-with-env]]):

```cmd
SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add -o env
```

> Adds the entry and outputs environment variables associated with the persistence for debugging.

**Command** ([[commands/sharpersist-add-logonscript-persistence-cmd-calc]]):

```cmd
SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "logonscript" -m add
```

> Targets the logon script registry location for execution during user logon.

**Expected Output**: Tool-specific confirmation, e.g., `Persistence mechanism 'Test Stuff' added successfully to hkcurun.` Check registry as in Step 2. Post-logon, calc.exe launches.

> Why this step: SharpPersist handles complexity and supports enumeration/removal. Decision point: If SharpPersist unavailable, fall back to reg.exe; for real attacks, replace calc.exe with backdoor path. Success criteria: New registry values; observable payload execution (e.g., calculator opens).
