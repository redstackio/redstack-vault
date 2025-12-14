---
data: pip3 install requests bcrypt
tags:
  - setup
  - dependencies
type: command
output: Successfully installed requests-x.x.x and bcrypt-x.x.x
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.801Z'
id: 53ad58bb-44f1-489b-9260-079cba637470
verified: false
validated: true
submitted: true
---
# install-python-dependencies

## Command

```bash
pip3 install requests bcrypt
```

## Description

Installs Python packages required for HTTP requests and password hashing in the exploit script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| requests | HTTP client library | Yes |
| bcrypt | Password hashing library | Yes |

## Examples

### Basic Usage

```bash
pip3 install requests bcrypt
```

### Advanced Usage

```bash
pip3 install requests==2.28.0 bcrypt==4.0.0
```

## Expected Output

Requirement already satisfied or download progress, ending with 'Successfully installed'.

## Related

- [[commands/python3-post-auth-nosqli]]
