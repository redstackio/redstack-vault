---
id: e0d271b6-8f59-4172-bac1-c66992976341
name: MySQL-Time-Based-Blind-Injection-Using-Conditionals
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.723433+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial-Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/MySQL-Injection]]'
  - '[[tags/MySQL-Time-Based]]'
  - '[[tags/Using-Conditional-Statements]]'
  - sqli
  - blind-injection
commands:
  - '[[commands/curl-mysql-time-based-injection]]'
platforms:
  - Web
  - MySQL
tools:
  - '[[tools/sqlmap]]'
validated: true
---

# MySQL-Time-Based-Blind-Injection-Using-Conditionals

## Summary

This procedure exploits vulnerable web applications interacting with MySQL databases by injecting SQL payloads that use conditional statements and time-delay functions like BENCHMARK and SLEEP. In time-based blind SQL injection, no direct data is returned, but attackers infer information from response delays caused by true/false conditions, enabling extraction of sensitive data such as database users, versions, and contents.

## Description

Time-based blind SQL injection targets applications where error messages or data output are suppressed, making traditional SQLi ineffective. By crafting payloads with MySQL's IF function combined with delay functions, attackers test conditions (e.g., character values in a database field) and measure response times to determine true or false outcomes. This is useful against parameterized queries that fail union-based attacks but allow conditional execution. The technique assumes a vulnerable GET or POST parameter (e.g., 'id') in a web endpoint. Success depends on the application's response time consistency and lack of rate limiting. This procedure focuses on manual injection for learning; automated tools like SQLMap can scale it.

## Requirements

1. Network access to the vulnerable web application (e.g., HTTP/HTTPS endpoint).
2. Knowledge of the injection point (e.g., a URL parameter like ?id=1).
3. Tools for sending HTTP requests (e.g., curl) and measuring response times.
4. Optional: SQLMap for automation.
5. Basic understanding of MySQL functions (IF, ASCII, SUBSTRING, BENCHMARK, SLEEP).

## Defense

- Implement prepared statements and parameterized queries to separate code from user input.
- Use web application firewalls (WAFs) to detect and block SQL injection patterns, including time-delay functions.
- Enable database logging for anomalous queries and monitor response times for delays.
- Sanitize inputs and output-encode database responses.
- Regularly audit and update web frameworks to patch injection vulnerabilities.

## Objectives

1. Confirm the presence of a time-based blind SQL injection vulnerability.
2. Extract database information (e.g., current user, version) using conditional delays.
3. Infer sensitive data character-by-character to reconstruct full values.
4. Demonstrate data exfiltration without direct output from the application.

## Instructions

### Step 1: Identify and Test the Injection Point

**Context**: Locate a parameter vulnerable to SQL injection and verify basic injection by appending a comment to alter the query without errors. This confirms the endpoint processes unsanitized input.

**Command** ([[commands/curl-mysql-time-based-injection]]):
```bash
curl -s -w "%{time_total}s\n" "http://target.com/page?id=1'--" | head -n 1
```

> This sends a request with a SQL comment (-- ) to close the statement. Measure the total response time with -w. If the page loads normally (no errors) and time is consistent (e.g., <1s), the parameter is likely injectable. Expected output: The page content followed by a timestamp like 0.5s. If times vary significantly or errors occur, the point may not be vulnerable.

### Step 2: Deploy Time-Based Payloads to Test Conditions

**Context**: Use conditional statements to create delays based on true/false outcomes. For example, test if the first character of the database user has an ASCII value >=100. A delay indicates the condition's result, allowing boolean inference.

Reference the payloads in [[codes/MySQL-Time-Based-Blind-Injection-Payloads]]. Inject one via curl:

**Command** ([[commands/curl-mysql-time-based-injection]]):
```bash
curl -s -w "%{time_total}s\n" "http://target.com/page?id=1 AND IF(ASCII(SUBSTRING((SELECT USER()),1,1)))>=100,1, SLEEP(3)) --" | head -n 1
```

> Replace the URL with your target. Run multiple times (5-10) to average response times. If average >3s, the condition is false (SLEEP triggers); if ~0.5s, true (no delay). Use BENCHMARK for CPU-intensive delays if SLEEP is blocked. Expected output: Page content with timestamp; compare times to infer truth value.

### Step 3: Extract Data Character-by-Character

**Context**: Systematically guess data by binary search on ASCII values (e.g., 32-126 printable chars). Start with database user length, then each position. This step builds on Step 2, iterating conditions like ASCII(SUBSTRING(... ,pos,1)) > mid_value.

Adapt the payload from [[codes/MySQL-Time-Based-Blind-Injection-Payloads]] for extraction. Example for user length:

**Command** ([[commands/curl-mysql-time-based-injection]]):
```bash
curl -s -w "%{time_total}s\n" "http://target.com/page?id=1 AND IF(LENGTH((SELECT USER()))>$LEN, SLEEP(3),1)--" | head -n 1
```

> Iterate $LEN from 1 upward until delay confirms length. For characters, binary search: Test >64, then narrow (e.g., >96). Expected output: Timestamps allowing reconstruction (e.g., after 7 queries per char, infer 'r' as ASCII 114). Automate with scripts if manual is tedious.

### Step 4: Verify and Escalate Extraction

**Context**: Once basic info (user, version) is extracted, target tables/columns (e.g., via information_schema). Confirm MySQL version for compatible functions.

Use version check payload:

**Command** ([[commands/curl-mysql-time-based-injection]]):
```bash
curl -s -w "%{time_total}s\n" "http://target.com/page?id=1 OR IF(MID(@@version,1,1)='5',SLEEP(3),1)--" | head -n 1
```

> Delay confirms version starts with '5'. Expected output: Timestamp >3s for match. Proceed to dump schemas if successful, chaining conditions for table names.
