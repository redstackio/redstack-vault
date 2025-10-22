---
id: 8be5abc5-47bf-4c1b-aae8-c57e46d7982c
name: Cross Site Scripting - Bypassing cookie blacklist with window.cookieStore.get()
  method
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.698390+00:00'
updated_at: '2023-04-10T20:21:40.910395+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Bypass document.cookie blacklist]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
commands:
- '[[Get Cookie Value]]'
---

# Cross Site Scripting - Bypassing cookie blacklist with window.cookieStore.get() method

## Summary

Cross Site Scripting (XSS) is a type of injection attack where malicious scripts are injected into trusted websites. In this procedure, we will bypass the blacklist on document.cookie by using the window.cookieStore.get() method. This method allows us to access the cookies of the current website, e

## Description

# Description

Cross Site Scripting (XSS) is a type of injection attack where malicious scripts are injected into trusted websites. In this procedure, we will bypass the blacklist on document.cookie by using the window.cookieStore.get() method. This method allows us to access the cookies of the current website, even if they are not accessible through document.cookie. By exploiting this vulnerability, we can steal sensitive information such as session IDs and login credentials. This technique can be used to gain initial access to a system or to escalate privileges once access has been gained.

Technical Explanation: The window.cookieStore.get() method is used to retrieve cookies for the current website. This method is not affected by the same-origin policy, which means that it can access cookies from other domains. By using this method, we can bypass the blacklist on document.cookie and access the cookies of the current website.

Business Value: This attack can have severe consequences for businesses, as it can lead to the theft of sensitive information and the compromise of user accounts. By using this technique, attackers can gain access to internal systems and steal intellectual property or financial information.

## Requirements

1. Access to a vulnerable website

1. Knowledge of the window.cookieStore.get() method

## Defense

1. Implement input validation and output encoding to prevent XSS attacks

1. Use HttpOnly and Secure flags to protect cookies

1. Regularly update and patch web applications to prevent vulnerabilities

## Objectives

1. Bypass the document.cookie blacklist

1. Access sensitive information such as session IDs and login credentials

1. Gain initial access to a system

1. Escalate privileges once access has been gained

# Instructions

1. To access a specific cookie using window.cookieStore.get() method, replace 'COOKIE NAME' with the name of the cookie you want to access. The method returns a Promise which resolves to the cookie value. You can then use the value as per your requirements.

The 'window.cookieStore.get()' method is used to retrieve the value of a specific cookie. The method takes the name of the cookie as an argument and returns a Promise which resolves to the cookie value. The 'then()' method is used to handle the resolved Promise and the cookie value is passed as an argument to the callback function. In this case, the value is displayed using the 'alert()' method. You can replace the 'alert()' method with any other method to use the cookie value as per your requirements. This method can be used on Chrome, Edge, and Opera browsers.

**Command** ([[Get Cookie Value]]):

```bash
window.cookieStore.get('COOKIE NAME').then((cookieValue)=>{alert(cookieValue.value);});
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Get Cookie Value]]

## Tags

- [[Bypass document.cookie blacklist]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
