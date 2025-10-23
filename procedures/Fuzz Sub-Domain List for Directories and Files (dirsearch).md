---
id: 36d036cd-b768-4c85-94ea-58cab5014cde
name: Fuzz Sub-Domain List for Directories and Files (dirsearch)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:30.232193+00:00'
updated_at: '2023-05-26T00:43:10.546889+00:00'
commands:
- '[[dirsearch brute force directories and files from sub-domain list with custom
  paths wordlists]]'
---

# Fuzz Sub-Domain List for Directories and Files (dirsearch)

**Status**: ✓ Verified

## Summary

Use this tool to find directories and files in a list of sub-domains using a custom wordlist Custom Wordlist: paths.txt 

## Description

# Description

Use this tool to find directories and files in a list of sub-domains using a custom wordlist

Custom Wordlist: paths.txt



**Code**: [[
/phpinfo.php
/info.php
/admin.php
/api/apidocs
/a]]





[dirsearch](https://github.com/maurosoria/dirsearch)



##  Instructions

1. Pass in a list of sub-domains, paths and how many threads depending on the resources of your attacking system.



**Command** ([[dirsearch brute force directories and files from sub-domain list with custom paths wordlists]]):

```bash
python3 dirsearch.py -L sub-domains.txt -e .* -w paths.txt --simple-report=output.txt -t 50

```





## Commands Used

- [[dirsearch brute force directories and files from sub-domain list with custom paths wordlists]]


