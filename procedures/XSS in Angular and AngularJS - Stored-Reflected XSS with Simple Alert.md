---
id: 45476a0c-3e7f-4b2e-9563-53d02161747a
name: XSS in Angular and AngularJS - Stored/Reflected XSS with Simple Alert
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.668846+00:00'
updated_at: '2023-04-10T20:24:51.812871+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Code Signing|T1116 - Code Signing]]'
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Hardware Additions|T1200 - Hardware Additions]]'
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Client Side Template Injection]]'
- '[[Stored/Reflected XSS - Simple alert in AngularJS]]'
- '[[XSS in Angular and AngularJS]]'
---

# XSS in Angular and AngularJS - Stored/Reflected XSS with Simple Alert

## Summary

This procedure involves exploiting stored or reflected cross-site scripting (XSS) vulnerabilities in Angular and AngularJS, specifically targeting the ability to display a simple alert message. By injecting malicious code into the application, an attacker can execute arbitrary JavaScript code in th

## Description

# Description

This procedure involves exploiting stored or reflected cross-site scripting (XSS) vulnerabilities in Angular and AngularJS, specifically targeting the ability to display a simple alert message. By injecting malicious code into the application, an attacker can execute arbitrary JavaScript code in the context of the victim's browser, potentially stealing sensitive information or performing unauthorized actions. This attack can be particularly effective against web applications that rely heavily on client-side rendering and dynamic content.

## Requirements

1. Access to a vulnerable web application built with Angular or AngularJS

1. Ability to inject malicious code into the application

## Defense

1. Implement input validation and sanitization techniques to prevent XSS attacks

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded by the web application

1. Regularly update and patch Angular and AngularJS to address known vulnerabilities

## Objectives

1. Inject and execute arbitrary JavaScript code in the context of the victim's browser

1. Trigger a simple alert message to display to the user

# Instructions

1. To exploit a Client Side Template Injection vulnerability, use one of the following payloads in the vulnerable input field:

**Code**: [[{{constructor.constructor('alert(1)')()}}]]

> The payload uses the constructor function to create a new function that displays an alert box with the message '1'. This payload can be used to test for Client Side Template Injection vulnerabilities in web applications.

2. The pop() method removes the last element from an array and returns that element. However, in this case, the pop() method is being replaced with a constructor function that executes a malicious alert(1) message. This vulnerability can be exploited by an attacker to execute arbitrary code on a victim's machine.

**Code**: [[{{[].pop.constructor('alert(1)')()}}]]

> The 'data' field contains the payload that exploits the vulnerability in the pop() method. The 'instruction' field provides a detailed explanation of the vulnerability, how it can be exploited, and the potential impact to the victim's machine. The 'name' field provides a descriptive name for the vulnerability to help users understand what the command does.

3. This command can be used to launch a Cross-Site Scripting (XSS) attack. The 'data' field contains the payload that can be injected into a vulnerable web page. The payload can execute arbitrary JavaScript code on the victim's browser.

**Code**: [[{{0[a='constructor'][a]('alert(1)')()}}
{{$eval.co]]

> The 'data' field contains three different payloads that can be used to launch an XSS attack. The first payload uses the 'constructor' property of an object to create a new function that executes the 'alert(1)' code. The second payload uses the '$eval' property of AngularJS to execute the 'alert(1)' code. The third payload uses the '$on' property of AngularJS to execute the 'alert(1)' code. The 'lang' field specifies that the payload is written in JavaScript. The 'text' field provides a link to an example of a vulnerable web page that can be used to test the XSS attack.

4. This command can be used to inject an expression in AngularJS 1.5.9 - 1.5.11 applications. The injected expression can be used to execute malicious code on the client side.

**Code**: [[{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;]]

> The command works by exploiting the AngularJS expression sandbox, which allows untrusted code to be executed in a restricted environment. By injecting an expression with a specially crafted payload, an attacker can bypass the sandbox and execute arbitrary code on the client side. The payload is constructed using a combination of AngularJS functions and JavaScript code. The injected expression is evaluated by the AngularJS $eval function, which executes the expression in the context of the AngularJS application. This allows the attacker to access the application's scope and execute arbitrary code.

5. The 'charAt' function of the String prototype in AngularJS can be modified to execute arbitrary code. This can be achieved by polluting the prototype object with a new function and then calling it using AngularJS's $eval function.

**Code**: [[{{x = {'y':''.constructor.prototype}; x['y'].charA]]

> To exploit this vulnerability, an attacker can create a new object 'x' with a property 'y' that points to the String prototype object. The 'charAt' function of this prototype object can then be replaced with a malicious function, such as 'alert(1)'. Finally, the attacker can call the $eval function with the payload 'x=alert(1)', which will execute the malicious code and trigger the alert.

6. This command exploits a prototype pollution vulnerability in AngularJS 1.4.0 - 1.4.9. It allows an attacker to modify the prototype of the 'constructor' function of any object in AngularJS, including the AngularJS 'scope' object. This can lead to arbitrary code execution.

**Code**: [[{{'a'.constructor.prototype.charAt=[].join;$eval(']]

> The payload sets the 'charAt' function of the 'constructor' prototype to an empty array's 'join' function. This allows an attacker to overwrite the 'constructor' function of any object in AngularJS. The payload then executes arbitrary code by setting the 'x' variable to 1 and injecting a malicious payload that executes an alert. This can be modified to execute any arbitrary code.

7. This command exploits a vulnerability in AngularJS version 1.3.20 and below, allowing an attacker to manipulate the prototype of an object and execute arbitrary code.

**Code**: [[{{'a'.constructor.prototype.charAt=[].join;$eval(']]

> The 'data' field contains the payload that exploits the vulnerability. The payload sets the 'charAt' function of the prototype of the 'constructor' object to an empty array, allowing an attacker to execute arbitrary code by calling the 'eval' function with the desired code as an argument. The 'name' field describes the vulnerability and the 'text' field specifies the version of AngularJS that is vulnerable.

8. This command is used to inject an alert command into an AngularJS application. The command exploits a vulnerability in AngularJS version 1.3.19.

**Code**: [[{{
    'a'[{toString:false,valueOf:[].join,length:]]

> The 'data' field contains the payload that will be injected into the AngularJS application. The payload uses the 'charAt' function to replace the 'join' function of the 'a' array. This allows the payload to execute the '$eval' function, which in turn executes the 'alert' command with a value of 1. The 'lang' field specifies that the payload is written in JavaScript. The 'text' field specifies the version of AngularJS that is being targeted. The 'instruction' field explains how to use this command, and the 'explain' field provides additional details about how the command works.

9. This command can be used to perform a prototype pollution attack on AngularJS 1.3.3 - 1.3.18. It allows an attacker to modify the prototype of the Object constructor and add new properties to it. This can be used to execute arbitrary code on the victim's machine.

**Code**: [[{{{}[{toString:[].join,length:1,0:'__proto__'}].as]]

> The 'data' field contains the payload that is used to perform the attack. The payload uses the __proto__ property to modify the prototype of the Object constructor and add a new property called 'assign'. This property is then assigned a function that is used to execute the payload. The payload itself is executed using the $eval function, which is provided by AngularJS. The payload in this case is a simple alert(1) statement, but it can be replaced with any arbitrary code that the attacker wants to execute.

10. The AngularJS Prototype Pollution vulnerability can be exploited to modify the prototype of AngularJS objects, leading to the ability to execute arbitrary code.

**Code**: [[{{
    {}[{toString:[].join,length:1,0:'__proto__']]

> The vulnerability works by modifying the prototype of AngularJS objects through the `__proto__` property. By assigning a value to the `__proto__` property of an object, it is possible to modify the prototype of that object, which can lead to the execution of arbitrary code. This can be exploited by an attacker to execute malicious code on a victim's machine.

11. This command exploits a prototype pollution vulnerability in AngularJS 1.3.0.

**Code**: [[{{!ready && (ready = true) && (
      !call
      ]]

> The vulnerability allows an attacker to modify the prototype of the `Object` object and inject malicious code into the application. This can lead to remote code execution or other attacks. The exploit code modifies the `Function.prototype` object to execute arbitrary code. It is recommended to upgrade to a newer version of AngularJS to avoid this vulnerability.

12. This command exploits a vulnerability in AngularJS versions 1.2.24 to 1.2.29 which allows attackers to pollute the prototype of the 'a' constructor function, leading to arbitrary code execution.

**Code**: [[{{'a'.constructor.prototype.charAt=''.valueOf;$eva]]

> The 'charAt' function of the 'a' constructor is overwritten with an empty string. The $eval function is then used to execute the payload which is constructed using the 'y' variable. The 'y' variable contains the code to check if 'window.x' exists and if not, set it to 1 and alert the value. Since 'window.x' does not exist, the code is executed and 'window.x' is set to 1, leading to arbitrary code execution.

13. This command exploits a prototype pollution vulnerability in AngularJS versions 1.2.19 to 1.2.23. It allows an attacker to modify the behavior of built-in JavaScript objects and potentially execute arbitrary code.

**Code**: [[{{toString.constructor.prototype.toString=toString]]

> The vulnerability is caused by the way AngularJS handles certain inputs. By passing a specially crafted input to the vulnerable application, an attacker can modify the prototype of the toString() function of the Array object. This allows the attacker to execute arbitrary code by sorting an array of values that contain the code they want to execute. This can result in the execution of malicious code on the victim's machine, such as stealing sensitive information or taking control of the system.

14. This command exploits a Cross-Site Scripting (XSS) vulnerability in AngularJS versions 1.2.6 through 1.2.18.

**Code**: [[{{(_=''.sub).call.call({}[$='constructor'].getOwnP]]

> The vulnerability allows an attacker to execute arbitrary JavaScript code on a victim's browser by injecting it into an AngularJS expression. The injected code is executed in the context of the victim's browser, allowing the attacker to steal sensitive information or perform actions on behalf of the victim. To exploit the vulnerability, the attacker needs to inject a specially crafted payload into an AngularJS expression. The payload is executed when the expression is evaluated by the victim's browser.

15. This command exploits a vulnerability in AngularJS 1.2.2 - 1.2.5 that allows an attacker to pollute the prototype of the 'a' object, which can lead to arbitrary code execution.

**Code**: [[{{'a'[{toString:[].join,length:1,0:'__proto__'}].c]]

> The payload sets the 'charAt' function of the 'a' object's prototype to the 'valueOf' function of an empty string. This allows an attacker to execute arbitrary code by injecting it into the 'x' variable using the 'eval' function. The injected code is executed in the context of the AngularJS application, which can allow an attacker to steal sensitive information or perform other malicious actions.

16. This command is used to inject code into AngularJS applications that are running version 1.2.0 to 1.2.1.

**Code**: [[{{a='constructor';b={};a.sub.call.call(b[a].getOwn]]

> The 'data' field in this JSON object contains the code that will be injected into the AngularJS application. The code takes advantage of a vulnerability in the constructor function of AngularJS. The 'name' field provides a descriptive name for this command that informs the reader of what it does.

17. The constructor injection vulnerability can be used by an attacker to execute arbitrary code on a vulnerable system. The vulnerability exists in the way the constructor function is executed, allowing an attacker to inject their own code into the constructor.

**Code**: [[{{constructor.constructor('alert(1)')()}}]]

> To exploit this vulnerability, an attacker can use the 'constructor.constructor' method to execute their own code. The 'constructor.constructor' method returns the constructor function of an object, which can then be used to execute arbitrary code. In this case, the attacker is using the 'alert(1)' function to display a pop-up message on the vulnerable system. This vulnerability affects AngularJS versions 1.0.1 through 1.1.5, as well as Vue JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Code Signing|T1116 - Code Signing]]
- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Hardware Additions|T1200 - Hardware Additions]]
- [[Remote Access Tools|T1219 - Remote Access Tools]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Client Side Template Injection]]
- [[Stored/Reflected XSS - Simple alert in AngularJS]]
- [[XSS in Angular and AngularJS]]
