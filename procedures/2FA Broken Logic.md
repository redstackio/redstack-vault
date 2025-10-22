---
id: f6b5c697-6670-4147-a0ee-5a275acf5618
name: 2FA Broken Logic
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T05:40:56.124670+00:00'
updated_at: '2023-05-26T01:29:57.813833+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Web Applications]]'
---

# 2FA Broken Logic

**Status**: ✓ Verified

## Summary

An attacker can use the application's logic to bypass the 2FA authentication and get unauthorised access to victim's account 

## Description

# Description

An attacker can use the application's logic to bypass the 2FA authentication and get unauthorised access to victim's account

# Instructions

1. Login to the application with given credentials and burp running and proxying requests .

2. Notice that the login has 2FA enabled and need to enter 4-digit security code.

3. Intercept the request and notice that verify parameter is used to determine the user 

4.Access your email and notice the 4-digit security code.

5.Enter the 4-digit code to login to the application

6.Identify the GET /Login2  request and send it to intruder tab.

7.From the *intruder* tab,Change the *verify *paramter value to *carlos *

8.From the positions tab, highlight the *mfa-code* value and click on *add *to add the value to position 

9.From payloads tab, enter the details as below and click on *start attack* to start the brute-forcing attack.

10.When the attack finishes , observe that only one response contains *302 response. Make a note of the mfa-code that generated 302 response.*

11.Notice that you are logged in to carlos account with out authentication by bypassing the application's logic.

## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]
