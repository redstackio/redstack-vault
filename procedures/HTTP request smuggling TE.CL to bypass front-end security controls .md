---
id: f196f50e-4d20-4fc8-827c-c2675f4a704a
name: 'HTTP request smuggling TE.CL to bypass front-end security controls '
type: procedure
verified: false
submitted: false
created_at: '2020-08-12T03:49:41.954433+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[Web Applications]]'
---

# HTTP request smuggling TE.CL to bypass front-end security controls 

## Summary

In this kind of attack, backend server doesnt support Transfer-Encoding . In this case front end server doesnot grant access to admin panel.To have access to admin panel , attacker will bypass the front end security controls. 

## Description

# Description

In this kind of attack, backend server doesnt support Transfer-Encoding . In this case front end server doesnot grant access to admin panel.To have access to admin panel , attacker will bypass the front end security controls.





# Instructions





1.Intercept the request using Burp Suite and send the request to the repeater tab. Observe the response to the request .In Burp Suite,  ensure that the "Update Content-Length" option is unchecked.







![a681bdc5-d98d-4a41-8bdf-16a13b480260.jpg](_assets/images/Mash/a681bdc5-d98d-4a41-8bdf-16a13b480260.jpg)







2. Add the following request to the request in step1 . Observe that content length has been added in the modified request . 







**Code**: [[
Modified request:

60
POST /admin HTTP/1.1
C]]









3. Send the modified request to the server and observe the response . Access to the admin panel is unauthorised. 



![41bb6670-1c55-4419-99ee-0b48663be6fc.jpg](_assets/images/Mash/41bb6670-1c55-4419-99ee-0b48663be6fc.jpg)





3. Add the host parameter to the modified request and send the request to the server to access the admin panel







**Code**: [[60
POST /admin HTTP/1.1
Host: localhost
Content]]









![621a8cb0-59e6-43cf-a92f-3b5037936d78.jpg](_assets/images/Mash/621a8cb0-59e6-43cf-a92f-3b5037936d78.jpg)















## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]


