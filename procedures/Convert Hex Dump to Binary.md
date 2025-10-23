---
id: 3b3c8cd2-df23-4a2e-b5d5-c661889ccc3e
name: Convert Hex Dump to Binary
type: procedure
verified: true
submitted: true
created_at: '2019-11-25T19:19:34.046112+00:00'
updated_at: '2023-05-26T00:42:28.631156+00:00'
platforms:
- Linux
tags:
- '[[convert]]'
commands:
- '[[xxd Convert Hex Dump to Binary]]'
---

# Convert Hex Dump to Binary

**Status**: ✓ Verified

## Summary

Hex dump is binary data represented in hex pairs. Data in this format can be converted back to binary using tools such as xxd. Example of data in hex pairs: 

## Description

# Description

Hex dump is binary data represented in hex pairs. Data in this format can be converted back to binary using tools such as xxd.



Example of data in hex pairs:





**Code**: [[eb 1d 1f 48 31 c0 5f 88 67 07 48 89 7f 08 48 89 47]]





# Instructions





**Command** ([[xxd Convert Hex Dump to Binary]]):

```bash
xxd -ps -r $_INPUT > $_OUTPUT
```





## Platforms

- Linux

## Commands Used

- [[xxd Convert Hex Dump to Binary]]

## Tags

- [[convert]]


