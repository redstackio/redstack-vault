---
type: command
executor: command_prompt
data: systeminfo
output: |-
  Host Name:                 Bob-PC
  OS Name:                   Microsoft Windows 10 Pro
  OS Version:                10.0.18362 N/A Build 18362
  ... (full system details including Hotfix(s) section with KB lists)
  Hotfix(s):                 9 Hotfix(s) Installed.
                             [01]: KB4515871
                             [02]: KB4503308
                             [03]: KB4506472
                             [04]: KB4509096
                             [05]: KB4515383
                             [06]: KB4516115
                             [07]: KB4520390
                             [08]: KB4521863
                             [09]: KB4517389
platforms:
  - Windows
tags:
  - Enumeration
verified: true
validated: true
---

# systeminfo-display-system-configuration

## Command

```command_prompt
systeminfo
```

## Description

This command displays detailed configuration information about the local Windows system, including OS details, hardware, network configuration, and installed hotfixes. It is useful for broad system reconnaissance during enumeration phases, particularly to identify patch levels and system properties without requiring additional tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Displays all available system information by default | Yes |

## Examples

### Basic Usage

```command_prompt
systeminfo
```

### Advanced Usage

Redirect output to a file for later analysis:

```command_prompt
systeminfo > systeminfo.txt
```

## Expected Output

A comprehensive report of system details, including host name, OS version, installed hotfixes, and more. Example excerpt:

Host Name:                 Bob-PC
OS Name:                   Microsoft Windows 10 Pro
OS Version:                10.0.18362 N/A Build 18362
...
Hotfix(s):                 9 Hotfix(s) Installed.
                          [01]: KB4515871
                          [02]: KB4503308
                          [03]: KB4506472
                          [04]: KB4509096
                          [05]: KB4515383
                          [06]: KB4516115
                          [07]: KB4520390
                          [08]: KB4521863
                          [09]: KB4517389

## Related

- [[tools/systeminfo]]
