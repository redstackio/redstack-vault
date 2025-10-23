---
id: 19a9d70e-f98e-40b7-b7e9-36c18369b035
name: Host Header Injection
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T13:22:56.651994+00:00'
updated_at: '2023-05-26T01:25:33.308362+00:00'
platforms:
- Web
tags:
- '[[Host header Injection]]'
- '[[Web Applications]]'
---

# Host Header Injection

**Status**: ✓ Verified

## Summary

Host header injection attack occurs when the application server doesnot validate the host header for every reqeust. 

## Description

# Description

 Host header injection attack occurs when the application server doesnot validate the host header for every reqeust.



# Instructions





1. Intercept the request and send it to the repeater.





![6d1bb6c2-090d-4ce0-8785-389197d10bc4.png]()







2. Change the host header parameter value to any url, in this case its changed to bing.com. Observe that the response reflects the host header value. 





![74f9ca0f-9374-4015-8fe3-1defee27f57d.png]()







3. Right click on the url from step 2 and click on *copy url* to copy the url to the clipboard. Paste the url into the browser and observe that bing.com is loaded .









![a6322fb8-1a08-4348-8dff-d911148fb878.png]()



## Platforms

- Web

## Tags

- [[Host header Injection]]
- [[Web Applications]]


