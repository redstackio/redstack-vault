---
id: 6bf9f487-b164-43c5-976a-1626ca9118ad
name: 'HTML Injection Reflected URL parameter '
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T16:47:07.781259+00:00'
updated_at: '2023-05-26T18:11:29.969512+00:00'
platforms:
- Web
tags:
- '[[HTML Injection]]'
- '[[injection]]'
- '[[Web Applications]]'
---

# HTML Injection Reflected URL parameter 

**Status**: ✓ Verified

## Summary

Reflected injection vulnerability can be exploited by an attacker by injecting malicious code by manipulating the url parameter. 

## Description

# Description

Reflected injection vulnerability can be exploited by an attacker by injecting malicious code by manipulating the url parameter.



# Instructions

1. Observe the url in the browser and in the body.







![c820c5b5-7bfd-44cb-b4e6-d22f98027b9a.PNG](_assets/images/Mash/c820c5b5-7bfd-44cb-b4e6-d22f98027b9a.PNG)









2. Intercept the request using burp 







![f717bc4c-7422-485c-9ecd-2af477b30bbb.PNG](_assets/images/Mash/f717bc4c-7422-485c-9ecd-2af477b30bbb.PNG)







3. Modify the host parameter in burp request with malicious url. 







![e7bb9b3c-7beb-4d14-b789-a81e1c6d6fa6.PNG](_assets/images/Mash/e7bb9b3c-7beb-4d14-b789-a81e1c6d6fa6.PNG)





4. Modified url has been reflected onto the page as shown below.









![da43e026-b08b-45dd-840f-9332662c5625.PNG](_assets/images/Mash/da43e026-b08b-45dd-840f-9332662c5625.PNG)









## Platforms

- Web

## Tags

- [[HTML Injection]]
- [[injection]]
- [[Web Applications]]


