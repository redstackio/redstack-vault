---
id: fc08321a-93f2-453f-9c55-94b88fae1cb4
name: Fuzz Website Directories and Files (dirsearch)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:43.608472+00:00'
updated_at: '2023-05-26T18:35:38.799780+00:00'
commands:
- '[[dirsearch enumerate directories and files against a domain name]]'
---

# Fuzz Website Directories and Files (dirsearch)

**Status**: ✓ Verified

## Summary

Use this tool to find directories and files in a website. It can locate configuration files, hidden directories, and api endpoints like grpc or graphql dirsearch 

## Description

# Description

Use this tool to find directories and files in a website.

It can locate configuration files, hidden directories, and api endpoints like grpc or graphql

[dirsearch](https://github.com/maurosoria/dirsearch)



##  Instructions

1. Using the dirsearch tool pass in a domain name and an extensions list



**Command** ([[dirsearch enumerate directories and files against a domain name]]):

```bash
python3 dirsearch.py -u redstack.io -e .*

```





## Commands Used

- [[dirsearch enumerate directories and files against a domain name]]


