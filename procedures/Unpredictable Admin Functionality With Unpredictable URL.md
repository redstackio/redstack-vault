---
id: e53ec2ef-5f7e-40a6-8e90-e514d0f4be9f
name: Unpredictable Admin Functionality With Unpredictable URL
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T18:07:42.380324+00:00'
updated_at: '2023-05-26T18:24:13.248035+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# Unpredictable Admin Functionality With Unpredictable URL

**Status**: ✓ Verified

## Summary

Description Some application's sensitive functionality is not protected enough ,but concealed by giving it a unpredictable url. This is also called securty by obscurity. Instructions 1. Navigate to the application home page and right click on the applciation's page. Click on developer tools --> ins

## Description

Description



Some application's sensitive functionality is not protected enough ,but concealed by giving it a unpredictable url. This is also called securty by obscurity.



# Instructions





1. Navigate to the application home page and right click on the applciation's page. Click on developer tools --> inspect element







![df5505fd-d1f3-4e8c-9984-95046eb59951.png]()





2.Click on inspector and observe the admin url in the *inspect *element. Copy the admin url.





![bfa472b5-4a5a-4436-8514-ea7c826b472b.png]()





3.Paste the url in the browser window.





![a41dcb23-0e05-4843-92e1-b9b1773ccd62.png]()

4. Observe that you have access to the admin panel without authentication. An attacker can delete the user account.





![f93f585a-5ab1-4172-8078-031c7665575b.png]()





## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]


