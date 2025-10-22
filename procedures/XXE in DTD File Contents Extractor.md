---
id: 9ae10da8-6598-4e88-ae97-2bb93d1f1833
name: XXE in DTD File Contents Extractor
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.667448+00:00'
updated_at: '2023-04-10T20:24:43.009380+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[XML External Entity]]'
- '[[XXE in exotic files]]'
- '[[XXE inside DTD file]]'
commands:
- '[[Convert JSON to XML]]'
- '[[Install xml-js package]]'
- '[[Require xml-js package]]'
- '[[Selecting a specific element from an XML file]]'
- '[[XML Command]]'
---

# XXE in DTD File Contents Extractor

## Summary

The XXE in DTD File Contents Extractor is a procedure that takes advantage of the XML External Entity vulnerability to extract file contents from exotic files. This procedure works by injecting malicious code into a DTD file and then exploiting the vulnerability to extract the contents of the targe

## Description

# Description

The XXE in DTD File Contents Extractor is a procedure that takes advantage of the XML External Entity vulnerability to extract file contents from exotic files. This procedure works by injecting malicious code into a DTD file and then exploiting the vulnerability to extract the contents of the target file. This procedure is commonly used by attackers to extract sensitive data from a target system, such as credentials or configuration files. To execute this procedure, the attacker needs to have access to the target system and be able to inject the malicious code into the DTD file.

## Requirements

1. Access to the target system

1. Ability to inject malicious code into the DTD file

## Defense

1. Disable XML External Entities (XXE) processing if not needed

1. Use input validation to prevent injection of malicious code into DTD files

1. Restrict access to sensitive files and directories

## Objectives

1. Extract file contents from exotic files

1. Obtain sensitive data from a target system

# Instructions

1. To execute these payloads, the attacker needs to modify the DTD and insert the payload into it. Once the payload is inserted, the attacker can send the malicious XML request to the target application.

**Code**: [[DOCTYPE]]

> The DTD (Document Type Definition) is a set of rules that defines the structure of an XML document. By modifying the DTD, attackers can insert malicious payloads that get executed by the target application. This technique is commonly used in XXE (XML External Entity) attacks.

2. The XML block is used to define an XML fragment.

**Code**: [[xml]]

> The `xml` data type is used to define an XML fragment. It can be used to define an XML element or attribute. The `xml` block can contain any valid XML content, including other `xml` blocks. The `xml` block can be used in conjunction with other data types, such as `string` or `number`, to create complex data structures.

**Command** ([[XML Command]]):

```bash
xml
```

3. Use this command to control the DTD file associated with a given XML file.

**Code**: [[xml]]

> The DTD file is responsible for defining the structure and contents of an XML file. In some cases, you may not have the ability to modify the XML file itself, but you can still control the DTD file. This command allows you to modify the DTD file to ensure that the XML file is properly structured and contains the necessary content. The arguments for this command include the location of the XML file and the desired changes to the DTD file.

**Command** ([[Install xml-js package]]):

```bash
npm install xml-js
```

**Command** ([[Require xml-js package]]):

```bash
const xmljs = require('xml-js');
```

**Command** ([[Convert JSON to XML]]):

```bash
const json = {name: 'John', age: 30};
const options = {compact: true, ignoreComment: true, spaces: 4};
const xml = xmljs.js2xml(json, options);
```

4. To prevent XXE attacks, disable the DTD processing completely. If DTD processing is required, implement a secure XML parser that restricts external entities and only allows trusted sources.

**Code**: [[xml]]

> An XML External Entity (XXE) attack is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. The external entity can be used to disclose internal files, execute remote code, and perform other malicious activities. To prevent XXE attacks, it is important to disable DTD processing completely or implement a secure XML parser that restricts external entities and only allows trusted sources.

**Command** ([[Selecting a specific element from an XML file]]):

```bash
xmlstarlet sel -t -v '//book[2]/title' -nl data/books.xml
```

5. To extract the contents of a sensitive file, replace the file path in the 'payload' variable with the path of the file you want to extract. Then, run the XML code to create a new entity called 'external' which will make an HTTP request to the specified URL with the contents of the file in the 'x' parameter. The contents of the file will then be accessible from the specified URL.

**Code**: [[<!-- Load the contents of a sensitive file into a ]]

> This command uses XML entities to extract the contents of a sensitive file and send it to a specified URL. The 'payload' entity is used to load the contents of the file into a variable, and the 'param1' and 'external' entities are used to construct an HTTP request with the contents of the file in the URL. This can be used to extract sensitive information from a target system and send it to an attacker-controlled server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Convert JSON to XML]]
- [[Install xml-js package]]
- [[Require xml-js package]]
- [[Selecting a specific element from an XML file]]
- [[XML Command]]

## Tags

- [[XML External Entity]]
- [[XXE in exotic files]]
- [[XXE inside DTD file]]
