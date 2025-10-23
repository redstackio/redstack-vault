---
id: f5566488-b6e4-40c1-b438-8edbbc9ddd85
name: 2FA Bypass using Burp Macros And Intruder
type: procedure
verified: false
submitted: false
created_at: '2020-08-04T18:02:46.716386+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Web
tags:
- '[[authentication bypass]]'
- '[[broken authentication]]'
- '[[Burp]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# 2FA Bypass using Burp Macros And Intruder

## Summary

Description Macros in burpsuite allows us to sent a sequence of HTTP requests to the server prior to the requests which has been proxied by the burp. A set of parameters will be taken from the response of the final macro request which will further be used . In this case, mfa-code from the last resp

## Description

# Description 

Macros in burpsuite allows us to sent a sequence of HTTP requests to the server prior to the requests which has been proxied by the burp. A set of parameters will be taken from the response of the final macro request which will further be used . In this case, *mfa-code *from the last response of the macro is used for bruteforce attack.



# Instruction





1. Login into the application with victim's credentials obtained through different attack techniques with burp intercept off,but still logging requests under proxy--- HTTP history tab  Application will prompt you to enter a 4-digit security code .





![83569eb2-cd0d-480a-9d59-a0eba1d21a53.PNG](_assets/images/Mash/83569eb2-cd0d-480a-9d59-a0eba1d21a53.PNG)









2. Enter wrong 4-digit security code twice which will take you back to the login page with message* incorrect security code* .









![f6cd709f-bd5b-4346-a6cd-a5b047cec147.PNG](_assets/images/Mash/f6cd709f-bd5b-4346-a6cd-a5b047cec147.PNG)





3. Goto *project options  --->   sessions . *Under *sessions , *click* add. *A seperate dialogue box will open* *,goto * scope* and select * include alll URLs.*







![78f1d26f-45a8-4059-a482-fe71f29f91b0.PNG](_assets/images/Mash/78f1d26f-45a8-4059-a482-fe71f29f91b0.PNG)







4. Goto *Details* tab, and under *Rules Actions *click *Add t*o  select *run a macro .*







![66ae9010-56fe-4223-b11e-3f02fe232d0b.PNG](_assets/images/Mash/66ae9010-56fe-4223-b11e-3f02fe232d0b.PNG)









5. Under Select Macro click *add *to add *Macro Recorder* which show all the requests from *HTTP history* tab. 



select the following requests and then click* ok.*





*GET /Login*

*POST /Login*

*GET /Login2*







![619d0372-555f-4827-9d66-b3eeb3a14267.PNG](_assets/images/Mash/619d0372-555f-4827-9d66-b3eeb3a14267.PNG)







6.Under *Macro editor, we can observe the three selected requests . Click on Test Macro *to check that final response contains the request with* 4-digit security code. *Continue to click on *ok *until all dialogue boxes are closed and you are in main burp window







![46a36db1-f3c5-4214-bdb4-690601c208b2.PNG](_assets/images/Mash/46a36db1-f3c5-4214-bdb4-690601c208b2.PNG)







7. Send the *POST /Login2* request from* HTTP History to intruder *tab by right clicking on the request.







![7ad4bebd-e726-4e98-9b10-98754fc00934.PNG](_assets/images/Mash/7ad4bebd-e726-4e98-9b10-98754fc00934.PNG)







8.







![69d2fba9-76f3-4c51-b9c6-75120712c458.PNG](_assets/images/Mash/69d2fba9-76f3-4c51-b9c6-75120712c458.PNG)







9.under* Payloads , *select *numbers *from drop down list.





![3ac315ff-c4a8-4367-b9cb-4f4f04e17fdb.PNG](_assets/images/Mash/3ac315ff-c4a8-4367-b9cb-4f4f04e17fdb.PNG)







10.Insert the values in each parameter as shown below and *start attack*







![aa5c636f-3ddf-40af-a86c-35804dc68ea0.PNG](_assets/images/Mash/aa5c636f-3ddf-40af-a86c-35804dc68ea0.PNG)







11. A new window will open with brute forcing* mfa-code  *parameter with values ranging from 0-9999. A status code response 200 can be observed for every parameter.







![4021ba9c-f0ba-4f41-b01c-1c2650d57d6c.PNG](_assets/images/Mash/4021ba9c-f0ba-4f41-b01c-1c2650d57d6c.PNG)









Continue the attack till there is a* 302 response* observed in the above window. Right click on the request with 302 response code and copy the url and paste it in the browser . We can observe that the login is successful.

## Platforms

- Web

## Tags

- [[authentication bypass]]
- [[broken authentication]]
- [[Burp]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


