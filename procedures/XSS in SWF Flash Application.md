---
id: f5411930-56bd-4034-bdb1-4e03c799dbaf
name: XSS in SWF Flash Application
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.110342+00:00'
updated_at: '2023-04-10T20:21:40.558498+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Drive-by Compromise|T1189 - Drive-by Compromise]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in files]]'
- '[[XSS in SWF flash application]]'
commands:
- '[[XSS demo on browsers other than IE]]'
- '[[XSS demo on IE8]]'
- '[[XSS demo on IE9]]'
---

# XSS in SWF Flash Application

## Summary

XSS in SWF Flash Application is a type of attack where an attacker injects malicious code into a SWF file that can be executed when the file is loaded by a web page. The attacker can use this attack to steal sensitive information from the user, such as session cookies, and to perform actions on the

## Description

# Description

XSS in SWF Flash Application is a type of attack where an attacker injects malicious code into a SWF file that can be executed when the file is loaded by a web page. The attacker can use this attack to steal sensitive information from the user, such as session cookies, and to perform actions on the user's behalf, such as making unauthorized purchases. This attack can be executed by tricking the user into visiting a website that contains the malicious SWF file or by exploiting a vulnerability in a web application that allows the attacker to upload the malicious SWF file. 

Technical Explanation: The attacker creates a SWF file that contains malicious code, such as JavaScript. The attacker then injects the malicious code into the file using a technique such as DOM-based XSS or Stored XSS. When the user visits a web page that loads the SWF file, the malicious code is executed in the user's browser. This allows the attacker to steal sensitive information from the user and to perform actions on the user's behalf. 

Business Value: This attack can result in the theft of sensitive information, such as user credentials, credit card numbers, and other personal information. It can also result in financial loss for the victim if the attacker uses the stolen information to make unauthorized purchases.

## Requirements

1. Access to a vulnerable web application or the ability to trick the user into visiting a website that contains the malicious SWF file.

1. Knowledge of SWF file format and how to inject malicious code into it.

## Defense

1. Implement input validation and sanitization to prevent injection of malicious code into SWF files.

1. Use Content Security Policy (CSP) to restrict the sources from which SWF files can be loaded.

1. Regularly update and patch web applications to ensure that known vulnerabilities are addressed.

## Objectives

1. To inject and execute malicious code in a SWF file that can be used to steal sensitive information from the user or perform actions on the user's behalf.

1. To gain unauthorized access to a web application by exploiting a vulnerability that allows the attacker to upload a malicious SWF file.

# Instructions

1. This command is used to perform an XSS (Cross-Site Scripting) attack on a target website. The 'data' field contains URLs for different browsers that can be used to execute the attack. The 'explain' field provides more details on how to use these URLs.

**Code**: [[Browsers other than IE: http://0me.me/demo/xss/xss]]

> For browsers other than IE, use the URL provided in the 'data' field and replace the 'alert(document.domain);' part with your own payload. For IE8, use the URL provided in the 'data' field and replace the 'alert(document.domain)' part with your own payload. If the payload throws an error, the browser will redirect to the previous page. For IE9, use the URL provided in the 'data' field and replace 'invalidfileinvalidfileinvalidfile' with your own payload. The payload will open a new window and then close it after 1ms, triggering the 'alert' function with the URL of the new window. Note that XSS attacks can be illegal and should only be performed on websites with permission from the owner.

**Command** ([[XSS demo on browsers other than IE]]):

```bash
http://0me.me/demo/xss/xssproject.swf?js=alert(document.domain);
```

**Command** ([[XSS demo on IE8]]):

```bash
http://0me.me/demo/xss/xssproject.swf?js=try{alert(document.domain)}catch(e){ window.open(‘?js=history.go(-1)’,’_self’);}
```

**Command** ([[XSS demo on IE9]]):

```bash
http://0me.me/demo/xss/xssproject.swf?js=w=window.open(‘invalidfileinvalidfileinvalidfile’,’target’);setTimeout(‘alert(w.document.location);w.close();’,1);
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Drive-by Compromise|T1189 - Drive-by Compromise]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[XSS demo on browsers other than IE]]
- [[XSS demo on IE8]]
- [[XSS demo on IE9]]

## Tags

- [[Cross Site Scripting]]
- [[XSS in files]]
- [[XSS in SWF flash application]]
