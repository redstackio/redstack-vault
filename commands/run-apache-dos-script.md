---
id: cmd-uuid-005
data: ./apache_dos_poc.sh owncloud.com 80
tags:
  - dos
  - execution
type: command
output: |-
  Request: 1
  Request: 2
  ... up to 5000
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.968Z'
verified: false
validated: true
submitted: true
---
# run-apache-dos-script

## Command

```bash
./apache_dos_poc.sh owncloud.com 80
```

## Description

Executes the PoC to send 5000 DoS requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| owncloud.com | Target host | Yes |
| 80 | Port | No (default 80) |

## Examples

### Basic Usage

```bash
./script.sh target.com
```

### Advanced Usage

```bash
./script.sh target.com 443
```

## Expected Output

Progress: "Request: N" for each iteration.

## Related

- [[Related Procedure]]
