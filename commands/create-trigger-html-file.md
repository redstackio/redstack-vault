---
id: cmd-uuid-2
data: touch hackerone.com.html
tags:
  - file-creation
  - unix
type: command
output: No output if successful; file is created
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.091Z'
verified: false
validated: true
submitted: true
---
# create-trigger-html-file

## Command

```bash
touch hackerone.com.html
```

## Description

Creates an empty file named 'hackerone.com.html' to serve as the trigger for the hekto redirection logic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hackerone.com.html | Filename to create | Yes |

## Examples

### Basic Usage

```bash
touch hackerone.com.html
```

### Advanced Usage

```bash
touch example.com.html
```

## Expected Output

Silent success; use 'ls' to confirm file existence.

## Related

- [[Related Procedure|procedures/Create-Trigger-HTML-File]]
