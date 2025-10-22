---
id: 8c13a2d6-b552-4c77-8842-987ee8384ae0
name: Visual Basic
type: sub-technique
mitre_id: T1059.005
mitre_url: null
created_at: '2023-04-06T00:31:27.056347+00:00'
updated_at: '2023-04-06T00:31:27.056347+00:00'
parent_technique: '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks]]'
- '[[Macro Delivery of Meterpreter Shellcode]]'
- '[[Office Word Macro Payload Delivery with Metasploit]]'
---

# Visual Basic

**MITRE ID**: T1059.005

**Parent Technique**: [[Command-Line Interface|T1059 - Command-Line Interface]]

This is a sub-technique of T1059 - Command-Line Interface.

## Summary

Adversaries may abuse Visual Basic (VB) for execution. VB is a programming language created by Microsoft with interoperability with many Windows technologies such as [Component Object Model](https://attack.mitre.org/techniques/T1559/001) and the [Native API](https://attack.mitre.org/techniques/T1106

## Description

Adversaries may abuse Visual Basic (VB) for execution. VB is a programming language created by Microsoft with interoperability with many Windows technologies such as [Component Object Model](https://attack.mitre.org/techniques/T1559/001) and the [Native API](https://attack.mitre.org/techniques/T1106) through the Windows API. Although tagged as legacy with no planned future evolutions, VB is integrated and supported in the .NET Framework and cross-platform .NET Core.(Citation: VB .NET Mar 2020)(Citation: VB Microsoft)

Derivative languages based on VB have also been created, such as Visual Basic for Applications (VBA) and VBScript. VBA is an event-driven programming language built into Microsoft Office, as well as several third-party applications.(Citation: Microsoft VBA)(Citation: Wikipedia VBA) VBA enables documents to contain macros used to automate the execution of tasks and other functionality on the host. VBScript is a default scripting language on Windows hosts and can also be used in place of [JavaScript](https://attack.mitre.org/techniques/T1059/007) on HTML Application (HTA) webpages served to Internet Explorer (though most modern browsers do not come with VBScript support).(Citation: Microsoft VBScript)

Adversaries may use VB payloads to execute malicious commands. Common malicious usage includes automating execution of behaviors with VBScript or embedding VBA content into [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001) payloads (which may also involve [Mark-of-the-Web Bypass](https://attack.mitre.org/techniques/T1553/005) to enable execution).(Citation: Default VBS macros Blocking )

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]

## Related Procedures

There are 3 procedures using this sub-technique:

- [[Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks]]
- [[Macro Delivery of Meterpreter Shellcode]]
- [[Office Word Macro Payload Delivery with Metasploit]]
