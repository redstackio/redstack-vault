---
id: cc4ca29f-dd1e-4ed1-8918-549b48d12d8b
name: User Role Controlled By Request Paramter
type: procedure
verified: false
submitted: false
created_at: '2020-08-31T18:23:18.939853+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# User Role Controlled By Request Paramter

## Summary

Few application's determine the user access rights at login with a hidden filed or parameter in a cookie . An aatacker can modify these parameter values to access unauthorised content. 

## Description

# Description



Few application's determine the user access rights at login with a hidden filed or parameter in a cookie . An aatacker can modify these parameter values to access unauthorised content.



# Instructions





1.Try to access the admin panel from the browser. Observe that the admin panel is not accessible with out credentials.





![cf0e851d-b3d0-49d6-84d2-45c62f1ac804.png](_assets/images/Mash/cf0e851d-b3d0-49d6-84d2-45c62f1ac804.png)





2.Navigate to the login page and intercept the request using burp . Change the cookie parameter *Admin=false* to A*dmin=true*  and submit the request.





![165c7414-d433-4225-85ef-b62e552779df.png](_assets/images/Mash/165c7414-d433-4225-85ef-b62e552779df.png)





3.Observe the response contains a 200 ok 









![2660a423-0605-4540-9c32-1889752c70a9.png](_assets/images/Mash/2660a423-0605-4540-9c32-1889752c70a9.png)





4. Click on admin panel and intercept the request. Modify the cookie parameter *Admin=false* to *Admin=true*





![43f55c4d-abe0-4a95-95ab-ac5b5e1c55e7.png](_assets/images/Mash/43f55c4d-abe0-4a95-95ab-ac5b5e1c55e7.png)





5. Observe the response with 200 ok





![efdab8ef-84b5-44ab-9c17-bd5594ab4683.png](_assets/images/Mash/efdab8ef-84b5-44ab-9c17-bd5594ab4683.png)



6. Go back to browser and observe that admin is looaded in the browser with out authentication.





![b9c42247-d4e8-467d-b33e-98d30923a81e.png](_assets/images/Mash/b9c42247-d4e8-467d-b33e-98d30923a81e.png)



## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]


