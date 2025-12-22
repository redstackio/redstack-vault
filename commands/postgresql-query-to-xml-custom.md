---
id: 6bb51322-fa7c-4b44-8305-68af68ab6dab
name: postgresql-query-to-xml-custom
type: command
executor: sql
data: 'select query_to_xml(''SELECT * FROM users WHERE age > 30'', true, true, '''');'
output: null
created_at: '2023-04-06T03:56:35.763614+00:00'
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

# postgresql-query-to-xml-custom

## Command

```sql
select query_to_xml('SELECT * FROM users WHERE age > 30', true, true, '');
```

## Description

Serializes the results of a custom SQL query (e.g., filtered user data) into XML format using PostgreSQL's built-in function, enabling structured data exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'SELECT * FROM users WHERE age > 30' | Custom query to serialize | Yes |
| true | Include column names | Yes |
| true | Pretty-print XML | Yes |
| '' | Root element (empty default) | Yes |

## Examples

### Basic Usage

```sql
select query_to_xml('SELECT * FROM users WHERE age > 30', true, true, '');
```

### Advanced Usage

```sql
select query_to_xml('SELECT name, email FROM customers', true, true, 'customers_export');
```

## Expected Output

XML rows for matching records:

<row set="1">
  <id xsi:type="xs:integer">1</id>
  <name>John Doe</name>
  <age xsi:type="xs:integer">35</age>
  ...
</row>

## Related

- [[procedures/PostgreSQL-XML-Data-Exfiltration]]
- [[commands/postgresql-query-to-xml-pg-user]]
