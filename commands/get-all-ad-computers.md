---
id: 57fd56bb-5426-488c-b71d-8f7b9e63b21e
name: get-all-ad-computers
type: command
executor: powershell
data: Get-ADComputer -Filter * -Properties *
output: null
created_at: '2023-04-06T03:56:02.419598+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - computer-enumeration
verified: true
validated: true
---

# get-all-ad-computers

## Command

```powershell
Get-ADComputer -Filter * -Properties *
```

## Description

Enumerates all computer objects in the domain with all available properties for full asset discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Filter * | Retrieves all computers | Yes |
| -Properties * | Includes all attributes | Yes |

## Examples

### Basic Usage

```powershell
Get-ADComputer -Filter * -Properties *
```

### Export to CSV

```powershell
Get-ADComputer -Filter * -Properties * | Export-Csv -Path computers.csv -NoTypeInformation
```

## Expected Output

List of computer objects:

```
DistinguishedName : CN=WORKSTATION1,OU=Computers,DC=contoso,DC=com
Name              : WORKSTATION1
OperatingSystem   : Windows 10 Enterprise
...
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/get-all-ad-groups]]
