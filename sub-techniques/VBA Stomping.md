---
id: 350588a1-eb53-4e2d-81ee-3448235dde1e
name: VBA Stomping
type: sub-technique
mitre_id: T1564.007
mitre_url: null
created_at: '2023-04-06T00:31:26.915143+00:00'
updated_at: '2023-04-06T00:31:26.915143+00:00'
parent_technique: '[[Hide Artifacts|T1564 - Hide Artifacts]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# VBA Stomping

**MITRE ID**: T1564.007

**Parent Technique**: [[Hide Artifacts|T1564 - Hide Artifacts]]

This is a sub-technique of T1564 - Hide Artifacts.

## Summary

Adversaries may hide malicious Visual Basic for Applications (VBA) payloads embedded within MS Office documents by replacing the VBA source code with benign data.(Citation: FireEye VBA stomp Feb 2020)

MS Office documents with embedded VBA content store source code inside of module streams. Each mod

## Description

Adversaries may hide malicious Visual Basic for Applications (VBA) payloads embedded within MS Office documents by replacing the VBA source code with benign data.(Citation: FireEye VBA stomp Feb 2020)

MS Office documents with embedded VBA content store source code inside of module streams. Each module stream has a <code>PerformanceCache</code> that stores a separate compiled version of the VBA source code known as p-code. The p-code is executed when the MS Office version specified in the <code>_VBA_PROJECT</code> stream (which contains the version-dependent description of the VBA project) matches the version of the host MS Office application.(Citation: Evil Clippy May 2019)(Citation: Microsoft _VBA_PROJECT Stream)

An adversary may hide malicious VBA code by overwriting the VBA source code location with zero’s, benign code, or random bytes while leaving the previously compiled malicious p-code. Tools that scan for malicious VBA source code may be bypassed as the unwanted code is hidden in the compiled p-code. If the VBA source code is removed, some tools might even think that there are no macros present. If there is a version match between the <code>_VBA_PROJECT</code> stream and host MS Office application, the p-code will be executed, otherwise the benign VBA source code will be decompressed and recompiled to p-code, thus removing malicious p-code and potentially bypassing dynamic analysis.(Citation: Walmart Roberts Oct 2018)(Citation: FireEye VBA stomp Feb 2020)(Citation: pcodedmp Bontchev)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
