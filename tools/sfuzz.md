---
id: b76fc347-743e-43b2-af70-281ca2c74101
name: sfuzz
type: tool
verified: false
created_at: '2019-08-28T21:17:36.023997+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# sfuzz

## Overview

simple fuzz is exactly what it sounds like – a simple fuzzer. don’t mistake simple with a lack of fuzz capability. this fuzzer has two network modes of operation, an output mode for developing command line fuzzing scripts, as well as taking fuzzing strings from literals and building strings from se

## Description

simple fuzz is exactly what it sounds like – a simple fuzzer. don’t mistake simple with a lack of fuzz capability. this fuzzer has two network modes of operation, an output mode for developing command line fuzzing scripts, as well as taking fuzzing strings from literals and building strings from sequences.simple fuzz is built to fill a need – the need for a quickly configurable black box testing utility that doesn’t require intimate knowledge of the inner workings of C or require specialized software rigs. the aim is to just provide a simple interface, clear inputs/outputs, and reusability.Features:

simple script language for creating test cases

support for repeating strings as well as fixed strings (‘sequences’ vs. ‘literals’)

variables within test cases (ex: strings to be replaced with different strings)

tcp and udp payload transport (icmp support tbd)

binary substitution support (see basic.a11 for more information)

plugin support (NEW!) see plugin.txt for more information.

previous packet contents inclusion
