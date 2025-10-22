---
id: be7cff00-e937-4d44-9c1c-1ebfe1ca2a3b
name: Indicator Blocking
type: sub-technique
mitre_id: T1562.006
mitre_url: null
created_at: '2023-04-06T00:31:26.362147+00:00'
updated_at: '2023-04-06T00:31:26.362147+00:00'
parent_technique: '[[Impair Defenses|T1562 - Impair Defenses]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Indicator Blocking

**MITRE ID**: T1562.006

**Parent Technique**: [[Impair Defenses|T1562 - Impair Defenses]]

This is a sub-technique of T1562 - Impair Defenses.

## Summary

An adversary may attempt to block indicators or events typically captured by sensors from being gathered and analyzed. This could include maliciously redirecting (Citation: Microsoft Lamin Sept 2017) or even disabling host-based sensors, such as Event Tracing for Windows (ETW),(Citation: Microsoft A

## Description

An adversary may attempt to block indicators or events typically captured by sensors from being gathered and analyzed. This could include maliciously redirecting (Citation: Microsoft Lamin Sept 2017) or even disabling host-based sensors, such as Event Tracing for Windows (ETW),(Citation: Microsoft About Event Tracing 2018) by tampering settings that control the collection and flow of event telemetry. (Citation: Medium Event Tracing Tampering 2018) These settings may be stored on the system in configuration files and/or in the Registry as well as being accessible via administrative utilities such as [PowerShell](https://attack.mitre.org/techniques/T1059/001) or [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047).

ETW interruption can be achieved multiple ways, however most directly by defining conditions using the [PowerShell](https://attack.mitre.org/techniques/T1059/001) <code>Set-EtwTraceProvider</code> cmdlet or by interfacing directly with the Registry to make alterations.

In the case of network-based reporting of indicators, an adversary may block traffic associated with reporting to prevent central analysis. This may be accomplished by many means, such as stopping a local process responsible for forwarding telemetry and/or creating a host-based firewall rule to block traffic to specific hosts responsible for aggregating events, such as security information and event management (SIEM) products.

In Linux environments, adversaries may disable or reconfigure log processing tools such as syslog or nxlog to inhibit detection and monitoring capabilities to facilitate follow on behaviors (Citation: LemonDuck).

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
