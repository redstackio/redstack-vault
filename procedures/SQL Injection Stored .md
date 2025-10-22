---
id: 4f15d675-07a6-4d67-85be-97a684b75bb0
name: 'SQL Injection Stored '
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T17:37:22.800268+00:00'
updated_at: '2023-05-26T01:07:56.772476+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sql stored]]'
- '[[Web Applications]]'
---

# SQL Injection Stored 

**Status**: ✓ Verified

## Summary

In Stored SQL Injection, the payload is stored in the application through input fileds like address/comment box etc. and the response is displayed in the application response that can be viewed by anyone who visits the page. 

## Description

# Description

In Stored SQL Injection, the payload is stored in the application through input fileds like address/comment box etc. and the response is displayed in the application response that can be viewed by anyone who visits the page.

# Instructions

# 

1. If an entry is made in the blog , the current page displays the added entry to the blog. Test the *add an entry* text box by inserting single quote .

2. An error is displayed at the bottom of the page indicating that the *single quote* is being parsed by the database.

3. Construct a SQL query based on the error message displayed in step 2. Step 2 indicates that the database being used is *MariaDB. *

4. Response to query from step 3 can be observed with *MariaDB *version being displayed for everyone who make a successful entry to the blog 

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sql stored]]
- [[Web Applications]]
