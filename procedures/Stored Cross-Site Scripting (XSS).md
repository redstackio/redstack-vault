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



![a89439ae-a320-4959-98f8-621173147763.jpg](_assets/images/Mash/a89439ae-a320-4959-98f8-621173147763.jpg)







2. Admin tries to load the list of users by clicking on *Users List* option in the admin panel.







![12d5ab3a-483d-4213-b767-ea24157fe17f.png](_assets/images/Mash/12d5ab3a-483d-4213-b767-ea24157fe17f.png)











3. As the First Name parameter is stored with script tag in the Step 1, the script is executed when an admin tries to list the user's details.







![736dfbc1-9fca-4be6-9b0a-53ac6632b70d.jpg](_assets/images/Mash/736dfbc1-9fca-4be6-9b0a-53ac6632b70d.jpg)









## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Stored XSS]]
- [[Web Applications]]
- [[xss]]


