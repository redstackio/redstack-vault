---
id: 22538c12-55db-48df-8378-9e387d14c377
name: Manipulate Web Socket Messages To Trigger XSS
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T14:42:03.772376+00:00'
updated_at: '2023-05-26T18:23:38.347176+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web sockets]]'
- '[[xss]]'
---

# Manipulate Web Socket Messages To Trigger XSS

**Status**: ✓ Verified

## Summary

An attacker may intercept the web socket messages and modify the messages with the malicious payload. 

## Description

# Description

An attacker may intercept the web socket messages and modify the messages with the malicious payload.



# Instructions





1. Type a message in the chat window of the application.







![952d7f83-9fc1-4202-a2ec-ccdecf5e31cd.png]()







2. Under burp proxy tab --> web sockets history tab , identify the message from step 1. change the message to xss payload :  *`<img src=1 onerror='alert(1)'*>`





![74316d5d-0f14-4b9e-b415-b5b3da156db9.png]()





3. Send the modified request to the server. Observe that the payload gets parsed by the application and a popup can be observed in the browser.







![8dd20599-c879-4472-ac2c-10cd17303d67.png]()



## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web sockets]]
- [[xss]]


