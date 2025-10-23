---
id: 32493876-48b5-413c-b8dc-471ebb9ff0b0
name: SQLMap Specify Parameters With Data
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T17:58:12.846645+00:00'
updated_at: '2023-05-26T01:50:35.998751+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[sqli]]'
- '[[SQLMap]]'
- '[[Web Applications]]'
commands:
- '[[SQLMap Command With Data]]'
---

# SQLMap Specify Parameters With Data

**Status**: ✓ Verified

## Summary

SQLMap is an automated SQL injection exploitation tool. Data can be specified with --data option. 

## Description

# Description

SQLMap is an automated SQL injection exploitation tool. Data can be specified with *--data* option.



# Procedure

# 

1. The following SQLMap command can be used to pass the parameters in the page. The parameters are injected with SQL payloads.







**Command** ([[SQLMap Command With Data]]):

```bash
sqlmap -u 'http://192.168.1.10/vcart/login.php' --data='user=demo@vcart.com&pass=demo&selop=2'
```





## Platforms

- Web

## Commands Used

- [[SQLMap Command With Data]]

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[sqli]]
- [[SQLMap]]
- [[Web Applications]]


