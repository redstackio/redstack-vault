---
id: cmd-uuid-10
data: fcrackzip -u -D -p wordlists/passwords.txt my_secure_files_not_for_you.zip
tags:
  - cracking
type: command
output: 'PASSWORD FOUND!!!!: pw == hahahaha'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.423Z'
verified: false
validated: true
submitted: true
---
# Fcrackzip Crack Zip

## Command

```bash
fcrackzip -u -D -p wordlists/passwords.txt my_secure_files_not_for_you.zip
```

## Description

Brute-forces ZIP file password.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Unzip check | No |
| -D | Dictionary | Yes |
| -p | Password list | Yes |
| File | ZIP target | Yes |

## Examples

### Basic Usage

```bash
fcrackzip -D -p list.zip file.zip
```

## Expected Output

Found password.

## Related

- [[procedures/Brute-Force-Credentials-and-Manipulate-Base64-Cookie]]
