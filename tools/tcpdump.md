---
id: 519d3441-dc7b-4729-9a47-c2bd7d304874
name: tcpdump
type: tool
verified: false
created_at: '2019-08-28T21:17:40.229526+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[tcpdump Intercept Packets on Loopback Interface]]'
platforms:
- Linux
tags:
- '[[data exposure]]'
- '[[Network]]'
---

# tcpdump

## Overview

Tcpdump prints out a description of the contents of packets on a network interface that match the boolean expression; the description is preceded by a time stamp, printed, by default, as hours,minutes, seconds, and fractions of a second since midnight.  It can also be run with the -w flag, which ca

## Description

# Description

Tcpdump prints out a description of the contents of packets on a network interface that match the boolean expression; the description is preceded by a time stamp, printed, by default, as hours,minutes, seconds, and fractions of a second since midnight.  It can also be run with the -w flag, which causes it to save the packet data to a file for later analysis, and/or with the -r flag, which causes it to read from a saved packet file rather than to read packets from a network interface.

Tcpdump is a priceless tool when it comes to penetration testing, as attackers can use it to monitor network traffic reaching a system and potentially derive sensitive information from the packet dumps.

# Example

# Installation

## Install on Debian/Ubuntu

## Platforms

- Linux

## Commands (1)

- [[tcpdump Intercept Packets on Loopback Interface]]

## Tags

- [[data exposure]]
- [[Network]]
