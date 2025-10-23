---
id: 50efc607-3ff7-49d1-a670-4a216e69d777
name: Lan Turtle
type: tool
verified: true
created_at: '2020-02-19T23:14:12.987926+00:00'
updated_at: '2023-05-30T01:09:50.013875+00:00'
commands:
- '[[ssh Lan Turtle Initial Setup]]'
tags:
- '[[Hardware]]'
- '[[Social Engineering]]'
---

# Lan Turtle

**Status**: ✓ Verified

## Overview

The LAN Turtle is a hardware device that can be plugged in at a target location to provide stealth remote access, network intelligence gathering, and man-in-the-middle surveillance capabilities through a simple graphic shell. 

## Description

## Description

The LAN Turtle is a hardware device that can be plugged in at a target location to provide stealth remote access, network intelligence gathering, and man-in-the-middle surveillance capabilities through a simple graphic shell.

![9bd91364-e190-42f5-a075-5f158a4a0470.jpg](_assets/images/data.redstack.io/Ermis/9bd91364-e190-42f5-a075-5f158a4a0470.jpg)



## Setup

Initial setup on the lan turtle requires an RJ-45 cable to your router, plug that into one end, and plug the USB side into the attacker computer. Configure its Internet Access and Update the Lan Turtle Software.



1.) The Lan Turtle supports DHCP, your computer will need an IP in the range of: 172.16.84.0/24



![7d8f1724-4d88-463f-ae7d-4759de826a12.png](_assets/images/data.redstack.io/Ermis/7d8f1724-4d88-463f-ae7d-4759de826a12.png)



2.) SSH into the Lan Turtle using the following credentials & configure a new password



{{EMBEDDED_COMMAND_48affa3e-4f34-41dd-a294-27042ae9eabd}}



3.) Configure the WAN IP: CONFIG -> Change WAN IP Settings -> DHCP



4.) Update the Lan Turtle Device: Config -> Check for Updates



![ed2cae38-a3d7-4754-a8a3-03a0f721b7c5.png](_assets/images/data.redstack.io/Ermis/ed2cae38-a3d7-4754-a8a3-03a0f721b7c5.png)



5.) The Lan Turtle should now have Internet Access to obtain Modules, and is fully updated to the latest software releases. The lan turtle initial setup is completed. From here look up "lan turtle" Payloads to find different ways to use the lan turtle device.

## Commands (1)

- [[ssh Lan Turtle Initial Setup]]

## Tags

- [[Hardware]]
- [[Social Engineering]]


