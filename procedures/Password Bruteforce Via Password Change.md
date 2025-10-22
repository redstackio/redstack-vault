---
id: 9f07f4b3-a211-4856-86be-714da33f021b
name: Password Bruteforce Via Password Change
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T13:43:58.812507+00:00'
updated_at: '2023-05-26T18:08:02.085621+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Web Applications]]'
---

# Password Bruteforce Via Password Change

**Status**: ✓ Verified

## Summary

Password change functioanlity can be used by an attacker to bruteforce and identify the password if there are no sufficient protections inplace. 

## Description

# Description

Password change functioanlity can be used by an attacker to bruteforce and identify the password if there are no sufficient protections inplace.

# Instructions

1. Login to the application with Weiner credentials. Open the burpsuite and configure the browser to intercept the requests.

2.Access my account and observe that there is a change password functionality where a current password , new password and confirm new password fields are required to change the password. Intercept the *changepassword *request.

3.Back to login page and try to login with incorrect credentials twice and observe the error pages.

4.Enter the incorrect password and observe the response from the server. It says *Current password is incorrect*.

5.Now enter the current password and in new password fileds enter two different password. Response says *New passwords do not match*.

6.Identify the change password request from HTTP History and send the request to intruder tab.Make sure that the new password parameters are different.

7.Two password parameters are different *new-password-1=hacker888&new-password-2=hacker999*

8.From the positions tab in the intruder window , highlight the current password and click on add to the *current password* parameter to the payload position.

9.Navigate to payloads tab and select* simple list* for payload type. Paste the list of passwords in the tab.

Password list can be obtained from:[*https://github.com/1N3/IntruderPayload](https://github.com/1N3/IntruderPayloads)s*

10. Go to options tab from the intruder window and add a grep match rule to flag responses containing *New passwords do not match*. Click on *start attack *

12.observe that one response contains* `New passwords do not match*` message, Make a note of the password for this request

13.Login with the identified password from the above step

## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]
