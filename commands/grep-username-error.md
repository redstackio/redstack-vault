---
data: grep "Username does not exist"
tags:
  - filtering
  - log-analysis
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.166Z'
id: e70952ba-ef64-4e7f-b3d6-a595b7fa672b
verified: false
validated: true
submitted: true
---
# grep-username-error

## Command

```bash
grep "Username does not exist"
```

## Description

This command searches for the exact error string 'Username does not exist' in API response logs or output files to identify invalid username attempts during brute-forcing, allowing isolation of valid usernames by exclusion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "Username does not exist" | Exact string to match in input (e.g., file or stdin) | Yes |
| <input_file> | File containing response logs (if not piped) | No |

## Examples

### Basic Usage

```bash
grep "Username does not exist" responses.log
```

### Advanced Usage

```bash
grep -v "Username does not exist" responses.log > valid_usernames.txt
```

## Expected Output

Lines from the input containing the matched string, e.g., full response JSON with the error for invalid usernames.

## Related

- [[Related Procedure: Enumerate-Valid-Usernames-via-Error-Messages]]
