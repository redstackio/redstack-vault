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

2.Replace the stockApi URI with [http://localhost/admin](http://localhost/admin)

3. Observe the *admin interface* after sending the request from *repeater *tab to the server in step2.

4.Change the stockApi URI to [*http://localhost/admin/delete?username=carlo](http://localhost/admin/delete?username=carlos)s* to delete the user carlos.

## Platforms

- Web

## Tags

- [[SSRF]]
- [[Web Applications]]
