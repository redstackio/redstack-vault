---
id: f37f1f17-d8b5-4df1-a59b-144a144f79db
name: File Retrieval via XXE Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.139243+00:00'
updated_at: '2023-04-10T20:24:39.124473+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]'
tags:
- '[[Classic XXE]]'
- '[[Exploiting XXE to retrieve files]]'
- '[[XML External Entity]]'
commands:
- '[[View Password File]]'
---

# File Retrieval via XXE Injection

## Summary

File Retrieval via XXE Injection is a technique used by attackers to exfiltrate sensitive data from an application through XML External Entity (XXE) vulnerabilities. XXE vulnerabilities arise when an application processes XML input that includes a reference to an external entity. Attackers can expl

## Description

# Description

File Retrieval via XXE Injection is a technique used by attackers to exfiltrate sensitive data from an application through XML External Entity (XXE) vulnerabilities. XXE vulnerabilities arise when an application processes XML input that includes a reference to an external entity. Attackers can exploit this vulnerability to retrieve files from the server or other internal systems. This technique can be used to steal sensitive data such as password files, configuration files, or other confidential information. The attacker can then use this information to further compromise the system or sell it on the dark web.

## Requirements

1. Access to the target application

1. Knowledge of the XXE vulnerability

1. Ability to send malicious XML payloads

## Defense

1. Implement input validation and sanitization to prevent XXE vulnerabilities

1. Use a web application firewall to detect and block XXE attacks

1. Monitor network traffic for suspicious activity, such as large file transfers or unusual network connections

## Objectives

1. Retrieve sensitive files from the target system

1. Exfiltrate the stolen data to a remote server

1. Maintain persistence on the target system

# Instructions

1. To display the content of a file, use the 'cat' command followed by the file path. For example, 'cat /etc/passwd'.

**Code**: [[/etc/passwd]]

> The 'cat' command is used to display the contents of a file. In this case, we are trying to display the content of the '/etc/passwd' file. The '/etc/passwd' file contains information about the system's users, including their usernames, user IDs, and home directories. By using the 'cat' command, we can view the contents of this file and see the information it contains.

**Command** ([[View Password File]]):

```bash
/etc/passwd
```

2. The XML External Entity Injection (XXE) attack is a vulnerability that allows an attacker to interfere with an application's processing of XML data. The attacker can exploit this vulnerability to read sensitive data, execute remote code, or conduct denial-of-service attacks.

**Code**: [[<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test]]

> In this JSON object, the 'data' field contains a sample payload for the XXE attack. The payload contains an external entity that references the '/etc/passwd' file. When the XML parser processes the payload, it resolves the external entity and includes the contents of the '/etc/passwd' file in the parsed output. This can reveal sensitive information about the system, such as usernames and hashed passwords.

3. This command retrieves the password file from the system.

**Code**: [[<?xml version="1.0"?>
<!DOCTYPE data [
<!ELEMENT d]]

> The command uses an XML payload with an external entity to retrieve the password file from the system. The retrieved file can contain sensitive information such as user passwords and should be handled with care.

4. This command is used to test for XML external entity (XXE) injection vulnerabilities. The provided XML data includes a reference to an external entity which is resolved and the contents of the file are included in the response. If the file specified in the entity contains sensitive information, it can be disclosed through this vulnerability.

**Code**: [[<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DO]]

> The 'data' field contains the XML data to be sent in the request. The 'instruction' field provides information on how to use the command and what it is testing for. The 'name' field should be filled with a name that accurately describes the vulnerability being tested for. In this case, the vulnerability is XML External Entity Injection (XXE) which can be used to disclose sensitive information through the inclusion of external entities in XML documents. The 'lang' field specifies the language of the data being sent and the 'text' field can be used to provide additional context or information.

5. This command is used to test for XML External Entity (XXE) injection vulnerabilities. The provided XML data contains a reference to an external entity that points to the file c:/boot.ini on the server. If the server is vulnerable to XXE injection, the contents of the file will be returned in the response.

**Code**: [[<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCT]]

> The provided XML data contains a DOCTYPE declaration that defines an external entity named xxe. The value of this entity is set to the file path of c:/boot.ini. When the XML parser processes the XML data, it will attempt to resolve the external entity reference, which can lead to sensitive information disclosure if the server is vulnerable to XXE injection. 

6. Use this command to display a warning message from the system.

**Code**: [[SYSTEM]]

> This command takes no arguments and simply displays a warning message from the system. It can be used to alert users of any issues or problems that may be affecting the system, and to provide guidance on how to address the issue if necessary.

7. Use this command to add a public text to your content.

**Code**: [[PUBLIC]]

> The 'PUBLIC' argument signifies that the text is meant to be visible to all users. The 'text' field should contain the actual text that you want to add to your content. You can use this command multiple times to add more than one public text to your content.

8. To perform an XML External Entity (XXE) injection attack, the attacker can use specially crafted XML input containing external entities that reference files or URLs that the attacker wants to read or access. The attacker can then send this input to the vulnerable application, which will process the input and potentially disclose sensitive information or perform unauthorized actions. 

**Code**: [[<!ENTITY % xxe PUBLIC "Random Text" "URL">
<!ENTIT]]

> The 'data' field contains the actual XML input that will be sent to the vulnerable application in an XXE attack. The first line defines an external entity named 'xxe' that references a URL containing random text. The second line defines a second external entity named 'xxe' that references a URL containing any text. The 'instruction' field provides a brief overview of how an XXE attack works, while the 'explain' field provides additional details on the attack and its potential impact. The 'lang' field specifies the programming language used in the attack code.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]

## Commands Used

- [[View Password File]]

## Tags

- [[Classic XXE]]
- [[Exploiting XXE to retrieve files]]
- [[XML External Entity]]
