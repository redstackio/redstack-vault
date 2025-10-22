---
id: d88eb6a4-b979-4c56-bebe-f3e6b0224857
name: ident-user-enum
type: tool
verified: false
created_at: '2019-08-28T21:17:27.853111+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# ident-user-enum

## Overview

ident-user-enum is a simple PERL script to query the ident service (113/TCP) in order to determine the owner of the process listening on each TCP port of a target system. This can help to prioritise target service during a pentest (you might want to attack services running as root first).  Alternat

## Description

ident-user-enum is a simple PERL script to query the ident service (113/TCP) in order to determine the owner of the process listening on each TCP port of a target system.

This can help to prioritise target service during a pentest (you might want to attack services running as root first).  Alternatively, the list of usernames gathered can be used for password guessing attacks on other network services.
