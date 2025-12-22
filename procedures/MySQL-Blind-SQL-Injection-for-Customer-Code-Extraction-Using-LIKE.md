---
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - mysql-injection
  - blind-sqli
  - like-operator
  - data-exfiltration
commands: []
platforms:
  - Web
tools: []
verified: true
validated: true
---

# MySQL-Blind-SQL-Injection-for-Customer-Code-Extraction-Using-LIKE

## Summary

This procedure exploits a blind SQL injection vulnerability in a MySQL-backed web application to extract customer codes that match specific name patterns using the LIKE operator. By injecting crafted SQL payloads into a vulnerable input field, such as a customer search form, the attacker infers data from response differences in boolean-based or time-based blind techniques, enabling gradual extraction of sensitive database information without direct query output visibility.

## Description

Blind SQL injection occurs when an application does not return database query results directly but allows inference through side-channel effects, such as response time delays or conditional page content changes. In this procedure, the LIKE operator is used within an injected subquery to filter customer records by name patterns (e.g., names starting with 'k', followed by two characters, ending with 'l'). This is particularly useful for targeted data exfiltration in scenarios where partial knowledge of naming conventions exists, such as during reconnaissance of a customer database. The attack assumes a vulnerable parameter in a web form (e.g., POST request to a search endpoint) and requires iterative requests to confirm matches. Success can lead to full database enumeration, credential access, or further exploitation like privilege escalation if admin tables are reachable. This maps to exploiting public-facing applications for execution and collection.

## Requirements

1. Access to a vulnerable web application with a MySQL backend and an injectable parameter (e.g., customer name search field).
2. Knowledge of basic SQL injection techniques, including boolean and time-based blind methods.
3. A proxy tool like Burp Suite or command-line tool like curl for intercepting and modifying requests (though not strictly required for manual testing).
4. Understanding of the application's response behaviors to distinguish true/false conditions.

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries in application code to prevent SQL injection.
- Implement a Web Application Firewall (WAF) to detect and block anomalous SQL patterns in inputs.
- Enable database logging for failed queries and monitor for unusual response times or error patterns indicative of blind injection attempts.
- Validate and sanitize all user inputs, rejecting wildcard patterns like '%' or '_' in search fields.

## Objectives

1. Identify and confirm a blind SQL injection vulnerability in a customer search endpoint.
2. Extract customer codes matching specific name patterns using LIKE-based payloads.
3. Infer database structure and content iteratively for broader data exfiltration.

## Instructions

### Step 1: Confirm Vulnerability and Identify Injectable Parameter

**Context**: Locate a user input field (e.g., a search box for customer names) that interacts with the database and test for SQL injection by appending a single quote or comment to trigger errors or behavioral changes. This step verifies the endpoint is vulnerable to blind injection without direct output.

**Test Injection**: Submit a basic payload like `test'` in the search field and observe if the response differs (e.g., generic error page vs. normal results) or if time delays occur.

> If the application returns different content or delays for invalid syntax, proceed. Otherwise, the parameter may not be injectable.

### Step 2: Craft and Inject LIKE-Based Payload for Pattern Matching

**Context**: Use a boolean condition to inject the LIKE query, forcing the database to evaluate the pattern match. For boolean blind SQLi, wrap the SELECT in an AND clause that alters the response based on whether the condition is true (e.g., page loads normally) or false (e.g., error or empty results). Iterate by adjusting the pattern to extract one character or match at a time.

**Payload** ([[codes/MySQL-LIKE-Customer-Code-Query-Payload]]):

```sql
SELECT cust_code FROM customer WHERE cust_name LIKE 'k__l'
```

> Inject as: `k%' AND (SELECT cust_code FROM customer WHERE cust_name LIKE 'k__l') IS NOT NULL --`. Send via the vulnerable parameter (e.g., POST data: search=k%' AND (SELECT cust_code FROM customer WHERE cust_name LIKE 'k__l') IS NOT NULL --). If true, the response indicates a match (e.g., results page); if false, no match (e.g., empty page). Modify the pattern (e.g., 'k%l', 'ka_l') to narrow down and extract full codes. For time-based blind, use `SLEEP(5)` instead of IS NOT NULL to delay responses on true conditions.

### Step 3: Iterate and Extract Data

**Context**: Based on response differences, refine the LIKE pattern to guess characters systematically (e.g., start with first letter, then length, then each position). Log successful matches to reconstruct customer codes.

**Verification**: Repeat injections with varied patterns (e.g., LIKE 'k%a%', LIKE 'k%b%') and note which elicit true responses. Combine with length checks like `LENGTH(cust_name) > 3` to bound the search space.

> Expected success: Consistent true/false inference allowing reconstruction of at least one customer code matching the pattern.
