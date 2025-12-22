---
data: '.txt:hello'
tags:
  - protocol
  - windows
type: command
executor: bash
platforms:
  - Windows
id: 3ae6750e-ce8b-44f7-86b0-f3c19d10631b
created_at: '2025-12-11T06:10:17.623Z'
updated_at: '2025-12-11T06:10:17.623Z'
verified: false
validated: true
submitted: true
---
# custom-protocol-txt

## Command

```bash
.txt:hello
```

## Description

Opens a .txt file association with a parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `hello` | Parameter | No |

## Examples

### Basic Usage

```bash
.txt:hello
```

## Expected Output

Opens Notepad with 'hello'.

## Related

- [[commands/custom-protocol-calculator]]
- [[procedures/Explore-Custom-Protocols-and-Directory-Traversal]]
