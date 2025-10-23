---
id: 084c68b5-6037-412c-805e-53bf95aa2318
name: XXE in DOCX Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.624654+00:00'
updated_at: '2023-04-10T20:24:44.994476+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[XML External Entity]]'
- '[[XXE in exotic files]]'
- '[[XXE inside DOCX file]]'
commands:
- '[[Convert to various file formats]]'
- '[[Update [Content_Types].xml in xxe.docx]]'
---

# XXE in DOCX Files

## Summary

XXE in DOCX files is a technique used by attackers to inject malicious code into a Microsoft Word document. This technique is achieved by exploiting the XML External Entity vulnerability in the DOCX file format. Attackers can use this technique to execute arbitrary code on a victim's machine, which

## Description

# Description

XXE in DOCX files is a technique used by attackers to inject malicious code into a Microsoft Word document. This technique is achieved by exploiting the XML External Entity vulnerability in the DOCX file format. Attackers can use this technique to execute arbitrary code on a victim's machine, which can lead to further compromise of the victim's network. This technique is commonly used in phishing attacks, where attackers send a malicious DOCX file to the victim, enticing them to open it.

 

## Requirements

1. Access to a DOCX file

1. OXML_XXE Tool Command

 

## Defense

1. Ensure that all software and applications are up-to-date with the latest security patches

1. Implement strict email filters and educate employees on phishing attacks

1. Use antivirus and anti-malware software to detect and prevent malicious code injection

 

## Objectives

1. To inject malicious code into a DOCX file

1. To execute arbitrary code on a victim's machine

1. To gain access to a victim's network

 

# Instructions

1. The 'zip -u' command updates the specified file in the existing zip archive. In this case, the command updates the 'xxe.docx' file with the changes made to the '[Content_Types].xml' file.

 



**Code**: [[zip -u xxe.docx [Content_Types].xml]]



> - 'zip': This command is used to create, modify, and extract files from zip archives.
- '-u': This option updates the specified files in the zip archive.
- 'xxe.docx': This is the name of the zip archive file that needs to be updated.
- '[Content_Types].xml': This is the name of the file that contains the changes that need to be updated in the zip archive.



**Command** ([[Update [Content_Types].xml in xxe.docx]]):

```bash
zip -u xxe.docx [Content_Types].xml
```



2. The OXML_XXE tool is used for exploiting XXE vulnerabilities in various file formats such as DOCX, XLSX, PPTX, ODT, ODG, ODP, ODS, SVG, XML, PDF, JPG and GIF files. This tool can be used to extract sensitive information from the target system or to perform remote code execution.

 



**Code**: [[DOCX/XLSX/PPTX
ODT/ODG/ODP/ODS
SVG
XML
PDF (experi]]



> The 'data' field lists the file formats that can be exploited using this tool. The 'lang' field specifies the language used in the file format. The 'text' field provides the link to the tool's Github repository. The 'instruction' field provides a brief overview of the tool's capabilities. The 'explain' field can be used to provide additional details about the tool or the XXE vulnerability.



**Command** ([[Convert to various file formats]]):

```bash
DOCX/XLSX/PPTX
ODT/ODG/ODP/ODS
SVG
XML
PDF (experimental)
JPG (experimental)
GIF (experimental)
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Convert to various file formats]]
- [[Update [Content_Types].xml in xxe.docx]]

## Tags

- [[XML External Entity]]
- [[XXE in exotic files]]
- [[XXE inside DOCX file]]


