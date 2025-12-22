---
id: 00d8844e-4637-47e8-a7d5-030c6635a0cd
name: Malleable C2
type: tool
verified: true
created_at: '2019-08-28T21:17:34.653735+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - c2
  - evasion
  - cobalt-strike
  - command-and-control
url: >-
  https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/c2_profiles-malleable_c2.htm
validated: true
---

# Malleable C2

**Status**: Unverified

## Overview

Malleable C2 is a domain-specific language (DSL) created for Cobalt Strike, a popular commercial adversary simulation platform. It allows red team operators to customize the communication profiles of Beacon implants, enabling the modification of traffic patterns to resemble legitimate network activity. This tool is primarily used in command and control (C2) operations to evade detection by endpoint detection and response (EDR) systems, network intrusion detection systems (NIDS), and other security controls.

Common use cases include blending C2 traffic with normal HTTP/HTTPS web traffic, adjusting DNS queries to mimic legitimate resolutions, or altering SMB communications to avoid signature-based detection.

## Description

Malleable C2 profiles are text-based configuration files (with a .profile extension) that define how Beacon communicates with its C2 server. The language supports multiple protocols including HTTP, HTTPS, DNS, and SMB. Key capabilities include:

- Customizing HTTP headers, user-agents, and URIs to match specific web applications or browsers.
- Implementing jitter (random delays) and sleep intervals to avoid rhythmic communication patterns.
- Using transform functions to encode/decode data in ways that obscure payloads (e.g., base64, netbios).
- Defining metadata formats and response structures to make beacons appear as benign API calls or file downloads.

Profiles are loaded into a Cobalt Strike team server, which then applies them to all connected Beacons. This makes Malleable C2 essential for advanced red teaming where stealth is paramount. It does not require compilation; profiles are human-readable and editable with any text editor.

## Features

- **Protocol Support**: HTTP/S, DNS, SMB for flexible C2 channels.
- **Traffic Morphing**: Redefine request/response formats, headers, and bodies to mimic legitimate traffic.
- **Evasion Techniques**: Jitter, proxy awareness, and data transformation to bypass heuristics.
- **Modularity**: Profiles can be staged (e.g., initial beacon vs. post-exploitation) for dynamic behavior.
- **Validation**: Built-in syntax checking within Cobalt Strike to ensure profile correctness.

## Installation

### Requirements

- Valid Cobalt Strike license (commercial tool; not open-source).
- Java Runtime Environment (JRE) version 11 or higher for Cobalt Strike.
- Text editor (e.g., VS Code, Vim) for profile creation.

### Install Commands

Malleable C2 is bundled with Cobalt Strike. No separate installation is needed:

```bash
# Download and run Cobalt Strike (requires license key)
# This is typically done via the vendor's client portal
java -jar cobaltstrike.jar
```

For profile examples and community profiles:

```bash
# Clone community profiles repository (optional, for reference)
git clone https://github.com/rsmudge/Malleable-C2-Profiles.git
```

On Kali Linux/Ubuntu (Cobalt Strike is cross-platform but primarily Windows-based for the client):

```bash
# Install Java if needed
sudo apt update && sudo apt install default-jre
# Then launch Cobalt Strike as above
```

## Basic Usage

```bash
# No direct CLI; profiles are created as text files
# Example: Create a basic HTTP profile file
cat > basic-http.profile << EOF
http-get {
    set uri "/index.php";
    client {
        header "User-Agent" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)";
        metadata {
            base64;
            prepend "action=";
            parameter "data";
        }
    }
    server {
        output {
            print;
        }
    }
}
http-post {
    set uri "/submit.php";
    ... # similar structure
}
EOF
```

Load the profile in Cobalt Strike:
1. Start the Team Server.
2. In the Cobalt Strike client: Attacks > Web Drive-by > Scripted Web Delivery (or directly via Malleable tab).
3. Select "Use Malleable C2 Profile" and load your .profile file.

### Common Options

Profiles use declarative syntax rather than CLI flags. Key profile directives:

| Directive | Description |
|-----------|-------------|
| `set uri` | Defines the path for C2 requests |
| `set jitter` | Adds randomness to sleep intervals (e.g., 30%) |
| `transform` | Encodes data (e.g., base64, gzip) |
| `header` | Customizes HTTP headers |
| `sleep` | Sets beacon check-in interval |

## Examples

### Example 1: Basic Usage

Create and load a simple HTTP GET profile to mimic a login form submission:

Profile content (save as login.profile):

```
http-get {
    set uri "/login";
    client {
        header "Accept" "text/html";
        metadata {
            transform "${unique-id}";
            base64;
            header "X-Forwarded-For";
        }
    }
    server {
        input {
            base64;
            print;
        }
    }
    sleep 5000;
    jitter 20;
}
```

Load in Cobalt Strike and generate a payload. The beacon will use "/login" URIs with base64-encoded metadata.

### Example 2: Advanced Usage

For DNS C2 (evade firewalls):

```
dns-beacon {
    set hostname "example.com";
    sleep 30000;
    jitter 60;
    get {
        transform "${beacon}.unique";
    }
    post {
        transform "${action}.data";
    }
}
```

This makes DNS queries look like subdomains under example.com.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Encrypted Channel]] Encrypted Channel (customizes encrypted C2 traffic)
- [[Asymmetric Cryptography]] HTTPS (HTTP/S profile support)
- [[Obfuscated Files or Information]] Obfuscated Files or Information (transforms and encodes payloads)
- [[Archive Collected Data]] Archive Collected Data (data transformation in profiles)

### Tactics

- [[Command and Control]] Command And Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP User-Agent strings or URI patterns in network traffic that don't match known applications.
- High jitter in beacon sleep times leading to irregular but periodic connections.
- Base64 or custom-encoded data in HTTP POST bodies or headers.
- DNS queries with long, encoded subdomains (for DNS profiles).
- Monitor for Cobalt Strike artifacts like specific Java processes or profile files on operator machines.
- Use network behavioral analysis to detect non-standard C2 patterns despite customization.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Cobalt Strike]]
- [[Sliver C2]]
- [[tools/Empire]]

## References

- Official Cobalt Strike Documentation: https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/c2_profiles-malleable_c2.htm
- Community Profiles: https://github.com/rsmudge/Malleable-C2-Profiles
- Blog on Evasion: https://www.cobaltstrike.com/blog/learning-malleable-c2
