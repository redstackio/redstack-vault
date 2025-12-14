---
id: c2b2c3d4-e5f6-7890-abcd-ef1234567895
name: capture-url-argument
type: command
executor: cmd
data: set arg1=%1
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.854Z'
platforms:
  - Windows
tags:
  - batch
verified: false
validated: true
submitted: true
---

# capture-url-argument

## Command

```cmd
set arg1=%1
```

## Description

Captures the first command-line argument (%1, typically the triggered URL) into a variable for use in batch scripts during protocol handler invocation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %1 | The passed URL or parameter | Yes |

## Examples

### Basic Usage

```cmd
set arg1=%1
echo %arg1%
```

### Advanced Usage

```cmd
set arg1=%1
if not "%arg1%"=="" echo Captured: %arg1%
```

## Expected Output

Silent variable set; use `echo %arg1%` to verify the URL.

## Related

- [[commands/log-url-to-file]]
