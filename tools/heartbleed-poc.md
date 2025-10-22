---
id: c3d47148-d045-48ae-b65a-1674ff817cf0
name: heartbleed-poc
type: tool
verified: true
created_at: '2020-02-22T05:15:06.784664+00:00'
updated_at: '2023-05-30T19:51:26.200390+00:00'
commands:
- '[[Exploit Heartbleed to Read Protected Memory]]'
- '[[Heartbleed Dump Vulnerable Memory of a Server]]'
platforms:
- Linux
tags:
- '[[Cryptography]]'
- '[[known vulnerability]]'
- '[[Network]]'
---

# heartbleed-poc

**Status**: ✓ Verified

## Overview

heartbleed-poc.py is a tool used to test for and exploit the Heartbleed vulnerability (CVE-2014-0160) on remote systems. Heartbleed affects OpenSSL libraries earlier than 1.0.1g, which allows remote attackers to read protected memory on the affected web server, potentially disclosing sensitive info

## Description

# Description

heartbleed-poc.py is a tool used to test for and exploit the Heartbleed vulnerability (CVE-2014-0160) on remote systems. Heartbleed affects OpenSSL libraries earlier than 1.0.1g, which allows remote attackers to read protected memory on the affected web server, potentially disclosing sensitive information including private keys, passwords, and other sensitive information.

# Example

Installation

Clone the repo and execute the script

## Platforms

- Linux

## Services

- https
- https

## Commands (2)

- [[Exploit Heartbleed to Read Protected Memory]]
- [[Heartbleed Dump Vulnerable Memory of a Server]]

## Tags

- [[Cryptography]]
- [[known vulnerability]]
- [[Network]]
