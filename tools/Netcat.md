---
id: 7e7f4297-8a04-4c6d-a583-d872b6addbb4
name: Netcat
type: tool
verified: false
created_at: '2019-08-28T21:17:40.581707+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[Netcat Connect to a Remote Server]]'
platforms:
- Linux
- Windows
tags:
- '[[Exfiltration]]'
- '[[Network]]'
- '[[Service Attacks]]'
---

# Netcat

## Overview

Netcat (also known as ncat, nc), is a computer networking utility for reading from and writing to network connections using TCP or UDP. The command is designed to be a dependable back-end that can be used directly or easily driven by other programs and scripts. At the same time, it is a feature-ric

## Description

# Description

Netcat (also known as ncat, nc), is a computer networking utility for reading from and writing to network connections using TCP or UDP. The command is designed to be a dependable back-end that can be used directly or easily driven by other programs and scripts. At the same time, it is a feature-rich network debugging and investigation tool, since it can produce almost any kind of connection its user could need and has a number of built-in capabilities.

Netcat is most commonly used in penetration testing to connect to and receive connections from remote servers, often with a command prompt or Bash terminal session. Netcat is often set to either listen on a system and catch reverse shells, or connect to a remote system which is listening with a bind shell.

There are multiple versions of Netcat with slightly different features. The main difference between them is the OpenBSD version does not support the "-e" argument, which executes a program and connects the stdin/stdout/stderr to a network socket.

# Example

# Installation

## Install on Debian/Ubuntu

Note: Depending on the package manager and sources, Netcat may need to be installed using the name "nc" , "ncat" , or "netcat". 

## Platforms

- Linux
- Windows

## Commands (1)

- [[Netcat Connect to a Remote Server]]

## Tags

- [[Exfiltration]]
- [[Network]]
- [[Service Attacks]]
