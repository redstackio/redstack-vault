---
id: 4a6457c1-f4d2-4ea9-a59c-648bc4aeb76a
name: URL Based Access Control Manipulated
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T18:54:28.566367+00:00'
updated_at: '2023-05-26T01:25:48.335175+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# URL Based Access Control Manipulated

**Status**: ✓ Verified

## Summary

Few applications enforce access controls at the platform layer by restricting access to specific URLs and HTTP methods based on the user's role. 

## Description

# Description



Few applications enforce access controls at the platform layer by restricting access to specific URLs and HTTP methods based on the user's role.



# Instructions



1.Try to access the admin panel 





![9cb89f85-4b20-429a-973e-26702e044d22.png]()



2. Observe that the access is denied





![341f6ad6-c799-4194-9e9f-3fef4d02ad64.png]()





3. Use burp to capture the request and send the request to the repeater tab. Add the *`X-Original-URL: /invali*d in the reuqest and send the request to the server `



`Observe the " not found " response . With that response we can confirm that X-Original_URL has been parsed by the server.`

![e5a0291e-908e-4b3d-a253-f171407ece15.png]()





4. Now change the *`X-Original-URL: /invalid* to *X-Original-URL: /admin/delete* to delte the user. Send the modified request to the server . Observe that the user account ahas been delete`d.





![83b29c98-beb2-4700-9b1e-bf217cda965f.png]()



## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]


