---
id: 9d2a2822-f135-4206-a643-569178311445
name: Detection of .NET Serialization Attacks
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.065177+00:00'
updated_at: '2023-04-06T03:55:59.078007+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[Process Discovery|T1057 - Process Discovery]]'
- '[[Software Discovery|T1518 - Software Discovery]]'
tags:
- '[[Detection]]'
- '[[.NET Serialization]]'
---

# Detection of .NET Serialization Attacks

## Summary

This procedure focuses on detecting .NET serialization attacks. .NET serialization is the process of converting an object into a stream of bytes that can be persisted to a storage medium or transmitted over a network. Attackers can abuse this functionality to execute arbitrary code on a target syst

## Description

# Description

This procedure focuses on detecting .NET serialization attacks. .NET serialization is the process of converting an object into a stream of bytes that can be persisted to a storage medium or transmitted over a network. Attackers can abuse this functionality to execute arbitrary code on a target system. This procedure provides a way to detect the use of .NET serialization by an attacker, allowing defenders to respond before any damage is done. 

Technical Explanation: .NET serialization is a feature in the .NET framework that allows developers to convert objects into a stream of bytes that can be used for storage or transmission. Attackers can abuse this functionality by crafting a serialized object that contains malicious code. When the object is deserialized, the code is executed on the target system. This procedure provides a way to detect the use of .NET serialization by monitoring for certain indicators of compromise (IOCs). 

Business Value: This procedure helps to protect against .NET serialization attacks, which can be used to execute arbitrary code on a target system. By detecting these attacks early, defenders can respond before any damage is done, preventing data theft, system compromise, or other negative outcomes.

 

## Requirements

1. Access to logs and monitoring tools

1. Knowledge of .NET serialization and its potential for abuse

 

## Defense

1. Implement network segmentation to limit the impact of any successful attacks

1. Regularly review and update security policies and procedures to stay up-to-date with the latest threats

1. Train employees on how to recognize and respond to suspicious activity or indicators of compromise

 

## Objectives

1. Detect the use of .NET serialization by an attacker

1. Alert security personnel when .NET serialization is detected

1. Prevent data theft, system compromise, or other negative outcomes

 

# Instructions

1. To monitor for .NET serialization attacks, you can use tools such as Sysmon or network intrusion detection systems (NIDS) to look for certain indicators of compromise (IOCs). These can include the creation of serialized objects in the network traffic or file system, or the use of certain .NET serialization libraries. When these IOCs are detected, an alert can be generated and sent to security personnel for further investigation.

 



**Code**: [[AAEAAAD/////AQAAAAAAAAAMAgAAAF9TeXN0ZW0u[...]0KPC9]]



> Serialized objects can be identified by their file extension (.dat, .bin, .ser, etc.) or by their content, which will be a stream of bytes that can be converted back into an object. Some .NET serialization libraries that are commonly abused by attackers include BinaryFormatter, NetDataContractSerializer, and DataContractSerializer.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[Process Discovery|T1057 - Process Discovery]]
- [[Software Discovery|T1518 - Software Discovery]]

## Tags

- [[Detection]]
- [[.NET Serialization]]


