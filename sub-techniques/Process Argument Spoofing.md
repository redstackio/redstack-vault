---
id: e3f729b6-8780-4a35-bb70-de4d6c470071
name: Process Argument Spoofing
type: sub-technique
mitre_id: T1564.010
mitre_url: null
created_at: '2023-04-06T00:31:27.249657+00:00'
updated_at: '2023-04-06T00:31:27.249657+00:00'
parent_technique: '[[Hide Artifacts|T1564 - Hide Artifacts]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Process Argument Spoofing

**MITRE ID**: T1564.010

**Parent Technique**: [[Hide Artifacts|T1564 - Hide Artifacts]]

This is a sub-technique of T1564 - Hide Artifacts.

## Summary

Adversaries may attempt to hide process command-line arguments by overwriting process memory. Process command-line arguments are stored in the process environment block (PEB), a data structure used by Windows to store various information about/used by a process. The PEB includes the process command-

## Description

Adversaries may attempt to hide process command-line arguments by overwriting process memory. Process command-line arguments are stored in the process environment block (PEB), a data structure used by Windows to store various information about/used by a process. The PEB includes the process command-line arguments that are referenced when executing the process. When a process is created, defensive tools/sensors that monitor process creations may retrieve the process arguments from the PEB.(Citation: Microsoft PEB 2021)(Citation: Xpn Argue Like Cobalt 2019)

Adversaries may manipulate a process PEB to evade defenses. For example, [Process Hollowing](https://attack.mitre.org/techniques/T1055/012) can be abused to spawn a process in a suspended state with benign arguments. After the process is spawned and the PEB is initialized (and process information is potentially logged by tools/sensors), adversaries may override the PEB to modify the command-line arguments (ex: using the [Native API](https://attack.mitre.org/techniques/T1106) <code>WriteProcessMemory()</code> function) then resume process execution with malicious arguments.(Citation: Cobalt Strike Arguments 2019)(Citation: Xpn Argue Like Cobalt 2019)(Citation: Nviso Spoof Command Line 2020)

Adversaries may also execute a process with malicious command-line arguments then patch the memory with benign arguments that may bypass subsequent process memory analysis.(Citation: FireEye FiveHands April 2021)

This behavior may also be combined with other tricks (such as [Parent PID Spoofing](https://attack.mitre.org/techniques/T1134/004)) to manipulate or further evade process-based detections.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
