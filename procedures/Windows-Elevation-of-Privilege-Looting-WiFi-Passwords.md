---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Wifi passwords]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/netsh-wlan-show-profiles]]'
  - '[[commands/netsh-wlan-show-profile-key]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-Elevation-of-Privilege-Looting-WiFi-Passwords

## Summary

This procedure demonstrates how to escalate privileges on a Windows system to access and extract Wi-Fi passwords stored in profile files. By obtaining administrative access, attackers can retrieve clear-text credentials for saved wireless networks, enabling lateral movement or persistence within the target network.

## Description

Wi-Fi passwords on Windows are stored in encrypted form within wireless profile XML files, accessible only with elevated privileges. This technique involves first enumerating available Wi-Fi profiles using the netsh utility, then dumping the clear-text keys for specific or all profiles. It assumes initial low-privilege access and relies on a privilege escalation vector (e.g., exploiting a vulnerability like T1068) to reach administrator level. Once elevated, the netsh commands reveal credentials that can be used to connect to the same networks from other devices. This is particularly useful in post-exploitation scenarios for expanding network access without additional authentication.

## Requirements

1. Initial access to a Windows machine (user-level shell or command prompt).
2. Elevated privileges (administrator) obtained via exploitation or misconfiguration.
3. Command Prompt (cmd.exe) available on the target system.
4. No additional tools required; uses built-in Windows utilities.

## Defense

- Regularly apply Windows security patches to mitigate privilege escalation vulnerabilities.
- Implement least-privilege principles and monitor for unauthorized elevation attempts using tools like Windows Event Logging (Event ID 4672 for privilege use).
- Use Group Policy to restrict access to wireless profiles and enable Wi-Fi password protection.
- Monitor for netsh executions via Sysmon or EDR solutions, focusing on 'wlan show profile' commands.

## Objectives

1. Escalate to administrative privileges if not already elevated.
2. Enumerate all saved Wi-Fi profiles on the system.
3. Extract clear-text passwords for targeted or all profiles.
4. Collect credentials for potential lateral movement.

## Instructions

### Step 1: Enumerate Wi-Fi Profiles

**Context**: This step lists all saved Wi-Fi network profiles (SSIDs) on the system, providing an overview of accessible networks. It requires elevated privileges to execute fully but can run at user level to identify profiles.

**Command** ([[commands/netsh-wlan-show-profiles]]):
```cmd
netsh wlan show profiles
```

> This command queries the wireless configuration store and outputs a list of profiles. Look for the 'All User Profile' or 'User Profile' sections to identify SSIDs. If run without elevation, it may only show user-specific profiles; elevation reveals all.

### Step 2: Extract Key for Specific Profile

**Context**: After identifying a target SSID from Step 1, this retrieves the clear-text password for that specific Wi-Fi network. Administrative privileges are mandatory to access the key material.

**Command** ([[commands/netsh-wlan-show-profile-key]]):
```cmd
netsh wlan show profile name="<SSID>" key=clear
```

> Replace `<SSID>` with the exact profile name (e.g., "CorporateWiFi"). The output includes the 'Key Content' field under the security settings, displaying the plaintext password if stored. Verify success by checking for the 'Key Content' line without errors.

### Step 3: Dump All Wi-Fi Keys Using One-Liner Script

**Context**: For efficiency, use this batch script to automate extraction of SSIDs and keys for all profiles in one execution. It clears the screen, loops through profiles, and filters output to show only relevant details like SSID and password. Requires administrative privileges.

**Code** ([[codes/Batch-Script-Dump-All-WiFi-Keys]]):
```batch
cls & echo. & for /f "tokens=4 delims=: " %a in ('netsh wlan show profiles ^| find "Profile "') do @echo off > nul & (netsh wlan show profiles name=%a key=clear | findstr "SSID Cipher Content" | find /v "Number" & echo.) & @echo on
```

> Execute this in an elevated Command Prompt. It parses profiles with netsh, requests keys, and uses findstr to isolate SSID names, encryption type (e.g., WPA2), and 'Key Content' (password). Output appears as paired lines for each profile. If no keys are found, profiles may use certificate-based auth instead.
