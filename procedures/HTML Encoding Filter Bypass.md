---
id: 68409cd7-e65c-45d5-8192-e17dc05dbb96
name: HTML Encoding Filter Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.879566+00:00'
updated_at: '2023-04-10T20:21:34.987832+00:00'
tags:
- '[[Bypass using HTML encoding]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# HTML Encoding Filter Bypass

## Summary

HTML encoding filter bypass is an advanced technique used in Cross Site Scripting (XSS) attacks. The attacker uses HTML encoding to bypass the filters implemented by the target application. This technique allows the attacker to inject malicious code into a web page, which can then be executed by un

## Description

# Description

HTML encoding filter bypass is an advanced technique used in Cross Site Scripting (XSS) attacks. The attacker uses HTML encoding to bypass the filters implemented by the target application. This technique allows the attacker to inject malicious code into a web page, which can then be executed by unsuspecting users who visit the page.

From a technical standpoint, HTML encoding involves converting special characters into their corresponding HTML entities. By encoding characters such as '<' and '>', the attacker can bypass filters that are looking for these characters in the input. This allows the attacker to inject malicious code that can be executed by the user's browser.

The business value of this attack is that it can be used to steal sensitive information such as login credentials, credit card numbers, and other personal data. It can also be used to deface websites and spread malware.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of HTML encoding

1. A web browser to execute the attack

 

## Defense

1. Implement input validation to prevent the injection of malicious code

1. Use a Content Security Policy (CSP) to restrict the types of content that can be loaded by the web page

1. Regularly update and patch the web application to prevent known vulnerabilities

 

## Objectives

1. Inject malicious code into a web page

1. Execute the injected code on the victim's browser

1. Steal sensitive information from the victim

 

# Instructions

1. To perform a Cross-Site Scripting (XSS) Attack, the attacker injects malicious code into a web page viewed by other users. The code can be in any language supported by the browser, such as JavaScript. This code can then be executed by unsuspecting users, potentially allowing the attacker to steal sensitive information or take control of the user's account.

 



**Code**: [[%26%2397;lert(1)
&#97;&#108;&#101;&#114;&#116;
></]]



> The 'data' field in this JSON object contains the malicious code that is injected into the web page. The 'lang' field indicates the language of the code, in this case, JavaScript. The 'instruction' field provides an overview of how the attack is performed, and the 'explain' field provides additional details on the attack and its potential consequences. It is important to ensure that input from users is properly sanitized and validated to prevent XSS attacks.

## Tags

- [[Bypass using HTML encoding]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


