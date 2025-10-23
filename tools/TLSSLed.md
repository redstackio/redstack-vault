---
id: 0bdb7d19-9394-4470-ba5d-ead70a2177b3
name: TLSSLed
type: tool
verified: false
created_at: '2019-08-28T21:17:31.394924+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[TLSSLed Query SSL/TLS for Weak Ciphers, Configuration, and Keys]]'
platforms:
- Web
tags:
- '[[data encryption]]'
- '[[Enumeration]]'
- '[[Network]]'
---

# TLSSLed

## Overview

TLSSLed is a Linux shell script which evaluates the security of a target's SSL/TLS (HTTPS) web server implementation. The current tests include checking if the target supports the SSLv2 protocol, the NULL cipher, weak ciphers based on their key length (40 or 56 bits), the availability of strong cip

## Description

# Description

TLSSLed is a Linux shell script which evaluates the security of a target's SSL/TLS (HTTPS) web server implementation. The current tests include checking if the target supports the SSLv2 protocol, the NULL cipher, weak ciphers based on their key length (40 or 56 bits), the availability of strong ciphers (like AES), if the digital certificate is MD5 signed, and the current SSL/TLS renegotiation capabilities.



# Example



{{EMBEDDED_COMMAND_4ba14af9-d268-4757-89d7-659536fb720c}}



# Installation

## Install on Kali



TLSSLed can also be downloaded here: [http://www.taddong.com/tools/TLSSLed_v1.3.sh](http://www.taddong.com/tools/TLSSLed_v1.3.sh)







## Platforms

- Web

## Services

- https
- https

## Commands (1)

- [[TLSSLed Query SSL/TLS for Weak Ciphers, Configuration, and Keys]]

## Tags

- [[data encryption]]
- [[Enumeration]]
- [[Network]]


