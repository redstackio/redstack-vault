---
id: 108b8126-60b8-467a-b037-6c003a25c413
name: XML External Entity Injection Detection and Mitigation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.099165+00:00'
updated_at: '2023-04-10T20:24:39.916950+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Spearphishing Link|T1192 - Spearphishing Link]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Detect the vulnerability]]'
- '[[XML External Entity]]'
commands:
- '[[Extract First Name]]'
- '[[Print last name]]'
---

# XML External Entity Injection Detection and Mitigation

## Summary

XML External Entity (XXE) Injection is a type of attack that exploits an application's processing of XML data. The attacker sends malicious input to the application, which is then processed by the XML parser. The malicious input contains an external entity reference that can be used to read sensiti

## Description

# Description

XML External Entity (XXE) Injection is a type of attack that exploits an application's processing of XML data. The attacker sends malicious input to the application, which is then processed by the XML parser. The malicious input contains an external entity reference that can be used to read sensitive data or execute arbitrary code. XXE Injection can be used to steal sensitive data, perform denial of service attacks, or execute arbitrary code. This procedure detects and mitigates XXE Injection attacks by testing for the vulnerability and implementing measures to prevent exploitation.

 

## Requirements

1. Access to the application's source code

1. Knowledge of XML and XXE Injection vulnerabilities

1. Tools for testing and mitigating XXE Injection attacks

 

## Defense

1. Ensure that input validation is performed on all XML data to prevent XXE Injection attacks

1. Implement strict firewall rules to prevent unauthorized access to the application's network

1. Monitor application logs for suspicious activity and respond promptly to any detected attacks

 

## Objectives

1. Detect XXE Injection vulnerabilities in applications

1. Prevent XXE Injection attacks from being executed

1. Protect sensitive data from being stolen or compromised

 

# Instructions

1. To perform this test, include an external entity in the XML data that points to a file containing the string "John". If the XML parser is vulnerable to XML External Entity Injection, the resulting parsed data will contain the string "John".

 



**Code**: [[firstName]]



> XML External Entity Injection is a type of attack that allows an attacker to include external entities in an XML document, which can be used to disclose sensitive information, execute remote code, or perform denial of service attacks. This test is used to check if a system is vulnerable to this type of attack.



**Command** ([[Extract First Name]]):

```bash
firstName
```



2. Use this command to find all users with the last name Doe.

 



**Code**: [[lastName]]



> The 'lastName' field in the data parameter specifies the last name to search for. This command will return all users whose last name matches 'Doe'.



**Command** ([[Print last name]]):

```bash
console.log('lastName')
```



3. DOCTYPE is used to define the document type and version of an HTML page.

 



**Code**: [[DOCTYPE]]



> The DOCTYPE declaration is not an HTML tag; it is an instruction to the web browser about what version of HTML the page is written in. The declaration should be the very first thing in an HTML document, before the <html> tag. The DOCTYPE declaration is not case sensitive. It can be written in uppercase or mixed case. The DOCTYPE declaration for HTML5 is <!DOCTYPE html>.

4. To replace an entity in XML, use the <!ENTITY> declaration. The syntax is as follows:
<!ENTITY entity_name "entity_value">.
In the above example, the entity 'example' is declared with the value 'Doe'.
To use the entity in the XML document, simply reference it using the '&' symbol followed by the entity name and a semicolon.

 



**Code**: [[<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!E]]



> This XML document demonstrates the use of entity replacement. The value of the 'lastName' element is defined as the 'example' entity, which is declared as 'Doe' in the document type declaration. When the document is parsed, the entity is replaced with its value, resulting in the 'lastName' element displaying 'Doe' instead of '&example;'.

5. Use this command to set the Content-Type header of an HTTP request to application/xml.

 



**Code**: [[Content-Type: application/xml]]



> The Content-Type header is used to indicate the media type of the resource being requested or sent in an HTTP request or response. Setting the Content-Type header to application/xml indicates that the data being sent or requested is in XML format. This is useful when working with APIs that require XML data, or when sending XML data to a server.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Spearphishing Link|T1192 - Spearphishing Link]]
- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Extract First Name]]
- [[Print last name]]

## Tags

- [[Detect the vulnerability]]
- [[XML External Entity]]


