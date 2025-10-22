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

2. Enter wrong 4-digit security code twice which will take you back to the login page with message* incorrect security code* .

3. Goto *project options  --->   sessions . *Under *sessions , *click* add. *A seperate dialogue box will open* *,goto * scope* and select * include alll URLs.*

4. Goto *Details* tab, and under *Rules Actions *click *Add t*o  select *run a macro .*

5. Under Select Macro click *add *to add *Macro Recorder* which show all the requests from *HTTP history* tab. 

select the following requests and then click* ok.*

*GET /Login*

*POST /Login*

*GET /Login2*

6.Under *Macro editor, we can observe the three selected requests . Click on Test Macro *to check that final response contains the request with* 4-digit security code. *Continue to click on *ok *until all dialogue boxes are closed and you are in main burp window

7. Send the *POST /Login2* request from* HTTP History to intruder *tab by right clicking on the request.

8.

9.under* Payloads , *select *numbers *from drop down list.

10.Insert the values in each parameter as shown below and *start attack*

11. A new window will open with brute forcing* mfa-code  *parameter with values ranging from 0-9999. A status code response 200 can be observed for every parameter.

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
