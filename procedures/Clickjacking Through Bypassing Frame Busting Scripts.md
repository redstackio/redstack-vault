---
id: 942d4857-3198-4444-81aa-8724bc120614
name: Clickjacking Through Bypassing Frame Busting Scripts
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T12:45:20.713986+00:00'
updated_at: '2023-05-26T01:04:39.765777+00:00'
platforms:
- Web
tags:
- '[[Clickjacking]]'
- '[[frame buster]]'
- '[[Web Applications]]'
---

# Clickjacking Through Bypassing Frame Busting Scripts

**Status**: ✓ Verified

## Summary

Frame busting scripts are used as client side security mechanism by restricting the framing capabilities of the application. Sandbox attribute of HTML5 is used to bypass the frame busting script. 

## Description

# Description

Frame busting scripts are used as client side security mechanism by restricting the framing capabilities of the application. *Sandbox attribute *of HTML5 is used to bypass the frame busting script.



# 

# Instructions

# 

1. Create  an account as a legitimate user of the application and login to the application.





![b04a6e6c-9684-40fb-8afa-b12743c69bb0.PNG]()









2. After login into the application , access the *change email *to observe the url and tha page.





![3ffbd992-2c88-4976-9410-447f26522cfb.PNG]()





3.Create a HTML page with sandbox attribute to "*allow-forms". * A similar page as below can be created with all the corresponding attributes and values.



Observe the sandbox attribute with "allow-forms" .





**Code**: [[<style>
   iframe {
       position:relative;
 ]]









4. Save the code from step 3 with html extension and send the link to the victim through social engineering .





Opaque is set to 0.1 in the code from step  3. If needed opaque can be set to much lower level to make the original application completely invisible.



![6d6dc55e-42d7-4d7f-9b67-71db47d55402.PNG]()



5.  Attacker's email Id is updated in the url provided to victim which can be observed below.



![a1e87524-9c0e-4017-b86f-6c20770ff286.PNG]()





6. A victim upon clicking the malicious link , will get the email changed to attacker provided email without knowing of the victim.





![c0f50782-03ad-4730-836f-80600a3864fc.PNG]()





## Platforms

- Web

## Tags

- [[Clickjacking]]
- [[frame buster]]
- [[Web Applications]]


