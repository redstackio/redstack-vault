---
id: b37aeb8d-5044-4646-b06f-771a1df2a6a0
name: Brute Force Valid Users from a Forgotten Password Form
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T23:27:07.457615+00:00'
updated_at: '2023-05-26T18:36:07.091192+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Web
tags:
- '[[Web Applications]]'
commands:
- '[[wfuzz Brute Force a HTTP POST Form]]'
---

# Brute Force Valid Users from a Forgotten Password Form

**Status**: ✓ Verified

## Summary

Website login forms often include a 'Forgot Your Password' feature to help users retrieve their passwords. Many of these forms display a different message depending on whether a valid username was entered, allowing attackers to enumerate valid usernames. 

## Description

# Description

Website login forms often include a 'Forgot Your Password' feature to help users retrieve their passwords. Many of these forms display a different message depending on whether a valid username was entered, allowing attackers to enumerate valid usernames.



# Instructions

This example will deal with WordPress, but the concepts are applicable on any web application which discloses whether a user is valid or not.



## Recon

1. Use the "Lost Your Password" link, then enter an invalid username of 'test' to return "ERROR:Invalid username or e-mail".



![e86ffef3-793e-4222-a4ec-50ee5cda046c.png](_assets/images/Mark/e86ffef3-793e-4222-a4ec-50ee5cda046c.png)



2. Entering a valid username returns a different message.



![01c7123a-4486-4866-b14d-9bd2bbad04c6.png](_assets/images/Mark/01c7123a-4486-4866-b14d-9bd2bbad04c6.png)



Use Burp Suite's Interceptor to intercept a POST request to the "Forgot Your Password" form. These parameters can be added to a Wfuzz command to automatically fuzz for valid usernames.



![107d7c10-f02b-4bd9-8542-7b51692becf9.png](_assets/images/Mark/107d7c10-f02b-4bd9-8542-7b51692becf9.png)



From this request, we can determine:

- POST request is sent to: "/wp-login.php?action=lostpassword"

- Data is set to: "user_login=test&redirect_to=&wp-submit=Get+New+Password"



## Dictionary Brute Force

Using the information found in the Recon phase, build the Wfuzz request.





**Command** ([[wfuzz Brute Force a HTTP POST Form]]):

```bash
wfuzz --hc 200 -w $_USERS.txt -u 'http://$_TARGET_IP/wp-login.php?action=lostpassword' -d '$_POST_DATA'
```





Note: In this example, WordPress returns a 200 response for invalid users, so the "--hc 200" is added to suppress these results.

Without "--hc 200"



![0d995cff-0abf-418e-bb69-4e789111a6d6.png](_assets/images/Mark/0d995cff-0abf-418e-bb69-4e789111a6d6.png)

With "--hc 200", a valid username is found returning a 500 response code:



![f91bfb1f-5377-428c-8f25-febdc1ba2798.png](_assets/images/Mark/f91bfb1f-5377-428c-8f25-febdc1ba2798.png)



## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[wfuzz Brute Force a HTTP POST Form]]

## Tags

- [[Web Applications]]


