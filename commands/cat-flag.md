---
data: cat flag
tags:
  - verification
  - data-leak
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.205Z'
id: 11de443c-3fb5-4f03-b96e-bd357a75837a
verified: false
validated: true
submitted: true
---
# cat-flag

## Command

```bash
cat flag
```

## Description

Displays the contents of the 'flag' file to verify if exploitation resulted in cookie data being written to it, confirming overwrite or leakage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| flag | Target file path | Yes |

## Examples

### Basic Usage

```bash
cat flag
```

### With Line Numbers

```bash
cat -n flag
```

## Expected Output

Post-exploit: Cookie file contents like '# Netscape HTTP Cookie File\n#HttpOnly_google.com FALSE / FALSE 0 NID 123...'. Pre-exploit: Original data like 'secret'.

## Related

- [[commands/ls-long]]
- [[procedures/Verify-Exploitation-Outcome]]
