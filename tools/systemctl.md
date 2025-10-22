---
id: 246d45f2-d6e1-4212-b6f9-7757243084d1
name: systemctl
type: tool
verified: true
created_at: '2020-02-19T23:08:13.147049+00:00'
updated_at: '2023-05-30T19:45:23.367846+00:00'
commands:
- '[[systemctl Enable and Start a Service by File Name]]'
platforms:
- Linux
tags:
- '[[administrator]]'
- '[[Operating Systems]]'
---

# systemctl

**Status**: ✓ Verified

## Overview

Systemctl is used to control the systemd system and service manager, which is present on almost all Linux distributions built after 2015. While systemctl has many uses, it is primarily used by administrators to stop, start, and create services. Root privileges are generally required to modify servi

## Description

# Description

Systemctl is used to control the systemd system and service manager, which is present on almost all Linux distributions built after 2015. While systemctl has many uses, it is primarily used by administrators to stop, start, and create services. Root privileges are generally required to modify services using systemctl, but if configured with SUID or sudo permissions, it may be used for privilege escalation.

# Example

# Installation

systemctl is installed with systemd, and installed with the operating system.

## Platforms

- Linux

## Commands (1)

- [[systemctl Enable and Start a Service by File Name]]

## Tags

- [[administrator]]
- [[Operating Systems]]
