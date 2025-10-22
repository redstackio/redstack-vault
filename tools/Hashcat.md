---
id: d4648b01-02f8-4dad-b0b9-3e3da8f509e2
name: Hashcat
type: tool
verified: false
created_at: '2019-08-28T21:17:39.946056+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[hashcat Brute Force Password Hashes]]'
platforms:
- Linux
- Windows
tags:
- '[[Brute Force]]'
- '[[Cryptography]]'
---

# Hashcat

## Overview

Hashcat is a "password recovery tool", which attempts an offline  brute force attack against hashed passwords using a wordlist of potential guesses. Hashcat supports a large number of hashed password formats, but unlike John the Ripper, it does not automatically detect the type. The hash format mus

## Description

# Description

Hashcat is a "password recovery tool", which attempts an offline  brute force attack against hashed passwords using a wordlist of potential guesses. Hashcat supports a large number of hashed password formats, but unlike John the Ripper, it does not automatically detect the type. The hash format must be identified by analyzing the hash's prefix and finding the corresponding mode via their [example hashes webpage](https://hashcat.net/wiki/doku.php?id=example_hashes), or by running Hashcat with the "--example-hashes" argument and reviewing the results.

Hashcat supports both GPU and CPU brute forcing, though GPU is heavily favored as it tends to be much faster. Hashcat also supports the ability to mutate wordlists using rules to create variations of an existing list. For example, a common rule would be to replace characters with digits that look similar, aka "leetspeak" (password becomes p@$$w0rd), or to append dates to the password list to find common passwords with birthdays appended.

# Example

# Installation

## Install on Debian/Ubuntu

## Install with Nvidia Drivers on on Debian/Ubuntu

1. Make sure the host OS is updated

2. Disable the "nvidia-nouveau" driver and reboot.

3. Prepare the environment with build tools

4. Download the latest driver for your GPU from Nvidia: [https://www.nvidia.com/Download/index.aspx](https://www.nvidia.com/Download/index.aspx)

5. Install the driver

6. Download the Hashcat source: [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/)

7. Extract the files

8. Enter the hashcat directory then build and install Hashcat

## Install on Windows

1. Download the Hashcat binaries: [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/)

2. Extract the archive to disk

3. Enter the Hashcat folder and execute either hashcat32.exe or hashcat64.exe

## Platforms

- Linux
- Windows

## Commands (1)

- [[hashcat Brute Force Password Hashes]]

## Tags

- [[Brute Force]]
- [[Cryptography]]
