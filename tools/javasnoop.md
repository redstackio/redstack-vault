---
id: 01541feb-ae78-449f-8ad8-4a662762ba22
name: javasnoop
type: tool
verified: false
created_at: '2019-08-28T21:17:37.078836+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# javasnoop

## Overview

Normally, without access to the original source code, testing the security of a Java client is unpredictable at best and unrealistic at worst. With access the original source, you can run a simple Java program and attach a debugger to it remotely, stepping through code and changing variables where 

## Description

Normally, without access to the original source code, testing the security of a Java client is unpredictable at best and unrealistic at worst. With access the original source, you can run a simple Java program and attach a debugger to it remotely, stepping through code and changing variables where needed. Doing the same with an applet is a little bit more difficult.Unfortunately, real-life scenarios don’t offer you this option, anyway. Compilation and decompilation of Java are not really as deterministic as you might imagine. Therefore, you can’t just decompile a Java application, run it locally and attach a debugger to it.Next, you may try to just alter the communication channel between the client and the server, which is where most of the interesting things happen anyway. This works if the client uses HTTP with a configurable proxy. Otherwise, you’re stuck with generic network traffic altering mechanisms. These are not so great for almost all cases, because the data is usually not plaintext. It’s usually a custom protocol, serialized objects, encrypted, or some combination of those.JavaSnoop attempts to solve this problem by allowing you attach to an existing process (like a debugger) and instantly begin tampering with method calls, run custom code, or just watch what’s happening on the system.javasnoop Homepage | Kali javasnoop Repo






