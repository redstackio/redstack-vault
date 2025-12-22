---
data: 'jarfile:c:/windows/whatever.exe'
tags:
  - protocol
  - windows
type: command
executor: bash
platforms:
  - Windows
id: 9bb3d024-4834-4762-9762-e43176d47f23
created_at: '2025-12-11T06:10:17.587Z'
updated_at: '2025-12-11T06:10:17.587Z'
verified: false
validated: true
submitted: true
---
# custom-protocol-jarfile-path

## Command

```bash
jarfile:c:/windows/whatever.exe
```

## Description

Attempts to execute a file via jarfile protocol.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `c:/windows/whatever.exe` | File path | Yes |

## Examples

### Basic Usage

```bash
jarfile:c:/windows/whatever.exe
```

## Expected Output

Tries to run with Java, may fail due to path issues.

## Related

- [[commands/custom-protocol-jarfile-traversal]]
- [[procedures/Explore-Custom-Protocols-and-Directory-Traversal]]
