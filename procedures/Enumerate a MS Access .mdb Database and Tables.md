---
id: bdccc71b-824e-42c5-aa33-6169f31e17d8
name: Enumerate a MS Access .mdb Database and Tables
type: procedure
verified: false
submitted: false
created_at: '2019-12-13T19:52:08.251775+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
commands:
- '[[mdb-export List Table Contents from a Database]]'
- '[[mdb-tables List Tables in a Database]]'
---

# Enumerate a MS Access .mdb Database and Tables

## Summary

List tables and their contents from a Microsoft Access Database file (.mdb). 

## Description

# Description

List tables and their contents from a Microsoft Access Database file (.mdb).



# Instructions

1. Query the database for table names.





**Command** ([[mdb-tables List Tables in a Database]]):

```bash
mdb-tables -1 $_DATABASE.mdb
```





2. Query the database by table name for the contents.





**Command** ([[mdb-export List Table Contents from a Database]]):

```bash
mdb-export $_DATABASE.mdb $_TABLE
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]

## Commands Used

- [[mdb-export List Table Contents from a Database]]
- [[mdb-tables List Tables in a Database]]

## Tags

- [[data exposure]]


