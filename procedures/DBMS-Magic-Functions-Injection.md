---
id: f6678452-8492-432f-b89d-9dfea07d5cb2
name: DBMS-Magic-Functions-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.373100+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/DBMS Magic functions]]'
  - '[[tags/Hibernate Query Language Injection]]'
  - sql-injection
  - database-exploitation
commands: []
platforms:
  - Database
  - PostgreSQL
  - Oracle
tools: []
validated: true
---

# DBMS-Magic-Functions-Injection

## Summary

DBMS Magic Functions Injection exploits vulnerabilities in applications using Hibernate Query Language (HQL) by injecting database-specific functions to execute arbitrary SQL commands on the backend database. This technique bypasses HQL's abstraction layer to perform operations like data retrieval, version checking, or conditional logic, leading to data exfiltration, privilege escalation, or full system compromise.

## Description

In applications built with frameworks like Hibernate, HQL queries are translated to native SQL, but if user input is not properly sanitized, attackers can inject DBMS-specific 'magic' functions (proprietary to databases like PostgreSQL or Oracle) directly into the query. These functions enable execution of arbitrary SQL, such as querying system information or performing blind injections via conditional checks. The attack targets web applications interacting with databases, requiring knowledge of the underlying DBMS. Success depends on the injection point (e.g., search fields, login forms) and can chain with other exploits for lateral movement. This procedure covers PostgreSQL and Oracle examples, focusing on XML generation and array/condition manipulation for injection payloads.

## Requirements

1. Access to a vulnerable web application endpoint that accepts user input in HQL queries (e.g., via HTTP POST/GET parameters).
2. Knowledge of the target DBMS (PostgreSQL or Oracle) and its magic functions.
3. Tools for testing injections, such as a browser, Burp Suite, or SQLMap (though manual injection is detailed here).
4. Network access to the application and database server.

## Defense

- Use parameterized queries and prepared statements in HQL to prevent direct SQL concatenation.
- Implement strict input validation, sanitization, and whitelisting to block DBMS-specific functions.
- Regularly patch the DBMS and application framework (e.g., Hibernate) to address known injection flaws.
- Enable database logging and monitoring for anomalous queries, XML outputs, or unexpected function calls.
- Apply web application firewalls (WAFs) with rules tuned for SQL/HQL injection patterns.

## Objectives

1. Execute arbitrary SQL commands via injected DBMS magic functions to bypass HQL restrictions.
2. Retrieve sensitive database information, such as user details, versions, or system metadata.
3. Perform conditional checks for blind injection to extract data bit-by-bit or escalate privileges.

## Instructions

### Step 1: Inject PostgreSQL Query-to-XML Function

**Context**: Use the query_to_xml function to convert arbitrary SQL results into XML, allowing execution of unauthorized queries in an HQL context. This is useful for data exfiltration where direct SELECTs are filtered.

**Code** ([[codes/PostgreSQL-Query-To-XML-Injection]]):

```sql
query_to_xml('Arbitrary SQL')
```

> Inject this payload into an HQL parameter (e.g., a search field). The function executes the inner SQL and returns results as XML. Verify by checking for XML-formatted output in responses or database logs. If successful, the arbitrary SQL runs, potentially dumping tables or system info.

### Step 2: Use PostgreSQL Array Upper with XPath for Length Check

**Context**: Combine array_upper, xpath, and query_to_xml to perform a length-based blind injection check. This determines if a condition (e.g., a SQL truth test) holds by measuring the array length of XML nodes, useful when no direct output is visible.

**Code** ([[codes/PostgreSQL-Array-Upper-XPath-Length-Check]]):

```sql
array_upper(xpath(query_to_xml('select 1 where 1337>1'), '//row'), 1)
```

> Replace the condition (1337>1) with your test (e.g., substring comparison for data extraction). The xpath extracts rows from the XML, and array_upper returns the count (1 if true, null/0 if false). Observe response differences (e.g., error vs. normal) to infer results. This step confirms injection viability without visible output.

### Step 3: Inject Oracle DBMS_XMLGEN GetXML Function

**Context**: In Oracle-backed HQL apps, use DBMS_XMLGEN.getxml to generate XML from arbitrary SQL, similar to PostgreSQL's query_to_xml. This enables executing and exporting query results in XML format for further manipulation or exfiltration.

**Code** ([[codes/Oracle-DBMS-XMLGEN-GetXML-Injection]]):

```sql
DBMS_XMLGEN.getxml('SQL')
```

> Inject into HQL input fields. The function takes a SQL query as input and outputs XML. Customize with options for formatting or namespaces if needed. Success is indicated by XML in the response or logs, confirming arbitrary SQL execution.

### Step 4: Perform Oracle NVL Condition Check for Blind Injection

**Context**: Use NVL and DBMS_XMLGEN to create a boolean expression for blind SQL injection, testing conditions without direct output. This is ideal for extracting data via true/false responses (e.g., time delays or content length).

**Code** ([[codes/Oracle-NVL-Condition-Check-Injection]]):

```oracle sql
NVL(TO_CHAR(DBMS_XMLGEN.getxml('select 1 where 1337>1')),'1')!='1'
```

> Substitute the condition (1337>1) with your payload (e.g., 'password like "a%"'). If true, getxml returns '1', NVL/TO_CHAR makes it '1', and != '1' evaluates false (or alters response). If false, null becomes '1' via NVL, making != true. Analyze response changes to extract info bit-by-bit.
