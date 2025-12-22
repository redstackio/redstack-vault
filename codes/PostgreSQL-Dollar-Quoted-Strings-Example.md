---
id: 32307f50-d72a-454a-961b-db6daa022e2a
name: PostgreSQL-Dollar-Quoted-Strings-Example
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.076789+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - sql-injection
  - quoting
  - strings
validated: true
---

# PostgreSQL-Dollar-Quoted-Strings-Example

## Code

```sql
SELECT $$This is a string$$
SELECT $TAG$This is another string$TAG$
```

## Description

This SQL code snippet illustrates PostgreSQL's dollar-quoted string literals, which allow embedding complex strings (including quotes and special chars) without escaping. The $$ delimiter is anonymous, while $TAG$ uses a custom identifier. This is valuable in SQL injections to encapsulate shell commands or payloads without quote conflicts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; strings are literals. Custom tags like TAG can be any non-$ sequence | N/A |

## Usage

Use in injections to include commands directly, e.g., COPY (SELECT $$ls -la$$) TO PROGRAM 'echo done'. Ideal for payloads with internal quotes or when single/double quotes are filtered. Test in union selects to confirm string integrity.

## Detection

- Logs revealing dollar-quoted strings in SELECT or COPY statements, especially with unusual tags.
- Application responses echoing dollar-delimited content.
- IDS signatures for $$ or $[^$]*$ patterns in SQL traffic.

## Related

- [[procedures/PostgreSQL-Command-Execution-via-Injection]]
