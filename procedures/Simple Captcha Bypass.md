---
id: b526eced-c8a4-486d-8540-322f1abf1d66
name: Simple Captcha Bypass
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T16:27:31.645257+00:00'
updated_at: '2023-05-26T18:40:44.268396+00:00'
platforms:
- Web
tags:
- '[[Bypass]]'
- '[[Captcha ]]'
- '[[Web Applications]]'
---

# Simple Captcha Bypass

**Status**: ✓ Verified

## Summary

Description Captcha is used as an defense against the attacks by the bots on the application server . An attacker can bypass the captcha reqeust by simply removing the capthca parameter. Instructions 1. Fill the application form and click on i'm not a robot captcha and intercept the request though 

## Description

Description 

Captcha is used as an defense against the attacks by the bots on the application server . An attacker can bypass the captcha reqeust by simply removing the capthca parameter.

Instructions

1. Fill the application form and click on* i'm not a robot* captcha and intercept the request though burp suite proxy .

2. Observe the re-captcha parameter in the body of the request.

3. Remove the whole parameter and forward the request.

4. Observe that register form has been successfully submitted due to no validation on the captcha parameter.

## Platforms

- Web

## Tags

- [[Bypass]]
- [[Captcha ]]
- [[Web Applications]]
