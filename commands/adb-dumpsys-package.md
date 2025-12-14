---
id: cmd-adb-dumpsys-package
data: adb shell dumpsys package com.owncloud.android
tags:
  - recon
  - android
type: command
output: Package details including activities and intent filters
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:41.885Z'
verified: false
validated: true
submitted: true
---
# adb shell dumpsys package

## Command

```bash
adb shell dumpsys package com.owncloud.android
```

## Description

This command dumps detailed information about the specified Android package, including exported activities, services, and intent filters, useful for identifying vulnerabilities like insecure exported components in apps such as ownCloud.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| package_name | The Android package to inspect (e.g., com.owncloud.android) | Yes |

## Examples

### Basic Usage

```bash
adb shell dumpsys package com.owncloud.android
```

### Advanced Usage

```bash
adb shell dumpsys package com.owncloud.android | grep -i exported
```

## Expected Output

Detailed XML-like output showing components, e.g., activities with export status and intent filters for SEND_MULTIPLE, confirming vulnerabilities.

## Related

- [[commands/adb-shell]]
- [[procedures/Identify-Vulnerable-Exported-Activity]]
