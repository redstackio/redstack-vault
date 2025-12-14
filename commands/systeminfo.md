---
data: systeminfo
tags:
  - recon
  - system-info
type: command
output: >-
  System details such as Host Name, OS Name: Microsoft Windows Server 2019
  Standard, OS Version: 10.0.17763, processors, memory, network cards, and list
  of hotfixes.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:54.391Z'
id: aa6ede95-39c1-46dc-97c4-6dc369886212
verified: false
validated: true
submitted: true
---
# systeminfo

## Command

```cmd
systeminfo
```

## Description

Retrieves detailed system information from a Windows machine, including OS configuration, hardware specs, network details, and installed updates. Used in RCE scenarios to enumerate the target's environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs full system query | No |

## Examples

### Basic Usage

```cmd
systeminfo
```

### Advanced Usage

```cmd
systeminfo /s:remotehost
```

## Expected Output

Detailed text output listing system components, e.g., 'Host Name: SERVER01', 'OS Name: Microsoft Windows Server 2019 Standard', total physical memory, network adapters, and hotfix list.

## Related

- [[Related Procedure|procedures/Exploit-Liferay-Deserialization-RCE]]
