---
id: 9978fcc1-7919-4aa7-98cd-65d2ba9ab990
name: Client-side Desynchronization through Request Smuggling
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.083955+00:00'
updated_at: '2023-04-10T20:23:23.135421+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Client-side desync]]'
- '[[Request Smuggling]]'
---

# Client-side Desynchronization through Request Smuggling

## Summary

Client-side desynchronization through request smuggling is a technique used by attackers to bypass security measures put in place by web applications. By exploiting the way that web servers and proxies handle HTTP requests, attackers can insert malicious requests into legitimate traffic, causing th

## Description

# Description

Client-side desynchronization through request smuggling is a technique used by attackers to bypass security measures put in place by web applications. By exploiting the way that web servers and proxies handle HTTP requests, attackers can insert malicious requests into legitimate traffic, causing the client to receive and execute unexpected responses. This can lead to the execution of malicious code, disclosure of sensitive information, and other attacks. From an offensive perspective, this technique can be used to bypass WAFs, IDSs, and other security measures put in place by the target organization. Technical explanation: An attacker can use the HTTP request smuggling technique to exploit the differences in how web servers and proxies handle HTTP requests. By sending specially crafted requests that contain conflicting headers, an attacker can cause the server and proxy to interpret the request in different ways. This can result in the client receiving unexpected responses, which can be used to execute malicious code or steal sensitive information. Business Value: This technique can be used by attackers to bypass security measures put in place by web applications, allowing them to execute attacks that would otherwise be blocked.

 

## Requirements

1. Access to the target organization's web application

1. Knowledge of the HTTP request smuggling technique

1. Ability to craft and send malicious requests

 

## Defense

1. Implement strict input validation and sanitization to prevent malicious input from being processed

1. Configure web servers and proxies to handle HTTP requests consistently

1. Use WAFs, IDSs, and other security measures to detect and block malicious requests

 

## Objectives

1. To bypass security measures put in place by the target organization

1. To execute attacks that would otherwise be blocked

 

# Instructions

1. To execute this command, replace the URL in the `fetch` function with the URL of the vulnerable website. The `body` parameter should contain the HTTP request to be sent, including the payload for the XSS attack. The `credentials` parameter should be set to `include` to include any cookies for the target domain. The `mode` parameter should be set to `cors` to prevent the browser from following the redirect and allowing the attack to be executed.

 



**Code**: [[fetch('https://www.example.com/redirect', {
    me]]



> This command sends a POST request to a vulnerable website with a specially crafted HTTP request containing an XSS payload in the `x` parameter of the `GET` request. The `mode` parameter is set to `cors` to prevent the browser from following the redirect and allowing the attack to be executed. If the attack is successful, the payload will be executed in the context of the vulnerable website, allowing an attacker to steal sensitive information, perform actions on behalf of the victim, or perform other malicious actions.

2. To resolve this issue, you can try the following commands:
1. Use a different HTTP method, such as POST or PUT, instead of GET.
2. Check the server logs to identify any errors or misconfigurations.
3. Try accessing the resource directly without any query parameters.
4. If the issue persists, contact the server administrator for further assistance.

 



**Code**: [[GET /x?x=&lt;script&gt;...]]



> The GET request with a query parameter containing a script tag is being misinterpreted by the server, causing it to return a 404 error with a content-length. This may be due to a misconfiguration on the server or a security measure in place to prevent cross-site scripting attacks. Using a different HTTP method or accessing the resource directly may help bypass this issue. If the issue persists, it is recommended to contact the server administrator for further assistance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Client-side desync]]
- [[Request Smuggling]]


