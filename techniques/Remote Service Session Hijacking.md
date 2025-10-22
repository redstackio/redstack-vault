---
id: e424fdb5-a392-4f1f-b725-07f17d919a0c
name: Remote Service Session Hijacking
type: technique
mitre_id: T1563
mitre_url: null
created_at: '2023-04-06T00:31:26.193349+00:00'
updated_at: '2023-04-06T03:56:27.404447+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[DCOM Shell Command Execution via MMC Application Class]]'
- '[[RDP Session Takeover with Mimikatz]]'
- '[[RDP Session Takeover with Mimikatz]]'
- '[[Subdomain Enumeration and Takeover using Hostile Subdomain Bruteforcer]]'
---

# Remote Service Session Hijacking

**MITRE ID**: T1563

## Description

Adversaries may take control of preexisting sessions with remote services to move laterally in an environment. Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet, SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous interaction with that service.

Adversaries may commandeer these sessions to carry out actions on remote systems. [Remote Service Session Hijacking](https://attack.mitre.org/techniques/T1563) differs from use of [Remote Services](https://attack.mitre.org/techniques/T1021) because it hijacks an existing session rather than creating a new session using [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation: RDP Hijacking Medium)(Citation: Breach Post-mortem SSH Hijack)

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (4)

- [[DCOM Shell Command Execution via MMC Application Class]]
- [[RDP Session Takeover with Mimikatz]]
- [[RDP Session Takeover with Mimikatz]]
- [[Subdomain Enumeration and Takeover using Hostile Subdomain Bruteforcer]]
