---
id: b9909e88-014b-4e75-aba1-bb846d162b6f
name: Privilege Escalation Using LDAP Injection
type: procedure
verified: true
submitted: true
created_at: '2020-08-16T19:14:49.521323+00:00'
updated_at: '2023-05-26T01:24:54.940284+00:00'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - LDAP Injection
  - OWASP
  - OWASP Top 10
  - Privilege Escalation
  - Web Applications
commands:
  - '[[commands/curl-fetch-low-security-documents]]'
  - '[[commands/curl-ldap-injection-for-privilege-escalation]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Privilege Escalation Using LDAP Injection

## Summary

This procedure demonstrates how to exploit LDAP injection vulnerabilities in web applications to escalate privileges by modifying LDAP queries through user input or URL parameters, allowing unauthorized access to higher-security resources such as documents intended for privileged users.

## Description

LDAP injection occurs when an application constructs LDAP queries using unsanitized user input, enabling attackers to alter the query logic. In this scenario, a web application uses URL parameters to build an LDAP filter for retrieving documents based on security levels. A low-privilege user can normally only access low-security documents via a query like *(&(directory=documents)(security_level=low))*. By injecting payload into the security_level parameter, such as 'low*)(level=*)*', the attacker closes the intended filter and appends a broader condition (level=*), effectively retrieving medium and high-security documents. This technique requires access to a vulnerable endpoint and the ability to manipulate requests, typically via a browser or proxy tool. It targets web applications integrated with LDAP directories for authentication and authorization.

## Requirements

1. Network access to the target web application.
2. Valid low-privilege credentials or session to the application.
3. Tools for request manipulation, such as [[tools/Burp-Suite]] or curl.
4. Knowledge of the application's LDAP query structure, often identifiable through error messages or response analysis.

## Defense

Defensive measures and detection strategies:

- Use parameterized LDAP queries or LDAP filters to prevent injection by treating input as literal data rather than executable code.
- Implement input validation and sanitization to escape special LDAP characters like '(', ')', '*', '&'.
- Enable LDAP query logging on the directory server to monitor for anomalous filters or excessive access attempts.
- Apply least privilege principles to LDAP binds, ensuring application accounts have minimal permissions.
- Use web application firewalls (WAFs) with rules to detect LDAP injection patterns in requests.

## Objectives

1. Identify vulnerable input points in LDAP-dependent web endpoints.
2. Inject payloads to bypass security level restrictions in LDAP queries.
3. Gain unauthorized access to privileged resources like high-security documents.
4. Verify escalation by observing expanded data retrieval.

## Instructions

### Step 1: Access Low-Security Documents to Understand Query Structure

**Context**: First, send a legitimate request to retrieve low-security documents. This establishes the baseline LDAP query and confirms the application's behavior, typically resulting in an LDAP filter like *(&(directory=documents)(security_level=low))*. Analyze the response to identify accessible resources and infer the query construction.

**Command** ([[commands/curl-fetch-low-security-documents]]):
```bash
curl -X GET "http://target.example.com/app?directory=documents&security_level=low" -H "Cookie: session=your_session_cookie"
```

> This command fetches documents filtered by low security level. Replace the URL and session cookie with actual values. The response should list only low-security files, confirming the query is built from parameters.

### Step 2: Inject Payload to Escalate Access to Higher Security Levels

**Context**: Modify the security_level parameter to inject LDAP syntax that closes the original filter and adds a wildcard condition for all levels. The payload 'low*)(level=*)*' transforms the query to *(&(directory=documents)(security_level=low)(level=*))*, bypassing restrictions and retrieving medium and high-security documents.

**Command** ([[commands/curl-ldap-injection-for-privilege-escalation]]):
```bash
curl -X GET "http://target.example.com/app?directory=documents&security_level=low*)(level=*)*" -H "Cookie: session=your_session_cookie"
```

> Execute this to test the injection. If successful, the response will include documents from higher security levels. Use a proxy like [[tools/Burp-Suite]] for more complex manipulations if the application uses POST requests or additional headers. Verify no errors occur and observe expanded file listings.

### Step 3: Verify Privilege Escalation and Document Unauthorized Access

**Context**: Compare the responses from Steps 1 and 2 to confirm escalation. Download or view the newly accessible documents to assess the impact, such as sensitive data exposure.

**Instructions**: Manually inspect the JSON/XML/HTML response for additional files. If using Burp Suite, repeat the request in Repeater to fine-tune the payload (e.g., adjust for different query formats like OR conditions with '|'). Log the accessed resources for reporting.

> Expected: Response contains medium/high-security documents not visible in the baseline query.
