---
data: frida -U -l bounty_app.js --no-pause -f bounty.pay
tags:
  - hooking
type: command
output: 'Logs values from getValue() calls, e.g., ''Token'''
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.916Z'
id: 6a396d9f-7ff2-4f04-a5e9-3d47075edc9e
verified: false
validated: true
submitted: true
---
# frida-attach-script

## Command

```bash
frida -U -l bounty_app.js --no-pause -f bounty.pay
```

## Description

Attach Frida to app, load script to hook Firebase DataSnapshot.getValue().

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U | USB device | Yes |
| -l | Script path | Yes |
| --no-pause | No pause | No |
| -f | Force spawn | Yes |

## Examples

### Basic Usage

```bash
frida -U -l bounty_app.js --no-pause -f bounty.pay
```

## Expected Output

Hooked logs: 'Token' value.

## Related

- [[procedures/Extract-API-Token-from-APK-Using-ADB-and-Frida]]
