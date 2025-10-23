---
id: 112db766-011b-4721-b69f-c9b69a9b6afd
name: CSRF No Validation Of CSRF Token(Delete Token)
type: procedure
verified: true
submitted: true
created_at: '2020-08-25T09:12:59.157676+00:00'
updated_at: '2023-05-26T18:07:50.076872+00:00'
platforms:
- Web
tags:
- '[[CSRF]]'
- '[[Web Applications]]'
---

# CSRF No Validation Of CSRF Token(Delete Token)

**Status**: ✓ Verified

## Summary

Descritpion CSRF tokens are implemented to avoid CSRF attacks. Insecure implementation of tokens will let an attacker to takeover the user's account. In this case, CSRF token is not being validated by the application server. Instructions 1.With burp proxying requests and intercept off, browse the a

## Description

# Descritpion

CSRF tokens are implemented to avoid CSRF attacks. Insecure implementation of tokens will let an attacker to takeover the user's account. In this case, CSRF token is not being validated by the application server.

# Instructions





1.With burp proxying requests and intercept off, browse the application. Under HTTP history tab , identify the *change email* request and send the request to the repeater tab.





![c20e3745-e145-43cc-a168-8bedd073cfda.png]()





2. Change the CSRF token to some random number and submit the modified request to the server. Observe that the request is rejected.







![c3c46d7d-2bc5-4b79-8019-606f6cec96e7.png]()





3.Now delete the CSRF token from the body and submit the request. Observe that the request has been accepted.





![947a4c2d-77ac-48a3-8142-5e02f3209834.png]()





4.Right click on the application and select CSRF PoC generator from enagagement tools. It will generate a form for the CSRF chnage email request which can modify the victim's email to attacker's defined emailID. Make sure to enable the option to include am auto-submit script and click on regenerate.





![2e718abe-fd53-4a30-bd42-93fd7f10e9cb.png]()





5.Copy the form from above step into the exploit server and deliver the exploit to the victim. When victim access the exploit the emailID of the victim will be changed to attacker's emailID.





![0be17ab2-2f46-441a-8ebf-2f51dd7ccef1.png]()



## Platforms

- Web

## Tags

- [[CSRF]]
- [[Web Applications]]


