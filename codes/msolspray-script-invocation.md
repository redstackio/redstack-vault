---
type: code
language: powershell
verified: true
tags:
  - password-spraying
  - azure-ad
  - script-loading
platforms:
  - Windows
validated: true
---

# msolspray-script-invocation

## Code

```powershell
PS> . C:\Tools\MSOLSpray\MSOLSpray.ps1
PS> Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password <PASSWORD> -Verbose
```

## Description

This PowerShell code snippet loads the MSOLSpray script into the current session and invokes the password spraying function. It dotsources the external script file to make its functions available, then runs the spraying operation against a user list with a specified password. Used in Azure AD credential access scenarios to test weak passwords across multiple accounts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| C:\Tools\MSOLSpray\MSOLSpray.ps1 | Path to the downloaded MSOLSpray script file | C:\Tools\MSOLSpray\MSOLSpray.ps1 |
| C:\Tools\validemails.txt | Path to the file containing target email addresses | C:\Tools\validemails.txt |
| <PASSWORD> | The common password to spray | Password123 |

## Usage

Execute this in a PowerShell session after downloading MSOLSpray from GitHub. It prepares and runs the spraying attack as part of a broader credential access procedure, such as in red team engagements targeting Office 365. Follow with accessing successful accounts via web interfaces.

## Detection

- PowerShell script block logging capturing the dotsource and Invoke-MSOLSpray calls.
- Azure AD sign-in logs showing multiple authentication failures from the same IP.
- Network traffic to login.microsoftonline.com with patterns of sequential user attempts.

## Related

- [[procedures/Azure-Password-Spraying]]
- [[commands/msolspray-invoke-password-spray]]
