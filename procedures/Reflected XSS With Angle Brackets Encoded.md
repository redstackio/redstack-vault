---
id: d46dfca7-55a5-468c-ba98-7ca3466592e9
name: Reflected XSS With Angle Brackets Encoded
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T10:05:07.024482+00:00'
updated_at: '2023-05-26T01:29:19.129287+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS With Angle Brackets Encoded

**Status**: ✓ Verified

## Summary

Descritpion To escape the HTML encode functionality of the application in HTML context , an attacker will use other event handlers to trigger the payload. Instructions 1.Enter random string in the search box. 

## Description

# Descritpion

To escape the HTML encode functionality of the application in HTML context , an attacker will use other event handlers to trigger the payload.



# Instructions





1.Enter random string in the search box.





![4b778e4d-8dfc-4ff7-ab24-5c1c5f284421.png]()





2.Observe that the random string has been reflected inside single quote attribute.





![0da4ca3f-5752-4842-b641-e999f5201a55.png]()





3. Use double quoted payload to escape the single quote attribute and observe the page source after submitting the payload to the server.

*“payloadtype=”alert(1) .*





![4bf2281d-4fb0-4282-b354-0a3c116c9ee2.png]()







4. Craft the following code in such a way that it escapes the quoted attribute from step 2 using an *ocmouseover* event handler.

*` "onmouseover="alert(1*)`





![51e3dfd8-962c-4500-ba61-f56c8e08c4a9.png]()





5. observe the alert pop triggered by the payload from the above step.







![b2b19344-4534-4a7d-ba1b-0a8a5ad5774b.png]()



## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]


