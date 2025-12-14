---
id: cmd-adb-install-app
data: adb install path/to/malicious_app.apk
tags:
  - deployment
  - android
type: command
output: 'Success: installed com.malicious'
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:41.880Z'
verified: false
validated: true
submitted: true
---
# adb install

## Command

```bash
adb install path/to/malicious_app.apk
```

## Description

Installs an APK file to the connected Android device, essential for deploying malicious apps to trigger intents or exploits like in ownCloud file theft scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path/to/apk | Full path to the APK file | Yes |
| -r | Replace existing app | No |

## Examples

### Basic Usage

```bash
adb install malicious_app.apk
```

### Advanced Usage

```bash
adb install -r malicious_app.apk
```

## Expected Output

'Success' message with package name, indicating installation complete.

## Related

- [[commands/adb-shell-am-start]]
- [[procedures/Trigger-File-Upload-via-StartActivity]]
