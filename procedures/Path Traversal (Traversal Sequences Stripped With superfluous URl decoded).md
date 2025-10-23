---
id: fce0396a-9414-43e5-978e-cdf2ffbc7492
name: Path Traversal (Traversal Sequences Stripped With superfluous URl decoded)
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T17:42:19.572967+00:00'
updated_at: '2023-05-26T18:53:39.154837+00:00'
platforms:
- Web
tags:
- '[[Path Traversal]]'
- '[[Web Applications]]'
---

# Path Traversal (Traversal Sequences Stripped With superfluous URl decoded)

**Status**: ✓ Verified

## Summary

Description Non-Standard encoding can be used to bypass the application's input filters Instructions 1.Intercept the request using burp suite's proxy tab. 

## Description

Description

Non-Standard encoding can be used to bypass the application's input filters



Instructions



1.Intercept the request using burp suite's proxy tab.





![c92264fd-adce-4eea-99a1-df59e661754a.png]()





2. Send the request to the repeater tab.





![47a65d39-c8f5-47c4-95b3-3b53544495a0.png]()





3. URL encode the "/" and "../" using the burp decoder tab. The resultant encoded would be similar to the following :

%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66etc%25%32%66passwd





 ../../../../../../etc/passwd





![39ceb747-d754-40ca-9856-0247c33cbe42.png]()



4. Modify the filename parameter vlaue to the one created in the above step and send the modified request to the server. Observe that the file contents of passwd are loaded in the response.





![303e8f48-9a96-40da-ad10-49bc2ea8bffa.png]()





## Platforms

- Web

## Tags

- [[Path Traversal]]
- [[Web Applications]]


