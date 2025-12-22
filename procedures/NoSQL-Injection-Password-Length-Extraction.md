---
id: 1e536e9e-1c61-4852-a2b6-cf168e68bd37
name: NoSQL-Injection-Password-Length-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.448796+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
  - >-
    [[techniques/Exploitation for Credential Access|T1555 - Credentials from
    Password Stores]]
sub_techniques:
  - '[[techniques/Brute Force/Password Guessing|T1110.001 - Password Guessing]]'
tags:
  - '[[tags/Exploit]]'
  - '[[tags/Extract length information]]'
  - '[[tags/NoSQL Injection]]'
  - '[[tags/Brute Force]]'
  - '[[tags/MongoDB]]'
commands:
  - '[[commands/curl-nosql-injection-length-test]]'
platforms:
  - Web
tools: []
validated: true
---

# NoSQL-Injection-Password-Length-Extraction

## Summary

This procedure demonstrates how to exploit a NoSQL injection vulnerability in a web application's login form to extract the length of a target user's password. By injecting MongoDB query operators like $ne (not equal) and $regex into the username and password fields, an attacker can perform a length oracle attack, determining the exact character count of the password to optimize subsequent brute-force attempts. This is particularly effective against applications using raw user input in MongoDB queries without proper sanitization.

## Description

NoSQL databases like MongoDB are vulnerable to injection attacks when user inputs are directly concatenated into queries. In this scenario, a login endpoint processes credentials as query parameters, allowing injection of operators to manipulate the query logic. For example, setting username[$ne] to a known value bypasses equality checks, while password[$regex] uses regular expressions to test password lengths (e.g., .{n} matches strings of length n). Success is indicated by a different response (e.g., error vs. success) when the length matches. This technique reveals password metadata without full disclosure, aiding in targeted brute-forcing. It targets web applications on platforms like Node.js with Mongoose ORM, assuming the attacker has network access to the login endpoint.

## Requirements

1. Network access to the vulnerable web application's login endpoint (e.g., HTTP POST to /login).
2. Knowledge of a valid username (e.g., 'admin' or 'toto') but unknown password.
3. Tools like curl for sending HTTP requests or a proxy like Burp Suite for interception and modification.
4. Basic understanding of MongoDB query syntax and regex patterns.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, rejecting inputs containing special characters like $, [, or ].
- Use parameterized queries or MongoDB's query builders (e.g., Mongoose sanitize) to prevent operator injection.
- Enable web application firewall (WAF) rules to block regex patterns or query operators in login payloads.
- Monitor application logs for anomalous login attempts, such as repeated failures with varying regex lengths, and implement rate limiting on authentication endpoints.
- Conduct regular security audits and use tools like NoSQLMap for vulnerability scanning.

## Objectives

1. Identify the exact length of the target user's password through differential responses to injected queries.
2. Use the extracted length to narrow down brute-force wordlists (e.g., limit to passwords of that length).
3. Achieve credential access optimization without triggering full brute-force detection.

## Instructions

### Step 1: Identify the Vulnerable Endpoint and Test Basic Injection

**Context**: Confirm the login endpoint accepts POST requests with username and password parameters and is vulnerable to NoSQL injection. Start with a basic payload to bypass authentication or elicit errors that reveal query behavior.

**Command** ([[commands/curl-nosql-injection-length-test]]):
```bash
curl -X POST http://target.com/login -d "username[$ne]=toto&password[$ne]=null" -v
```

> This sends a payload that always evaluates to true ($ne means 'not equal'), potentially bypassing login if vulnerable. Observe the response: a successful login or different error message indicates injection success. If it returns a generic error, the app may be sanitized; otherwise, proceed to length testing.

### Step 2: Inject Regex Payload to Probe Password Length

**Context**: Use the NoSQL injection payload to test password lengths incrementally. The regex .{n} matches any string of exactly n characters. Iterate n from 1 to a reasonable maximum (e.g., 20). A matching length typically returns a 'valid' response or different error, while non-matching returns 'invalid credentials'.

**Code** ([[codes/NoSQL-Injection-Regex-Payload-for-Password-Length]]):
Embed the payload in requests as follows, replacing {n} with test values.

**Command** ([[commands/curl-nosql-injection-length-test]]):
```bash
curl -X POST http://target.com/login -d "username[$ne]=toto&password[$regex]=.{5}" -v
```

> Submit payloads for each length (e.g., .{1}, .{2}, etc.). Compare responses: a length match might show a successful auth attempt or specific error (e.g., 'password too short'). Non-matches show standard failure. Automate with a script looping over lengths if manual testing is inefficient. Expected: Identify the exact n where response changes, confirming password length.

### Step 3: Verify and Optimize Brute Force

**Context**: Once the length is known (e.g., 8 characters), generate a targeted wordlist and perform brute force. This step uses the length info to filter candidates, reducing attempts and detection risk.

> Create a wordlist with tools like crunch: `crunch 8 8 -t @@@@@@@@ -o passwords.txt` (for 8 chars). Then brute force using the same endpoint, but limit to length 8. Monitor for account lockouts. Success: Valid credentials obtained.
