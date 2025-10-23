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





![f551af06-f796-43a4-988c-9e9e60f5150d.jpg](_assets/images/Mash/f551af06-f796-43a4-988c-9e9e60f5150d.jpg)







2. Rename the malicious file by adding an additional extension that is allowed in the application. In the below screenshot, the application allows jpg extension and Malicious.php is renamed as *Malicious.php.jpg*







![acf1500c-b063-43ec-a279-87b9d84a40c9.jpg](_assets/images/Mash/acf1500c-b063-43ec-a279-87b9d84a40c9.jpg)









3. Click on submit after selecting the malicious file





![5360d418-579a-4b5a-a747-5c0bb9a53a5f.jpg](_assets/images/Mash/5360d418-579a-4b5a-a747-5c0bb9a53a5f.jpg)





4. Intercept the request in Burp and remove the added extension (.jpg). Forward the request









![404a57d8-9d9a-44d0-a9d6-221af698f9b5.jpg](_assets/images/Mash/404a57d8-9d9a-44d0-a9d6-221af698f9b5.jpg)





5. Malicious.php file is uploaded to the server











![9ffe1185-7463-448c-8afe-77aab5bd9962.jpg](_assets/images/Mash/9ffe1185-7463-448c-8afe-77aab5bd9962.jpg)





## Platforms

- Web

## Tags

- [[File Uploads]]
- [[Web Applications]]


