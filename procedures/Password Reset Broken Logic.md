---
id: 26b40818-e691-4cb2-80b2-117420e72a3c
name: Password Reset Broken Logic
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T16:19:37.720885+00:00'
updated_at: '2023-05-26T01:09:34.963005+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Web Applications]]'
---

# Password Reset Broken Logic

**Status**: ✓ Verified

## Summary

Most of the applications will send an email with an unique url to reset the password. During the reset process, the functional logic can be exploited to change the user's password. 

## Description

# Description

Most of the applications will send an email with an unique url to reset the password. During the reset process, the functional logic can be exploited to change the user's password.





# Instructions





1.Login to the application  with the credentials provided. Keep the burp running while it is intercepting the requests from the browser.





![6e6a8794-0d07-485c-869d-0bc022134967.png]()



2.Enter the username and click on submit 





![3c8508ca-52c0-4be5-a113-252af76eacba.png]()







3. Access email to check for password link.





![c42d2512-be3a-42e6-8658-be5899fdec18.png]()





4.Click on the link to change the password





![c4b39a92-c5d7-4edb-8573-babe17a6cbbf.png]()





5. Enter new password and confirm password.





![d144b122-c856-414f-8cee-ff593154f29b.png]()





6.From the HTTP history , identify the request with POST forgot-password and send the request to the repeater tab.Observe the temp-forgot-password-token in the url and body as well.







![8cbebff0-b2ff-473f-a6b6-7fb325fbd9d3.png]()





7.Remove the forgot-password-token value from the url and body . Change the username to *carlos *and submit the request to the server. Observe the *302 *response. Now from the browser, enter new password and submit to change the password of *carlos*.







![64640094-55ee-4fa3-9012-cbf5e9fc0259.png]()







8. Login to the application using newly changed password.





![b0da13e6-032b-416b-b7fc-4056fdfdfc0a.png]()



## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]


