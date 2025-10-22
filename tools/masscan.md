---
id: f552db8e-79cd-4cc9-89c1-46bf28e46b45
name: masscan
type: tool
verified: false
created_at: '2019-08-28T21:17:26.818074+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[masscan portscan list of ips]]'
platforms:
- Linux
- Mac OSx
tags:
- '[[Enumeration]]'
- '[[Network]]'
- '[[port scanner]]'
---

# masscan

## Overview

This is the fastest Internet port scanner. It can scan the entire Internet in under 6 minutes, transmitting 10 million packets per second.It produces results similar to nmap, the most famous port scanner. Internally, it operates more like scanrand, unicornscan, and ZMap, using asynchronous transmis

## Description

# Description

This is the fastest Internet port scanner. It can scan the entire Internet in under 6 minutes, transmitting 10 million packets per second.It produces results similar to nmap, the most famous port scanner. Internally, it operates more like scanrand, unicornscan, and ZMap, using asynchronous transmission. The major difference is that it’s faster than these other scanners. In addition, it’s more flexible, allowing arbitrary address ranges and port ranges.NOTE: masscan uses a custom TCP/IP stack. Anything other than simple port scans will cause conflict with the local TCP/IP stack. This means you need to either use the -S option to use a separate IP address, or configure your operating system to firewall the ports that masscan uses.

## Example

## 

## Installation

## 

## 

## Usage

## Platforms

- Linux
- Mac OSx

## Services

- all

## Commands (1)

- [[masscan portscan list of ips]]

## Tags

- [[Enumeration]]
- [[Network]]
- [[port scanner]]
