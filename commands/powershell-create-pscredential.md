---
id: 77405553-c24b-48e5-84e9-1ff4a18795fc
name: powershell-create-pscredential
type: command
executor: powershell
data: >-
  $Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force

  $Cred = New-Object -TypeName System.Management.Automation.PSCredential
  -Argument "$_DOMAIN\$_USER", $Pass
output: Secure credential object created.
created_at: '2020-03-17T05:07:20.698649+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powershell
  - credential
verified: true
validated: true
---

# powershell-create-pscredential

## Command

```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```

## Description

Creates PSCredential object for auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PASSWORD | Password | Yes |
| $_DOMAIN | Domain | Yes |
| $_USER | Username | Yes |

## Examples

### Basic Usage

```powershell
$Pass = ConvertTo-SecureString -String "pass" -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential -Argument "domain\user", $Pass
```

## Expected Output

$Cred variable with credential.
