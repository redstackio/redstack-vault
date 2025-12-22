---
id: a6dd58ae-6284-46bb-8bbb-62232447a92c
name: Disable-Windows-Firewall
type: procedure
verified: true
submitted: true
created_at: '2019-11-15T01:22:12.424921+00:00'
updated_at: '2023-05-25T19:48:10.238386+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disabling Security Tools]]'
sub_techniques: []
tags:
  - antivirus-bypass
  - service-attacks
commands:
  - '[[commands/allow-application-through-windows-firewall-windows-7-plus]]'
  - '[[commands/allow-port-through-windows-firewall-windows-2008-and-earlier]]'
  - '[[commands/allow-port-through-windows-firewall-windows-7-plus]]'
  - '[[commands/disable-windows-firewall-windows-7-plus]]'
  - '[[commands/disable-windows-firewall-windows-2008-and-earlier]]'
platforms:
  - Windows
tools: []
validated: true
---

# Disable-Windows-Firewall

## Summary

This procedure disables the Windows Firewall or adds exceptions for specific ports and applications to allow unauthorized network access, bypassing default security restrictions on modern Windows systems.

## Description

Windows Firewall blocks inbound and outbound traffic by default unless explicitly allowed. In offensive security scenarios, attackers may disable the firewall entirely to facilitate lateral movement, command and control, or remote access, or add rules to permit specific tools or ports. This procedure covers methods for Windows 7 and later (using netsh advfirewall) and Windows Server 2008 and earlier (using legacy netsh firewall). It requires administrative privileges and is mapped to MITRE ATT&CK technique T1089 for impairing security tools. Use in controlled environments only, as it reduces system security.

## Requirements

1. Administrative privileges on the target Windows system
2. Command Prompt access (cmd.exe) with elevated rights
3. Target OS: Windows 7/Server 2008 or later
4. No additional tools required; uses built-in netsh utility

## Defense

- Enable Windows Firewall auditing to log rule changes and disable attempts
- Implement application whitelisting (e.g., AppLocker) to restrict netsh execution
- Monitor for unexpected outbound connections or process executions involving netsh
- Use endpoint detection tools to alert on firewall modifications

## Objectives

1. Disable Windows Firewall to allow unrestricted network traffic
2. Add inbound rules for specific ports to enable remote access without full disable
3. Permit specific applications to bypass firewall rules for targeted persistence
4. Verify changes to ensure successful evasion of network controls

## Instructions

### Windows 7 and Later

#### Step 1: Disable Firewall for All Profiles

**Context**: Completely turns off the firewall for domain, private, and public profiles, allowing all inbound and outbound traffic.

**Command** ([[commands/disable-windows-firewall-windows-7-plus]]):
```command_prompt
netsh advfirewall set allprofiles state off
```

> This command immediately disables the firewall. Run as administrator to avoid access denied errors.

#### Step 2: Allow a Specific Port Through the Firewall

**Context**: Adds an inbound rule to open a TCP port, useful for enabling listeners like reverse shells without disabling the entire firewall.

**Command** ([[commands/allow-port-through-windows-firewall-windows-7-plus]]):
```command_prompt
netsh advfirewall firewall add rule name="Open Port $_PORT" dir=in action=allow protocol=TCP localport=$_PORT
```

> Replace $_PORT with the desired port number (e.g., 4444). This creates a persistent rule that survives reboots.

#### Step 3: Allow a Specific Application Through the Firewall

**Context**: Permits a program to receive inbound connections, bypassing firewall blocks for custom tools or malware.

**Command** ([[commands/allow-application-through-windows-firewall-windows-7-plus]]):
```command_prompt
netsh advfirewall firewall add rule name="Allow $_PROGRAM to bypass firewall rules" dir=in action=allow program="C:\$_PATH\$_PROGRAM.exe" enable=yes
```

> Specify the full path to the executable. This rule enables the application while keeping other protections intact.

### Windows Server 2008 and Earlier

#### Step 1: Disable Firewall Using Legacy Command

**Context**: Disables the firewall on older Windows versions where advanced firewall commands are unavailable.

**Command** ([[commands/disable-windows-firewall-windows-2008-and-earlier]]):
```command_prompt
netsh firewall set opmode DISABLE
```

> This legacy command turns off the firewall profile. Verify with 'netsh firewall show opmode' afterward.

#### Step 2: Allow a Specific Port Through the Firewall

**Context**: Opens a TCP port for inbound traffic on legacy systems, similar to modern port rules.

**Command** ([[commands/allow-port-through-windows-firewall-windows-2008-and-earlier]]):
```command_prompt
netsh firewall add portopening TCP $_PORT "Open Port $_PORT"
```

> Use this to allow specific services like RDP or custom ports. The rule name helps in later identification and removal.
