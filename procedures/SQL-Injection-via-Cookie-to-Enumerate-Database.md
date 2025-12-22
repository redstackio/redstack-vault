---
id: 608eb59b-f22f-4da4-af34-d680db42bf25
name: SQL-Injection-via-Cookie-to-Enumerate-Database
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T09:09:00.281666+00:00'
updated_at: '2023-05-26T18:51:04.842771+00:00'
platforms:
  - Web
tags:
  - injection
  - owasp
  - SQL
  - Web Applications
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# SQL-Injection-via-Cookie-to-Enumerate-Database

## Summary

This procedure demonstrates how to exploit a SQL injection vulnerability in a web application's TrackingID cookie to bypass authentication checks and enumerate database names and column structures. By manipulating the cookie value with SQL payloads, an attacker can confirm injection points, test boolean conditions, and use UNION-based techniques to extract metadata, assuming prior knowledge of at least one valid username.

## Description

Web applications often set cookies to track user sessions or personalize content, but if these cookies are directly concatenated into backend SQL queries without proper sanitization, they become injectable entry points. This procedure targets the TrackingID cookie, which is typically set on the homepage and used in queries to fetch user-specific data like welcome messages. The attack begins with error-based confirmation using single quotes to induce syntax errors, followed by boolean-based blind SQL injection to validate payloads. Once confirmed, the Intruder tool in Burp Suite automates enumeration of database names via table existence checks and column names via equality conditions on known usernames. This technique is effective against applications using vulnerable query constructions and can lead to data exfiltration if extended to SELECT sensitive fields. It requires interception of HTTP requests via a proxy and assumes the target uses a SQL backend like MySQL.

## Requirements

- Access to the web application's homepage to capture the initial TrackingID cookie.
- Burp Suite Professional with Intruder enabled for payload automation.
- Knowledge of at least one valid database username (e.g., 'administrator') obtained via other reconnaissance.
- Proxy setup to intercept and modify HTTP requests (e.g., browser configured to route through Burp).
- Basic understanding of SQL syntax for crafting UNION payloads.

## Defense

- Use prepared statements or parameterized queries to separate code from user input, preventing injection.
- Implement web application firewalls (WAFs) to detect and block anomalous SQL patterns in cookies.
- Validate and sanitize all cookie inputs server-side, rejecting unexpected characters like quotes or UNION keywords.
- Enable database logging to monitor for failed queries or unusual SELECT patterns.
- Regularly audit cookie usage in backend code and consider HTTP-only and secure flags to limit client-side access.

## Objectives

1. Confirm the presence of a SQL injection vulnerability in the TrackingID cookie by observing changes in application behavior.
2. Enumerate database names by testing for table existence using boolean conditions.
3. Extract column names from the identified database using known usernames in WHERE clauses.
4. Establish a foundation for further data extraction, such as dumping user credentials or sensitive records.

## Instructions

### Step 1: Intercept and Analyze Initial Request

**Context**: Capture the homepage request to identify the TrackingID cookie and baseline the normal response, which includes a personalized welcome message indicating successful query execution.

Navigate to the target application's homepage using a browser proxied through [[tools/Burp-Suite]]. Intercept the GET request in Burp's Proxy tab and forward it. Observe the response for the 'welcome back' message, confirming the cookie is used in a backend query.

### Step 2: Test for Injection with Single Quote

**Context**: Introduce a single quote to break the SQL query syntax, verifying if the cookie is unsanitized by checking for the absence of the welcome message.

In Burp's Repeater tab, modify the TrackingID cookie value to append a single quote (e.g., original_value'). Forward the request and confirm the response lacks the 'welcome back' message, indicating a SQL error or failed query.

### Step 3: Validate Boolean True Condition

**Context**: Use a tautology payload to force a true condition in the query, restoring the welcome message and confirming blind boolean-based SQL injection is possible.

Update the TrackingID cookie to: original_value' OR 1=1 -- -. Forward the request in Repeater. The presence of the 'welcome back' message confirms the payload executes successfully, bypassing any user-specific checks.

### Step 4: Validate Boolean False Condition

**Context**: Test a false condition to ensure the application's response differentiates based on query results, solidifying the injection point.

Change the TrackingID to: original_value' OR 1=2 -- -. Forward and verify the 'welcome back' message is absent, proving the boolean logic works for conditional payloads.

### Step 5: Enumerate Database Names with Intruder

**Context**: Automate table name guessing to identify databases by injecting a UNION SELECT that checks for table existence, using the welcome message as a success indicator.

Send the request from Repeater to Intruder. Set the payload position around the table name in: original_value' UNION SELECT 'a' FROM ($payload$) WHERE 1=1 -- -. Load a wordlist of common database names (e.g., users, admin, mysql) into position 1. Configure grep - extract for the 'welcome back' string in responses. Start the attack and review results; a matching response indicates a valid database name like 'users'.

### Step 6: Enumerate Columns in Identified Database

**Context**: Probe for column names in the confirmed database (e.g., users) by testing equality against a known username, automating with Intruder to find valid structures.

Send a new request to Intruder. Set payload in: original_value' UNION SELECT 'a' FROM users WHERE ($payload$)='administrator' -- -. Use a wordlist of common column names (e.g., username, password, id, email). Grep for 'welcome back' in responses. Launch the attack; successful payloads reveal valid columns like 'username' or 'password'.
