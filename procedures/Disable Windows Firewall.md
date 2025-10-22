---
id: a6dd58ae-6284-46bb-8bbb-62232447a92c
name: Disable Windows Firewall
type: procedure
verified: true
submitted: true
created_at: '2019-11-15T01:22:12.424921+00:00'
updated_at: '2023-05-25T19:48:10.238386+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Disabling Security Tools|T1089 - Disabling Security Tools]]'
platforms:
- Windows
tags:
- '[[Antivirus Bypass]]'
- '[[Service Attacks]]'
commands:
- '[[Allow an Application Through Windows Firewall (Windows 7+)]]'
- '[[Allow a Port Through Windows Firewall (Windows 2008 and Earlier)]]'
- '[[Allow a Port Through Windows Firewall (Windows 7+)]]'
- '[[Disable Windows Firewall (Windows 7+)]]'
- '[[Windows Firewall Disable Firewall (Windows 2008 and Earlier)]]'
---

# Disable Windows Firewall

**Status**: ✓ Verified

## Summary

Windows Firewall is enabled on almost all modern systems and will block access to most ports unless specifically whitelisted. Attackers will often want to disable the firewall, or add exceptions so they can access resources which are normally unavailable remotely. 

## Description

# Description

Windows Firewall is enabled on almost all modern systems and will block access to most ports unless specifically whitelisted. Attackers will often want to disable the firewall, or add exceptions so they can access resources which are normally unavailable remotely.

# Instructions

## Windows 7 and Later

**Command** ([[Disable Windows Firewall (Windows 7+)]]):

```bash
netsh advfirewall set allprofiles state off
```

**Command** ([[Allow a Port Through Windows Firewall (Windows 7+)]]):

```bash
netsh advfirewall firewall add rule name="Open Port $_PORT" dir=in action=allow protocol=TCP localport=$_PORT
```

**Command** ([[Allow an Application Through Windows Firewall (Windows 7+)]]):

```bash
netsh advfirewall firewall add rule name="Allow $_Program to bypass firewall rules" dir=in action=allow program="C:\$_PATH\$_PROGRAM.exe" enable=yes
```

## Windows 2008 and Earlier

**Command** ([[Windows Firewall Disable Firewall (Windows 2008 and Earlier)]]):

```bash
netsh firewall set opmode DISABLE
```

**Command** ([[Allow a Port Through Windows Firewall (Windows 2008 and Earlier)]]):

```bash
netsh firewall add portopening TCP $_PORT "Open Port $_PORT"
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Disabling Security Tools|T1089 - Disabling Security Tools]]

## Commands Used

- [[Allow an Application Through Windows Firewall (Windows 7+)]]
- [[Allow a Port Through Windows Firewall (Windows 2008 and Earlier)]]
- [[Allow a Port Through Windows Firewall (Windows 7+)]]
- [[Disable Windows Firewall (Windows 7+)]]
- [[Windows Firewall Disable Firewall (Windows 2008 and Earlier)]]

## Tags

- [[Antivirus Bypass]]
- [[Service Attacks]]
