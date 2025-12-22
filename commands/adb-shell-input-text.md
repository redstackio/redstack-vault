---
data: adb shell input text 8e9998ee3137ca9ade8f372739f062c1
tags:
  - input-simulation
type: command
output: Text entered into focused field
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.913Z'
id: d1bb18bb-a935-4027-aa4f-f1e6298fdbff
verified: false
validated: true
submitted: true
---
# adb-shell-input-text

## Command

```bash
adb shell input text 8e9998ee3137ca9ade8f372739f062c1
```

## Description

Simulate text input in app field.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| text | String to input | Yes |

## Examples

### Basic Usage

```bash
adb shell input text 8e9998ee3137ca9ade8f372739f062c1
```

## Expected Output

Field populated.

## Related

- [[procedures/Extract-API-Token-from-APK-Using-ADB-and-Frida]]
