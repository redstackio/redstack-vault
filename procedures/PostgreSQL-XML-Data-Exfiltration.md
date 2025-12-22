---
id: 2264e573-2557-4b4b-868d-0ff34c9c53f1
name: PostgreSQL-XML-Data-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.772926+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Data-from-Information-Repositories|T1213 - Data from
    Information Repositories]]
  - >-
    [[techniques/Exfiltration-Over-Alternative-Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques: []
tags:
  - '[[tags/PostgreSQL-injection]]'
  - '[[tags/XML-exfiltration]]'
  - '[[tags/database-exfiltration]]'
commands:
  - '[[commands/postgresql-query-to-xml-pg-user]]'
  - '[[commands/postgresql-query-to-xml-custom]]'
  - '[[commands/postgresql-select-with-limit]]'
  - '[[commands/postgresql-database-to-xml]]'
  - '[[commands/postgresql-database-to-xml-schema]]'
platforms:
  - Linux
  - Databases
tools: []
validated: true
---

# PostgreSQL-XML-Data-Exfiltration

## Summary

This procedure demonstrates how to exfiltrate sensitive data from a PostgreSQL database using built-in XML export functions like query_to_xml and database_to_xml. By injecting these SQL functions through a vulnerable endpoint (e.g., SQL injection), an attacker can format query results as XML for easier extraction and transmission, bypassing some data size limitations or detection mechanisms.

## Description

In scenarios where an attacker has gained SQL injection access to a PostgreSQL database, this technique leverages native XML serialization functions to convert query results into structured XML output. This allows for the export of user data, entire database schemas, or limited result sets without relying on external tools. The XML format facilitates parsing and exfiltration over protocols like HTTP if the injection is web-based. This method is particularly useful for stealing credentials, financial data, or intellectual property while evading basic logging that might flag large binary exports. It assumes the attacker has execute privileges on the database and can capture the output from the vulnerable application.

## Requirements

1. Valid SQL injection point or direct authenticated access to the PostgreSQL database (e.g., via psql or a web app backend).
2. Knowledge of target tables (e.g., pg_user for system users) or schema details.
3. PostgreSQL version 8.3+ (when XML functions were introduced).
4. Ability to capture and parse XML output (e.g., via Burp Suite or custom scripts).

## Defense

- Use parameterized queries and prepared statements to prevent SQL injection.
- Implement database firewalls (e.g., pgBadger) to monitor and block anomalous queries involving XML functions.
- Enforce least privilege: Restrict user roles from executing system catalog queries like pg_user.
- Enable logging of all queries and audit for XML-related functions; integrate with SIEM for alerts on data export patterns.

## Objectives

1. Export sensitive database contents (e.g., user tables) as parseable XML.
2. Limit exfiltration volume to avoid detection while gathering key data.
3. Dump full database structure or content for offline analysis.

## Instructions

### Step 1: Export System User Data as XML

**Context**: Begin by querying the pg_user system catalog to extract user information and serialize it as XML. This step targets built-in PostgreSQL users and provides initial reconnaissance on database access levels. Use the query_to_xml function to format the output for easy exfiltration.

**Code** ([[codes/PostgreSQL-Query-To-XML-For-PG-User]]):

**Command** ([[commands/postgresql-query-to-xml-pg-user]]):
```sql
select query_to_xml('select * from pg_user', true, true, '');
```

> This SQL command executes a subquery on pg_user and converts the results to a single indented XML row including column names. The empty string sets the root element. Expected output is an XML structure like <row><usesuper>true</usesuper><usename>postgres</usename>...</row>, revealing user privileges and names. If successful, this confirms injection viability and provides credential hints.

### Step 2: Export Custom Query Results as XML

**Context**: For application-specific data (e.g., user tables), craft a custom query and serialize it to XML. This allows targeted exfiltration of sensitive records like customer details, filtered by conditions to focus on high-value data.

**Command** ([[commands/postgresql-query-to-xml-custom]]):
```sql
select query_to_xml('SELECT * FROM users WHERE age > 30', true, true, '');
```

> Adapt the inner query to target relevant tables (e.g., replace 'users' with actual table name). The function parameters ensure readable XML with headers. Expected output: XML rows for matching users, e.g., <row><id>1</id><name>John Doe</name><age>35</age>...</row>. This step enables selective data theft without dumping everything at once.

### Step 3: Apply Limits to Control Exfiltration Volume

**Context**: To avoid overwhelming the response or triggering size-based defenses, use LIMIT to restrict results. This is crucial for iterative exfiltration in blind injection scenarios where full dumps might fail.

**Command** ([[commands/postgresql-select-with-limit]]):
```sql
SELECT * FROM customers LIMIT 5 OFFSET 0;
```

> Combine with XML export in a full query like select query_to_xml('SELECT * FROM customers LIMIT 5', true, true, ''). The OFFSET allows pagination. Expected output: Limited rows in tabular or XML format, e.g., first 5 customer records. Success confirms controlled data retrieval; iterate OFFSET for more.

### Step 4: Dump Entire Database to XML

**Context**: For comprehensive exfiltration, use database_to_xml to serialize the full database content, including tables and data. This is a high-impact step for stealing all accessible information but may generate large output.

**Code** ([[codes/PostgreSQL-Database-To-XML-And-Schema]]):

**Command** ([[commands/postgresql-database-to-xml]]):
```sql
select database_to_xml(true, true, '');
```

> The 'true' flags include schema and column names; empty string for root. Expected output: A large XML document with <table> elements containing rows, e.g., full dump of all tables. Use in injection to capture everything; parse offline for analysis.

### Step 5: Dump Database Schema to XML

**Context**: Extract the database structure (tables, columns) separately for mapping relationships before full data dumps. This aids in identifying high-value targets.

**Command** ([[commands/postgresql-database-to-xml-schema]]):
```sql
select database_to_xmlschema(true, true, '');
```

> Similar to the full dump but focuses on schema. Expected output: XML schema definition, e.g., <schema><table name="users"><column name="id" type="integer"/></table>...</schema>. This reveals table layouts without data volume.
