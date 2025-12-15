---
data: pip3 install requests bcrypt
tags:
  - setup
  - dependencies
type: command
output: Successfully installed requests-x.x.x bcrypt-x.x.x
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.425Z'
id: bb43a49e-fb25-4445-b7b4-a109d39e39f1
verified: false
validated: true
submitted: true
---
# pip3-install-requests-bcrypt

## Command

```bash
pip3 install requests bcrypt
```

## Description

Installs Python libraries required for HTTP requests and password handling in the exploit script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| requests | HTTP client library | Yes |
| bcrypt | Password hashing tool | Yes |

## Examples

### Basic Usage

```bash
pip3 install requests bcrypt
```

### Advanced Usage

```bash
pip3 install --user requests bcrypt
```

## Expected Output

Requirement already satisfied: requests... Successfully installed.

## Related

- [[commands/python3-post-auth-nosqli-py]]
