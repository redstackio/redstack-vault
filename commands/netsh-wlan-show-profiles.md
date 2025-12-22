---
type: command
executor: cmd
data: netsh wlan show profiles
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - credential-access
  - windows
verified: true
validated: true
---

# netsh-wlan-show-profiles

## Command

```cmd
netsh wlan show profiles
```

## Description

This command displays all wireless profile names (SSIDs) saved on the Windows system, including user and all-user profiles. It is used during reconnaissance to identify previously connected networks for credential extraction. Requires elevated privileges for complete visibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters; shows all profiles by default | No |

## Examples

### Basic Usage

```cmd
netsh wlan show profiles
```

Outputs a list like:

Profiles on interface Wi-Fi:

Group policy profiles (read only)
---------------------------------
<None>

User profiles
-------------
All User Profile     : CorporateWiFi
All User Profile     : HomeNetwork

### Advanced Usage

To filter output, pipe to find:

```cmd
netsh wlan show profiles | findstr "Profile"
```

## Expected Output

A formatted list of profiles under 'User profiles' or 'All User Profile' sections, showing SSID names. Success is indicated by no errors and presence of profile entries. Example:

All User Profile     : TargetSSID

If no profiles exist, it reports '<None>'.
