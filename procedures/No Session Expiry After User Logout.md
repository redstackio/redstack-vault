---
id: ed1cbb2b-ea1f-4397-b6eb-bc3e3e4ef7d4
name: No Session Expiry After User Logout
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T18:43:04.369480+00:00'
updated_at: '2023-05-26T18:22:45.114586+00:00'
platforms:
- Web
tags:
- '[[Session Management]]'
- '[[Web Applications]]'
---

# No Session Expiry After User Logout

**Status**: ✓ Verified

## Summary

An attacker can take over the victim's account if the victim's session doesnot gets expired even after logout. 

## Description

# Description

An attacker can take over the victim's account if the victim's session doesnot gets expired even after logout.





# Instructions



1.Login to the application.





![7601beb9-39b9-4aa1-9183-05181fb34433.png]()





2. Install Cookie-editor extension on your browser.







![1a02d1d1-cc1e-4ae4-aea9-5c5bec00ba72.png]()





3.Go to the web page and export all the cookies with the extension





![6216c8e9-6cab-4dad-8865-1ca2ea5045cd.png]()





4.Now log out from the web app





![b7909450-d2f5-4560-b5e8-873b4912da67.png]()





5. Go to the Cookie-editor extension and delete all the cookies and paste the previously copied cookies in the import section and import the cookies.





![32faa126-fe95-4e3e-b4b7-133105c47fe3.png]()







6. Reload the page and see the session still persists.





![c58a8072-a1cd-43dc-8fd8-8c171f1080c1.png]()



## Platforms

- Web

## Tags

- [[Session Management]]
- [[Web Applications]]


