---
id: 1c1d443d-30d4-4718-a3be-c11067f74f7e
type: command
executor: command_prompt
data: 'wmic qfe get Caption,Description,HotFixID,InstalledOn'
output: >-
  Caption                                     Description      HotFixID  
  InstalledOn

  http://support.microsoft.com/?kbid=4515871  Update           KB4515871 
  10/5/2019

  http://support.microsoft.com/?kbid=4503308  Security Update  KB4503308 
  7/9/2019

  http://support.microsoft.com/?kbid=4506472  Update           KB4506472 
  7/9/2019

  http://support.microsoft.com/?kbid=4509096  Security Update  KB4509096 
  7/9/2019

  http://support.microsoft.com/?kbid=4515383  Security Update  KB4515383 
  10/5/2019

  http://support.microsoft.com/?kbid=4516115  Security Update  KB4516115 
  10/5/2019

  http://support.microsoft.com/?kbid=4520390  Security Update  KB4520390 
  10/5/2019

  http://support.microsoft.com/?kbid=4521863  Security Update  KB4521863 
  10/14/2019

  http://support.microsoft.com/?kbid=4517389  Update           KB4517389 
  10/21/2019
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - Enumeration
verified: true
validated: true
---

# wmic-query-installed-hotfixes

## Command

```command_prompt
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

## Description

This command uses WMIC to query the Windows quick fix engineering (QFE) database, listing installed hotfixes with details like KB ID and installation date. Use it during host discovery to identify patch levels for vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `qfe` | Queries the hotfix database (WMI class for quick fixes) | Yes (built-in) |
| `get Caption,Description,HotFixID,InstalledOn` | Specifies output fields: title link, type, KB ID, date | Yes |

## Examples

### Basic Usage

```command_prompt
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

### Advanced Usage

Pipe to file for analysis:

```command_prompt
wmic qfe get HotFixID,InstalledOn /format:csv > hotfixes.csv
```

## Expected Output

A table listing installed hotfixes, such as:

Caption                                     Description      HotFixID   InstalledOn
http://support.microsoft.com/?kbid=4515871  Update           KB4515871  10/5/2019
http://support.microsoft.com/?kbid=4503308  Security Update  KB4503308  7/9/2019
http://support.microsoft.com/?kbid=4506472  Update           KB4506472  7/9/2019
http://support.microsoft.com/?kbid=4509096  Security Update  KB4509096  7/9/2019
http://support.microsoft.com/?kbid=4515383  Security Update  KB4515383  10/5/2019
http://support.microsoft.com/?kbid=4516115  Security Update  KB4516115  10/5/2019
http://support.microsoft.com/?kbid=4520390  Security Update  KB4520390  10/5/2019
http://support.microsoft.com/?kbid=4521863  Security Update  KB4521863  10/14/2019
http://support.microsoft.com/?kbid=4517389  Update           KB4517389  10/21/2019

## Related

- [[tools/wmic]]
