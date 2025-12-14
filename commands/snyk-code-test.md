---
data: snyk code test --file=NextcloudTalk.apk
tags:
  - static-analysis
  - security-scan
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.589Z'
id: ec6ae0ce-d743-4874-b5f0-94e7ba5cd874
verified: false
validated: true
submitted: true
---
# snyk-code-test

## Command

```bash
snyk code test --file=NextcloudTalk.apk
```

## Description

Runs Snyk's static code analysis on an Android APK to detect vulnerabilities like missing permissions in broadcast receivers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--file` | Path to the APK or source directory | Yes |
| `--severity-threshold` | Minimum severity to report (low, medium, high) | No |

## Examples

### Basic Usage

```bash
snyk code test --file=app.apk
```

### Advanced Usage

```bash
snyk code test --file=app.apk --severity-threshold=high --json
```

## Expected Output

A formatted report with vulnerability details, including code paths and remediation advice, e.g., "Issue: Missing broadcastPermission in registerReceiver at line 123."

## Related

- [[commands/snyk-auth]]
- [[procedures/Perform-Static-Analysis-on-Android-App-with-Snyk]]
