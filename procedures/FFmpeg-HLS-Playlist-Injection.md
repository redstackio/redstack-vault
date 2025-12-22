---
id: 5fd4bb2b-1c2b-4f03-b575-bf8dc0ad1bcb
name: FFmpeg-HLS-Playlist-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.818564+00:00'
updated_at: '2024-10-01T12:00:00+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - >-
    [[techniques/Deobfuscate/Decode Files or Information|T1140 -
    Deobfuscate/Decode Files or Information]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/FFmpeg HLS vulnerability]]'
  - '[[tags/How it works (Explanations from neex - Hackerone links)]]'
  - command-injection
  - ffmpeg-exploit
commands:
  - '[[commands/create-malicious-hls-data-json]]'
  - '[[commands/gab2-generate-avi-with-hls]]'
platforms:
  - Linux
tools:
  - '[[tools/GAB2]]'
validated: true
---

# FFmpeg HLS Playlist Injection

## Summary

FFmpeg is a popular open-source multimedia framework that can be used to decode, encode, transcode, and stream audio and video. A vulnerability exists in FFmpeg that allows an attacker to inject arbitrary commands into the FFmpeg command line. This vulnerability can be exploited by an attacker to execute malicious code on the target system by creating a specially crafted AVI file with a malicious HLS playlist embedded inside.

## Description

FFmpeg is a popular open-source multimedia framework that can be used to decode, encode, transcode, and stream audio and video. A vulnerability exists in FFmpeg that allows an attacker to inject arbitrary commands into the FFmpeg command line. This vulnerability can be exploited by an attacker to execute malicious code on the target system. The vulnerability is caused by FFmpeg's handling of HLS playlists. By creating a specially crafted AVI file with a malicious HLS playlist, an attacker can inject arbitrary FFmpeg commands into the command line, allowing them to execute code on the target system. This technique can be used for various purposes, such as gaining remote access to a system, stealing sensitive data, or installing malware.

Technical Explanation: The vulnerability exists because FFmpeg does not properly sanitize input when parsing HLS playlists embedded in certain container formats like AVI. By crafting the playlist data with a malicious URI in the segment list (e.g., using shell metacharacters like '; command;' in the URI field), the parsing process can lead to command injection during segment fetching or processing, especially in configurations where external downloaders are used or in vulnerable versions. The attacker embeds this playlist into an AVI file using a generator tool, tricking the target into processing the file with FFmpeg (e.g., ffmpeg -i malicious.avi).

Business Value: An attacker can use this technique to gain access to sensitive data, install malware, or take control of a system. This can result in significant financial losses, reputational damage, and legal liabilities for the victim organization.

## Requirements

1. Vulnerable version of FFmpeg installed on the target system (e.g., versions prior to patches for the specific CVE; check advisories for affected ranges).
2. Ability to deliver the crafted AVI file to the target (e.g., via phishing, file share, or drive-by download).
3. GAB2 tool installed on the attacker's machine for generating the embedded AVI file.
4. Basic knowledge of shell command injection payloads.

## Defense

Defensive measures and detection strategies:

- Always keep FFmpeg updated to the latest version to apply security patches for known vulnerabilities.
- Implement input validation and sanitization in applications that use FFmpeg, especially when processing user-supplied media files.
- Use network segmentation to prevent attackers from accessing critical systems and monitor for anomalous FFmpeg executions.
- Employ endpoint detection tools to monitor for unexpected command executions spawned by FFmpeg processes (e.g., via Sysmon or auditd).
- Scan media files for embedded malicious content using antivirus or specialized tools before processing.

## Objectives

1. Inject arbitrary commands into the FFmpeg command line via a crafted HLS playlist.
2. Execute malicious code on the target system upon FFmpeg processing the AVI file.
3. Achieve remote code execution or data exfiltration depending on the injected payload.

## Instructions

### Step 1: Create Malicious HLS Data JSON

**Context**: Prepare the JSON configuration for the HLS playlist, including a malicious URI in one of the segment entries to enable command injection. The 'data' field is an array of objects specifying durations and URIs; craft the URI to include shell injection (e.g., '; whoami > /tmp/pwned.txt;') assuming the vulnerability triggers a system call with the URI.

**Command** ([[commands/create-malicious-hls-data-json]]):
```bash
echo '{"data": [{"duration": 10, "uri": "dummy-segment.ts"}, {"duration": 10, "uri": "dummy.com; whoami > /tmp/pwned.txt;"}] }' > hls-data.json
```

> This step creates a JSON file defining the playlist structure. The malicious URI will be parsed during FFmpeg's HLS handling, injecting the command. Verify the file with cat hls-data.json to ensure the injection payload is correctly placed. If the target environment uses a different shell, adjust the payload (e.g., use $() for bash subshells).

### Step 2: Generate AVI File with Embedded HLS Playlist

**Context**: Use the GAB2 tool to embed the malicious HLS playlist data into an AVI container file. This creates a polyglot file that appears as a valid AVI but triggers HLS parsing and command injection when processed by vulnerable FFmpeg.

**Command** ([[commands/gab2-generate-avi-with-hls]]):
```bash
gab2 -f hls-data.json -o malicious.avi
```

> This generates the malicious AVI file. The tool processes the JSON 'data' field to build the playlist with EXTINF tags for durations, EXT-X-MEDIA-SEQUENCE starting at 0, and EXT-X-ENDLIST to mark completion. Success is indicated by the creation of malicious.avi (check with ls -la malicious.avi). Test locally on a vulnerable FFmpeg instance if possible, but avoid on production systems.

### Step 3: Deliver and Trigger Execution

**Context**: Deliver the AVI file to the target and ensure it is processed by FFmpeg. This could involve social engineering to get the user to run ffmpeg -i malicious.avi or integrating into a larger application that uses FFmpeg.

**Instructions**: Transfer the file via email, USB, or shared drive. If direct access, execute on target: ffmpeg -i malicious.avi -f null -

> Expected: The command injection triggers during playlist parsing, executing the payload (e.g., writing output to /tmp/pwned.txt). Verify success by checking for the indicator file or process artifacts on the target.
