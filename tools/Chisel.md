---
id: 6ba0bee0-c6c3-4f37-abcb-25eb215efdb0
name: Chisel
type: tool
verified: true
created_at: '2020-02-20T07:17:13.475860+00:00'
updated_at: '2023-05-30T19:47:09.397765+00:00'
commands:
- '[[Chisel Deploy a Reverse Port Forwarding Server]]'
tags:
- '[[Network]]'
- '[[Pivot]]'
- '[[proxy]]'
- '[[tunnel]]'
---

# Chisel

**Status**: ✓ Verified

## Overview

Chisel is a fast TCP tunnel, transported over HTTP, secured via SSH. It can be built for multiple OS and architectures and is compiled to a single executable which includes both client and server. Written in Go (golang). Chisel is mainly useful for passing through firewalls, though it can also be u

## Description

# Description

Chisel is a fast TCP tunnel, transported over HTTP, secured via SSH. It can be built for multiple OS and architectures and is compiled to a single executable which includes both client and server. Written in Go (golang). Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network. It supports reverse port forwarding and dynamic port forwarding through a SOCKS5 proxy.

# Example



{{EMBEDDED_COMMAND_6d7635ae-c7d1-4125-b1e7-1d3e7539821a}}



# Installation





## Building Chisel for Other Platforms

Set the  "GOOS" and "GOARCH" environment variables to compile Chisel to run on other platforms. To build Chisel to run on a Windows x64 machine:



Common GOOS values:

- windows

- linux

- android

- darwin

Common GOARCH values:

- 386

- amd64

- arm

- arm64

For a full list, see: [https://golang.org/doc/install/source](https://golang.org/doc/install/source)







## Services

- http
- http

## Commands (1)

- [[Chisel Deploy a Reverse Port Forwarding Server]]

## Tags

- [[Network]]
- [[Pivot]]
- [[proxy]]
- [[tunnel]]


