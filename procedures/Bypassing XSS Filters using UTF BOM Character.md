---
id: 567bdce0-ba68-42d4-82fe-6773a01607b5
name: Bypassing XSS Filters using UTF BOM Character
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.129415+00:00'
updated_at: '2023-04-10T20:21:41.246500+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Bypass using BOM]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
commands:
- '[[BOM Character for UTF-16 Encoding - Big Endian]]'
- '[[BOM Character for UTF-16 Encoding - Little Endian]]'
- '[[BOM Character for UTF-16 Encoding - XSS]]'
- '[[BOM Character for UTF-32 Encoding - Big Endian]]'
- '[[BOM Character for UTF-32 Encoding - Little Endian]]'
- '[[BOM Character for UTF-32 Encoding - XSS]]'
---

# Bypassing XSS Filters using UTF BOM Character

## Summary

This technique involves using the byte-order mark (BOM) character to bypass XSS filters. The BOM character is a Unicode character that is used to indicate the byte order of a text file or stream. By adding a BOM character to an XSS payload, it can bypass certain filters that are not designed to han

## Description

# Description

This technique involves using the byte-order mark (BOM) character to bypass XSS filters. The BOM character is a Unicode character that is used to indicate the byte order of a text file or stream. By adding a BOM character to an XSS payload, it can bypass certain filters that are not designed to handle this character. This can be useful when other filter bypass techniques are not working or when exotic payloads are needed.

From a technical perspective, the BOM character is added to the beginning of the payload, which changes the encoding of the payload. This can cause the payload to bypass certain filters that are looking for specific encodings or patterns. However, not all filters can be bypassed using this technique, and it may require some trial and error to find the right combination of payload and filter.

From a business perspective, this technique can be used by attackers to bypass security controls and inject malicious code into websites. This can lead to the theft of sensitive information, such as login credentials, or the installation of malware on user's devices.

 

## Requirements

1. Access to a vulnerable website

1. Knowledge of the target's XSS filter

1. A payload that can be encoded using the BOM character

 

## Defense

1. Implement input validation and output encoding to prevent XSS attacks

1. Regularly update and patch web applications to address known vulnerabilities

1. Use a web application firewall (WAF) to block malicious traffic and payloads

 

## Objectives

1. Bypass XSS filters

1. Inject malicious code into websites

1. Steal sensitive information

1. Install malware on user's devices

 

# Instructions

1. To add a BOM character to a UTF-encoded file, simply add the corresponding bytes at the beginning of the file. For UTF-16 encoding, add either 0xFE 0xFF (big endian) or 0xFF 0xFE (little endian). For UTF-32 encoding, add either 0x00 0x00 0xFE 0xFF (big endian) or 0xFF 0xFE 0x00 0x00 (little endian).

 



**Code**: [[BOM Character for UTF-16 Encoding:
Big Endian : 0x]]



> The BOM character is a special marker that indicates the byte order of a text file encoded in UTF-16 or UTF-32. It is not required for UTF-8 encoding. The BOM character must be the first character in the file, otherwise it will not be recognized by some software. The XSS code provided in the 'data' field is an example of how an attacker can use a BOM character to inject malicious code into a web page that is not properly encoded.



**Command** ([[BOM Character for UTF-16 Encoding - Big Endian]]):

```bash
0xFE 0xFF
```





**Command** ([[BOM Character for UTF-16 Encoding - Little Endian]]):

```bash
0xFF 0xFE
```





**Command** ([[BOM Character for UTF-16 Encoding - XSS]]):

```bash
%fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E
```





**Command** ([[BOM Character for UTF-32 Encoding - Big Endian]]):

```bash
0x00 0x00 0xFE 0xFF
```





**Command** ([[BOM Character for UTF-32 Encoding - Little Endian]]):

```bash
0xFF 0xFE 0x00 0x00
```





**Command** ([[BOM Character for UTF-32 Encoding - XSS]]):

```bash
%00%00%fe%ff%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[BOM Character for UTF-16 Encoding - Big Endian]]
- [[BOM Character for UTF-16 Encoding - Little Endian]]
- [[BOM Character for UTF-16 Encoding - XSS]]
- [[BOM Character for UTF-32 Encoding - Big Endian]]
- [[BOM Character for UTF-32 Encoding - Little Endian]]
- [[BOM Character for UTF-32 Encoding - XSS]]

## Tags

- [[Bypass using BOM]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


