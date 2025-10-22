---
id: e2c48955-fa67-44c0-a8aa-71003f1098a4
name: Stored Cross-Site Scripting (XSS)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T15:47:48.948265+00:00'
updated_at: '2023-05-26T01:06:57.108768+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Stored XSS]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# Stored Cross-Site Scripting (XSS)

**Status**: ✓ Verified

## Summary

When a malicious script is inserted through form fields and stored in the application database, it gets executed whenever the user tries to visit the page that loads the stored script. 

## Description

# Description

When a malicious script is inserted through form fields and stored in the application database, it gets executed whenever the user tries to visit the page that loads the stored script.

# Instructions

1. Insert script tag through the *First Name* field and click on submit to store the script in the application database.

2. Admin tries to load the list of users by clicking on *Users List* option in the admin panel.

3. As the First Name parameter is stored with script tag in the Step 1, the script is executed when an admin tries to list the user's details.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Stored XSS]]
- [[Web Applications]]
- [[xss]]
