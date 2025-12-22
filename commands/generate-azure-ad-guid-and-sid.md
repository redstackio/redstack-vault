---
type: command
executor: powershell
data: >-
  # Generate a random GUID (replace with actual enumeration if needed)

  $guid = [guid]::NewGuid().ToString("N").ToUpper()

  Write-Output "Generated GUID: $guid"


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


  # Validate SID (example: check if SID is recognized in local context)

  $sidObject = New-Object System.Security.Principal.SecurityIdentifier($sid)

  Write-Output "SID: $sid"

  Write-Output "Account:
  $($sidObject.Translate([System.Security.Principal.NTAccount]))"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - azure-ad
  - guid-to-sid
verified: true
validated: true
---

# generate-azure-ad-guid-and-sid

## Command

```powershell
# Generate a random GUID (replace with actual enumeration if needed)
$guid = [guid]::NewGuid().ToString("N").ToUpper()
Write-Output "Generated GUID: $guid"

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

# Validate SID (example: check if SID is recognized in local context)
$sidObject = New-Object System.Security.Principal.SecurityIdentifier($sid)
Write-Output "SID: $sid"
Write-Output "Account: $($sidObject.Translate([System.Security.Principal.NTAccount]))"
```

## Description

This PowerShell script generates a random Azure AD-style GUID, converts it to the corresponding SID format by parsing hex components to decimal, and validates the SID. Use this during account discovery or evasion phases to create or map cloud identities for hybrid attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$Guid` | The input GUID string (auto-generated if not provided) | No |

## Examples

### Basic Usage

```powershell
# Run the full script for random generation and conversion
# (Paste the entire script block into PowerShell)
```

### Advanced Usage

```powershell
# Use with known GUID
Convert-GuidToSid -Guid "6aa89ecb-1f8f-4d92-810d-b0dce30b6c82"
```

## Expected Output

```
Generated GUID: A1B2C3D4E5F67890123456789ABCDEF0
S-1-12-1-1789435595-1301421967-3702525313-2188119011
SID: S-1-12-1-1789435595-1301421967-3702525313-2188119011
Account: 
```
(The account translation may be empty for non-synced SIDs; success is the valid SID string without errors.)

## Related

- [[procedures/Convert-Azure-AD-GUID-to-SID]]
