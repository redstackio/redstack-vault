---
id: 5fd4bb2b-1c2b-4f03-b575-bf8dc0ad1bcb
name: FFmpeg HLS Playlist Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.818564+00:00'
updated_at: '2023-04-06T03:56:40.829624+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Deobfuscate/Decode Files or Information|T1140 - Deobfuscate/Decode Files or Information]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[FFmpeg HLS vulnerability]]'
- '[[How it works (Explanations from neex - Hackerone links)]]'
---

# FFmpeg HLS Playlist Injection

## Summary

FFmpeg is a popular open-source multimedia framework that can be used to decode, encode, transcode, and stream audio and video. A vulnerability exists in FFmpeg that allows an attacker to inject arbitrary commands into the FFmpeg command line. This vulnerability can be exploited by an attacker to e

## Description

# Description

FFmpeg is a popular open-source multimedia framework that can be used to decode, encode, transcode, and stream audio and video. A vulnerability exists in FFmpeg that allows an attacker to inject arbitrary commands into the FFmpeg command line. This vulnerability can be exploited by an attacker to execute malicious code on the target system. The vulnerability is caused by FFmpeg's handling of HLS playlists. By creating a specially crafted AVI file with a malicious HLS playlist, an attacker can inject arbitrary FFmpeg commands into the command line, allowing them to execute code on the target system. This technique can be used for various purposes, such as gaining remote access to a system, stealing sensitive data, or installing malware. 

Technical Explanation: The vulnerability exists because FFmpeg does not properly sanitize input when parsing HLS playlists. By creating a specially crafted AVI file with a malicious HLS playlist, an attacker can inject arbitrary FFmpeg commands into the command line. These commands can be used to execute arbitrary code on the target system. 

Business Value: An attacker can use this technique to gain access to sensitive data, install malware, or take control of a system. This can result in significant financial losses, reputational damage, and legal liabilities for the victim organization.

 

## Requirements

1. Access to a system running FFmpeg

1. Ability to create a specially crafted AVI file with a malicious HLS playlist

 

## Defense

1. Always keep FFmpeg updated to the latest version

1. Implement input validation and sanitization in applications that use FFmpeg

1. Use network segmentation to prevent attackers from accessing critical systems

 

## Objectives

1. Inject arbitrary commands into the FFmpeg command line

1. Execute malicious code on the target system

 

# Instructions

1. This command creates an AVI file with an HLS playlist inside using GAB2. The resulting playlist contains the specified files in the order they are listed in the 'data' field.

 

The 'data' field contains the list of files to be included in the playlist, along with their duration. The 'EXTINF' tag specifies the duration of each file in seconds. The 'EXT-X-MEDIA-SEQUENCE' tag specifies the sequence number of the first file in the playlist. The 'EXT-X-ENDLIST' tag indicates that the playlist is complete and no more media files will be added to it. The resulting AVI file will contain the HLS playlist and can be played using any compatible media player.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Deobfuscate/Decode Files or Information|T1140 - Deobfuscate/Decode Files or Information]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[FFmpeg HLS vulnerability]]
- [[How it works (Explanations from neex - Hackerone links)]]


