---
data: echo hello
tags:
  - container
type: command
output: hello
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:53.978Z'
id: 6310506c-1396-4771-b8a1-f48e98ce7c47
verified: false
validated: true
submitted: true
---
# echo-hello

## Command

```bash
echo hello
```

## Description

Simple command included in the task payload to execute inside the container, serving as a legitimate workload overshadowed by the host RCE injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Basic echo with string argument | No |

## Examples

### Basic Usage

```bash
echo hello
```

### Advanced Usage

```bash
echo "Task executed successfully"
```

## Expected Output

Prints 'hello' to stdout inside the container context.

## Related

- [[Related Procedure: Submit-Malicious-Task-Definition]]
