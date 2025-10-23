---
id: 3968650a-8ba8-47aa-875f-66d5acdcf373
name: Identifying Blind SQL Injection Out Of Band (Cookie Parameter)
type: procedure
verified: true
submitted: true
created_at: '2020-08-11T15:14:21.935395+00:00'
updated_at: '2023-05-26T18:09:50.714725+00:00'
platforms:
- Web
tags:
- '[[blind SQL]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Identifying Blind SQL Injection Out Of Band (Cookie Parameter)

**Status**: ✓ Verified

## Summary

An attacker will use unvalidated parameters in the application to craft a payload. Once the application executes the payload ,the attacker will recieve response on his server. In this case ,cookie parameter is used for delivering the payload to the application's server. 

## Description

# Description

An attacker will use unvalidated parameters in the application to craft a payload. Once the application executes the payload ,the attacker will recieve response on his server. In this case ,*cookie *parameter is used for delivering the payload to the application's server.





# Instructions



1.Open the application in the browser .









![d9100c04-45cc-4501-8652-c3ca44e9afb0.png](_assets/images/Mash/d9100c04-45cc-4501-8652-c3ca44e9afb0.png)







2. Intercept the request using Burp Suite .Observe the *cookie* parameter *TrackingId. *Launch the Burp collaborator from Burp Menu .(Only available for Burp Professional)





![e6f40be1-7f6a-4962-b003-d28bef6c1523.png](_assets/images/Mash/e6f40be1-7f6a-4962-b003-d28bef6c1523.png)





3.Modify the cookie parameter with payload. Replace the burp collaborator url in the payload with your own payload.







**Code**: [[TrackingId=x'+UNION+SELECT+extractvalue(xmltype('<]]









![cd5006e2-d810-4ea6-ad9d-5abfde50a565.png](_assets/images/Mash/cd5006e2-d810-4ea6-ad9d-5abfde50a565.png)







4.Open the burp collaborator window and click on *poll now . *Observe that there are couple of DNS LOOKUP requests in the collaborator panel which confirms the communication from payload being executed on the applciation's server .





![af79ae4f-193e-406e-b053-a81e8ddce57a.png](_assets/images/Mash/af79ae4f-193e-406e-b053-a81e8ddce57a.png)













## Platforms

- Web

## Tags

- [[blind SQL]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


