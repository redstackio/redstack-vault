---
id: f2da7d36-5198-47d5-ae10-60d069f97bfd
name: Information Disclosure in Version Control History
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T16:11:22.093895+00:00'
updated_at: '2023-05-26T01:04:54.246259+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[information disclosure]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Information Disclosure in Version Control History

**Status**: ✓ Verified

## Summary

Git files if allowed to access using the browser, it is possible to download and access the files. Git commands can be used to find and retrieve sensitive information. 

## Description

# Description

Git files if allowed to access using the browser, it is possible to download and access the files. Git commands can be used to find and retrieve sensitive information.



# Procedure



1. Access the application and /.git directory. Contents are loaded in the browser.





![8cfdb765-19ea-473b-becf-ac7358328312.png]()



2. Use the wget command to download the git folder from the server.





![275a0289-4422-4cbe-8dcc-9d009b2a7263.png]()



3. Use the git command *git show* to see the files and observe the difference. ADMIN_PASSWORD is observed in the command output.





![5628fb02-6ec4-4467-9313-532b7758d3d4.png]()



4. Use the admin password from the output to access the application as admin user.





![0fdaba2f-c82a-4974-82d3-c0dad1005d79.png]()





## Platforms

- Web

## Tags

- [[broken authentication]]
- [[information disclosure]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


