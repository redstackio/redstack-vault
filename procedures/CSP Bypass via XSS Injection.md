---
id: 16a8db57-49ad-40d9-ada2-7e9eab594c69
name: CSP Bypass via XSS Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.280672+00:00'
updated_at: '2023-04-10T20:21:32.580274+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Regsvr32|T1117 - Regsvr32]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Bypass CSP by [@404death](https://twitter.com/404death/status/1191222237782659072)]]'
- '[[Cross Site Scripting]]'
- '[[CSP Bypass]]'
---

# CSP Bypass via XSS Injection

## Summary

Cross Site Scripting (XSS) is a type of attack where an attacker injects malicious code into a web page viewed by other users. CSP Bypass via XSS Injection is a technique where an attacker leverages an XSS vulnerability to bypass the Content Security Policy (CSP) implemented on a website. CSP is a 

## Description

# Description

Cross Site Scripting (XSS) is a type of attack where an attacker injects malicious code into a web page viewed by other users. CSP Bypass via XSS Injection is a technique where an attacker leverages an XSS vulnerability to bypass the Content Security Policy (CSP) implemented on a website. CSP is a security feature that helps prevent XSS attacks by restricting the sources from which a website can load scripts. By bypassing CSP, an attacker can execute arbitrary code on a website, potentially compromising sensitive user data or taking control of the website.

To bypass CSP using XSS Injection, an attacker can inject a malicious script into a vulnerable web page. The script can then be executed by the browser, allowing the attacker to bypass CSP restrictions and execute arbitrary code on the website. This technique can be used to steal user credentials, perform phishing attacks or deliver malware to unsuspecting users.

The business value of this technique is that it allows an attacker to bypass a security feature implemented on a website, potentially compromising sensitive user data and damaging the reputation of the website.

## Requirements

1. Access to a vulnerable website

1. Knowledge of XSS Injection techniques

## Defense

1. Implement strict input validation to prevent XSS vulnerabilities

1. Implement a strong CSP policy to restrict the sources from which a website can load scripts

1. Regularly scan for and patch vulnerabilities on your website

## Objectives

1. Bypass the CSP implemented on a website

1. Execute arbitrary code on a website

1. Steal user credentials

1. Perform phishing attacks

1. Deliver malware to unsuspecting users

# Instructions

1. Use this command to specify the sources for script content that can be executed on the page. The sources can be whitelisted or blacklisted based on the CSP policy.

**Code**: [[script-src &#39;self&#39; data:]]

> The 'script-src' directive specifies the valid sources for JavaScript. In this example, the sources allowed are the same origin ('self') and data: URIs. This command can be used to prevent cross-site scripting (XSS) attacks by controlling the sources of script content that can be executed on the page.

2. To execute a cross-site scripting (XSS) attack, an attacker can inject malicious code into a vulnerable web page by using the script tag. The script tag can be used to load external scripts or execute inline scripts. In this example, the attacker has injected a script tag with a source that executes an alert(1) function. When the page is loaded, the script is executed and the alert message is displayed.

**Code**: [[<script src="data:,alert(1)">/</script>]]

> The 'data' field contains the payload that is being injected. The 'lang' field specifies the programming language used in the payload. The 'text' field can be used to include any additional text or comments. The 'instruction' field provides step-by-step instructions on how to execute the attack. The 'explain' field provides a detailed explanation of the attack, including the impact and potential mitigations.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Regsvr32|T1117 - Regsvr32]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Bypass CSP by [@404death](https://twitter.com/404death/status/1191222237782659072)]]
- [[Cross Site Scripting]]
- [[CSP Bypass]]
