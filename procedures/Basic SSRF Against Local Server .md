---
id: eb08a971-21fa-4e11-9334-dcc358fdf964
name: 'Basic SSRF Against Local Server '
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T17:32:05.421319+00:00'
updated_at: '2023-05-26T18:24:27.472643+00:00'
platforms:
- Web
tags:
- '[[SSRF]]'
- '[[Web Applications]]'
---

# Basic SSRF Against Local Server 

**Status**: ✓ Verified

## Summary

Description Instructions 1.Navigate to access the product and click on check stock . Intercept the request and send it to the server. 

## Description

Description



Instructions



1.Navigate to access the product and click on check stock . Intercept the request and send it to the server.





![6e94397d-577a-4f36-a965-b9871bb93349.png]()





2.Replace the stockApi URI with [http://localhost/admin](http://localhost/admin)





![2fe77aec-bd32-4224-9a05-c3b53af47ad9.png]()





3. Observe the *admin interface* after sending the request from *repeater *tab to the server in step2.





![7816f960-e286-49b8-8bad-335d95143e8e.png]()



4.Change the stockApi URI to [*http://localhost/admin/delete?username=carlo](http://localhost/admin/delete?username=carlos)s* to delete the user carlos.





![d58a9b7c-c326-467e-9d5f-2480f0630318.png]()



## Platforms

- Web

## Tags

- [[SSRF]]
- [[Web Applications]]


