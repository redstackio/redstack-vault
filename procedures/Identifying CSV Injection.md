---
id: a0b2a32f-bd84-4bc6-8829-691595fab328
name: Identifying CSV Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T18:08:48.242789+00:00'
updated_at: '2023-05-26T01:08:37.345596+00:00'
platforms:
- Web
tags:
- '[[CSV Injection]]'
- '[[injection]]'
- '[[Web Applications]]'
---

# Identifying CSV Injection

**Status**: ✓ Verified

## Summary

CSV injection can be tested in an application that has an export functionality which extracts information in the form of CSV files. 

## Description

# Description

CSV injection can be tested in an application that has an export functionality which extracts information in the form of CSV files.

# Instructions



1. In the below screenshot, the *Return Product* function has a comment box and a sample CSV formula is added in it.





![fcd87929-0bd6-406f-8ecf-012c85ff993a.jpg](_assets/images/Mash/fcd87929-0bd6-406f-8ecf-012c85ff993a.jpg)







2. Login as admin user and the inserted formula is observed in the *User Comments* under *Return Products List *function.







![b8a9adcd-ba4a-4247-a638-7b424841dc27.jpg](_assets/images/Mash/b8a9adcd-ba4a-4247-a638-7b424841dc27.jpg)





3. If admin clicks on the Download CSV option, the list gets exported in a CSV file as shown below.





![af9db7e4-2165-47ee-98d9-c38c88d60e65.jpg](_assets/images/Mash/af9db7e4-2165-47ee-98d9-c38c88d60e65.jpg)





4. When the CSV file is opened, the inserted formula is processed and *3* is displayed in the *remarks* cell. The value has to be ideally *=1+2*.









![ff15b33c-d63b-4f0a-a2b2-d3640567b1d8.jpg]()









## Platforms

- Web

## Tags

- [[CSV Injection]]
- [[injection]]
- [[Web Applications]]


