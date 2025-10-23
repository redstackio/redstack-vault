---
id: 3eb43c75-dfcc-423c-882f-c4ae8625bdde
name: Brute-force a Stay-logged-in Cookie
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T18:13:33.631001+00:00'
updated_at: '2023-05-26T18:50:37.090970+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Web Applications]]'
---

# Brute-force a Stay-logged-in Cookie

**Status**: ✓ Verified

## Summary

Stay-logged-in will allow users to stay logged in even after browser is closed. This implementation can be manipulated by an attacker to gain un-authorised access or sometimes lead to account take over. 

## Description

# Description

Stay-logged-in will allow users to stay logged in even after browser is closed. This implementation can be manipulated by an attacker to gain un-authorised access or sometimes lead to account take over.

# Instructions





1.Login to the application while burp is running and proxying the requests. Notice that the cookie contains *stay-logged-in.*





![0a8666df-986d-4479-a688-bfe64f53a213.png](_assets/images/Mash/0a8666df-986d-4479-a688-bfe64f53a213.png)





2.Highlight the cookie value and right click on it and select *send to decoder.*





![23e69b2a-077b-4e07-9c28-d0dd836ab0eb.png](_assets/images/Mash/23e69b2a-077b-4e07-9c28-d0dd836ab0eb.png)





3.Notice that the result *wiener:51dc30ddc473d43a6011e9ebba6ca770 *seems to be* username:md5 of password  . *Use online MD5 Hash cracker to crack the password*.*





![1bb88c3d-44c5-45cd-9985-817f26acabe1.png](_assets/images/Mash/1bb88c3d-44c5-45cd-9985-817f26acabe1.png)





4.Logout of the application and send the GET / request to the intruder tab







![2a3c503a-99f1-445a-89fc-242a33841012.png](_assets/images/Mash/2a3c503a-99f1-445a-89fc-242a33841012.png)





5.From the intruder window , under positions tab highlight the *stay-logged-in* cookie and click on* add* to add the cookie to the payload posotion





![3f477e92-f21a-475e-84dd-496f524edcbd.png](_assets/images/Mash/3f477e92-f21a-475e-84dd-496f524edcbd.png)





6.1. Under *Payload processing*, add the following rules in order. The rules will be applied sequentially to each payload before the request is submitted. For payloads tab add only the correct password.

*Hash: MD5*

*Add prefix: wiener:*

*Encode: Base64-encode*





![5e9eb781-d10e-4148-8391-c01f0d12f443.png](_assets/images/Mash/5e9eb781-d10e-4148-8391-c01f0d12f443.png)





7.On the "Options" tab, add a grep match rule to flag any responses containing the words `My account` and start the attack.





![f15267c9-95a6-47db-b225-3f7991676f3c.png](_assets/images/Mash/f15267c9-95a6-47db-b225-3f7991676f3c.png)





8.The attack finishes quickly and the responses are as expected and also it confirms that your payload processing rules work as expected and constructed a valid cookie







![e54e26af-004d-4f5f-bc1e-4097d6c42d88.png](_assets/images/Mash/e54e26af-004d-4f5f-bc1e-4097d6c42d88.png)





9.Now back to intruder window , repeat the same settings as above intruder attack.









![f09f1e4c-444c-481d-9111-9875d2c99429.png](_assets/images/Mash/f09f1e4c-444c-481d-9111-9875d2c99429.png)





10.use the username `carlos` in the "Add prefix" rule and use the list of passwords as the payload set instead of correct password as in step 6.





![3a75abf0-5857-432b-93ae-0d3357737fb4.png](_assets/images/Mash/3a75abf0-5857-432b-93ae-0d3357737fb4.png)





11.When attack finishes , notice that there is only one response containing *myaccount*.





![77164f42-196d-48da-85ac-e401402962d9.png](_assets/images/Mash/77164f42-196d-48da-85ac-e401402962d9.png)





12.Right click on the response and select copy url .





![b5273680-8b9d-45b9-a975-95e2307adb52.png](_assets/images/Mash/b5273680-8b9d-45b9-a975-95e2307adb52.png)





13.Load the url in the browser and observe that you're now logged in as carlos user with out having to provide credentials.





![d1713856-c9ec-4c5f-99de-c71d141d08d8.png]()







## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]


