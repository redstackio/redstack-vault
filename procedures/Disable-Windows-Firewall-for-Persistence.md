---
id: 1c5af038-0269-4c41-80be-113a420a6092
name: Disable-Windows-Firewall-for-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.703274+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - '[[tags/Disable Antivirus and Security]]'
  - '[[tags/Disable Windows Firewall]]'
  - '[[tags/Windows - Persistence]]'
  - evasion
  - persistence
commands:
  - '[[commands/netsh-advfirewall-show-allprofiles]]'
  - '[[commands/netsh-advfirewall-set-allprofiles-state-off]]'
  - '[[commands/new-netfirewallrule-create-whitelist]]'
platforms:
  - Windows
tools: []
validated: true
---

# Disable-Windows-Firewall-for-Persistence

## Summary

This procedure disables the Windows Firewall across all profiles to evade network-based detection and allow unrestricted inbound and outbound traffic from an attacker-controlled IP. It includes viewing current settings, turning off the firewall, and creating a whitelist rule for persistence, enabling ongoing access without triggering alerts.

## Description

Disabling the Windows Firewall is a common defense evasion technique used post-compromise to maintain persistence and facilitate lateral movement. By setting all firewall profiles (Domain, Private, Public) to an off state via netsh and creating custom inbound rules with PowerShell, attackers can bypass restrictions that might block command-and-control communications or tool transfers. This is particularly effective in Windows environments where firewall is enabled by default. Note: While the procedure name references antivirus, the provided steps focus on firewall; antivirus disabling typically requires separate registry modifications (e.g., via sc stop or reg add for Windows Defender), which are not detailed here.

## Requirements

1. Administrator-level privileges on the target Windows machine (required for netsh and New-NetFirewallRule).
2. PowerShell execution policy allowing scripts (bypass if needed with Set-ExecutionPolicy).
3. Knowledge of the attacker's IP address for whitelisting.
4. Local or remote access to run commands (e.g., via PSRemoting or initial shell).

## Defense

- Enable Windows Firewall with strict inbound rules and monitor for unauthorized changes using Event ID 4946 (rule added) or 4948 (rule modified) in Windows Security logs.
- Implement application whitelisting (e.g., AppLocker) to prevent unauthorized PowerShell or netsh execution.
- Use endpoint detection tools to alert on firewall state changes or unusual registry modifications in HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess.
- Regularly audit firewall profiles with Group Policy and enforce via centralized management like Intune.

## Objectives

1. View and confirm current Windows Firewall state across all profiles.
2. Disable the firewall to remove network traffic restrictions.
3. Create a persistent whitelist rule for attacker IP to allow future connections without re-disabling.
4. Verify the changes to ensure evasion from network security controls.

## Instructions

### Step 1: View Current Firewall Profiles

**Context**: Before disabling, enumerate the current state of all firewall profiles (Domain, Private, Public) to understand the baseline and confirm the changes post-execution. This helps in troubleshooting if the disable fails due to policy restrictions.

**Command** ([[commands/netsh-advfirewall-show-allprofiles]]):
```powershell
netsh advfirewall show allprofiles
```

> This command queries the Windows Firewall configuration and displays the state (ON/OFF) for each profile, along with settings like logging and remote management. Run it in an elevated PowerShell or Command Prompt. If profiles are already off, proceed; otherwise, expect to see 'State OFF' after the next step.

### Step 2: Disable All Firewall Profiles

**Context**: Turn off the firewall for all profiles to immediately allow all inbound and outbound traffic, evading any port or IP-based blocks that could hinder C2 or lateral movement.

**Command** ([[commands/netsh-advfirewall-set-allprofiles-state-off]]):
```powershell
netsh advfirewall set allprofiles state off
```

> Executed in an elevated shell, this applies the off state globally. It requires admin rights and may prompt UAC. Success is silent unless errors occur (e.g., access denied). Re-run the show command from Step 1 to verify all profiles now show 'State OFF'.

### Step 3: Create Whitelist Rule for Attacker IP

**Context**: For persistence, add a custom inbound rule allowing all traffic from the attacker's IP, ensuring future sessions aren't blocked even if firewall is re-enabled by AV or admin.

**Command** ([[commands/new-netfirewallrule-create-whitelist]]):
```powershell
New-NetFirewallRule -Name "morph3inbound" -DisplayName "morph3inbound" -Enabled True -Direction Inbound -Protocol ANY -Action Allow -Profile ANY -RemoteAddress $_ATTACKER_IP
```

> This PowerShell cmdlet creates a new rule named 'morph3inbound' that permits all protocols from the specified IP across all profiles. Replace $_ATTACKER_IP with the actual IP (e.g., 192.168.1.100). Verify with Get-NetFirewallRule -Name "morph3inbound" to see the rule listed as Enabled.

### Step 4: Verify Overall Changes

**Context**: Confirm the firewall is disabled and the rule is active to ensure the procedure succeeded and persistence is established.

**Command** ([[commands/netsh-advfirewall-show-allprofiles]]):
```powershell
netsh advfirewall show allprofiles
```

> Re-execute the view command. Expected: All profiles show 'State OFF', and querying rules (netsh advfirewall firewall show rule name="morph3inbound") confirms the whitelist exists. If not, check for GPO overrides or rerun steps with elevated privileges.

## Expected Output

- Step 1/4: Output like "Domain Profile Settings: State OFF/ON", listing profiles.
- Step 2: No output on success; error if insufficient privileges.
- Step 3: No output; use Get-NetFirewallRule for confirmation showing the rule details.
- Overall: Firewall logs (if enabled) show rule additions; network tests (e.g., telnet to blocked ports) succeed post-disable.
