---
id: 9f809f60-eba3-499b-bfcb-1cdecc1df4b5
name: CSRF Attack with Bypassed Referer Header Validation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:55.583740+00:00'
updated_at: '2023-04-06T03:55:55.607093+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
- '[[Spearphishing Attachment|T1193 - Spearphishing Attachment]]'
tags:
- '[[Basic payload]]'
- '[[Bypass referer header validation]]'
- '[[Cross-Site Request Forgery]]'
commands:
- '[[Bypass referer header validation]]'
- '[[Create a malicious web page with a hidden form]]'
- '[[Host the malicious web page]]'
- '[[Perform the action on the target web application]]'
- '[[Trick the user into visiting the malicious web page]]'
---

# CSRF Attack with Bypassed Referer Header Validation

## Summary

A CSRF attack with bypassed referer header validation is a type of attack where an attacker tricks a user into performing an action on a web application without their knowledge or consent. The attacker creates a malicious web page that contains a hidden form that performs the desired action on the 

## Description

# Description

A CSRF attack with bypassed referer header validation is a type of attack where an attacker tricks a user into performing an action on a web application without their knowledge or consent. The attacker creates a malicious web page that contains a hidden form that performs the desired action on the target web application. When the user visits the malicious web page, the form is automatically submitted, and the action is performed on the target web application. By bypassing referer header validation, the attacker can make the request appear legitimate to the target web application. This attack can be used to perform actions such as changing a user's password, transferring funds, or making unauthorized purchases.

 

## Requirements

1. Access to a web application vulnerable to CSRF attacks

 

## Defense

1. Implement referer header validation to ensure that requests are coming from legitimate sources.

1. Use anti-CSRF tokens to prevent attackers from generating legitimate-looking requests.

1. Educate users on the dangers of clicking on links from untrusted sources.

 

## Objectives

1. Perform unauthorized actions on a target web application

1. Bypass referer header validation

 

# Instructions

1. 

 



**Code**: [[1) Create a malicious web page with a hidden form ]]



> The attacker creates a malicious web page that contains a hidden form that performs the desired action on the target web application. By bypassing referer header validation, the attacker can make the request appear legitimate to the target web application. The user is tricked into visiting the malicious web page, and the form is automatically submitted, performing the action on the target web application.



**Command** ([[Create a malicious web page with a hidden form]]):

```bash
1) Create a malicious web page with a hidden form that performs the desired action on the target web application.
```





**Command** ([[Bypass referer header validation]]):

```bash
2) Bypass referer header validation by setting the referer header to the target web application's domain.
```





**Command** ([[Host the malicious web page]]):

```bash
3) Host the malicious web page on a server under the attacker's control.
```





**Command** ([[Trick the user into visiting the malicious web page]]):

```bash
4) Trick the user into visiting the malicious web page.
```





**Command** ([[Perform the action on the target web application]]):

```bash
5) The form is automatically submitted, and the action is performed on the target web application.
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Scripting|T1064 - Scripting]]
- [[Spearphishing Attachment|T1193 - Spearphishing Attachment]]

## Commands Used

- [[Bypass referer header validation]]
- [[Create a malicious web page with a hidden form]]
- [[Host the malicious web page]]
- [[Perform the action on the target web application]]
- [[Trick the user into visiting the malicious web page]]

## Tags

- [[Basic payload]]
- [[Bypass referer header validation]]
- [[Cross-Site Request Forgery]]


