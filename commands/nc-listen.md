---
data: nc -nvlp 3333
tags:
  - listen
  - reverse-shell
type: command
output: 'listening on [any] 3333 ... connect to [127.0.0.1] from ...'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.967Z'
id: d9d24257-eadc-45a1-821a-22f29377b4c3
verified: false
validated: true
submitted: true
---
# nc-listen

## Command

```bash
nc -nvlp 3333
```

## Description

Starts netcat in listen mode on localhost port 3333 to receive the reverse shell from the root payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | No DNS resolution | Yes |
| -v | Verbose output | Yes |
| -l | Listen mode | Yes |
| -p 3333 | Port to bind | Yes |

## Examples

### Basic Usage

```bash
nc -nvlp 3333
```

### Advanced Usage

```bash
nc -nvlp 0.0.0.0 4444
```

## Expected Output

'listening on [any] 3333 ... connect to [127.0.0.1] from (localhost)'

## Related

- [[commands/echo-deploy-payload]]
- [[procedures/Deploy-Reverse-Shell-Payload]]
