---
id: a9206879-33db-4794-9deb-045653b3b1a6
name: HTTP-Parameter-Pollution-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.026991+00:00'
updated_at: '2023-04-10T20:22:28.716927+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/How to test]]'
  - '[[tags/HTTP Parameter Pollution]]'
  - web-attack
  - hpp
  - waf-bypass
  - injection
commands:
  - '[[commands/curl-send-hpp-request]]'
platforms:
  - web
tools: []
validated: true
---

# HTTP-Parameter-Pollution-Attack

## Summary

The HTTP Parameter Pollution (HPP) attack exploits inconsistencies in how different web components parse multiple HTTP parameters with the same name. By injecting a benign value in the first instance and a malicious payload in the second, attackers can bypass front-end security like Web Application Firewalls (WAFs) that inspect only the first parameter, while the backend processes the malicious one. This procedure demonstrates HPP to enable SQL injection in a search parameter, allowing unauthorized data access.

## Description

HTTP Parameter Pollution relies on the absence of a standardized parsing method for duplicate parameters in HTTP requests. For example, some parsers (like certain WAFs) take the first occurrence, while others (like PHP's $_GET by default) take the last. In this scenario, a target web application has a 'search' parameter vulnerable to SQL injection, protected by a WAF that filters malicious patterns in the first parameter. The attacker crafts a GET request with two 'search' parameters: the first ('Beth') appears innocent and passes the WAF, the second (' OR 1=1 --) reaches the backend unfiltered, potentially dumping database contents. This technique is effective against pattern-based defenses in web applications handling user inputs in queries. Target environment: Public-facing web apps with GET parameters and layered security (WAF + backend). Expected outcomes: Successful injection without triggering alerts, leading to data exfiltration or logic manipulation.

## Requirements

1. Network access to the target web application endpoint.
2. Identification of a pollutable parameter (e.g., 'search') via reconnaissance or testing.
3. Tools for crafting custom HTTP requests, such as curl (command-line) or Burp Suite (GUI proxy).
4. Basic knowledge of the target parameter's backend processing (e.g., SQL query construction).

## Defense

- Enforce consistent parameter parsing across all components (e.g., configure servers to always use the first or last instance).
- Implement comprehensive input validation that checks all duplicate parameters for malicious content.
- Deploy advanced WAF rules to detect and block requests with duplicate parameter names.
- Use parameterized queries in backend code to prevent injection attacks regardless of input manipulation.
- Monitor and log HTTP requests for anomalies like duplicate parameters, triggering alerts or blocks.

## Objectives

1. Bypass front-end security filters (e.g., WAF) by polluting parameters with benign and malicious values.
2. Inject payloads (e.g., SQL injection) into backend processing to manipulate application logic.
3. Retrieve sensitive data or achieve unauthorized actions, such as dumping database records.

## Instructions

### Step 1: Identify and Test Parameter Parsing Behavior

**Context**: Determine how the target application and its defenses handle duplicate parameters. This step involves sending test requests to observe if the first or last value is processed. Why: Understanding parsing ensures the pollution order (benign first, malicious second) is correct for bypass.

Manually inspect the application (e.g., via browser dev tools) or use a simple test request with non-malicious duplicates like ?search=test1&search=test2. Check responses or logs to see which value is used.

**Expected Output**: Confirmation of parsing behavior (e.g., response reflects 'test1' for WAF, 'test2' for backend).

### Step 2: Craft Benign-Malicious HPP Request

**Context**: Prepare the polluted request where the first parameter evades filters and the second delivers the payload. Why: This splits the attack vector to exploit parsing differences, allowing the malicious input to reach the vulnerable backend.

Use the identified parameter name. For SQL injection example, set first value to a safe search term and second to an injection string.

**Command** ([[commands/curl-send-hpp-request]]):
```bash
curl -X GET "$_TARGET_URL" -G -d "search=$_BENIGN_VALUE" -d "search=$_MALICIOUS_PAYLOAD"
```

> Substitute $_TARGET_URL (e.g., http://example.com/search), $_BENIGN_VALUE (e.g., Beth), $_MALICIOUS_PAYLOAD (e.g., ' OR 1=1 --). The -G flag converts -d to query string; multiple -d create duplicates. If using POST, adjust to -X POST -d params.

**Expected Output**: HTTP 200 response with backend processing the malicious payload (e.g., all database rows returned instead of filtered results).

### Step 3: Analyze Response and Verify Bypass

**Context**: Inspect the server response for injection success and confirm WAF bypass. Why: Validates the HPP worked; if not, adjust payload or order based on parsing.

Review response body for anomalies (e.g., excessive data, SQL errors). If proxied (e.g., via Burp), check upstream/downstream traffic to see parameter handling.

Decision point: If WAF blocks, swap parameter order (malicious first). If backend ignores second, try different pollution techniques (e.g., array notation like search[]=benign&search[]=malicious).

**Expected Output**: Response indicating successful injection, such as unfiltered search results or database error messages revealing structure.

## Expected Output

A successful HPP execution produces a server response reflecting the malicious parameter's effect (e.g., SQL injection dumping data) while security logs show only the benign value, confirming the bypass.

**Success Indicators**:
- Response contains unexpected data (e.g., full database dump).
- No WAF alerts or blocks triggered.
- Backend logs (if accessible) show processing of the second parameter.
