---
id: fc299fae-e5eb-46c1-a402-f5a0573a25cd
name: YSoSerial.Net
type: tool
verified: true
created_at: '2020-03-06T07:21:51.887229+00:00'
updated_at: '2023-05-30T19:55:57.747597+00:00'
commands:
- '[[YSoSerial Generate a .NET Deserialization Payload]]'
platforms:
- Windows
tags:
- '[[deserialization]]'
---

# YSoSerial.Net

**Status**: ✓ Verified

## Overview

A collection of utilities and property-orientated program "gadget chains" discovered in common .NET libraries that can, under the right conditions, exploit .NET applications performing unsafe deserialization of objects.  The main driver program takes a user-specified command and wraps it in the use

## Description

# Description

A collection of utilities and property-orientated program "gadget chains" discovered in common .NET libraries that can, under the right conditions, exploit .NET applications performing unsafe deserialization of objects.  The main driver program takes a user-specified command and wraps it in the user-specified gadget chain, then serializes these objects to stdout. When an application with the required gadgets on the classpath unsafely deserializes this data, the chain will automatically be invoked and cause the command to be executed on the application host.



# Example



{{EMBEDDED_COMMAND_f6a8fff3-7ed3-4bb8-8cc7-a0461130d796}}





# Instructions

## Build from Source (Windows)

YSoSerial.Net can be compiled with Microsoft Visual Studio Community 2019 with ".NET desktop development" installed.



1. Clone the repository



2. Open "ysoserial.sln" with Visual Studio
3. Set the "Solutions Configuration" to "Release"
4. Select "Build" > "Rebuild Solution"



The compiled .exe can be found in <YSoSerialDirectory>\ysoserial\bin\Release\ysoserial.exe







## Platforms

- Windows

## Commands (1)

- [[YSoSerial Generate a .NET Deserialization Payload]]

## Tags

- [[deserialization]]


