---
data: ruby ftp.rb
tags:
  - exfiltration
  - oob
type: command
executor: bash
platforms:
  - Linux
id: 05793148-5e7c-4c74-9ffc-32267e76dd84
created_at: '2025-12-13T09:00:27.530Z'
updated_at: '2025-12-13T09:00:27.530Z'
verified: false
validated: true
submitted: true
---
# Run Ruby FTP Server

## Command

```bash
ruby ftp.rb
```

## Description

This command executes a Ruby script to start an FTP server designed for receiving exfiltrated data during out-of-band XXE attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ftp.rb` | The Ruby script file | Yes |

## Examples

### Basic Usage

```bash
ruby ftp.rb
```

### Advanced Usage

```bash
ruby ftp.rb --port 21 --host 0.0.0.0
```

## Expected Output

FTP server starts listening and receives connections with exfiltrated file contents, such as lines from /etc/passwd.

## Related

- [[procedures/Refine-OOB-XXE-with-FTP-Exfiltration]]
- [[tools/ftp-rb]]
