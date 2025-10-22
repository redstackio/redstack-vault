---
id: ae6bc819-ff7f-4d01-8b57-6e69a0cb3adf
name: sshuttle
type: tool
verified: true
created_at: '2020-03-07T01:02:20.822852+00:00'
updated_at: '2023-05-30T19:47:48.455176+00:00'
commands:
- '[[sshuttle Forward all traffic through SSH Tunnel]]'
platforms:
- Linux
tags:
- '[[data encryption]]'
- '[[Pivot]]'
- '[[tunnel]]'
---

# sshuttle

**Status**: ✓ Verified

## Overview

sshuttle creates a VPN connection between a local system and a remote ssh server, as long as the remote server has Python 2.3+ on it. sshuttle requires root permissions on the local machine on which it's being run.

Note: If when trying to create a tunnel to a remote ssh server, sshuttle fails with

## Description

# Description

sshuttle creates a VPN connection between a local system and a remote ssh server, as long as the remote server has Python 2.3+ on it. sshuttle requires root permissions on the local machine on which it's being run.

Note: If when trying to create a tunnel to a remote ssh server, sshuttle fails with "error code 255", try appending "-x $_TARGET_IP" to the command, where $_TARGET_IP is the same IP/hostname as the target. Specifically excluding the target server seems to resolve the issue.

# Example

# Installation

## Install on Debian/Ubuntu

## Install with Python 3

## Platforms

- Linux

## Commands (1)

- [[sshuttle Forward all traffic through SSH Tunnel]]

## Tags

- [[data encryption]]
- [[Pivot]]
- [[tunnel]]
