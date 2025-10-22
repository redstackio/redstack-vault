---
id: 4e0ea9d3-d7ea-4aa3-ba89-eb3f8d053cbe
name: File Upload Double Extension
type: procedure
verified: true
submitted: true
created_at: '2020-08-01T14:21:20.705964+00:00'
updated_at: '2023-05-26T01:09:04.157332+00:00'
platforms:
- Web
tags:
- '[[File Uploads]]'
- '[[Web Applications]]'
---

# File Upload Double Extension

**Status**: ✓ Verified

## Summary

Client-side restrictions on file upload can be bypassed my using double extensions. Allowed extension is appended to the malicious file and later stripped by intercepting the upload request in Burp. 

## Description

# Description

Client-side restrictions on file upload can be bypassed my using double extensions. Allowed extension is appended to the malicious file and later stripped by intercepting the upload request in Burp.

# Instructions

# 

1. Identify file upload functionality in the application

2. Rename the malicious file by adding an additional extension that is allowed in the application. In the below screenshot, the application allows jpg extension and Malicious.php is renamed as *Malicious.php.jpg*

3. Click on submit after selecting the malicious file

4. Intercept the request in Burp and remove the added extension (.jpg). Forward the request

5. Malicious.php file is uploaded to the server

## Platforms

- Web

## Tags

- [[File Uploads]]
- [[Web Applications]]
