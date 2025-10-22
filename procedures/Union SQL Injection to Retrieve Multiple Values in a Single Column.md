---
id: cdf98df3-55c7-4146-92e1-4da7ee903ca0
name: Union SQL Injection to Retrieve Multiple Values in a Single Column
type: procedure
verified: true
submitted: true
created_at: '2020-08-28T06:38:19.124753+00:00'
updated_at: '2023-05-26T01:14:15.553964+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[Web Applications]]'
---

# Union SQL Injection to Retrieve Multiple Values in a Single Column

**Status**: ✓ Verified

## Summary

Union SQL injection will retrieve data from the database tables. First number of columns in the table has to be identified. Then the payload is customised based on the columns. 

## Description

# Description

Union SQL injection will retrieve data from the database tables. First number of columns in the table has to be identified. Then the payload is customised based on the columns.

# Procedure

1. Access the application and apply filter to observe category parameter in the URL. Inject SQL injection payload through the parameter.

2. Based on the number of columns and containing text, construct the payload by trying to retrieve content from other tables. From the above screenshot, only 1 column is containing text and the payload is fetching the content from two columns.

*'+UNION+SELECT+NULL,username||'~'||password+FROM+users--*

3. Usernames and Passwords are retrieved from the table.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[SQL Injection]]
- [[Web Applications]]
