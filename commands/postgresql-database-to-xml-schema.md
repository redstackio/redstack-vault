---
id: acb38378-9647-49d9-b8af-cc09ef77187d
name: postgresql-database-to-xml-schema
type: command
executor: sql
data: 'select database_to_xmlschema(true, true, '''');'
output: null
created_at: '2023-04-06T03:56:35.763915+00:00'
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

# postgresql-database-to-xml-schema

## Command

```sql
select database_to_xmlschema(true, true, '');
```

## Description

Exports the schema (structure) of the current PostgreSQL database to XML, without data, for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| true | Include table schemas | Yes |
| true | Include column details | Yes |
| '' | Output file (empty for direct) | Yes |

## Examples

### Basic Usage

```sql
select database_to_xmlschema(true, true, '');
```

### Advanced Usage

```sql
select database_to_xmlschema(true, true, 'schema.xml');
```

## Expected Output

XML schema definition:

<schema xmlns:xsi="...">
  <table name="users">
    <column name="id" type="integer"/>
    <column name="name" type="varchar"/>
    ...
  </table>
  ...
</schema>

## Related

- [[procedures/PostgreSQL-XML-Data-Exfiltration]]
- [[commands/postgresql-database-to-xml]]
