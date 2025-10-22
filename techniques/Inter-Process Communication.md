---
id: e4d1468a-dadc-4634-8771-7d6056787da2
name: Inter-Process Communication
type: technique
mitre_id: T1559
mitre_url: null
created_at: '2023-04-06T00:31:26.712987+00:00'
updated_at: '2023-04-06T03:56:00.804393+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[JWT Key ID (kid) Claim Misuse]]'
- '[[Node Deserialization Exploitation using node-serialize]]'
---

# Inter-Process Communication

**MITRE ID**: T1559

## Description

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. 

Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows [Dynamic Data Exchange](https://attack.mitre.org/techniques/T1559/002) or [Component Object Model](https://attack.mitre.org/techniques/T1559/001). Linux environments support several different IPC mechanisms, two of which being sockets and pipes.(Citation: Linux IPC) Higher level execution mediums, such as those of [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)s, may also leverage underlying IPC mechanisms. Adversaries may also use [Remote Services](https://attack.mitre.org/techniques/T1021) such as [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) to facilitate remote IPC execution.(Citation: Fireeye Hunting COM June 2019)

## Tactics

- [[Execution|TA0002 - Execution]]

## Related Procedures (2)

- [[JWT Key ID (kid) Claim Misuse]]
- [[Node Deserialization Exploitation using node-serialize]]
