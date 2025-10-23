---
id: 14f90ae4-8fca-4514-9e15-3a68ff8ae9b0
name: Identifying Blind SSRF Out Of Band
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T10:00:54.169116+00:00'
updated_at: '2023-05-26T01:10:01.246777+00:00'
platforms:
- Web
tags:
- '[[Outof Band]]'
- '[[SSRF]]'
- '[[Web Applications]]'
---

# Identifying Blind SSRF Out Of Band

**Status**: ✓ Verified

## Summary

An attacker can exploit the ssrf by issuing backend HTTP request to the application , but the response from the backend request is not returned in the application's response. 

## Description

# Description

An attacker can exploit the ssrf by issuing backend HTTP request to the application , but the response from the backend request is not returned in the application's response.



# Instructions





1. Start the Collaborator in Burp Suite  professional and click on *copy to clipboard* to copy the collaborator URL.





![701ba61c-a1da-461e-8319-1f5f19005e2d.png](_assets/images/Mash/701ba61c-a1da-461e-8319-1f5f19005e2d.png)





2. Intercept the following request and right click on the request and select *send to repeater*





![328dbb01-ecce-48cb-b5f7-29ffc9d7ba6f.png](_assets/images/Mash/328dbb01-ecce-48cb-b5f7-29ffc9d7ba6f.png)





3.Modify the referer header to the* colloborator URL*  from step 1 and send the request to server in repeater tab .







![71b336f1-b1df-4460-b2b4-eb7066dd7f2f.png](_assets/images/Mash/71b336f1-b1df-4460-b2b4-eb7066dd7f2f.png)







4.Go back to the Burp Collaborator client window, and click "Poll now". You should see some DNS and HTTP interactions that were initiated by the application as the result of your payload.



![2638b7d8-bb2d-4867-8535-7de18d307cad.png](_assets/images/Mash/2638b7d8-bb2d-4867-8535-7de18d307cad.png)







## Platforms

- Web

## Tags

- [[Outof Band]]
- [[SSRF]]
- [[Web Applications]]


