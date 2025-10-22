---
id: f26cb9af-a3d0-4350-a707-d3d8f4acf589
name: Clear Command History
type: sub-technique
mitre_id: T1070.003
mitre_url: null
created_at: '2023-04-06T00:31:25.946568+00:00'
updated_at: '2023-04-06T00:31:25.946568+00:00'
parent_technique: '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Clear Command History

**MITRE ID**: T1070.003

**Parent Technique**: [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

This is a sub-technique of T1070 - Indicator Removal on Host.

## Summary

In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done.

On Linux 

## Description

In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done.

On Linux and macOS, these command histories can be accessed in a few different ways. While logged in, this command history is tracked in a file pointed to by the environment variable <code>HISTFILE</code>. When a user logs off a system, this information is flushed to a file in the user's home directory called <code>~/.bash_history</code>. The benefit of this is that it allows users to go back to commands they've used before in different sessions.

Adversaries may delete their commands from these logs by manually clearing the history (<code>history -c</code>) or deleting the bash history file <code>rm ~/.bash_history</code>.  

Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to clear command history data (<code>clear logging</code> and/or <code>clear history</code>).(Citation: US-CERT-TA18-106A)

On Windows hosts, PowerShell has two different command history providers: the built-in history and the command history managed by the <code>PSReadLine</code> module. The built-in history only tracks the commands used in the current session. This command history is not available to other sessions and is deleted when the session ends.

The <code>PSReadLine</code> command history tracks the commands used in all PowerShell sessions and writes them to a file (<code>$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt</code> by default). This history file is available to all sessions and contains all past history since the file is not deleted when the session ends.(Citation: Microsoft PowerShell Command History)

Adversaries may run the PowerShell command <code>Clear-History</code> to flush the entire command history from a current PowerShell session. This, however, will not delete/flush the <code>ConsoleHost_history.txt</code> file. Adversaries may also delete the <code>ConsoleHost_history.txt</code> file or edit its contents to hide PowerShell commands they have run.(Citation: Sophos PowerShell command audit)(Citation: Sophos PowerShell Command History Forensics)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
