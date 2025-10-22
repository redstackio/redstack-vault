---
id: 2f6b92d2-0bcc-4770-9e43-36172f701612
name: sudo
type: tool
verified: true
created_at: '2020-02-28T02:56:35.309492+00:00'
updated_at: '2023-05-30T19:51:51.199938+00:00'
commands:
- '[[sudo -l]]'
- '[[description]]'
platforms:
- Linux
tags:
- '[[administrator]]'
- '[[privileges]]'
---

# sudo

**Status**: ✓ Verified

## Overview

sudo allows a permitted user to execute a command as the superuser or another user, as specified by the security policy. Policies are set via "/etc/sudoers" and files in "/etc/sudoers.d/". These files typically require root privileges to read , write, and modify. While sudo can be configured to giv

## Description

# Description

sudo allows a permitted user to execute a command as the superuser or another user, as specified by the security policy. Policies are set via "/etc/sudoers" and files in "/etc/sudoers.d/". These files typically require root privileges to read , write, and modify. While sudo can be configured to give a user root privileges, this introduces a massive security risk and is considered a bad practice. Administrators may set specific commands to be whitelisted instead of all (such as docker), but this is often not sufficient, as many programs running with sudo privileges would allow attackers to escalate to root.

# Example

# Installation

## Install on Debian/Ubuntu

## Platforms

- Linux

## Commands (2)

- [[sudo -l]]
- [[description]]

## Tags

- [[administrator]]
- [[privileges]]
