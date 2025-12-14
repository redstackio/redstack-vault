---
id: c3b2c3d4-e5f6-7890-abcd-ef1234567896
name: log-url-to-file
type: command
executor: cmd
data: 'echo %date% : %1 >> C:\mal_log.txt'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.847Z'
platforms:
  - Windows
tags:
  - logging
verified: false
validated: true
submitted: true
---

# log-url-to-file

## Command

```cmd
echo %date% : %1 >> C:\mal_log.txt
```

## Description

Appends the current date and the passed URL (%1) to a log file in the protected C:\ root, demonstrating elevated write access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %date% | Current system date | Yes |
| %1 | The URL to log | Yes |
| >> C:\mal_log.txt | Append to file | Yes |

## Examples

### Basic Usage

```cmd
echo %date% : https://example.com >> C:\mal_log.txt
```

### Advanced Usage

```cmd
echo %date% %time% : %1 >> C:\mal_log.txt
```

## Expected Output

New line added to mal_log.txt in format 'YYYY-MM-DD : URL'; fails without admin rights.

## Related

- [[commands/capture-url-argument]]
