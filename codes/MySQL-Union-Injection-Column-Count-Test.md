---
id: 6fc7302d-0130-4750-b9f2-a8efa82f0ea5
name: MySQL-Union-Injection-Column-Count-Test
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.392523+00:00'
updated_at: '2023-04-10T20:22:52.412674+00:00'
platforms:
  - Web
tags:
  - sql-injection
  - union-based
validated: true
---

# MySQL-Union-Injection-Column-Count-Test

## Code

```sql
?id=(1)and(SELECT * from db.users)=(1)
-- Operand should contain 4 column(s)
```

## Description

This SQL payload tests the number of columns in the vulnerable query by attempting a subquery comparison that fails with an operand mismatch error, revealing the expected column count (e.g., 4) for crafting proper UNION statements.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| db | Database name | users |
| users | Target table | users |
| (1) | Placeholder subquery; increment to match columns | (1,2,3,4) |

## Usage

Inject into a vulnerable GET parameter (e.g., http://target.com/page?id=...) using a proxy like Burp Suite. Adjust the right-side SELECT to add columns until the error disappears, confirming the match. Use in error-based SQLi scenarios where union compatibility is needed.

## Detection

- WAF rules triggering on subquery patterns like SELECT * FROM ... = (SELECT ...).
- Database logs showing unbalanced operand errors.
- Application logs with SQL syntax errors from mismatched columns.

## Related

- [[procedures/MySQL-Union-Based-Injection-to-Extract-Column-Names]]
