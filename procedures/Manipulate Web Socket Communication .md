---
id: 04f4b3a1-5428-4b70-8c06-998a2d1ce361
name: 'Manipulate Web Socket Communication '
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T14:26:01.202086+00:00'
updated_at: '2023-05-26T01:10:27.514218+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web sockets]]'
---

# Manipulate Web Socket Communication 

**Status**: ✓ Verified

## Summary

An attacker will manipulate the web sockets messages by modifying and replaying the mesages with malicious payload . 

## Description

# Description

An attacker will manipulate the web sockets messages by modifying and replaying the mesages with malicious payload .



# Instructions





1. Obserev the live chat in the application.





![67ce588c-b3ce-40c2-a1d0-3036a1bd437c.png](_assets/images/Mash/67ce588c-b3ce-40c2-a1d0-3036a1bd437c.png)







2. With burp intercept on , intercept the request from step 1 and send it to the repeater.





![9a464a11-5f52-4f0d-8466-033d1a04a400.png](_assets/images/Mash/9a464a11-5f52-4f0d-8466-033d1a04a400.png)





3. Edit the web socket message from step 2 with a basic xss payload *`<img src=1 onerror='alert(1)'*> and send the message to the server. Observe that the message has been blocked and and the web socket connection is closed.`





![061e1aaa-90cb-4d81-a7b9-3f3e0ed0896c.png](_assets/images/Mash/061e1aaa-90cb-4d81-a7b9-3f3e0ed0896c.png)





4. Add the x-forwarded-for: 1.1.1.1 and click connect to re-establish web socket connection to the server





![2d96c883-ee3a-420d-b2d8-8affed5eb220.png](_assets/images/Mash/2d96c883-ee3a-420d-b2d8-8affed5eb220.png)





5. obfuscate XSS payload like: *`<iframe src='jAvAsCripT:alert`1`'></iframe>* and send the request to the repeater.Observe that the message has been parsed by the application`





![1733ab82-19ac-454f-8646-7da889159c6b.png](_assets/images/Mash/1733ab82-19ac-454f-8646-7da889159c6b.png)



## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web sockets]]


