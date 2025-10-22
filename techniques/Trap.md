---
id: 7cc43841-b5bc-4937-ac1a-01e0a0c71b20
name: Trap
type: technique
mitre_id: T1154
mitre_url: null
created_at: '2019-08-28T21:17:33.179972+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# Trap

**MITRE ID**: T1154

## Description

The trap command allows programs and shells to specify commands that will be executed upon receiving interrupt signals. A common situation is a script allowing for graceful termination and handling of common  keyboard interrupts like ctrl+c and ctrl+d. Adversaries can use this to register code to be executed when the shell encounters specific interrupts either to gain execution or as a persistence mechanism. Trap commands are of the following format trap 'command list' signals where "command list" will be executed when "signals" are received.

# Detection

Trap commands must be registered for the shell or programs, so they appear in files. Monitoring files for suspicious or overly broad trap commands can narrow down suspicious behavior during an investigation. Monitor for suspicious processes executed through trap interrupts.

# Mitigation

Due to potential legitimate uses of trap commands, it's may be difficult to mitigate use of this technique.

# Footnotes

## Defense

Due to potential legitimate uses of trap commands, it's may be difficult to mitigate use of this technique.

## Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
