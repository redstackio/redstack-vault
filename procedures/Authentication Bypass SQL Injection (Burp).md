---
id: 73c998d2-d9ec-4231-8bc3-3a5e4c2150ae
name: Authentication Bypass SQL Injection (Burp)
type: procedure
verified: true
submitted: true
created_at: '2020-07-23T10:59:25.216198+00:00'
updated_at: '2023-05-26T01:13:57.561193+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Burp]]'
- '[[hacking]]'
- '[[injection]]'
- '[[SQL]]'
- '[[sqli]]'
---

# Authentication Bypass SQL Injection (Burp)

**Status**: ✓ Verified

## Summary

Burp Intruder can be used to perform authentication bypass using SQL payloads. Intruder will brute-force the login form with the provided SQL payloads in the username and password fields. Successful authentication can be identified by looking at the HTTP status code/response/content length. 

## Description

# Description

Burp Intruder can be used to perform authentication bypass using SQL payloads. Intruder will brute-force the login form with the provided SQL payloads in the username and password fields. Successful authentication can be identified by looking at the HTTP status code/response/content length.

# Instructions



1. Enter username and password in the login page





![7a01f8ce-e90b-491c-87cf-e1a6568982a1.jpg](_assets/images/Mash/7a01f8ce-e90b-491c-87cf-e1a6568982a1.jpg)

2. Intercept the login request using Burp Suite





![4500d1cc-091b-462a-b2c1-90a4c7949684.jpg](_assets/images/Mash/4500d1cc-091b-462a-b2c1-90a4c7949684.jpg)







3. Right-click on the intercepted request and sent it to intruder as shown below





![9dfeb202-84b3-4f07-b4bc-a9f3db24ed6b.jpg](_assets/images/Mash/9dfeb202-84b3-4f07-b4bc-a9f3db24ed6b.jpg)





4. Identify the username and password fields, select the value and click on *Add* button







![805f6cca-594d-4b6f-8b4e-978ea888a563.jpg](_assets/images/Mash/805f6cca-594d-4b6f-8b4e-978ea888a563.jpg)





5. Select the attack type from the drop down list. Here, based on our requirement *Pitchfork* is selected.







![91bb8072-48a0-47d5-8879-8e1bd2759a67.jpg]()









6. In the payloads tab, select list 1 and add set of payloads as shown below. This list will be considered as usernames.







![112c499e-f6af-496b-b066-4142d66d4ff6.jpg](_assets/images/Mash/112c499e-f6af-496b-b066-4142d66d4ff6.jpg)





7. Select list 2 and add another set of payloads that are considered to be used as passwords. Click on *Start attack* button.





![ac3778f5-6c76-4737-bfcf-09513ff8dc8d.jpg](_assets/images/Mash/ac3778f5-6c76-4737-bfcf-09513ff8dc8d.jpg)









8. The Intruder attack window shows all the payloads and corresponding response status code along with the content length. In the below example, last two payloads have the response code as 302 and it can also be observed that the response contains Set-Cookie header which only is received if the authentication is success.









![288fe608-6e07-4987-a60c-3cdeef081072.jpg]()























## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Burp]]
- [[hacking]]
- [[injection]]
- [[SQL]]
- [[sqli]]


