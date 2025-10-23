---
id: b997e6c8-d982-439a-b2df-3b2b1581e548
name: SQLMap to Specify URL With Parameters
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T17:40:37.509883+00:00'
updated_at: '2023-05-26T18:11:17.788508+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[sqli]]'
- '[[SQLMap]]'
- '[[Web Applications]]'
commands:
- '[[SQLMap Command With Parameter]]'
---

# SQLMap to Specify URL With Parameters

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL injection exploitation tool. Parameters on which the tool injects the SQL payloads can be specified using -p option. 

## Description

# Description

SQLMap is an automated SQL injection exploitation tool. Parameters on which the tool injects the SQL payloads can be specified using *-p* option.



# Procedure



1. Use the below SQLMap command along with *-p* option to test for SQL injection on a web application.







**Command** ([[SQLMap Command With Parameter]]):

```bash
sqlmap -u "http://192.168.1.10/vcart/login.php?user=demo@vcart.com&pass=demo&selop=2" -p user
```





2. Output shows the payloads used to exploit the parameter.



## Platforms

- Web

## Commands Used

- [[SQLMap Command With Parameter]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[sqli]]
- [[SQLMap]]
- [[Web Applications]]


