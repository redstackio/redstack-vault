---
data: 'wget ''f[h-j]le:///etc/passwd'''
tags:
  - comparison
type: command
output: 'f[h-j]le:///etc/passwd: 地址缺少协议类型. (Address lacks protocol type)'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.304Z'
id: efdff3aa-75b8-48a1-83e9-64bc840e797b
verified: false
validated: true
submitted: true
---
# wget-glob-fail

## Command

```bash
wget 'f[h-j]le:///etc/passwd'
```

## Description

Attempts to download a globbed URL with wget, which fails due to no globbing support, treating it literally.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | Globbed URL 'f[h-j]le:///etc/passwd' | Yes |

## Examples

### Basic Usage

```bash
wget 'f[h-j]le:///etc/passwd'
```

### Advanced Usage

```bash
wget --no-check-certificate 'f[h-j]le:///etc/passwd'
```

## Expected Output

f[h-j]le:///etc/passwd: 地址缺少协议类型. (Address lacks protocol type)

## Related

- [[Related Procedure]]
