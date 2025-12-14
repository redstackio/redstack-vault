---
tags:
  - kvm
  - exposure
  - no-auth
  - remote-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Hardware
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:42.798Z'
sub_techniques: []
id: 2bb58bb2-b269-4348-855a-a78de008d412
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Access-Exposed-TinyPilot-KVM-Interface

## Summary

This procedure exploits an improperly configured TinyPilot KVM device exposed to the internet without authentication, allowing attackers to gain direct remote access to a connected workstation, such as a DoD system, for viewing and controlling the user's session.

## Description

TinyPilot is a hardware KVM (Keyboard, Video, Mouse) device used for remote management of computers. In this scenario, the device is connected to a sensitive DoD workstation and exposed online via its default web interface without any authentication. Visiting the IP address loads the KVM service, providing full screen viewing, mouse, and keyboard control. This enables confidentiality breaches (e.g., capturing displayed sensitive data), integrity violations (e.g., injecting inputs to alter actions), and availability impacts (e.g., disrupting operations). The attack requires only the exposed IP and a web browser, making it highly accessible to threat actors.

## Requirements

1. Knowledge of the exposed TinyPilot KVM IP address (e.g., obtained via reconnaissance or scanning)
2. Internet connectivity to reach the public IP
3. A standard web browser capable of handling HTML5 video streams for the KVM interface

## Defense

Defensive measures and detection strategies:

- Implement network segmentation to prevent internet exposure of internal management devices like KVMs
- Enforce strong authentication (e.g., username/password, MFA) on all remote access interfaces
- Use firewalls to block inbound traffic to non-essential ports and monitor for anomalous access to device IPs
- Regularly scan for exposed services using tools like Shodan or internal vulnerability scanners
- Enable logging on the KVM device to detect unauthorized access attempts

## Objectives

1. Achieve unauthenticated remote access to the target workstation
2. View and capture sensitive screen content in real-time
3. Manipulate the system via remote input to alter user actions or exfiltrate data

## Instructions

### Step 1: Locate and Access the Exposed Interface

**Context**: Identify the public IP of the TinyPilot KVM and navigate to it using a browser to initiate the connection without credentials.

No specific command required; use a web browser:

Open your browser and enter the URL: `https://<exposed-ip>` (replace `<exposed-ip>` with the actual IP, e.g., https://192.0.2.1).

> The page loads the TinyPilot web interface instantly. If HTTPS is enforced, accept any self-signed certificate warnings. The live video feed of the connected DoD workstation appears, along with input controls for mouse and keyboard.

### Step 2: Interact with the Workstation

**Context**: Once connected, use the interface to view the screen and send inputs, confirming full control.

No command; interact via the browser interface:

- Click within the video feed to capture mouse movements.
- Use keyboard to type inputs that are relayed to the workstation.
- Observe the screen for real-time updates, such as user sessions or displayed documents.

> Successful interaction shows immediate response on the remote screen, e.g., moving the mouse cursor or typing text into open applications. No notifications are sent to the local user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- kvm
- exposure
- no-auth
- remote-access
