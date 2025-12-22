---
id: feb94576-d843-476a-9e21-9a5f0577b74e
name: xxeinjector-log-requests
type: command
executor: bash
data: ruby XXEinjector.rb --logger --oob=http --output=/tmp/out.txt
output: null
created_at: '2023-04-06T03:56:43.973904+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
tags:
  - xxe
  - logging
verified: true
validated: true
---

# xxeinjector-log-requests

## Command

```bash
ruby XXEinjector.rb --logger --oob=http --output=/tmp/out.txt
```

## Description

Logs all generated requests for XXE testing without execution, useful for payload tuning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --logger | Enable logging mode | Built-in |
| --oob=http | HTTP OOB config | Built-in |
| --output=/tmp/out.txt | Output log file | Yes |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --logger --oob=http --output=/tmp/out.txt
```

## Expected Output

Requests saved to /tmp/out.txt for review.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
