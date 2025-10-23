---
id: f06b792c-4bf8-4a41-bb4b-cb5fbfacaf37
name: NetBIOS Enumeration
type: cheatsheet
verified: true
created_at: '2019-09-23T17:52:33.661910+00:00'
updated_at: '2023-05-30T20:08:56.573699+00:00'
---

# NetBIOS Enumeration

**Status**: ✓ Verified

## Description

Basic NetBIOS  scanning and enumeration.







**Command** ([[nmblookup Query a System Running NetBIOS]]):

```bash
nmblookup -A $_TARGET_IP
```







**Command** ([[NBTscan Query a System Running NetBIOS]]):

```bash
nbtscan _$TARGET_IP
```







**Command** ([[NBTscan a Windows 95 System Running NetBIOS]]):

```bash
nbtscan -r $_TARGET_IP
```







**Command** ([[NBTscan a Subnet for Systems Running NetBIOS]]):

```bash
nbtscan $_TARGET_SUBNET/$_CIDR
```






