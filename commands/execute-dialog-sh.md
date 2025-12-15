---
id: cmd-637840-002
data: |
  |
    ./dialog.sh
tags:
  - password-leak
  - poc
  - credential-theft
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.583Z'
verified: false
validated: true
submitted: true
---
# execute-dialog-sh

## Command

```bash
./dialog.sh
```

## Description

Proof-of-concept script to abuse MariaDB's dialog plugin, tricking the user into sending unhashed passwords to the server during connection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Script simulates connection and prompt | No |

## Examples

### Basic Usage

```bash
./dialog.sh
```

### Advanced Usage

Integrate with server:

```bash
# Run alongside malicious server, observe captured password
./dialog.sh
```

## Expected Output

User prompted for password; server logs unhashed credential.

## Related

- [[procedures/Abuse-Dialog-Plugin-for-Password-Leak]]
