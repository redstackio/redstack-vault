---
id: 9a6fc951-29ca-4a8e-9fe8-20b372fd58cb
name: User Role Modified in User Profile
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T18:35:39.509371+00:00'
updated_at: '2023-05-26T01:36:23.761397+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# User Role Modified in User Profile

**Status**: ✓ Verified

## Summary

Few applications due to poor design will let an attacker to modify the user role from the attacker's legitimate profile to get unauthorised access to other user accounts sometimes admin account. 

## Description

# Description

Few applications due to poor design will let an attacker to modify the user role from the attacker's legitimate profile to get unauthorised access to other user accounts sometimes admin account.



# Instructions





1.Login with the credentials provided.





![fcef81ca-af9c-4caf-a5bb-6f271d2e2696.png]()





2. Click on "My Account" and submit a new email address and capture the request on Burp and send it to the Repeater and observe the response that contains your role ID.





![809cfc0d-7888-40ca-aa88-0d2fe5f7eb6b.png]()





3.`Add "roleid":2` into the JSON in the request body, and resend it.





![710a5450-9c6b-430c-93f8-526299607fbf.png]()



4.Observe that the response shows your `roleid` has changed to 2 and the email is successfully changed.





![3d6918e8-dc3d-41be-828c-66cba0d6329d.png]()





5.Observe that the you have access to admin panel.





![be67b03d-ebc2-4bb2-bf40-6d4ec34e06d5.png]()





## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]


