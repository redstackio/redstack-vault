---
id: 4a951cfd-5825-4bbb-9d7b-39d3242f858a
name: Rubber Ducky
type: tool
verified: true
created_at: '2020-02-19T23:14:00.953690+00:00'
updated_at: '2023-05-30T19:45:08.980471+00:00'
commands:
- '[[duckencoder Encode Rubber Ducky Script into inject.bin]]'
tags:
- '[[Hardware]]'
- '[[Social Engineering]]'
---

# Rubber Ducky

**Status**: ✓ Verified

## Overview

A USB device to plug into a target computer and run payloads, you can have it install a backdoor, exfiltrate documents, steal passwords or execute any number of pentest tasks. The Rubber Ducky acts as a HID device - like a keyboard typing with perfect accuracy and injecting keystrokes. 

## Description

## Description





A USB device to plug into a target computer and run payloads, you can have it install a backdoor, exfiltrate documents, steal passwords or execute any number of pentest tasks. The Rubber Ducky acts as a HID device - like a keyboard typing with perfect accuracy and injecting keystrokes.

![c13abd5d-fefc-4b7a-a46b-227d03f24e50.jpg](_assets/images/data.redstack.io/Bassem/c13abd5d-fefc-4b7a-a46b-227d03f24e50.jpg)





# Payload

A rubber ducky encodes payloads into a binary that run the script when the device is plugged into a machine. There are many different types of payloads available or, look below at the Ducky Scripting language and syntax to write your own Payloads.



## Example

{{EMBEDDED_CODE_943a7e8e-391f-49d9-9ae5-4fd3a23847ff}}





## Ducky Script

Ducky Script is an easy to learn language for the USB Rubber Ducky. Writing scripts can be done from any common ascii text editor like vim or gedit and compiled to a binary the Rubber Ducky device can read using duckencoder.

Scripting is simple, each command resides on a new line and may have options that follow. Commands are written in ALL CAPS because ducks are loud and like to quack proudly.

Most of the commands invoke key-strokes or key-combos, strings or text while some might offer delays or pauses.



Please check the Usage for a short-list of Script Commands or the Rubber Ducky Wiki for their full documentation.











## Duck Encoder

Ducky Scripts are compiled into hex files ready to be named inject.bin and moved to the root of a microSD card for execution by the USB Rubber Ducky. This is done with the tool duckencoder.

This is a cross-platform CLI java program that converts a Ducky Script into a hex file.

Clone the repo of the Duck Encoder and run the java program to encode the payload script.



[Duck Encoder Github Repo](https://github.com/hak5darren/USB-Rubber-Ducky)







{{EMBEDDED_COMMAND_833cc87a-ff3c-4127-b276-cdd7deffe305}}







## Commands (1)

- [[duckencoder Encode Rubber Ducky Script into inject.bin]]

## Tags

- [[Hardware]]
- [[Social Engineering]]


