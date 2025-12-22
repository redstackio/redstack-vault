---
id: cmd-uuid-1
data: sleep 20
tags:
  - testing
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.134Z'
verified: false
validated: true
submitted: true
---
# sleep-20-injection

## Command

```bash
sleep 20
```

## Description

Pauses the current shell session for 20 seconds, used here as a proof-of-concept to demonstrate command injection by observing a delay in the web application response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 20 | Duration in seconds to sleep | Yes |

## Examples

### Basic Usage

```bash
sleep 20
```

### Advanced Usage

```bash
sleep 5  # Shorter delay for quicker testing
```

## Expected Output

No stdout output; the process hangs for 20 seconds before continuing, resulting in a delayed HTTP response.

## Related

- [[Related Procedure]]
