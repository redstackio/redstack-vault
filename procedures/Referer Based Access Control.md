---
id: c9a8a7bf-fcf7-4d06-a167-8c7eb1e8c72a
name: Referer Based Access Control
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T13:49:03.134743+00:00'
updated_at: '2023-05-26T18:38:38.980522+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# Referer Based Access Control

**Status**: ✓ Verified

## Summary

Few application use access controls based on the referer header . The referer header can be manipulated by an attacker and gain unauthorised access. 

## Description

# Description

Few application use access controls based on the referer header . The referer header can be manipulated by an attacker and gain unauthorised access.

# Instructions





1.Log in to the account with admin credentials





![468cc935-f2c4-448d-b63c-0d006b9c2f5c.png]()





2.Navigate to the panel and promote carlos(Normal) and intercept the request using burp proxy. Send the request to the repeater tab.





![97ebc7f1-4500-4ac6-bdad-38a282fd6799.png]()







3.Open a incognito window and log in to the applicaton using non admin account .





![b83b4f11-e698-4e52-a1d3-2605ee3f007a.png]()





4. Copy the session cookie value to the clipboard.





![e85602cd-c90e-4878-b33c-e22703ed4194.png]()





5.Navigate to to `/admin-roles?username=carlos&action=upgrade` and observe that the request is treated as unauthorized due to the icorrect referer header .





![4b0b01c7-2669-4332-9346-0969d2f0c08b.png]()





6.Modify the referer header as below and change the username in url to weiner and submit the request . Observe that the there is a 302 redirection which indicates the successful login.







![ffc5ab45-fb91-447a-9304-83635e30e279.png]()



## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]


