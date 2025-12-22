---
type: procedure
description: >-
  Converts an Azure Active Directory (AAD) object GUID to its corresponding
  Security Identifier (SID) format for use in hybrid identity environments.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[T1087.004]]'
sub_techniques: []
tags:
  - azure-ad
  - cloud-azure
  - guid-to-sid
  - discovery
  - evasion
commands:
  - '[[commands/generate-azure-ad-guid-and-sid]]'
platforms:
  - Azure
  - Windows
tools: []
validated: true
---

# Convert-Azure-AD-GUID-to-SID

## Summary

This procedure converts an Azure Active Directory (AAD) object GUID, such as a user or group identifier, into its Windows Security Identifier (SID) format. The SID follows the structure S-1-12-1- followed by the four parts of the GUID converted from hexadecimal to decimal. This technique is useful in hybrid Azure AD and on-premises Windows environments for obfuscating references to cloud identities, evading detection during account discovery or permission assignments, and facilitating attacks like lateral movement using cloud credentials.

## Description

In Azure AD Connect hybrid setups, cloud identities are represented in Windows with SIDs starting with S-1-12-1-, followed by the decimal equivalents of the GUID's components (8-hex, 4-hex, 4-hex, 4-hex, 12-hex parts). Attackers use this conversion to map AAD objects to local SIDs for tasks like querying group memberships, assigning permissions, or impersonating principals without directly exposing the GUID, which can trigger cloud-specific logging. The process involves parsing the GUID, converting each segment from hex to decimal, and concatenating them into the SID string. This is particularly relevant for post-compromise scenarios where an attacker has obtained AAD object IDs via enumeration tools like Azure CLI or PowerShell modules and needs to interact with them in a Windows context.

## Requirements

1. Valid AAD object GUID (e.g., obtained via enumeration of users or groups).
2. PowerShell environment on Windows or cross-platform compatible setup.
3. Permissions to execute scripts (e.g., no execution policy restrictions).
4. Knowledge of the target's hybrid identity configuration (Azure AD Connect synced).

## Defense

- Monitor Azure AD sign-in logs and audit logs for unusual GUID/SID queries or conversions using tools like Microsoft Sentinel or Azure Monitor.
- Implement least-privilege access to AAD enumeration endpoints and restrict PowerShell module usage (e.g., Az.Accounts) via Conditional Access policies.
- Enable advanced auditing for SID-related events in Windows Event Logs (e.g., Event ID 4624 for logons) and correlate with cloud activity.
- Use anomaly detection to flag scripted hex-to-decimal conversions or SID generation patterns in endpoint detection tools like Microsoft Defender for Endpoint.

## Objectives

1. Obfuscate AAD object references by converting to SID format to evade GUID-based detections.
2. Enable interaction with hybrid identities for discovery, privilege escalation, or persistence.
3. Maintain operational security by avoiding direct AAD API calls that log object IDs.

## Instructions

### Step 1: Obtain or Generate the AAD GUID

**Context**: Start with a valid AAD object GUID. If not already known, it can be enumerated from Azure AD using tools like Get-AzADUser. For demonstration, generate a random GUID to simulate an obtained object ID. This step ensures you have the input in standard format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.

**Command** ([[commands/generate-azure-ad-guid-and-sid]]):
```powershell
# Generate a random GUID (replace with actual enumeration if needed)
$guid = [guid]::NewGuid().ToString("N").ToUpper()
Write-Output "Generated GUID: $guid"
```

> This generates a random GUID. Expected output is a 32-character hexadecimal string without hyphens, e.g., "A1B2C3D4E5F67890123456789ABCDEF0". If using an existing GUID, skip generation and use the known value.

### Step 2: Convert GUID to SID Format

**Context**: Parse the GUID into its four components (8-hex, 4-hex, 4-hex, 12-hex after removing hyphens), convert each from hexadecimal to decimal, and construct the SID as "S-1-12-1-<dec1>-<dec2>-<dec3>-<dec4>". This mimics the Azure AD Connect SID generation and allows use in Windows APIs or commands.

**Command** ([[commands/generate-azure-ad-guid-and-sid]]):
```powershell
# Function to convert GUID to SID (input your GUID here)
function Convert-GuidToSid {
    param([string]$Guid)
    $cleanGuid = $Guid -replace "-", ""
    $parts = @(
        $cleanGuid.Substring(0,8),
        $cleanGuid.Substring(8,4),
        $cleanGuid.Substring(12,4),
        $cleanGuid.Substring(16,12)
    )
    $decParts = $parts | ForEach-Object { [Convert]::ToInt64($_, 16) }
    $sid = "S-1-12-1-$($decParts[0])-$($decParts[1])-$($decParts[2])-$($decParts[3])"
    Write-Output $sid
}

# Example usage with generated or known GUID
Convert-GuidToSid -Guid $guid
```

> Replace $guid with your actual GUID. Expected output is the SID string, e.g., "S-1-12-1-1789435595-1301421967-3702525313-2188119011". Verify by checking if the decimal values match hex conversions (use calculator for manual validation).

### Step 3: Validate the SID

**Context**: Test the SID in a Windows command to confirm it's usable, such as querying group membership if in a hybrid environment. This verifies the conversion for downstream actions like wmic or PowerShell AD queries.

**Command** ([[commands/generate-azure-ad-guid-and-sid]]):
```powershell
# Validate SID (example: check if SID is recognized in local context)
$sidObject = New-Object System.Security.Principal.SecurityIdentifier($sid)
Write-Output "SID: $sid"
Write-Output "Account: $($sidObject.Translate([System.Security.Principal.NTAccount]))"
```

> If the SID corresponds to a known AAD object, it may resolve to the account name in hybrid setups. Expected output includes the SID and any translated account info; errors indicate invalid format.
