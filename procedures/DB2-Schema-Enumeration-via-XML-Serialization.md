---
id: 6d6d6293-caea-4f9b-9c99-4b6e4082b769
name: DB2-Schema-Enumeration-via-XML-Serialization
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.122870+00:00'
updated_at: '2023-04-10T20:22:05.830477+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/DB2-Cheatsheet]]'
  - '[[tags/DB2-Injection]]'
  - '[[tags/Serialize-to-XML-for-Error-Based]]'
commands:
  - '[[commands/DB2-Select-XMLAgg-XMLRow-Table-Schema-From-SysIBM-Tables]]'
  - >-
    [[commands/DB2-Select-XMLAgg-XMLRow-Distinct-Table-Schema-From-SysIBM-Tables]]
  - >-
    [[commands/DB2-Select-XML2Clob-XMLElement-Table-Schema-From-SysIBM-Tables-V8]]
platforms:
  - Linux
  - Windows
  - Cloud
tools: []
validated: true
---

# DB2-Schema-Enumeration-via-XML-Serialization

## Summary

This procedure extracts metadata about database tables, columns, and other objects in a DB2 database by injecting SQL queries that serialize the schema into XML format. It is particularly useful in SQL injection scenarios to map the database structure for further exploitation, such as identifying sensitive data locations, without relying on error-based or union-based techniques alone.

## Description

DB2 Schema Enumeration via XML Serialization leverages DB2's built-in XML functions to convert schema information from system tables like SYSIBM.TABLES into a structured XML output. This is injected through vulnerable application parameters susceptible to SQL injection. The resulting XML can be parsed to reveal table schemas, helping attackers understand the database layout for targeted data extraction or privilege escalation. This technique is effective in both on-premises and cloud-hosted DB2 environments, assuming the attacker has injection access. From a defensive standpoint, it highlights the risks of unparameterized queries in applications interacting with DB2 databases.

## Requirements

1. Valid SQL injection point in the target application (e.g., via a web form or API endpoint).
2. Knowledge of the underlying database being DB2 (confirm via error messages or fingerprinting).
3. Access to a SQL client or proxy tool like [[tools/sqlmap]] or [[tools/Burp-Suite]] to inject and capture output.
4. DB2 version compatibility (v8+ for some queries; test accordingly).

## Defense

- Implement strict input validation and prepared statements/parameterized queries to block SQL injection.
- Enable DB2 logging for anomalous queries involving XML functions like XMLAGG or XMLELEMENT.
- Use web application firewalls (WAFs) to detect and block XML serialization patterns in payloads.
- Regularly audit database schemas and restrict access to system tables like SYSIBM.TABLES.

## Objectives

1. Retrieve a complete list of table schemas in XML format for parsing and analysis.
2. Identify unique schemas without duplicates to streamline reconnaissance.
3. Adapt queries for different DB2 versions to ensure compatibility during enumeration.

## Instructions

### Step 1: Inject Basic Schema Enumeration Query

**Context**: Start with the standard query to aggregate all table schemas into a single XML string. This provides a comprehensive view but may include duplicates. Use this in an SQL injection payload, such as appending to a vulnerable SELECT statement.

**Command** ([[commands/DB2-Select-XMLAgg-XMLRow-Table-Schema-From-SysIBM-Tables]]):
```sql
select xmlagg(xmlrow(table_schema)) from sysibm.tables
```

> This command serializes all table schemas from the SYSIBM.TABLES view into an aggregated XML row. Inject it via a tool like sqlmap or Burp Suite. If the application echoes results, the output will be a concatenated XML string listing schemas.

### Step 2: Inject Query for Unique Schemas

**Context**: If duplicates appear in the output, use this variant to fetch distinct schemas only, reducing noise and improving parseability for larger databases.

**Command** ([[commands/DB2-Select-XMLAgg-XMLRow-Distinct-Table-Schema-From-SysIBM-Tables]]):
```sql
select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables)
```

> This wraps the original query in a subquery to eliminate repeats. Expected output is cleaner XML without redundant schema entries. Verify by parsing the XML to confirm uniqueness.

### Step 3: Inject Version-Specific Query for DB2 v8

**Context**: For older DB2 versions (v8), use the XML2CLOB function to handle output display issues. Cast to VARCHAR if the full result isn't shown due to length limits.

**Command** ([[commands/DB2-Select-XML2Clob-XMLElement-Table-Schema-From-SysIBM-Tables-V8]]):
```sql
select xml2clob(xmelement(name t, table_schema)) from sysibm.tables
```

> This creates an XML element and converts it to a CLOB for better handling in v8. If output is truncated, modify to: CAST(xml2clob(xmelement(name t, table_schema)) AS varchar(500)). Success is indicated by full XML retrieval without errors.
