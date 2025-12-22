---
type: procedure
description: >-
  Procedure to check the current enforcement mode of Windows Defender
  Application Control (WDAC) using PowerShell to assess defense posture.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - Windows Defender Application Control
  - Windows - Defenses
  - discovery
  - reconnaissance
commands:
  - '[[commands/powershell-get-computerinfo-wdac-status]]'
platforms:
  - Windows
tools: []
validated: true
---

# Check-WDAC-Enforcement-Mode

## Summary

This procedure checks the current enforcement mode of Windows Defender Application Control (WDAC), a Windows security feature that restricts unauthorized applications from running. By determining if WDAC is in Audit Mode, Enforce Mode, or Disabled, attackers can assess the effort required to bypass application controls, while defenders can verify policy effectiveness.

## Description

Windows Defender Application Control (WDAC) enforces code integrity policies to prevent malicious or unauthorized code execution. The enforcement mode dictates policy strictness: Audit Mode logs violations without blocking, Enforce Mode blocks non-compliant applications, and Disabled applies no restrictions. From an offensive standpoint, identifying the mode helps evaluate bypass opportunities, such as exploiting allowed paths or weak policies. Defensively, it ensures policies align with security requirements. This procedure uses PowerShell to query system information, focusing on DeviceGuard properties that indicate WDAC status in kernel and user modes. It requires administrative access for full visibility but can run in user context for basic checks.

## Requirements

1. Access to a Windows machine (Windows 10/11 or Server 2016+ with WDAC potentially enabled).
2. PowerShell execution privileges (run as administrator recommended for complete output).
3. No external tools required; uses built-in PowerShell cmdlet.

## Defense

Defensive measures and detection strategies:

- Configure WDAC in Enforce Mode with comprehensive policies to block unauthorized executables.
- Enable PowerShell logging (Module, Script Block, and Transcription) to monitor Get-ComputerInfo usage.
- Implement endpoint detection and response (EDR) solutions to alert on system information queries.
- Regularly audit WDAC policies via Group Policy or MDM tools and review event logs for policy violations (Event ID 3076 in Microsoft-Windows-CodeIntegrity/Operational).

## Objectives

1. Determine the current WDAC enforcement mode (Audit, Enforce, or Disabled).
2. Assess the level of protection provided by WDAC against unauthorized application execution.
3. Identify potential bypass vectors based on the mode (e.g., audit-only allows testing without blocks).

## Instructions

### Step 1: Query WDAC Enforcement Status

**Context**: Use the built-in Get-ComputerInfo cmdlet to retrieve system details, including WDAC-related properties. This step reveals the enforcement status for both kernel-mode (DeviceGuardCodeIntegrityPolicyEnforcementStatus) and user-mode (DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus) code integrity policies. Run this in an elevated PowerShell session to ensure accurate results.

**Command** ([[commands/powershell-get-computerinfo-wdac-status]]):
```powershell
Get-ComputerInfo
```

> This command outputs a comprehensive set of computer information. Focus on the DeviceGuard sections to identify WDAC mode. If the values show 'EnforcementMode', WDAC is actively blocking; 'AuditMode' means logging only; 'NotConfigured' or absent indicates disabled. Pipe to Format-List or select specific properties for cleaner output if needed (e.g., Get-ComputerInfo | Select-Object -ExpandProperty WindowsProductName, DeviceGuard*).

**Expected Output**:
```
DeviceGuardCodeIntegrityPolicyEnforcementStatus         : EnforcementMode
DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus : EnforcementMode
```

> Success is indicated by the presence of these properties. Cross-reference with full output to confirm WDAC configuration. If in Audit Mode, test unauthorized executables to verify logging without enforcement.
