---
id: 6fcb05bc-ae51-4d64-8ffa-42c6ba430c5f
name: Indicator Blocking
type: technique
mitre_id: T1054
mitre_url: null
created_at: '2019-08-28T21:17:40.538868+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Indicator Blocking

**MITRE ID**: T1054

## Description

An adversary may attempt to block indicators or events typically captured by sensors from being gathered and analyzed. This could include modifying sensor settings stored in configuration files and/or Registry keys to disable or maliciously redirect event telemetry. [1]In the case of network-based reporting of indicators, an adversary may block traffic associated with reporting to prevent central analysis. This may be accomplished by many means, such as stopping a local process responsible for forwarding telemetry and/or creating a host-based firewall rule to block traffic to specific hosts responsible for aggregating events, such as security information and event management (SIEM) products.

# Detection

Detect lack of reported activity from a host sensor. Different methods of blocking may cause different disruptions in reporting. Systems may suddenly stop reporting all data or only certain kinds of data.

Depending on the types of host information collected, an analyst may be able to detect the event that triggered a process to stop or connection to be blocked.

# Mitigation

Ensure event tracers/forwarders [2], firewall policies, and other associated mechanisms are secured with appropriate permissions and access controls. Consider automatically relaunching forwarding mechanisms at recurring intervals (ex: temporal, on-logon, etc.) as well as applying appropriate change management to firewall rules and other related system configurations.

# Footnotes

[1] Microsoft. (2009, May 17). Backdoor:Win32/Lamin.A. Retrieved September 6, 2018.

[2] Microsoft. (2018, May 30). Event Tracing. Retrieved September 6, 2018.

## Defense

Ensure event tracers/forwarders (Citation: Microsoft ETW May 2018), firewall policies, and other associated mechanisms are secured with appropriate permissions and access controls. Consider automatically relaunching forwarding mechanisms at recurring inte

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
