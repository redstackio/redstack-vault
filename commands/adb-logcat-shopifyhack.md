---
id: cmd-adb-logcat-001
data: 'adb logcat -s SHOPIFYHACK:V'
tags:
  - logcat
  - android-debug
type: command
output: >-
  Logs containing dumped response headers (e.g., admin_cookie), body (e.g.,
  access_token), and other extras from the broadcast
executor: bash
platforms:
  - Android
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:10.982Z'
verified: false
validated: true
submitted: true
---
# adb-logcat-shopifyhack

## Command

```bash
adb logcat -s SHOPIFYHACK:V
```

## Description

This command filters Android device logs using ADB to display verbose output for the 'SHOPIFYHACK' tag, revealing intercepted sensitive data from the POC APK after Shopify broadcasts are triggered.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Specifies the tag filter (SHOPIFYHACK) to show only relevant logs | Yes |
| `V` | Sets verbose log level to capture detailed output including extras | Yes |

## Examples

### Basic Usage

```bash
adb logcat -s SHOPIFYHACK:V
```

### Advanced Usage

```bash
adb logcat -s SHOPIFYHACK:V | grep "token"
```

> Filters further for specific keywords like 'token'.

## Expected Output

Real-time log stream with entries like:

V/SHOPIFYHACK: Cookie: admin_session=abc123...
V/SHOPIFYHACK: Token: access_token=xyz789...
V/SHOPIFYHACK: Headers: {...}
V/SHOPIFYHACK: Body: {"user": {...}}

Indicating successful data leakage.

## Related

- [[Related Procedure: View-Leaked-Data-in-Android-Logs]]
