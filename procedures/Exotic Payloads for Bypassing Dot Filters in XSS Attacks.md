---
id: f6f04f65-41f9-417f-be52-a79f1e9d8c93
name: Exotic Payloads for Bypassing Dot Filters in XSS Attacks
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.503941+00:00'
updated_at: '2023-04-10T20:21:41.957211+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Bypass dot filter]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
commands:
- '[[Access Router]]'
---

# Exotic Payloads for Bypassing Dot Filters in XSS Attacks

## Summary

Exotic payloads and filter bypass techniques can be used to evade detection and execute successful cross-site scripting attacks. In this procedure, we will explore how to bypass dot filters by using base64 encoding and decoding, and alert domain commands. By using these techniques, attackers can ex

## Description

# Description

Exotic payloads and filter bypass techniques can be used to evade detection and execute successful cross-site scripting attacks. In this procedure, we will explore how to bypass dot filters by using base64 encoding and decoding, and alert domain commands. By using these techniques, attackers can execute arbitrary code and steal sensitive data from unsuspecting victims. Successful XSS attacks can lead to data breaches, financial loss, and damage to a company's reputation.

 

## Requirements

1. Access to vulnerable web application

1. Knowledge of base64 encoding and decoding

1. Command line interface

 

## Defense

1. Implement input validation and output encoding in web applications

1. Use a web application firewall to detect and block XSS attacks

1. Regularly scan web applications for vulnerabilities and apply patches and updates

 

## Objectives

1. Execute successful cross-site scripting attacks

1. Bypass dot filters to evade detection

1. Steal sensitive data from unsuspecting victims

 

# Instructions

1. To execute this command, simply paste the provided code into the console of a web browser and press enter. This will trigger an alert box that displays the domain of the current webpage.

 



**Code**: [[<script>window['alert'](document['domain'])</scrip]]



> This command uses JavaScript to access the 'document' object, which contains information about the current webpage. The 'domain' property of the 'document' object returns the domain name of the current webpage. The provided code creates an alert box that displays the domain name when executed.

2. To convert an IP address into decimal format, follow these steps:
1. Separate the four numbers of the IP address (e.g. 192.168.1.1) into individual octets.
2. Convert each octet to binary format.
3. Combine the four binary octets into a single 32-bit binary number.
4. Convert the 32-bit binary number to decimal format.

 



**Code**: [[http://192.168.1.1]]



> For example, to convert the IP address 192.168.1.1 into decimal format, follow these steps:
1. 192 in binary format is 11000000
2. 168 in binary format is 10101000
3. 1 in binary format is 00000001
4. 1 in binary format is 00000001
5. Combine the four binary octets into a single 32-bit binary number: 11000000101010000000000100000001
6. Convert the 32-bit binary number to decimal format: 3232235777
Therefore, the decimal format of the IP address 192.168.1.1 is 3232235777.



**Command** ([[Access Router]]):

```bash
http://192.168.1.1
```



3. Converts an IP address from decimal format to dotted-quad format.

 



**Code**: [[http://3232235777]]



> The argument of this command is a decimal format IP address. The command will convert the decimal format to dotted-quad format, which is a more commonly used format for IP addresses.

4. To decode a Base64 encoded string, use the following command:

 



**Code**: [[<script>eval(atob("YWxlcnQoZG9jdW1lbnQuY29va2llKQ=]]



> The command uses the 'atob' function in JavaScript to decode the Base64 string. The 'eval' function is used to execute the decoded string as JavaScript code. The argument of 'atob' function should be the Base64 encoded string that you want to decode.

5. Use this command to encode your XSS payload in Base64 format. This command is useful when you need to transmit your payload over a network that only supports ASCII characters.

 



**Code**: [[echo -n &quot;alert(document.cookie)&quot; | base6]]



> The 'echo' command is used to print the specified text to the console. The '-n' option is used to suppress the newline character that is usually printed after the text. The '|' (pipe) symbol is used to redirect the output of the 'echo' command to the 'base64' command. The 'base64' command is used to encode the input in Base64 format. The resulting output can then be used in your XSS payload.

6. base64_decode

 



**Code**: [[YWxlcnQoZG9jdW1lbnQuY29va2llKQ==]]



> This command decodes a given Base64 encoded string. The argument of the command should be a Base64 encoded string that needs to be decoded.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Access Router]]

## Tags

- [[Bypass dot filter]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


