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

2. Change the CSRF token to some random number and submit the modified request to the server. Observe that the request is rejected.

3.Now delete the CSRF token from the body and submit the request. Observe that the request has been accepted.

4.Right click on the application and select CSRF PoC generator from enagagement tools. It will generate a form for the CSRF chnage email request which can modify the victim's email to attacker's defined emailID. Make sure to enable the option to include am auto-submit script and click on regenerate.

5.Copy the form from above step into the exploit server and deliver the exploit to the victim. When victim access the exploit the emailID of the victim will be changed to attacker's emailID.

## Platforms

- Web

## Tags

- [[CSRF]]
- [[Web Applications]]
