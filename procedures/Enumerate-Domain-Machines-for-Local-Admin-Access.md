---
id: db73e1c2-90a3-47f3-9a95-01338cca67aa
name: Enumerate-Domain-Machines-for-Local-Admin-Access
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T06:56:21.041867+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Permission Groups Discovery]]'
sub_techniques: []
tags:
  - pivot
  - privileges
  - discovery
commands:
  - '[[commands/Find-LocalAdminAccess-PowerView]]'
  - '[[commands/Find-WMILocalAdminAccess-PowerView]]'
  - '[[commands/Invoke-PSRemotingLocalAdminAccess-Nishang]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerSploit]]'
  - '[[tools/Nishang]]'
validated: true
---

# Enumerate-Domain-Machines-for-Local-Admin-Access

## Summary

This procedure identifies domain-joined Windows machines where the current user has local administrator privileges by leveraging PowerShell reconnaissance modules. It is useful for discovering lateral movement opportunities during penetration testing or red team engagements, allowing attackers to pinpoint hosts for further exploitation without brute-forcing credentials.

## Description

In a Windows Active Directory environment, domain users may have local admin rights on specific workstations or servers due to misconfigurations, such as adding user groups to local Administrators. This procedure systematically enumerates all domain computers and tests administrative access using different protocols (RPC, WMI, WinRM) to bypass potential network restrictions. It assumes the attacker has valid domain credentials and network access to the target domain. Success enables privilege escalation or pivoting to those machines. The approach starts with RPC-based checks (fastest but often firewalled), falls back to WMI if blocked, and uses WinRM as a last resort for restricted environments. This maps to MITRE ATT&CK technique T1069 (Permission Groups Discovery) under the Discovery tactic.

## Requirements

1. Valid domain user credentials with network logon rights.
2. PowerShell execution policy set to allow script execution (e.g., Unrestricted or Bypass).
3. Network access to target domain (SMB:445, RPC:135, WMI: various dynamic ports, WinRM:5985/5986).
4. Tools: PowerSploit (including PowerView module) and Nishang scripts downloaded and available.
5. Target environment: Windows domain with Active Directory.

## Defense

- Monitor PowerShell logs for script block execution involving reconnaissance modules (e.g., Event ID 4104 in PowerShell Operational logs).
- Implement Windows Defender Application Control (WDAC) or AppLocker to restrict unsigned script execution.
- Firewall RPC, WMI, and WinRM ports between segments; use just-in-time access for admin shares.
- Enable constrained delegation and audit local group membership changes.
- Deploy endpoint detection tools to alert on anomalous remote access attempts to admin shares (e.g., \hostname\C$).

## Objectives

1. Discover domain machines granting local admin access to the current user.
2. Validate access via multiple protocols to handle firewall restrictions.
3. Collect hostnames and access methods for subsequent lateral movement.
4. Expected outcome: A list of accessible machines for targeting in attack chains.

## Instructions

### Step 1: Enumerate Using RPC with PowerView

**Context**: This step uses the Find-LocalAdminAccess function from PowerView (part of PowerSploit) to query domain computers via RPC and check membership in the local Administrators group. It requires SMB and RPC ports to be open. Run this first as it is efficient for large domains. Import the PowerView module before execution.

**Command** ([[commands/Find-LocalAdminAccess-PowerView]]):
```powershell
Import-Module PowerView.ps1
Find-LocalAdminAccess -Verbose
```

> This command defaults to the current domain and tests all discoverable computers. The -Verbose flag provides detailed progress. If successful, it will output computers where admin access is confirmed by attempting a remote connection to the ADMIN$ share.

### Step 2: Fallback to WMI if RPC is Blocked

**Context**: If RPC ports are firewalled, switch to WMI for enumeration. The Find-WMILocalAdminAccess script (from PowerView or compatible) uses WMI queries to check local group membership remotely. This requires WMI service enabled on targets and appropriate firewall rules. Import PowerView if not already loaded.

**Command** ([[commands/Find-WMILocalAdminAccess-PowerView]]):
```powershell
Import-Module PowerView.ps1
. \Find-WMILocalAdminAccess.ps1
Find-WMILocalAdminAccess -Verbose
```

> The script queries WMI for Administrators group members across domain hosts. Use -Domain YourDomain.com if targeting a specific domain. Success is indicated by a list of hosts with matching group membership, without needing direct share access.

### Step 3: Use WinRM with Nishang if WMI Fails

**Context**: For environments blocking both RPC and WMI, use WinRM via the PSRemotingLocalAdminAccess script from Nishang. This tests PowerShell remoting access, which implies local admin if remoting is restricted to admins. Download and execute the script in the current session; it requires WinRM enabled on targets.

**Command** ([[commands/Invoke-PSRemotingLocalAdminAccess-Nishang]]):
```powershell
. \PSRemotingLocalAdminAccess.ps1
Invoke-PSRemotingLocalAdminAccess -Verbose
```

> This script attempts PSRemoting sessions to domain computers using the current credentials. If a session establishes, it confirms admin access. The -Verbose option logs connection attempts and results. Decision point: If fewer than 10% of machines respond, investigate WinRM configuration or use alternative credentials.
