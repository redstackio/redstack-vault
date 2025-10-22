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

2.Highlight the cookie value and right click on it and select *send to decoder.*

3.Notice that the result *wiener:51dc30ddc473d43a6011e9ebba6ca770 *seems to be* username:md5 of password  . *Use online MD5 Hash cracker to crack the password*.*

4.Logout of the application and send the GET / request to the intruder tab

5.From the intruder window , under positions tab highlight the *stay-logged-in* cookie and click on* add* to add the cookie to the payload posotion

6.1. Under *Payload processing*, add the following rules in order. The rules will be applied sequentially to each payload before the request is submitted. For payloads tab add only the correct password.

*Hash: MD5*

*Add prefix: wiener:*

*Encode: Base64-encode*

7.On the "Options" tab, add a grep match rule to flag any responses containing the words `My account` and start the attack.

8.The attack finishes quickly and the responses are as expected and also it confirms that your payload processing rules work as expected and constructed a valid cookie

9.Now back to intruder window , repeat the same settings as above intruder attack.

10.use the username `carlos` in the "Add prefix" rule and use the list of passwords as the payload set instead of correct password as in step 6.

11.When attack finishes , notice that there is only one response containing *myaccount*.

12.Right click on the response and select copy url .

13.Load the url in the browser and observe that you're now logged in as carlos user with out having to provide credentials.

## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]
