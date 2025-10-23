---
id: a05a198e-b1bb-48d1-bd75-3ebe970659cd
name: Attach to Existing tmux Server Socket by Path
type: procedure
verified: false
submitted: false
created_at: '2019-11-25T21:35:19.654137+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Linux
tags:
- '[[Misconfiguration]]'
commands:
- '[[ps List All Running Processes]]'
- '[[tmux Attach to a Socket]]'
---

# Attach to Existing tmux Server Socket by Path

## Summary

When creating a session, tmux allows users to specify an alternate path for the socket. This opens up a vulnerability if other users are able to read/write to the socket, allowing them to attach to the session with full permissions of the user who opened it. 

## Description

# Description

When creating a session, tmux allows users to specify an alternate path for the socket. This opens up a vulnerability if other users are able to read/write to the socket, allowing them to attach to the session with full permissions of the user who opened it.



# Instructions

1. Identify tmux sessions.





**Command** ([[ps List All Running Processes]]):

```bash
ps aux
```





If a tmux session is found with path (eg. /tmp/tmux/sess) and the current user has sufficient permissions, connect to it with the -S flag and specify the path.





**Command** ([[tmux Attach to a Socket]]):

```bash
tmux -S $_PATH/TO/SOCKET/FILE
```





## Platforms

- Linux

## Commands Used

- [[ps List All Running Processes]]
- [[tmux Attach to a Socket]]

## Tags

- [[Misconfiguration]]


