---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploitation for Defense Evasion|T1211 - Exploitation for
    Defense Evasion]]
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/defaults-attributes]]'
  - '[[tags/ldap-injection]]'
commands:
  - '[[commands/list-common-ldap-attributes]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# LDAP-Injection-with-Default-Attributes

## Summary

This procedure demonstrates how to perform an LDAP injection attack by leveraging default LDAP attributes to manipulate queries and extract unauthorized information from an LDAP directory. By injecting specially crafted payloads into user input fields of LDAP-enabled applications, attackers can bypass authentication or enumerate all directory entries containing specific attributes, such as usernames, emails, or even passwords if exposed.

## Description

LDAP injection targets applications that use LDAP (Lightweight Directory Access Protocol) for authentication, authorization, or directory services without proper input sanitization. In a typical scenario, an application's LDAP query might look like: `(&(objectClass=person)(uid=$_USERNAME))`. An attacker injects payloads into the `$USERNAME` field to alter the query logic, such as closing the current filter and adding a new one to return all matching entries for a default attribute (e.g., `uid=*`).

This technique is effective against web applications with login forms, search functions, or user directories backed by LDAP servers like OpenLDAP or Active Directory. The attack can lead to account enumeration, data exfiltration, or even privilege escalation if sensitive attributes like `userPassword` are queryable. It requires identifying vulnerable input points, often via trial-and-error or tools like Burp Suite for request manipulation. Success depends on the application's query structure and the LDAP server's configuration.

## Requirements

1. Network access to an LDAP-enabled web application (e.g., login or search form).
2. A proxy tool like Burp Suite to intercept and modify HTTP requests containing LDAP queries.
3. Basic knowledge of LDAP syntax and common default attributes (e.g., uid, cn, userPassword).
4. Target application must concatenate user input directly into LDAP filters without parameterization or escaping.

## Defense

- Implement input validation and sanitization: Escape special LDAP characters (e.g., *, (, ), &) in user inputs.
- Use parameterized LDAP queries or LDAP filters that treat inputs as literals, not filter components.
- Apply least privilege: Restrict LDAP bind credentials to minimal read access and log all queries for anomalies.
- Monitor for injection patterns: Alert on queries with unexpected wildcards (*) or unbalanced parentheses in logs.

## Objectives

1. Manipulate LDAP queries to bypass authentication or enumerate directory entries.
2. Extract sensitive data such as user accounts, emails, or passwords using default attributes.
3. Identify the structure of the LDAP directory for further attacks like privilege escalation.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate an input field in the application (e.g., username in a login form) that is directly incorporated into an LDAP query. Use a proxy to intercept requests and observe how input is passed to the server.

Intercept the request using Burp Suite and submit a test input like `admin` to confirm the parameter (e.g., `username=admin&password=pass`).

**Expected Output**: HTTP request showing the parameter in a POST body or query string, with a response indicating LDAP processing (e.g., 401 Unauthorized for invalid creds).

### Step 2: Test for LDAP Injection Vulnerability

**Context**: Inject a basic payload to detect if the input alters the LDAP query. A common test closes the intended filter and adds a universal match to bypass authentication or return extra results.

Use the [[codes/LDAP-Injection-Universal-Payload]]:

```text
*)(ATTRIBUTE_HERE=*
```

Replace `ATTRIBUTE_HERE` with a common attribute like `uid`. Submit as username: `admin` + payload (e.g., `admin*)(uid=*`).

**Expected Output**: Successful login without valid password or a response listing multiple directory entries instead of a single user error.

### Step 3: Enumerate Entries Using Default Attributes

**Context**: Once vulnerability is confirmed, systematically inject payloads with default LDAP attributes to extract all matching entries. This reveals the directory structure and sensitive data.

First, reference common attributes using [[commands/list-common-ldap-attributes]] to output a list:

```bash
list-common-ldap-attributes
```

Then, inject payloads like `*)(userPassword=*` or `*)(mail=*` into the vulnerable field and observe responses.

**Expected Output**: Application responses containing directory data, such as a list of users, emails, or other attributes for all matching entries.

### Step 4: Analyze and Extract Data

**Context**: Parse the returned data for valuable information. If the application echoes query results (e.g., in error messages or search outputs), collect and analyze offline.

Save responses to a file and grep for patterns like emails (`mail:`) or names (`cn:`).

**Expected Output**: Structured data exportable to CSV or text, showing enumerated accounts and attributes.

**Success Indicators**:
- Query returns more entries than expected (e.g., all users instead of one).
- Sensitive attributes like `userPassword` or `mail` are exposed in responses.
- No server errors; injection alters logic without crashing the app.
