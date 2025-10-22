---
id: 6db19644-6e79-4844-bee4-7a244ceab6b9
name: keimpx
type: tool
verified: false
created_at: '2019-08-28T21:17:34.886856+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# keimpx

## Overview

keimpx is an open source tool, released under a modified version of Apache License 1.1.It can be used to quickly check for valid credentials across a network over SMB. Credentials can be: Combination of user / plain-text password. Combination of user / NTLM hash. Combination of user / NTLM logon se

## Description

keimpx is an open source tool, released under a modified version of Apache License 1.1.It can be used to quickly check for valid credentials across a network over SMB. Credentials can be:

Combination of user / plain-text password.

Combination of user / NTLM hash.

Combination of user / NTLM logon session token.

If any valid credentials has been discovered across the network after its attack phase, the user is asked to choose which host to connect to and which valid credentials to use, then he will be prompted with an interactive SMB shell where the user can:

Spawn an interactive command prompt.

Navigate through the remote SMB shares: list, upload, download files, create, remove files, etc.

Deploy and undeploy his own service, for instance, a backdoor listening on a TCP port for incoming connections.

List users details, domains and password policy.
