---
id: bb16420e-3fc1-4448-a118-3ff8b9fcca1a
name: Unzip an AES Encrypted Zip Archive (Linux)
type: procedure
verified: true
submitted: true
created_at: '2019-12-13T22:09:49.776883+00:00'
updated_at: '2023-05-26T00:53:12.917123+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
platforms:
- Linux
tags:
- '[[extract]]'
commands:
- '[[7z Decompress a Password Protected Zip Archive]]'
---

# Unzip an AES Encrypted Zip Archive (Linux)

**Status**: ✓ Verified

## Summary

The standard "unzip" Linux utility does not have native support for AES encrypted zip files, and will fail with the  "unsupported compression method 99" error. A simple workaround is to use 7zip to extract such zip files. 

## Description

# Description

The standard "unzip" Linux utility does not have native support for AES encrypted zip files, and will fail with the  "unsupported compression method 99" error. A simple workaround is to use 7zip to extract such zip files.



# Instructions

Install 7zip from any popular package manager using the name "p7zip-full". Eg:





**Code**: [[apt update && apt install p7zip-full -y]]









**Command** ([[7z Decompress a Password Protected Zip Archive]]):

```bash
7z x $_FILENAME.zip
```





## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]

## Commands Used

- [[7z Decompress a Password Protected Zip Archive]]

## Tags

- [[extract]]


