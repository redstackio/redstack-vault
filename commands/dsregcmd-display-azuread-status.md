---
id: 1b7ae28c-99d2-40d0-9f3a-ef0527569912
name: dsregcmd-display-azuread-status
type: command
executor: cmd
data: dsregcmd.exe /status
output: |-
  C:\ dsregcmd.exe /status

  +----------------------------------------------------------------------+
  | SSO State                                                            |
  +----------------------------------------------------------------------+

                  AzureAdPrt : YES
         AzureAdPrtAuthority : https://login.microsoftonline.com/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
               EnterprisePrt : NO
      EnterprisePrtAuthority : NO

  +----------------------------------------------------------------------+
  | Device State                                                         |
  +----------------------------------------------------------------------+

               AzureAdJoined : YES
            EnterpriseJoined : NO
                DomainJoined : NO
                 Device Name : Target-PC
created_at: '2023-05-25T19:01:32.184127+00:00'
updated_at: '2023-05-25T19:01:32.394531+00:00'
platforms:
  - Windows
tags:
  - azure-ad
  - status-check
verified: true
validated: true
---

# dsregcmd-display-azuread-status

## Command

```cmd
dsregcmd.exe /status
```

## Description

This command displays the Azure AD join status and Single Sign-On (SSO) state of a Windows device, including whether a Primary Refresh Token (PRT) is present. Use it to verify prerequisites for PRT extraction techniques on AAD-joined machines.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /status   | Displays device registration and SSO status | Yes |

## Examples

### Basic Usage

```cmd
dsregcmd.exe /status
```

> Run from an elevated Command Prompt on the target Windows machine.

## Expected Output

```
C:\ dsregcmd.exe /status

+----------------------------------------------------------------------+
| SSO State                                                            |
+----------------------------------------------------------------------+

                AzureAdPrt : YES
       AzureAdPrtAuthority : https://login.microsoftonline.com/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
             EnterprisePrt : NO
    EnterprisePrtAuthority : NO

+----------------------------------------------------------------------+
| Device State                                                         |
+----------------------------------------------------------------------+

             AzureAdJoined : YES
          EnterpriseJoined : NO
              DomainJoined : NO
               Device Name : Target-PC
```

Look for AzureAdPrt: YES and AzureAdJoined: YES to confirm eligibility for PRT dumping.

## Related

- [[procedures/Azure-Pass-The-PRT-with-Mimikatz]]
