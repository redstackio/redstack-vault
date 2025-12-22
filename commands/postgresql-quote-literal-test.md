---
type: command
executor: sql
data: quote_literal(42.5)=quote_literal(42.5)
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Database
tags:
  - sql-injection
  - fingerprinting
verified: true
validated: true
---

# postgresql-quote-literal-test

## Command

```sql
quote_literal(42.5)=quote_literal(42.5)
```

## Description

Uses PostgreSQL's quote_literal function for string quoting test.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND quote_literal(42.5)=quote_literal(42.5) --`

## Expected Output

True if PostgreSQL.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/postgresql-ts-config-test]]
