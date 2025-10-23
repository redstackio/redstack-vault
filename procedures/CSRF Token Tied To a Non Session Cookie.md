---
id: fa066408-fc28-4499-8a39-8179257adba9
name: CSRF Token Tied To a Non Session Cookie
type: procedure
verified: true
submitted: true
created_at: '2020-08-25T10:51:02.222275+00:00'
updated_at: '2023-05-26T18:29:53.020873+00:00'
platforms:
- Web
tags:
- '[[CSRF]]'
- '[[Web Applications]]'
---

# CSRF Token Tied To a Non Session Cookie

**Status**: ✓ Verified

## Summary

Some applications implement a session cookie that is not tied to a CSRF token rather to a different token . In this case the csrfkey present in the cookie is not tied to the session cookie. 

## Description

# Description

Some applications implement a session cookie that is not tied to a CSRF token rather to a different token . In this case the csrfkey present in the cookie is not tied to the session cookie.



# Instructions







1.With burp proxying the requests from the browser , identify the *changemail *request and send the request to the repeater tab.







![d562c698-4de0-42a9-a1bc-87c0b10de72e.png]()





2.Observe that changing the session cookie will log you out of the applciation. But changing the csrfkey will show a* invalid csrf token.* With thsi we can confirm that csrfkey in the cookie may not be tied tosession cookie.





![a7df8c8f-38cb-487f-9697-670d1087d0e4.png]()





3. With the burp intercept on , intercept the *changeemail *request from the incognito window 







![5404d514-8292-4963-8893-6865b8cba5a8.png]()





4.Swap the csrfkey in the cookie and csrf token in the body . Observe that the request has been accepted.





![cf8855b2-f333-4ffb-8693-3c7757eaef5e.png]()





5.Bact to the browser and navigate to search function and intercept the search term.Send the request to the repeater tab. Observe that the search term gets reflected in the session cookie header and also the search term doesnot have the CSRF token implemented.



Use this request to inject into cookie header.









![0ba4273a-0b6f-464a-a5e4-3dd99323ce75.png]()







6.Use the following url to inject csrfkey into the victim's browser.



***`/?search=test%0d%0aSet-Cookie:%20csrfKey=your-*ke**y`



![7bf3b1b0-74fe-4b52-a6b7-5652453788a1.png]()







7. Use CSRF PoC generator to genearate a HTML form. With no protection for CSRF for the request, make sure to include CSRF token in the HTML form.





![0eb31aa3-2763-46a3-9ee9-64e17fd95783.png]()





8.Remove the script block from above step and replace it with the following code.

***<img src="$cookie-injection-url" onerror="document.forms[0].submit()*">**



**Send the modified csrfHTML form to the victim . When the victim clicks on the form , victim's emailID will be changed to that of the attacker's**



![b9f7ba44-8410-48a6-bde8-0b0f4ba97bc9.png]()



## Platforms

- Web

## Tags

- [[CSRF]]
- [[Web Applications]]


