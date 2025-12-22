---
id: 95515cf0-3b0c-46f4-a884-ae832c53f9ee
name: MSSQL-Error-Based-Injection-to-Extract-Version
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.823684+00:00'
updated_at: '2023-04-10T20:22:41.288868+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
  - >-
    [[techniques/Exploitation-of-Remote-Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/mssql]]'
  - '[[tags/sql-injection]]'
  - '[[tags/error-based]]'
  - '[[tags/version-extraction]]'
commands:
  - '[[commands/convert-int-@@version]]'
  - '[[commands/cast-int-@@version]]'
  - '[[commands/convert-string-@@version]]'
  - '[[commands/cast-string-@@version]]'
platforms:
  - Windows
  - MSSQL
tools: []
validated: true
---

# MSSQL-Error-Based-Injection-to-Extract-Version

## Summary

This procedure demonstrates an error-based SQL injection technique in Microsoft SQL Server (MSSQL) to extract the database server version by forcing conversion errors using CONVERT or CAST functions on the @@version system variable. By injecting payloads that attempt to convert the version string to an integer, the resulting error message leaks the full version details, aiding in vulnerability identification and attack planning.

## Description

Error-based SQL injection exploits vulnerabilities in web applications that fail to sanitize user inputs, allowing attackers to inject SQL code that triggers database errors containing sensitive information. In MSSQL, the @@version variable holds the server's version string (e.g., "Microsoft SQL Server 2019 (RTM) - 15.0.2000.5"). Attempting to convert this string to an integer using CONVERT(int, @@version) or CAST(@@version AS int) produces an error like "Error converting data type varchar to int," but the full error context reveals the version. This technique is useful during reconnaissance to determine the exact SQL Server version for targeted exploitation. It requires a vulnerable parameter (e.g., in a login form or search field) that influences a SELECT query. The attack works on MSSQL instances exposed via web applications, typically on Windows servers.

## Requirements

1. Access to a web application with a vulnerable SQL injection point in an MSSQL-backed database.
2. Knowledge of the injection parameter (e.g., username, ID) and basic SQL syntax.
3. Tools for sending HTTP requests, such as a browser, curl, or Burp Suite.
4. The target must return error messages to the client (not suppressed by the application).

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block injection attempts.
- Suppress detailed database error messages in production environments, logging them server-side instead.
- Regularly patch SQL Server to mitigate known vulnerabilities associated with specific versions.
- Monitor application logs for unusual SQL errors or conversion failures.

## Objectives

1. Extract the exact version of the MSSQL server to identify potential vulnerabilities.
2. Confirm the presence of an error-based SQL injection vulnerability.
3. Gather intelligence for subsequent attacks, such as exploiting version-specific flaws.

## Instructions

### Step 1: Identify the Injection Point and Test Basic Error Trigger

**Context**: Locate a vulnerable parameter in the web application (e.g., a search box or login field) and confirm SQL injection by triggering a basic error. This step verifies the endpoint echoes database errors.

Append a single quote (') to the input and submit. If an SQL error appears, proceed.

**Expected Output**: A generic SQL syntax error, such as "Unclosed quotation mark after the character string." This confirms the injection point is active and errors are visible.

### Step 2: Inject Payload to Force Version Conversion Error

**Context**: Use the CONVERT or CAST functions to attempt converting @@version to an integer, which will fail and leak the version in the error message. Choose the appropriate payload based on whether the parameter expects integer or string input.

For integer-expecting parameters, use [[commands/convert-int-@@version]] or [[commands/cast-int-@@version]] by appending it to the query via the injection point (e.g., ' OR 1=1; convert(int,@@version)--).

```sql
convert(int,@@version)
```

Alternatively, use [[commands/cast-int-@@version]]:

```sql
cast((SELECT @@version) as int)
```

For string-expecting parameters, concatenate the payload using [[commands/convert-string-@@version]] or [[commands/cast-string-@@version]] (e.g., ' + (SELECT convert(int,@@version)) + ').

```sql
' + convert(int,@@version) + '
```

Or:

```sql
' + cast((SELECT @@version) as int) + '
```

Reference the full payload variants in [[codes/MSSQL-@@version-Conversion-for-Error-Based-Extraction]].

**Expected Output**: An error message like "Msg 245, Level 16, State 1, Line 1 Conversion failed when converting the varchar value 'Microsoft SQL Server 2019 (RTM) - 15.0.2000.5 (X64)' to data type int." The version string is embedded in the error.

### Step 3: Analyze the Error and Verify Extraction

**Context**: Parse the returned error message to extract the version details. If the error is suppressed, try variations or use a proxy to inspect responses.

Review the HTTP response body or console output for the leaked version. Note the edition (e.g., RTM, SP1) and build number for vulnerability research.

**Expected Output**: Clear version information, such as "Microsoft SQL Server 2019 (RTM) - 15.0.2000.5," confirming successful extraction.

### Step 4: Document and Plan Next Steps

**Context**: Record the version for further reconnaissance or exploitation. Cross-reference with CVE databases for known issues.

No specific command; manually note the output and research exploits (e.g., via search engines or tools like Metasploit).

**Expected Output**: Version documented, with identified potential vulnerabilities (e.g., if version < 2016, check for outdated patches).
