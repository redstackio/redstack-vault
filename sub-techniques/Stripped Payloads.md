---
id: aa87d423-24d8-4f3b-a66d-bce427a49963
name: Stripped Payloads
type: sub-technique
mitre_id: T1027.008
mitre_url: null
created_at: '2023-04-06T00:31:25.829492+00:00'
updated_at: '2023-04-06T00:31:25.829492+00:00'
parent_technique: '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Stripped Payloads

**MITRE ID**: T1027.008

**Parent Technique**: [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

This is a sub-technique of T1027 - Obfuscated Files or Information.

## Summary

Adversaries may attempt to make a payload difficult to analyze by removing symbols, strings, and other human readable information. Scripts and executables may contain variables names and other strings that help developers document code functionality. Symbols are often created by an operating system’

## Description

Adversaries may attempt to make a payload difficult to analyze by removing symbols, strings, and other human readable information. Scripts and executables may contain variables names and other strings that help developers document code functionality. Symbols are often created by an operating system’s `linker` when executable payloads are compiled. Reverse engineers use these symbols and strings to analyze code and to identify functionality in payloads.(Citation: Mandiant golang stripped binaries explanation)(Citation: intezer stripped binaries elf files 2018)

Adversaries may use stripped payloads in order to make malware analysis more difficult. For example, compilers and other tools may provide features to remove or obfuscate strings and symbols. Adversaries have also used stripped payload formats, such as run-only AppleScripts, a compiled and stripped version of [AppleScript](https://attack.mitre.org/techniques/T1059/002), to evade detection and analysis. The lack of human-readable information may directly hinder detection and analysis of payloads.(Citation: SentinelLabs reversing run-only applescripts 2021)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
