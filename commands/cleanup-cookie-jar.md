---
id: cmd-cleanup-cookie-jar
data: rm "$cookiejar"
tags:
  - cleanup
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.371Z'
verified: false
validated: true
submitted: true
---
# cleanup-cookie-jar

## Command

```bash
rm "$cookiejar"
```

## Description

This command removes a temporary cookie jar file created during authentication, ensuring no sensitive session data is left on disk post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `rm "$cookiejar"` | Deletes the specified temporary file | Yes |

## Examples

### Basic Usage

```bash
rm cookies.txt
```

### Advanced Usage

```bash
rm "$cookiejar"
```

## Expected Output

No output; file is silently deleted if it exists.

## Related

- [[Related Procedure|procedures/wordpress-exploit-traversal-entropy]]
