---
id: 50391873-30fd-4035-bc7f-544e1ce98248
name: Safe Script Tag Injection via Django Templates
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.448522+00:00'
updated_at: '2023-04-10T20:23:30.717649+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Cross-site scripting]]'
- '[[Django Templates]]'
- '[[Server Side Template Injection]]'
---

# Safe Script Tag Injection via Django Templates

## Summary

Safe Script Tag Injection via Django Templates is a technique that can be used to prevent cross-site scripting attacks. This technique involves using the Django Templates engine to safely insert script tags into web pages. By doing this, the script tags are executed on the client-side, which reduce

## Description

# Description

Safe Script Tag Injection via Django Templates is a technique that can be used to prevent cross-site scripting attacks. This technique involves using the Django Templates engine to safely insert script tags into web pages. By doing this, the script tags are executed on the client-side, which reduces the risk of an attacker being able to inject malicious code into the page. This technique can be used to protect against a wide variety of cross-site scripting attacks, including reflected and stored XSS.

From a technical perspective, Safe Script Tag Injection works by using the 'safe' template tag in Django Templates. This tag tells the engine that the content being inserted into the page is safe and should not be escaped. By doing this, any script tags that are inserted into the page will be executed by the client-side browser, rather than being treated as plain text.

The business value of Safe Script Tag Injection is that it provides a simple and effective way to protect web applications against cross-site scripting attacks. By using this technique, organizations can reduce the risk of data breaches, protect their customers' sensitive information, and avoid costly legal and regulatory penalties.

## Requirements

1. Access to a web application that uses the Django Templates engine

1. Knowledge of the 'safe' template tag in Django Templates

## Defense

1. Always sanitize user input before using it in web pages

1. Use a Content Security Policy (CSP) to prevent the execution of untrusted scripts

1. Regularly scan web applications for vulnerabilities using a web application scanner

## Objectives

1. To protect web applications against cross-site scripting attacks

1. To prevent attackers from injecting malicious code into web pages

1. To reduce the risk of data breaches and protect sensitive information

# Instructions

1. The 'safe' filter is used in this example to prevent the script tag from executing. It is a filter that can be applied to a variable in a Django template to mark the variable's contents as safe HTML. When applied, the contents will not be escaped and will be rendered as raw HTML.

**Code**: [[{{ '<script>alert(3)</script>' }}
{{ '<script>aler]]

> The script tag is a common HTML tag used to embed or execute JavaScript code on a webpage. However, this can also be a security vulnerability if the code executed is malicious. In this example, the 'safe' filter is used to prevent the script tag from executing by marking its contents as safe HTML. This ensures that the script tag is rendered as plain text and not executed as code on the webpage.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Cross-site scripting]]
- [[Django Templates]]
- [[Server Side Template Injection]]
