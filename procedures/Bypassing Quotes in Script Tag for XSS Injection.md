---
id: d1cbf8c9-6514-4a74-9aca-91099adb1663
name: Bypassing Quotes in Script Tag for XSS Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.451487+00:00'
updated_at: '2023-04-10T20:21:48.171648+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Bootkit|T1067 - Bootkit]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Bypass quotes in script tag]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
commands:
- '[[URL Injection]]'
---

# Bypassing Quotes in Script Tag for XSS Injection

## Summary

Bypassing quotes in script tag is a technique used to inject malicious code into web pages that are vulnerable to Cross-Site Scripting (XSS) attacks. A successful XSS attack can allow an attacker to steal sensitive information, such as login credentials or session tokens, or to perform actions on b

## Description

# Description

Bypassing quotes in script tag is a technique used to inject malicious code into web pages that are vulnerable to Cross-Site Scripting (XSS) attacks. A successful XSS attack can allow an attacker to steal sensitive information, such as login credentials or session tokens, or to perform actions on behalf of the victim. The technique involves bypassing filters that are designed to prevent script injection by using exotic payloads, such as Unicode characters or HTML entities, to evade detection.

From a technical perspective, this technique involves crafting a payload that can bypass the filter by encoding the script tag in a way that the filter does not recognize it. This can be achieved by using different quotes or by encoding characters in the payload. Once the payload is injected, the script tag is executed by the victim's browser, allowing the attacker to execute arbitrary code.

The business value of this technique is that it can be used to gain unauthorized access to sensitive information or to perform actions on behalf of the victim, such as transferring funds or making unauthorized purchases.

 

## Requirements

1. Access to a vulnerable web page

1. Knowledge of exotic payload techniques

 

## Defense

1. Implement input validation and output encoding on web applications to prevent XSS attacks

1. Use Content Security Policy (CSP) to restrict the types of content that can be executed on a web page

1. Regularly scan web applications for vulnerabilities and apply security patches as needed

 

## Objectives

1. Inject malicious code into vulnerable web pages

1. Steal sensitive information, such as login credentials or session tokens

1. Perform actions on behalf of the victim

 

# Instructions

1. To prevent XSS injection attacks, ensure that all user input is properly sanitized and validated before being used in any context that could be interpreted as code. This includes input to URLs, form fields, and any other input fields. Also, make sure to use output encoding when displaying user input on the page.

 



**Code**: [[http://localhost/bla.php?test=</script><script>ale]]



> In this example, an attacker is attempting to inject malicious code into the URL parameter 'test'. If this parameter is not properly sanitized and validated, the injected code could be executed in the context of the page, leading to a potential security vulnerability. To prevent this, the input should be properly sanitized and validated before being used in any context that could be interpreted as code, and output encoding should be used when displaying user input on the page.



**Command** ([[URL Injection]]):

```bash
http://localhost/bla.php?test=</script><script>alert(1)</script>
<html>
  <script>
    <?php echo 'foo="text '.$_GET['test'].'";';`?>
  </script>
</html>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Bootkit|T1067 - Bootkit]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Commands Used

- [[URL Injection]]

## Tags

- [[Bypass quotes in script tag]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


