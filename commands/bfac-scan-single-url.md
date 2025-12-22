---
id: ade78991-14a6-44fd-8e0e-adbffa3ef468
name: bfac-scan-single-url
type: command
executor: bash
data: bfac --url $_TARGET_URL --level $_LEVEL
output: null
created_at: '2023-04-06T03:56:21.812479+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - recon
  - web
  - backup
verified: true
validated: true
---

# bfac-scan-single-url

## Command

```bash
bfac --url $_TARGET_URL --level $_LEVEL
```

## Description

This command scans a single target URL for exposed backup files and directories using BFAC, checking common backup patterns up to a specified depth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --url $_TARGET_URL | The specific URL or path to scan (e.g., http://example.com/test.php) | Yes |
| --level $_LEVEL | Scan depth for backup variations (1-5, higher is more thorough) | Yes |

## Examples

### Basic Usage

```bash
bfac --url http://example.com/index.php --level 3
```

### Advanced Usage

```bash
bfac --url https://target.com/admin --level 5 --timeout 10
```

## Expected Output

```
[+] http://example.com/test.php.bak (200 OK)
[+] http://example.com/test.php~ (404 Not Found)
[+] http://example.com/test.php.old (200 OK)
Scan completed. Found 2 backups.
```

Output lists potential backup URLs with status codes; 200 responses indicate downloadable files for further analysis.

## Related

- [[procedures/Web-Enumeration-and-Backup-File-Discovery]]
- [[tools/BFAC]]
