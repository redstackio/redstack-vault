---
id: 3642ea6b-1a6a-4508-9e38-9bf9bc4c98f1
name: Large File Upload - Disk Denial of Service
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T19:32:40.732456+00:00'
updated_at: '2023-05-26T01:15:28.652033+00:00'
platforms:
- Web
tags:
- '[[Denial of Service]]'
- '[[DOS]]'
- '[[File Uploads]]'
- '[[Web Applications]]'
---

# Large File Upload - Disk Denial of Service

**Status**: ✓ Verified

## Description

# Description

# 

Uploading large files through file upload functionality in an application could lead to Denial of Service on the Disk space.



# Procedure

# 

1. Access the file upload functionality in the application and select a large file of allowed type. In the below screenshot, 200 MB pdf file is created and selected to upload in the application.





![e9e66a80-ee62-4d54-8e63-bcf3946f912d.JPG]()



2. The selected file has been uploaded and uploading such large files in more number would result in complete utilization of disk space.





![c4d3b0a9-1da8-48fb-ae54-b6b936bec301.JPG]()





## Platforms

- Web

## Tags

- [[Denial of Service]]
- [[DOS]]
- [[File Uploads]]
- [[Web Applications]]


