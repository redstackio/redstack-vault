---
id: 24a28980-7e85-40f0-a64e-18287855b493
name: Advanced XSS in Angular and AngularJS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.722265+00:00'
updated_at: '2023-04-10T20:24:52.632756+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Advanced bypassing XSS]]'
- '[[Client Side Template Injection]]'
- '[[XSS in Angular and AngularJS]]'
commands:
- '[[Convert HTML Entity]]'
- '[[Replacing &quot; with actual quotes]]'
---

# Advanced XSS in Angular and AngularJS

## Summary

Advanced XSS in Angular and AngularJS is a technique used to exploit client-side template injection vulnerabilities in web applications built on Angular and AngularJS frameworks. This technique allows an attacker to inject malicious code into the application's templates, which are then executed on 

## Description

# Description

Advanced XSS in Angular and AngularJS is a technique used to exploit client-side template injection vulnerabilities in web applications built on Angular and AngularJS frameworks. This technique allows an attacker to inject malicious code into the application's templates, which are then executed on the client-side, leading to data theft, session hijacking, and other attacks. This attack can be used to bypass web application firewalls and other security measures, making it a powerful tool for attackers.

To execute this attack, an attacker must first identify a client-side template injection vulnerability in the target web application. They can then use various techniques, such as AngularJS escape characters, single and double quotes, and the String.fromCharCode() command, to bypass input validation and inject malicious code. The attacker can also use the AngularJS Imperva WAF bypass technique to bypass web application firewalls.

The business value of this attack is that it allows an attacker to steal sensitive data, compromise user accounts, and cause reputational damage to the targeted organization. This attack can be used by cybercriminals to steal financial information, personal data, and other sensitive information from web applications.

## Requirements

1. Client-side template injection vulnerability in the target web application

1. Knowledge of Angular and AngularJS frameworks

1. Access to the target web application

## Defense

1. Implement input validation and output encoding to prevent client-side template injection vulnerabilities

1. Use web application firewalls to detect and block client-side template injection attacks

1. Regularly scan web applications for vulnerabilities and patch them as soon as possible

## Objectives

1. Inject malicious code into the application's templates

1. Execute the injected code on the client-side

1. Steal sensitive data, compromise user accounts, and cause reputational damage to the targeted organization

# Instructions

1. Use the escape character &#39; to represent a single quote in AngularJS.

**Code**: [[&#39;]]

> When using single quotes in AngularJS, it is important to escape them properly to avoid syntax errors. The escape character &#39; can be used to represent a single quote in AngularJS, allowing you to use single quotes within your code without causing errors. For example, if you need to use a single quote within an AngularJS expression, you can use the escape character like this: {{ 'It\'s working!' }}. This will output the string 'It's working!' without causing any syntax errors.

2. To use single and double quotes in a string, you can escape them using a backslash (\). For example, if you want to include the word "don't" in a string, you would write it as 'don\'t'.

**Code**: [[&quot;]]

> The backslash tells the interpreter to treat the following character as a literal character and not as a special character. This is useful when you want to include quotes, backslashes, or other special characters in a string.

**Command** ([[Replacing &quot; with actual quotes]]):

```bash
&quot;
```

3. The String.fromCharCode() command returns a string created by using the specified sequence of Unicode values. The Unicode values are passed as arguments to the function.

**Code**: [[{{x=valueOf.name.constructor.fromCharCode;construc]]

> The String.fromCharCode() command takes one or more numeric parameters, which represent Unicode values, and returns a string created by converting each Unicode value to a character. For example, String.fromCharCode(65, 66, 67) returns the string 'ABC'.

4. To escape a string in AngularJS, use the ng-bind-html directive along with the $sce.trustAsHtml() method.

**Code**: [[&#39;]]

> The &#39; character represents a single quote in HTML. When using AngularJS, it is important to properly escape any user input to prevent XSS attacks. To do this, use the ng-bind-html directive along with the $sce.trustAsHtml() method to bind the escaped string to the DOM. For example, in a controller, you can use the following code:

$scope.escapedString = $sce.trustAsHtml('&#39;');

Then in your HTML, you can use the ng-bind-html directive to bind the escaped string to the DOM:

<div ng-bind-html='escapedString'></div>

5. Use the &quot; character to represent a double quote within a string literal surrounded by double quotes. Use the single quote character ' to represent a single quote within a string literal surrounded by single quotes.

**Code**: [[&quot;]]

> When working with string literals, it can be helpful to use both single and double quotes in your code. However, if you need to include a quote character within a string literal, you must use the opposite type of quote to surround the string. For example, if you want to include a double quote within a string surrounded by double quotes, you must use the &quot; character to represent the double quote. Similarly, if you want to include a single quote within a string surrounded by single quotes, you must use the single quote character ' to represent the single quote.

**Command** ([[Convert HTML Entity]]):

```bash
&quot;
```

6. Use double quotes to define a string literal in JSON.

**Code**: [[constructor]]

> In JSON, strings must be enclosed in double quotes. If the string itself contains double quotes, they must be escaped with a backslash (\). For example, the string "Hello, world!" would be represented in JSON as "\"Hello, world!\"".

7. The code generates a random string by combining two numbers and converting them to base 36. The resulting string is then returned.

**Code**: [[{{x=767015343;y=50986827;a=x.toString(36)+y.toStri]]

> The code uses JavaScript's built-in functions to generate a random string. The two numbers used for generating the string are hardcoded in the code. The toString() method is used to convert the numbers to base 36. The resulting string is then returned by calling the fromCharCode() method on the String object. Overall, this code can be useful for generating random strings for various purposes.

8. To generate a random string, follow these steps:
1. Define two variables, x and y, and assign them any integer values.
2. Convert the integer values of x and y to base 36 and concatenate them to create a random string.
3. Create an empty object, b.
4. Call the sub method on the string representation of variable a, which is the concatenated string of x and y.
5. Call the value of the sub method on the object b, using call and passing in the getOwnPropertyDescriptor method of the prototype of b[a].sub as the first argument, 0 as the second argument, and the fromCodePoint method of the String object with the arguments 112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41 as the third argument.
6. The result of this call will be the generated random string.

**Code**: [[{{x=767015343;y=50986827;a=x.toString(36)+y.toStri]]

> This command generates a random string using JavaScript. It does this by converting two integer values, x and y, to base 36 and concatenating them to create a random string. It then creates an empty object, b, and calls the sub method on the string representation of a, which is the concatenated string of x and y. It then calls the value of the sub method on the object b, using call and passing in the getOwnPropertyDescriptor method of the prototype of b[a].sub as the first argument, 0 as the second argument, and the fromCodePoint method of the String object with the arguments 112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41 as the third argument. The result of this call will be the generated random string.

9. This command generates a random string of characters.

**Code**: [[{{x=767015343;y=50986827;a=x.toString(36)+y.toStri]]

> The command uses JavaScript to generate a random string. The x and y values are used to generate a unique string. The a variable is created by concatenating the x and y values and converting them to base 36. The sub function is then called on the a variable and the call method is used to call the toString function on the document object. The result is a random string of characters.

10. This command generates a random name for a document.

**Code**: [[{{x=767015343;y=50986827;a=x.toString(36)+y.toStri]]

> The command uses a combination of two random numbers to create a unique string that is used as the document name. The string is generated using JavaScript's toString() method with a radix of 36 to convert the numbers to base 36. The resulting string is then used to call the 'sub' method of the String prototype, which returns a new string with the specified characters replaced. Finally, the 'call' method is used to call the 'toString' method of the document object and pass in the new string as an argument to create a new document name.

11. This command is used to bypass the Imperva Web Application Firewall (WAF) using AngularJS. The command executes a JavaScript code snippet that calls a function with a prompt to access the document's domain.

**Code**: [[{{x=['constr', 'uctor'];a=x.join('');b={};a.sub.ca]]

> The command is composed of a JavaScript code snippet that uses the AngularJS framework to bypass the Imperva WAF. The code creates an array of strings, 'constr' and 'uctor', and concatenates them to form the string 'constructor'. It then creates an empty object, 'b', and assigns the 'constructor' property of the object's prototype to the variable 'a'. The 'sub' method of the 'a' variable is called twice using the 'call' method of the 'sub' method itself and the 'call' method of the 'sub' method's 'call' method. The 'getOwnPropertyDescriptor' method is called on the 'b' object's prototype to get the descriptor of the 'constructor' property. The 'value' property of the descriptor is accessed and called with the arguments 0 and a prompt that displays the document's domain. This allows the code to bypass the Imperva WAF and execute arbitrary code on the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Commands Used

- [[Convert HTML Entity]]
- [[Replacing &quot; with actual quotes]]

## Tags

- [[Advanced bypassing XSS]]
- [[Client Side Template Injection]]
- [[XSS in Angular and AngularJS]]
