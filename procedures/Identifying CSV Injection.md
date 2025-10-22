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

2. Login as admin user and the inserted formula is observed in the *User Comments* under *Return Products List *function.

3. If admin clicks on the Download CSV option, the list gets exported in a CSV file as shown below.

4. When the CSV file is opened, the inserted formula is processed and *3* is displayed in the *remarks* cell. The value has to be ideally *=1+2*.

## Platforms

- Web

## Tags

- [[CSV Injection]]
- [[injection]]
- [[Web Applications]]
