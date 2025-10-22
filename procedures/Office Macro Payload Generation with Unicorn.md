---
id: 74a3e0a7-cb60-4933-8c75-a4ddfc34fa86
name: Office Macro Payload Generation with Unicorn
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.454876+00:00'
updated_at: '2023-04-10T20:36:53.764465+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Scheduled Task|T1053 - Scheduled Task]]'
sub_techniques:
- '[[Scheduled Task|T1053.005 - Scheduled Task]]'
tags:
- '[[DOCM - C# converted to Office VBA macro]]'
- '[[Office - Attacks]]'
commands:
- '[[Generate Unicorn Payload]]'
---

# Office Macro Payload Generation with Unicorn

## Summary

The Office Macro Payload Generation with Unicorn procedure is used to generate a payload for use in an Office macro attack. This procedure utilizes the Unicorn tool to generate a payload that can be used in a malicious Office macro. The payload is generated in C# and then converted to Office VBA ma

## Description

# Description

The Office Macro Payload Generation with Unicorn procedure is used to generate a payload for use in an Office macro attack. This procedure utilizes the Unicorn tool to generate a payload that can be used in a malicious Office macro. The payload is generated in C# and then converted to Office VBA macro format. This procedure is typically used by an attacker to gain access to a target's system or network. 

Technical Explanation: The Unicorn tool is a simple tool for generating payloads that can be used in various exploits. This procedure uses the Unicorn tool to generate a payload in C# format. The payload is then converted to Office VBA macro format using a conversion tool. The resulting macro can then be used to execute the payload on a target's system. 

Business Value: This procedure can be used by an attacker to gain access to a target's system or network. By using a payload generated with Unicorn, an attacker can execute code on a target's system without being detected. This can allow the attacker to steal sensitive data or gain access to a target's network.

## Requirements

1. Access to the Unicorn tool

1. Access to a conversion tool for converting the payload to Office VBA macro format

## Defense

1. Ensure that all Office macros are properly vetted and approved before execution

1. Implement network segmentation to limit the impact of a successful attack

1. Use endpoint protection software to detect and prevent the execution of malicious macros

## Objectives

1. Generate a payload for use in an Office macro attack

1. Execute code on a target's system

# Instructions

1. To generate a macro payload using Unicorn, run the following command:

**Code**: [[python unicorn.py payload.cs cs macro]]

> This command generates a macro payload using the Unicorn tool. The 'payload.cs' is the name of the file that will contain the generated payload. The 'cs' argument specifies the programming language of the payload. The 'macro' argument specifies that the payload will be a macro. The command should be executed in a Python environment.

**Command** ([[Generate Unicorn Payload]]):

```bash
python unicorn.py payload.cs cs macro
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Scheduled Task|T1053 - Scheduled Task]]

### Sub-Techniques

- [[Scheduled Task|T1053.005 - Scheduled Task]]

## Commands Used

- [[Generate Unicorn Payload]]

## Tags

- [[DOCM - C# converted to Office VBA macro]]
- [[Office - Attacks]]
