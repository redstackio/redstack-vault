---
id: 6e4ae063-f82a-4549-b5db-c82aaaa23217
name: mssql-view-permissions-for-object
type: command
executor: sql
data: >-
  SELECT * FROM fn_my_permissions('Sales.vIndividualCustomer', 'OBJECT') ORDER
  BY subentity_name, permission_name;
output: null
created_at: '2023-04-06T03:56:34.157896+00:00'
updated_at: '2023-04-10T20:22:47.331484+00:00'
platforms:
  - MSSQL
tags:
  - discovery
  - permissions
verified: true
validated: true
---

# mssql-view-permissions-for-object

## Command

```sql
SELECT * FROM fn_my_permissions('Sales.vIndividualCustomer', 'OBJECT') ORDER BY subentity_name, permission_name;
```

## Description

This SQL command checks effective permissions on a specific database object (e.g., a view like Sales.vIndividualCustomer) in MSSQL, ordered by subentity and permission name. Adapt for any object to evaluate targeted access during database reconnaissance via SQL injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'Sales.vIndividualCustomer' | Name of the target object (view, table, etc.) – replace with actual object | Yes |
| 'OBJECT' | Specifies object-level scope | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM fn_my_permissions('Sales.vIndividualCustomer', 'OBJECT') ORDER BY subentity_name, permission_name;
```

### Advanced Usage

For a table:

```sql
SELECT * FROM fn_my_permissions('dbo.Users', 'OBJECT') ORDER BY subentity_name, permission_name;
```

## Expected Output

Ordered table with permission_name (e.g., 'SELECT'), subentity_name ('Sales.vIndividualCustomer'), and permission_state. Example:

| entity_name | subentity_name | permission_name | permission_state | class_desc |
|-------------|----------------|-----------------|------------------|------------|
| Sales.vIndividualCustomer | NULL | SELECT | GRANT | OBJECT |

Empty results indicate no permissions on the object.

## Related

- [[procedures/mssql-injection-list-permissions]]
- [[commands/mssql-check-database-permissions]]
