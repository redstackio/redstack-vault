---
id: 4859e3fe-9930-4779-b9e0-63f554ea261b
name: 'Stored XSS To Capture Passwords Using Burp Collaborator '
type: procedure
verified: true
submitted: true
created_at: '2020-08-05T18:13:46.432602+00:00'
updated_at: '2023-05-26T01:30:22.636048+00:00'
platforms:
- Web
tags:
- '[[Burp]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Stored XSS]]'
- '[[Web Applications]]'
---

# Stored XSS To Capture Passwords Using Burp Collaborator 

**Status**: ✓ Verified

## Summary

This kind of attack technique will give access to every other account on the application to the attacker. A victim's password/sensitive info will be sent to attacker's domain that was created using burp collaborator which is available for users having Burp Suite Professional edition. 

## Description

# Description

This kind of attack technique will give access to every other account on the application to the attacker. A victim's password/sensitive info will be sent to attacker's domain that was created using burp collaborator which is available for users having Burp Suite Professional edition.



# 

# Instructions

# 

# 

1. Open the Burp Suite  Professional version. Under burp menu, click on *burp collaborator client .*





![2c780b46-03c9-494b-83e3-f76b319f855d.png](_assets/images/Mash/2c780b46-03c9-494b-83e3-f76b319f855d.png)









2.Insert the *payload *into comment section of the blog.



*Payload*:







**Code**: [[<input name=username id=username>
<input type=pas]]









![cfe8dc69-fb6d-4cb0-9453-1fa322d98e4f.png](_assets/images/Mash/cfe8dc69-fb6d-4cb0-9453-1fa322d98e4f.png)









3. Any user who visits the comment section of the blog get their credentials sent to attacker through the *burp collaborator* client . Comment that is submitted in step 2 can be seen in comment section.









![fbff7356-6637-4b5d-ade7-29fab58c561d.png](_assets/images/Mash/fbff7356-6637-4b5d-ade7-29fab58c561d.png)









4.In burp collaborator window, check for *http type requests . I*f you dont see any  requests* click on poll now* and wait for few seconds to observe the *HTTP request*







![92fab8d3-4542-41c9-a52a-545236499f2e.png](_assets/images/Mash/92fab8d3-4542-41c9-a52a-545236499f2e.png)





5. In Burp collaborator window Under *request to collaborator,* observe the username and password.







![60da7e7f-cee7-49b8-9596-c746af3aa65f.png](_assets/images/Mash/60da7e7f-cee7-49b8-9596-c746af3aa65f.png)









6. Login into the application with credentials from step 5.









![e35bdfa9-d8c6-4377-b1db-ab29ec6ec598.png](_assets/images/Mash/e35bdfa9-d8c6-4377-b1db-ab29ec6ec598.png)









7. With credentials obtained through burp collaborator, you can successfully login as *administrator*



![49ec32c9-e6e9-464c-a929-282508f24114.png](_assets/images/Mash/49ec32c9-e6e9-464c-a929-282508f24114.png)











## Platforms

- Web

## Tags

- [[Burp]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Stored XSS]]
- [[Web Applications]]


