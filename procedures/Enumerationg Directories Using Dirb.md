---
id: 1c33746f-dc64-44c2-8618-561c9c476599
name: Enumerationg Directories Using Dirb
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T15:05:51.550989+00:00'
updated_at: '2023-05-26T15:56:44.496394+00:00'
platforms:
- Web
tags:
- '[[Directory Listing]]'
- '[[Web Applications]]'
commands:
- '[[Dirb directory brute force]]'
---

# Enumerationg Directories Using Dirb

**Status**: ✓ Verified

## Summary

Dirb tool is used in enumerating the directories within an application. Dirb comes pre-installed in Kali Linux OS. 

## Description

# Description

Dirb tool is used in enumerating the directories within an application. Dirb comes pre-installed in Kali Linux OS. 



# Instructions

# 

1. Following *dirb* command can be used to enumerate the directories. The highlighted list are the enumerated directories (admin, css, images, invoices, js, uploads).







**Command** ([[Dirb directory brute force]]):

```bash
dirb http:/$_TARGET_IP $_WORDLIST -r
```









2. One of the enumerated directories is accessed in the browser to check the existence.





![48a760ae-ea76-4c8a-b0b4-9384b1241d8d.png](_assets/images/Mash/48a760ae-ea76-4c8a-b0b4-9384b1241d8d.png)









## Platforms

- Web

## Commands Used

- [[Dirb directory brute force]]

## Tags

- [[Directory Listing]]
- [[Web Applications]]


