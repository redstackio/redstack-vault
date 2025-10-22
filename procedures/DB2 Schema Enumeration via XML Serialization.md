---
id: 6d6d6293-caea-4f9b-9c99-4b6e4082b769
name: DB2 Schema Enumeration via XML Serialization
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.122870+00:00'
updated_at: '2023-04-10T20:22:05.830477+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[Serialize to XML (for error based)]]'
commands:
- '[[Select all table schemas in one xml-formatted string]]'
- '[[Select all table schemas in one xml-formatted string (v8)]]'
- '[[Select all table schemas in one xml-formatted string without repeated elements]]'
---

# DB2 Schema Enumeration via XML Serialization

## Summary

DB2 Schema Enumeration via XML Serialization is a technique used to extract metadata about tables, columns, and other database objects. This technique is useful for understanding the structure of a database and identifying potential targets for further exploitation. The technique involves injecting

## Description

# Description

DB2 Schema Enumeration via XML Serialization is a technique used to extract metadata about tables, columns, and other database objects. This technique is useful for understanding the structure of a database and identifying potential targets for further exploitation. The technique involves injecting specially crafted SQL queries into the target application in order to serialize the database schema to an XML format. This XML is then extracted and parsed to reveal the necessary information. 

From an offensive perspective, this technique can be used to identify sensitive information such as passwords, credit card numbers, and other confidential data. From a defensive perspective, understanding how attackers can use this technique can help organizations better secure their applications and databases.

## Requirements

1. Access to the target application

1. Knowledge of SQL injection techniques

1. Ability to serialize database schema to XML format

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use parameterized queries instead of dynamic SQL to prevent SQL injection attacks

1. Monitor database logs for suspicious activity

## Objectives

1. Identify the database schema of a target application

1. Identify potential targets for further exploitation

# Instructions

1. To retrieve all table schemas in XML format, run any of the following SQL commands:

**Code**: [[select xmlagg(xmlrow(table_schema)) from sysibm.ta]]

> The first SQL command retrieves all table schemas in one XML-formatted string. The second command does the same but removes any repeated elements. The third command retrieves all table schemas in one XML-formatted string, but is only available in version 8 of the software. You may need to cast the result as varchar(500) to display the output.

**Command** ([[Select all table schemas in one xml-formatted string]]):

```bash
select xmlagg(xmlrow(table_schema)) from sysibm.tables -- returns all in one xml-formatted string
```

**Command** ([[Select all table schemas in one xml-formatted string without repeated elements]]):

```bash
select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables) -- Same but without repeated elements
```

**Command** ([[Select all table schemas in one xml-formatted string (v8)]]):

```bash
select xml2clob(xmelement(name t, table_schema)) from sysibm.tables -- returns all in one xml-formatted string (v8). May need CAST(xml2clob(… AS varchar(500)) to display the result.
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Select all table schemas in one xml-formatted string]]
- [[Select all table schemas in one xml-formatted string (v8)]]
- [[Select all table schemas in one xml-formatted string without repeated elements]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[Serialize to XML (for error based)]]
