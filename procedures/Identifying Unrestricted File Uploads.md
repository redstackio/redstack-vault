---
id: f6e05521-ead8-457e-9df2-a678ed6927df
name: Identifying Unrestricted File Uploads
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T18:27:43.726239+00:00'
updated_at: '2023-05-26T01:33:15.838541+00:00'
platforms:
- Web
tags:
- '[[File Uploads]]'
- '[[Web Applications]]'
---

# Identifying Unrestricted File Uploads

**Status**: ✓ Verified

## Summary

File upload functionality can be validated by uploading dangerous file extensions like .exe, .php, .py, .sh etc. 

## Description

# Description

File upload functionality can be validated by uploading dangerous file extensions like .exe, .php, .py, .sh etc.

# Instructions

# 

1. Identify file upload functionality in the application. In the below screenshot *Return Product* functionality has *Upload Invoice* option. Click on the Browse button to select and upload the malicious file (shell.php). 

2. Click on Submit to upload the file to server. It can be observed that the file has been successfully uploaded.

## Platforms

- Web

## Tags

- [[File Uploads]]
- [[Web Applications]]
