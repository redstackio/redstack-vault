---
id: de000910-a2af-4ec2-815b-855bad221230
name: XML External Entity WAF Bypass via Character Encoding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.525591+00:00'
updated_at: '2023-04-10T20:24:43.837466+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Bypass via character encoding]]'
- '[[WAF Bypasses]]'
- '[[XML External Entity]]'
commands:
- '[[Convert to UTF-16]]'
- '[[Convert UTF-8 encoded XML file to UTF-16BE]]'
---

# XML External Entity WAF Bypass via Character Encoding

## Summary

XML External Entity (XXE) is a vulnerability that occurs when an XML parser processes input from an XML document that contains a reference to an external entity. This vulnerability can be exploited to disclose confidential data, execute remote code, and perform denial of service attacks. WAFs are o

## Description

# Description

XML External Entity (XXE) is a vulnerability that occurs when an XML parser processes input from an XML document that contains a reference to an external entity. This vulnerability can be exploited to disclose confidential data, execute remote code, and perform denial of service attacks. WAFs are often used to protect against XXE attacks, but they can be bypassed using various techniques. One such technique is to use character encoding to evade detection. By encoding the payload in a different format, the WAF may not be able to detect the XXE attack.

Technical Explanation:
This procedure involves using UTF-16 conversion and converting UTF-8 to UTF-16BE to bypass a WAF that is protecting against XXE attacks. By encoding the payload in a different format, the WAF may not be able to detect the XXE attack. This technique can be used to execute remote code, disclose confidential data and perform denial of service attacks.

Business Value:
By exploiting this vulnerability, an attacker can gain access to confidential data, execute remote code, and perform denial of service attacks. This can lead to financial loss, reputational damage, and legal consequences.

 

## Requirements

1. Access to a vulnerable application

1. Knowledge of XXE attacks

1. Tools for encoding payloads in different formats

 

## Defense

1. Implement input validation and sanitization to prevent XXE attacks

1. Implement a WAF that can detect and block XXE attacks

1. Regularly update and patch applications and servers to prevent vulnerabilities

 

## Objectives

1. Bypass a WAF protecting against XXE attacks

1. Execute remote code

1. Disclose confidential data

1. Perform denial of service attacks

 

# Instructions

1. Use this command to convert the payload to UTF-16 encoding.

 



**Code**: [[UTF-16]]



> The argument 'UTF-16' specifies the desired encoding format. This command is useful when dealing with text data that needs to be converted to a specific encoding format. The converted payload can then be used for further processing or storage.



**Command** ([[Convert to UTF-16]]):

```bash
UTF-16
```



2. To convert a UTF-8 encoded file to UTF-16BE, use the 'iconv' command followed by the input and output file names. The 'cat' command is used to read the input file and pass it to 'iconv' for conversion. The '>' symbol is used to redirect the output to a new file.

 



**Code**: [[cat utf8exploit.xml | iconv -f UTF-8 -t UTF-16BE >]]



> The 'iconv' command is a character set conversion utility that can be used to convert text files from one character set to another. In this case, we are converting a UTF-8 encoded file to UTF-16BE. The '-f' option specifies the input character set (UTF-8) and the '-t' option specifies the output character set (UTF-16BE). The 'cat' command is used to read the input file and pass it to 'iconv' for conversion. The '>' symbol is used to redirect the output to a new file. This command is useful when working with files that require a specific character set, such as XML files.



**Command** ([[Convert UTF-8 encoded XML file to UTF-16BE]]):

```bash
cat utf8exploit.xml | iconv -f UTF-8 -t UTF-16BE > utf16exploit.xml
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Commands Used

- [[Convert to UTF-16]]
- [[Convert UTF-8 encoded XML file to UTF-16BE]]

## Tags

- [[Bypass via character encoding]]
- [[WAF Bypasses]]
- [[XML External Entity]]


