---
data: '.txt:hello'
tags:
  - protocol
  - windows
type: command
executor: bash
platforms:
  - Windows
id: 2b4449f9-3ad1-4600-a048-9403ab8516bc
created_at: '2025-12-14T00:11:25.282Z'
updated_at: '2025-12-14T00:11:25.282Z'
verified: false
validated: true
submitted: true
---
# txt-hello-protocol

## Command

```bash
.txt:hello
```

## Description

Tests file type association by opening Notepad with a custom protocol via Win+R.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `protocol` | .txt: | Yes |
| `argument` | hello | Yes |

## Examples

### Basic Usage

```bash
.txt:hello
```

## Expected Output

Opens Notepad.

## Related

- [[procedures/Escalating-with-Steam-URI-Schemes]]
