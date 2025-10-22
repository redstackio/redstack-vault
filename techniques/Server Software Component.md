---
id: 43c006b0-a4f4-45b9-b145-48dd2fd1be68
name: Server Software Component
type: technique
mitre_id: T1505
mitre_url: null
created_at: '2023-04-06T00:31:27.006549+00:00'
updated_at: '2023-04-06T03:56:16.249788+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Cobalt Strike Team Server Installation and Execution]]'
- '[[Exploiting IIS Machine Keys to Generate ViewState for RCE]]'
- '[[Exploiting IIS Machine Keys to Generate ViewState for RCE]]'
- '[[Exploiting IIS Machine Keys to Generate ViewState for RCE]]'
- '[[ObjectDataProvider JSON.NET Deserialization RCE]]'
- '[[Type Confusion with LosFormatter and Calc.exe Execution]]'
---

# Server Software Component

**MITRE ID**: T1505

## Description

Adversaries may abuse legitimate extensible development features of servers to establish persistent access to systems. Enterprise server applications may include features that allow developers to write and install software or scripts to extend the functionality of the main application. Adversaries may install malicious components to extend and abuse server applications.(Citation: volexity_0day_sophos_FW)

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (6)

- [[Cobalt Strike Team Server Installation and Execution]]
- [[Exploiting IIS Machine Keys to Generate ViewState for RCE]]
- [[Exploiting IIS Machine Keys to Generate ViewState for RCE]]
- [[Exploiting IIS Machine Keys to Generate ViewState for RCE]]
- [[ObjectDataProvider JSON.NET Deserialization RCE]]
- [[Type Confusion with LosFormatter and Calc.exe Execution]]
