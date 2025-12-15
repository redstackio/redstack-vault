---
id: cmd-ls-macos-001
data: >-
  ls -l /Volumes/Kaspersky Internet Security/Kaspersky
  Downloader.app/Contents/MacOS
tags:
  - inspection
  - file-listing
type: command
output: |-
  total 3392
  -rwxr-xr-x 1 csaby staff 1015904 Oct 9 2019 Downloader
  -rwxr-xr-x 1 csaby staff 569152 Oct 9 2019 libkl_appkit.dylib
  -rwxr-xr-x 1 csaby staff 144256 Oct 9 2019 libz.1.2.11.dylib
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:10.004Z'
verified: false
validated: true
submitted: true
---
# list-macos-directory

## Command

```bash
ls -l /Volumes/Kaspersky Internet Security/Kaspersky Downloader.app/Contents/MacOS
```

## Description

Lists the contents of the MacOS directory in the Kaspersky Downloader app bundle in long format, revealing libraries like libkl_appkit.dylib for targeting in dylib proxying attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Long format listing showing permissions, sizes, and dates | Yes |
| Path | Specific directory path in the mounted volume | Yes |

## Examples

### Basic Usage

```bash
ls -l /Volumes/Kaspersky Internet Security/Kaspersky Downloader.app/Contents/MacOS
```

### Advanced Usage

```bash
ls -la /Volumes/Kaspersky Internet Security/Kaspersky Downloader.app/Contents/MacOS
```

## Expected Output

total 3392
-rwxr-xr-x 1 csaby staff 1015904 Oct 9 2019 Downloader
-rwxr-xr-x 1 csaby staff 569152 Oct 9 2019 libkl_appkit.dylib
-rwxr-xr-x 1 csaby staff 144256 Oct 9 2019 libz.1.2.11.dylib

## Related

- [[codesign-entitlements-check]]
- [[procedures/Prepare-Vulnerable-Installer]]
