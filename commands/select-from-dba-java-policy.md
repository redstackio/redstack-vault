---
id: 739195dc-0299-4231-be5c-c0bc6472861d
name: select-from-dba-java-policy
type: command
executor: sql
data: select * from dba_java_policy
output: null
created_at: '2023-04-06T03:56:35.304955+00:00'
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

# select-from-dba-java-policy

## Command

```sql
select * from dba_java_policy;
```

## Description

Queries the DBA_JAVA_POLICY view to retrieve all Java permission policies across the database, useful for reconnaissance of exploitable configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard SELECT query | No |

## Examples

### Basic Usage

```sql
select * from dba_java_policy;
```

### Advanced Usage

Filter by grantee:

```sql
select * from dba_java_policy where grantee = 'SCOTT';
```

## Expected Output

Table with columns: DB_USER, TYPE, NAME, ACTION, GRANT_OPTION, etc. Example:

| DB_USER | TYPE | NAME | ACTION | GRANT_OPTION |
|---------|------|------|--------|--------------|
| SCOTT | java.io.FilePermission | <<ALL FILES>> | execute | No |

## Related

- [[procedures/Oracle-SQL-and-Java-Command-Execution]]
