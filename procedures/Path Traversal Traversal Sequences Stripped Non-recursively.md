---
id: b1e10fa8-2c4f-4134-b661-c0387f79c16e
name: Path Traversal Traversal Sequences Stripped Non-recursively
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T15:54:57.463041+00:00'
updated_at: '2023-05-26T01:13:15.182245+00:00'
platforms:
- Web
tags:
- '[[Path Traversal]]'
- '[[Web Applications]]'
---

# Path Traversal Traversal Sequences Stripped Non-recursively

**Status**: ✓ Verified

## Summary

Nested traversal sequences can used to bypass the application's functionality and access the files 

## Description

# Description

Nested traversal sequences can used to bypass the application's functionality and access the files



# Instructions





1. Use the burp suite to intercept the following request.





![3e42bd03-4d3f-4a52-84cb-59dcccbb5714.png]()





2. Send the request to the repeater tab





![cd8420c4-217a-4e3a-a017-ea00c88c1808.png]()





3.Send the request to the server and observe the response. 





![1387e4fd-42fe-401b-bcb2-996e4c3eb5c5.png]()





4.Modify the filename parameter to the following payload and send the modified request to server . Observe that the response contains the *passwd *file contents

*`....//....//....//etc/passwd ( observe the nested traversal sequences will revert to simple traversal sequences *)`





![ad003a51-32a2-4f0a-8908-4047079362f0.png]()



## Platforms

- Web

## Tags

- [[Path Traversal]]
- [[Web Applications]]


