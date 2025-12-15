---
id: 123e4567-e89b-12d3-a456-426614174001
name: Trigger-Race-Condition-for-Error-Disclosure
tags:
  - information-disclosure
  - race-condition
  - error-message
  - stack-trace
  - sql-leak
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - .NET
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:26.808Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Trigger-Race-Condition-for-Error-Disclosure
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Reconnaissance]]
techniques: [[Gather Victim Host Information]], [[Exploit Public-Facing Application]]
sub_techniques: []
tags: [information-disclosure, race-condition, error-message, stack-trace, sql-leak]
commands: []
platforms: [Web, .NET]
tools: [[tools/Burp-Suite]]
---

# Trigger-Race-Condition-for-Error-Disclosure

## Summary

This procedure exploits concurrency vulnerabilities in a user registration endpoint, typically in .NET applications like Telerik Sitefinity, by sending rapid concurrent requests to trigger an OptimisticVerificationException, resulting in error messages that disclose internal file paths, SQL query structures, and stack traces for reconnaissance purposes.

## Description

In scenarios involving database operations with optimistic concurrency control, such as user registration in web applications, inadequate error handling can expose sensitive internals when race conditions occur. By using tools like Burp Suite's Intruder to flood the POST /registration endpoint with varying parameters (e.g., email addresses), an attacker can induce concurrent updates that fail with exceptions. The resulting responses reveal backend details like file paths (e.g., D:\\Agent\\ _work\\1825\\s\\Code\\DataAccessLayer\\Classes\\RegistrationRequestService.cs) and SQL statements (e.g., UPDATE [sf_dynamic_content] SET ...), aiding in further mapping of the application's architecture without leaking user data. This is effective against public-facing web apps with SQL backends and has low impact but high reconnaissance value.

## Requirements

1. Network access to the target web application (e.g., https://target.com/registration).
2. Burp Suite installed and configured as a proxy.
3. Basic knowledge of HTTP requests and form parameters (UserName, Password, EmailAddress).
4. No authentication required for the registration endpoint.

## Defense

Defensive measures and detection strategies:

- Implement proper error handling to sanitize responses and avoid exposing stack traces or SQL details in production.
- Use rate limiting on registration endpoints to prevent rapid concurrent requests.
- Monitor for high-volume POST requests to /registration and anomalous error rates using WAF or logging tools like ELK Stack.

## Objectives

1. Trigger OptimisticVerificationException through race conditions.
2. Extract internal application details from error messages.
3. Perform reconnaissance on backend structure without direct data access.

## Instructions

### Step 1: Access and Intercept Registration Request

**Context**: Prepare by navigating to the form and capturing a sample request to understand the payload structure.

No specific command; use browser to access https://valleyconnect.tva.gov/registration, fill form (e.g., UserName: test, Password: test, EmailAddress: test@example.com), and intercept POST /registration in Burp Suite Proxy.

> Forward the request to confirm normal behavior, noting parameters for later modification.

### Step 2: Configure Intruder for Concurrent Attacks

**Context**: Set up automated rapid requests targeting a mutable parameter to induce concurrency.

In Burp Suite, right-click the intercepted request and send to Intruder. Select the EmailAddress value as the attack position (§ symbol). Load a payload list with variations (e.g., Z@jetamooz.com, test1@example.com). Set thread count to maximum (e.g., 10-20) and launch the attack.

> Observe responses in the Intruder results table; filter for HTTP 500 errors or exceptions.

### Step 3: Analyze Exposed Information

**Context**: Review error responses for disclosed internals.

Examine the response body for stack traces indicating OptimisticVerificationException, noting exposed elements like file paths and SQL queries.

> Successful output includes details such as internal .cs file paths and partial SQL UPDATE statements, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[information-disclosure]]
- [[race-condition]]
- [[error-message]]
- [[stack-trace]]
- [[sql-leak]]
