---
id: cmd-wget-squid-source-2023
data: 'wget ''https://github.com/squid-cache/squid/archive/SQUID_4_8.tar.gz'''
tags:
  - download
type: command
output: Downloaded file SQUID_4_8.tar.gz
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.978Z'
verified: false
validated: true
submitted: true
---
# wget-squid-source

## Command

```bash
wget 'https://github.com/squid-cache/squid/archive/SQUID_4_8.tar.gz'
```

## Description

Downloads the Squid 4.8 source tarball from GitHub repository, essential for building the vulnerable version.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Source archive URL | Yes |

## Examples

### Basic Usage

```bash
wget 'https://github.com/squid-cache/squid/archive/SQUID_4_8.tar.gz'
```

### Advanced Usage

```bash
wget -O squid.tar.gz 'https://github.com/squid-cache/squid/archive/SQUID_4_8.tar.gz'
```

## Expected Output

Progress indicator and 'saved [size] bytes' message; file `SQUID_4_8.tar.gz` created.

## Related

- [[commands/tar-extract-squid]]
- [[procedures/Setup-Environment-and-Download-Squid-Source]]
