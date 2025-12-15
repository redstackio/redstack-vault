---
data: type HACKED.txt
tags:
  - verification
  - windows
type: command
output: null
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.617Z'
id: 0aae42ec-9f12-4ba2-80d8-fdfc8a6cb1d6
verified: false
validated: true
submitted: true
---
# type-view-file

## Command

```bash
type HACKED.txt
```

## Description

Displays the contents of the HACKED.txt file created by the exploited command to confirm injection success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `HACKED.txt` | File path to view | Yes |

## Examples

### Basic Usage

```bash
type HACKED.txt
```

### Advanced Usage

```bash
type HACKED.txt | find "HACKED"
```

## Expected Output

"HACKED" printed to console.

## Related

- [[commands/dir-list-directory]]
- [[procedures/Verify-Exploitation-Success]]
