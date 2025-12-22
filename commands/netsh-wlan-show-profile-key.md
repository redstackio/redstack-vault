---
type: command
executor: cmd
data: netsh wlan show profile name="<SSID>" key=clear
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

# netsh-wlan-show-profile-key

## Command

```cmd
netsh wlan show profile name="$_SSID" key=clear
```

## Description

This command retrieves detailed information for a specific Wi-Fi profile, including the clear-text security key (password) when run with elevated privileges. It is essential for extracting stored credentials from Windows wireless configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SSID | The name of the Wi-Fi profile (SSID) to query, enclosed in quotes if spaces | Yes |
| key=clear | Flag to display the key in plaintext (requires admin) | Yes |
| name= | Specifies the profile name parameter | Built-in |

## Examples

### Basic Usage

```cmd
netsh wlan show profile name="CorporateWiFi" key=clear
```

### Advanced Usage

For profiles with special characters:

```cmd
netsh wlan show profile name="My Home Network" key=clear
```

## Expected Output

Detailed profile info, including security settings. Success shows 'Key Content' with the password. Example snippet:

Security settings
-----------------
    Authentication         : WPA2
    Cipher                 : CCMP
    Security key           : Present
    Key Content            : MySecretPassword123

If the profile uses non-password auth (e.g., EAP), no 'Key Content' appears. Errors indicate invalid SSID or insufficient privileges.
