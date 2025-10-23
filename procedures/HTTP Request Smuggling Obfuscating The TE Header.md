---
id: 496ac5cd-3995-4f39-8e5c-873636f2c35c
name: HTTP Request Smuggling Obfuscating The TE Header
type: procedure
verified: true
submitted: true
created_at: '2020-08-12T03:10:39.271680+00:00'
updated_at: '2023-05-26T15:59:38.172684+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[known vulnerability]]'
- '[[Web Applications]]'
---

# HTTP Request Smuggling Obfuscating The TE Header

**Status**: ✓ Verified

## Summary

In this kind of attack, both front end and backend servers support Transfer-Encoding header . But one of the servers can be made not to process the header by obfuscating it in some way. In this case Transfer- encoding header was obfuscated by using another Transfer-Encoding with its value changed. 

## Description

# Description

In this kind of attack, both front end and backend servers support Transfer-Encoding header . But one of the servers can be made not to process the header by obfuscating it in some way. In this case Transfer- encoding header was obfuscated by using another Transfer-Encoding with its value changed.



# Instructions







1.Intercept the request using Burp Suite .







![372f7f22-f969-4b96-8750-1bfb4b6cbfba.jpg](_assets/images/Mash/372f7f22-f969-4b96-8750-1bfb4b6cbfba.jpg)







2.Send the request to the repeater tab.





![622e3a85-7985-40db-8528-d6c79c9af2d4.jpg](_assets/images/Mash/622e3a85-7985-40db-8528-d6c79c9af2d4.jpg)









3.Modify the request to the following in the repeater tab . Observe that Transfer-Encoding Header has been added in the modified request with its value changed to some random string. 







**Code**: [[POST / HTTP/1.1
Host: your-lab-id.web-security-ac]]







4. send the modified request to the application server. Observe the response from the server . This confirms that the modified request is being parsed by the application server.





![d915028e-f4b8-4ce5-b21f-b208249a957c.jpg](_assets/images/Mash/d915028e-f4b8-4ce5-b21f-b208249a957c.jpg)









## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[known vulnerability]]
- [[Web Applications]]


