---
id: 011c74d7-5e91-485e-8a33-d50c70ca2108
name: Blind OS Command Injection With Output Redirection
type: procedure
verified: true
submitted: true
created_at: '2020-08-30T18:31:31.868887+00:00'
updated_at: '2023-05-26T01:29:31.504897+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[os command injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Blind OS Command Injection With Output Redirection

**Status**: ✓ Verified

## Summary

In this kind of attack , an attacker will exploit the OS commnad injection vulnerability but no response can be seen immediately on the application's page. Instead attacker will redirect the output of the payload to a file which when accessed by an attacker will show the resultant output. 

## Description

# Description

In this kind of attack , an attacker will exploit the OS commnad injection vulnerability but no response can be seen immediately on the application's page. Instead attacker will redirect the output of the payload to a file which when accessed by an attacker will show the resultant output.

# Instructions

1.Navigate to feedback form of the application and enter the details to submit the feedback. Intercept the request using burp intruder tab and send the request to repeater tab.

2.Modify the email paramter with the following payload and send the request to the server.

*`email=||whoami>/var/www/images/output.txt|*|`

3.Observe that the server gives a 200 ok response.

4.Using burp intruder tab, intercept the resquest that loads the image of the product.

5.Modify the url paramter to access the email paramter in step 2 .

6.Change the url to the following to access the file uploaded in step 2 and send the request to the server ,

*filename=output.txt*

7. Observe that the response contains the output of the redirect file from Step2 showing the current username.

## Platforms

- Web

## Tags

- [[injection]]
- [[os command injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
