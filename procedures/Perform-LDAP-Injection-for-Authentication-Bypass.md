---
id: 57b9760b-b5e7-44be-b1d1-864c1e1996ca
name: Perform-LDAP-Injection-for-Authentication-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.607030+00:00'
updated_at: '2023-04-10T20:36:28.407087+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/LDAP Injection]]'
  - '[[tags/Payloads]]'
  - ldap-injection
  - authentication-bypass
commands:
  - '[[commands/curl-post-ldap-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# Perform-LDAP-Injection-for-Authentication-Bypass

## Summary

This procedure outlines how to test for LDAP injection vulnerabilities in web applications that use LDAP for user authentication. By injecting malicious payloads into input fields like usernames, attackers can manipulate LDAP queries to bypass authentication, impersonate users, or extract sensitive directory information.

## Description

LDAP Injection exploits poorly sanitized user inputs in applications that construct LDAP queries dynamically. For example, a login form might build a query like "(&(uid=$_INPUT)(userPassword={SHA}$PASSWORD))". An attacker can inject characters like "*" or ")(|" to alter the query logic, making it always true or targeting admin accounts. This technique is common in enterprise web apps integrated with Active Directory or OpenLDAP. Success allows unauthorized access without valid credentials. Use this in controlled environments like pentests to identify and report vulnerabilities.

## Requirements

1. Network access to the target web application's login endpoint (e.g., HTTP/HTTPS).
2. Valid or test credentials for initial interaction to understand normal behavior.
3. Intercepting proxy like Burp Suite to modify requests, or command-line tools like curl for automated testing.
4. Knowledge of the application's LDAP structure (e.g., via error messages revealing attributes like 'uid' or 'cn').

## Defense

- Implement strict input validation and sanitization, escaping special LDAP characters (e.g., *, (, ), &, |, =).
- Use parameterized LDAP queries or APIs that bind parameters safely, avoiding dynamic string concatenation.
- Apply role-based access controls on LDAP binds and log all queries for anomaly detection (e.g., unexpected wildcards or boolean operators).
- Employ web application firewalls (WAFs) with LDAP-specific rules to block injection patterns.

## Objectives

1. Confirm the presence of LDAP injection vulnerabilities in authentication flows.
2. Demonstrate authentication bypass or privilege escalation by impersonating high-privilege users.
3. Extract or enumerate LDAP directory entries if the injection allows read access.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Determine which input fields (e.g., username) are directly incorporated into LDAP queries. Submit normal inputs and observe error messages for LDAP-specific details like "invalid DN" or attribute names.

No specific command required; use browser or [[commands/curl-post-ldap-payload]] with benign inputs:

```bash
curl -X POST -d "username=admin&password=test" http://target.com/login
```

> Look for LDAP errors in responses indicating dynamic query construction.

### Step 2: Test with Malicious Payloads

**Context**: Inject payloads from the [[codes/LDAP-Injection-Payloads-List]] into the vulnerable field (typically username) to alter query logic. Start with simple ones like "*" to match all users, then escalate to admin impersonation.

**Command** ([[commands/curl-post-ldap-payload]]):
```bash
curl -X POST -d "username=$_PAYLOAD&password=anything" $_TARGET_URL -v
```

> Replace $_PAYLOAD with entries from the payload list (e.g., "admin*"). The -v flag shows headers and responses. Expected signs of success: Authentication without valid password or unexpected user data in responses.

If using a proxy, intercept the POST request, modify the parameter, and forward.

Decision point: If the response changes (e.g., login succeeds or error differs), the injection worked; proceed to refine payloads. If blocked, try URL encoding (e.g., %2A for *).

### Step 3: Verify and Escalate

**Context**: Confirm bypass by accessing protected resources post-login. If successful, attempt data extraction (e.g., inject "*)(uid=*)" to enumerate users) or privilege checks.

Re-use [[commands/curl-post-ldap-payload]] with refined payloads:

```bash
curl -X POST -d "username=admin*)(|userpassword=*)&password=anything" $_TARGET_URL -c cookies.txt
```

> Use -c to save session cookies. Then test access:

```bash
curl -b cookies.txt http://target.com/admin
```

Expected: Access to admin dashboard or directory dump. If partial success, chain with other techniques like error-based extraction.
