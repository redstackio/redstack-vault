---
id: 4c1665c3-d06a-460b-8c43-896b0d3fcd43
name: Linux - TMUX Session Hijacking
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.579869+00:00'
updated_at: '2023-04-10T20:34:30.315718+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Accessibility Features|T1546.008 - Accessibility Features]]'
tags:
- '[[Hijack TMUX session]]'
- '[[Linux - Privilege Escalation]]'
commands:
- '[[Create tmux socket]]'
- '[[List TMUX sessions]]'
---

# Linux - TMUX Session Hijacking

## Summary

The Linux - TMUX Session Hijacking procedure involves an attacker gaining access to a victim's TMUX session and using it to escalate privileges. TMUX is a terminal multiplexer that allows multiple terminals to be accessed and controlled from a single screen. By hijacking a TMUX session, an attacker

## Description

# Description

The Linux - TMUX Session Hijacking procedure involves an attacker gaining access to a victim's TMUX session and using it to escalate privileges. TMUX is a terminal multiplexer that allows multiple terminals to be accessed and controlled from a single screen. By hijacking a TMUX session, an attacker can execute commands as the victim, potentially gaining elevated privileges. 

To execute this attack, the attacker needs to have access to the victim's TMUX socket, which can be obtained by reading the socket file or by exploiting a vulnerability in the TMUX configuration. Once the attacker has access to the socket, they can use it to attach to the victim's TMUX session and execute commands as the victim.

This procedure can be valuable to an attacker as it allows them to gain privileged access to a system without needing to escalate privileges through traditional means, such as exploiting a vulnerability or brute-forcing credentials.

## Requirements

1. Access to the victim's TMUX socket

## Defense

1. Limit access to TMUX socket files to authorized users

1. Regularly monitor for suspicious TMUX activity

1. Use strong authentication measures to prevent unauthorized access to the system

## Objectives

1. Gain privileged access to a system

# Instructions

1. To gain read access to the tmux socket, use the following command: 

chmod +r /tmp/tmux-1000/default

**Code**: [[/tmp/tmux-1000/default]]

> This command changes the permissions of the tmux socket file to allow read access to all users. The tmux socket is a file used by the tmux terminal multiplexer to communicate with its sessions and windows. By granting read access to this file, you can use tmux commands to view the state of tmux sessions and windows without actually attaching to them.

**Command** ([[Create tmux socket]]):

```bash
tmux -S /tmp/tmux-1000/default new-session -d -s mysession
```

2. To list all the TMUX sessions running on the machine, run the following command:

**Code**: [[export TMUX=/tmp/tmux-1000/default,1234,0 
tmux ls]]

> - The 'export' command sets the environment variable TMUX to the specified value.
- The 'tmux ls' command lists all the currently running TMUX sessions.

**Command** ([[List TMUX sessions]]):

```bash
export TMUX=/tmp/tmux-1000/default,1234,0
tmux ls
```

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[Accessibility Features|T1546.008 - Accessibility Features]]

## Commands Used

- [[Create tmux socket]]
- [[List TMUX sessions]]

## Tags

- [[Hijack TMUX session]]
- [[Linux - Privilege Escalation]]
