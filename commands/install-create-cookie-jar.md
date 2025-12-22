---
id: c-install-cookie-jar
name: install-create-cookie-jar
type: command
executor: bash
data: install -m 600 /dev/null cookie.jar
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.772Z'
platforms:
  - Linux
tags:
  - file-creation
  - permissions
verified: false
validated: true
submitted: true
---

# install-create-cookie-jar

## Command

```bash
install -m 600 /dev/null cookie.jar
```

## Description

Creates an empty file named cookie.jar with strict permissions (0600, owner read/write only) by installing from /dev/null as the source. Used to set up secure storage for testing permission vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m 600` | Sets the file mode to 0600 (rw-------) | Yes |
| `/dev/null` | Source for empty content | Yes |
| `cookie.jar` | Destination filename | Yes |

## Examples

### Basic Usage

```bash
install -m 600 /dev/null cookie.jar
```

### Advanced Usage

```bash
install -m 600 -o owner -g group /dev/null securefile.txt
```

## Expected Output

No stdout output; file created with permissions -rw------- and size 0.

## Related

- [[commands/ls-check-initial-permissions]]
- [[procedures/Create-and-Verify-Secure-Cookie-Jar-File]]
