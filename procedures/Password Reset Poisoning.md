---
id: f6926594-a03a-4a94-be07-50580306e5fc
name: Password Reset Poisoning
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T17:26:11.571283+00:00'
updated_at: '2023-05-26T01:22:47.090957+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Web Applications]]'
---

# Password Reset Poisoning

**Status**: ✓ Verified

## Summary

Applications usually send the change password link to the customer's email.An attacker can maliciously change the password of the victim  by manipulating the password reset link . 

## Description

# Description

Applications usually send the change password link to the customer's email.An attacker can maliciously change the password of the victim  by manipulating the password reset link .



# Instructions





1.With burp running and proxying reqeusts ,Log in to the account with given credentials. Access my account page and observe the password reset functionality. Enter your username to reset the password and click on submit.





![678543a4-7483-4a38-be79-68c6e1e23f59.png]()



2. Observe that a reset link has been sent to email.





![b0906078-031c-4d15-a191-70c615722672.png]()







3. Access email and click on  the link to reset the password. Identify the forget-password request from the HTTPHistory and send the request to repeater tab.





![4e06c1da-1f84-4fee-86ab-9ad3a589a231.png]()









4.Notice that the request supports the X*-Forwarded-Host *header .





![25573488-d2e5-463c-8a1d-26d6b6785255.png]()





5. Add the *X-Forwarded-Host *header to the request and change the username to *carlos *and send the request to server.







![29a3d3dd-57c5-48f9-a902-7934e7366ded.png]()





6.Access exploit server and identify the GET forget-password link





![a90e2eda-07ef-4a16-9d91-c90c209efec8.png]()





7.Load the link in the browser 





![ad41f192-afe3-41a0-91cd-a6be49b8df7a.png]()





8.Enter new password to change the password of user *carlos*.





![8224f832-01e3-4772-9f9e-82a8d49ce5e5.png]()



## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]


