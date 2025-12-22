---
id: f828c0e8-6365-4a8f-a630-6f6ea9aab440
name: select-from-user-java-policy
type: command
executor: sql
data: select * from user_java_policy
output: null
created_at: '2023-04-06T03:56:35.305016+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - oracle
  - java
  - policy
verified: true
validated: true
---

# select-from-user-java-policy

## Command

```sql
select * from user_java_policy;
```

## Description

Queries the USER_JAVA_POLICY view to list Java permissions specific to the current database user, aiding in self-assessment for execution capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard SELECT query | No |

## Examples

### Basic Usage

```sql
select * from user_java_policy;
```

### Advanced Usage

Order by action:

```sql
select * from user_java_policy order by action;
```

## Expected Output

Table similar to DBA view but user-scoped. Example:

| DB_USER | TYPE | NAME | ACTION | GRANT_OPTION |
|---------|------|------|--------|--------------|
| Current | java.lang.RuntimePermission | writeFileDescriptor | - | No |

## Related

- [[procedures/Oracle-SQL-and-Java-Command-Execution]]
