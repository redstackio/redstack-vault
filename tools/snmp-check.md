---
id: e935bb63-acaf-4b80-820f-e8d1f8f6920d
name: snmp-check
type: tool
verified: false
created_at: '2019-08-28T21:17:28.403145+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[snmp-check Enumerate SNMP Server]]'
platforms:
- Linux
- Windows
tags:
- '[[Enumeration]]'
- '[[Network]]'
---

# snmp-check

## Overview

Query a network entitty for a tree of information typically related to the entity, using SNMP GETNEXT requests. Results are formatted in human friendly format, unlike snmpwalk which requires add-on(s). snmp-check enumerates a number of settings including: contact description detect write access (se

## Description

# Description

Query a network entitty for a tree of information typically related to the entity, using SNMP GETNEXT requests. Results are formatted in human friendly format, unlike snmpwalk which requires add-on(s).



snmp-check enumerates a number of settings including:



- contact

- description

- detect write access (separate action by enumeration)

- devices

- domain

- hardware and storage informations

- hostname

- IIS statistics

- IP forwarding

- listening UDP ports

- location

- motd

- mountpoints

- network interfaces

- network services

- processes

- routing information

- software components

- system uptime

- TCP connections

- total memory

- uptime

- user accounts



# Example



{{EMBEDDED_COMMAND_be12360e-df20-4322-8ea9-6691391e3835}}



# Installation

## Install on Debian/Ubuntu

1. Install the Ruby SNMP package



2. Download snmp-check: [Download from Author (Nothink)](http://www.nothink.org/codes/snmpcheck/index.php)







## Platforms

- Linux
- Windows

## Services

- snmp

## Commands (1)

- [[snmp-check Enumerate SNMP Server]]

## Tags

- [[Enumeration]]
- [[Network]]


