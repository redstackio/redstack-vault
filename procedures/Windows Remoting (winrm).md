---
id: 05fb3408-3134-423a-a6dd-1bac2eadab66
name: Windows Remoting (winrm)
type: procedure
verified: false
submitted: false
created_at: '2020-07-16T14:48:19.968350+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[Open interactive session with remote computer]]'
- '[[winrm client config trusted host for external domain]]'
- '[[winrm client default config]]'
- '[[winrm client enable unencrypted data transfer]]'
- '[[winrm Default Config]]'
- '[[winrm display running listener with ports]]'
- '[[winrm server enable basic authentication]]'
- '[[winrm server enable unencrypted data transfer]]'
- '[[winrm set channel binding token hardening level]]'
- '[[winrm test connection to winrm service]]'
- '[[winrm view permissions for basic authentication]]'
---

# Windows Remoting (winrm)

## Summary

Windows Remote Management (winrm) allows different vendor's hardware and operating systems to interoperate. You can authenticate and control a windows machine from linux, mac or bsd using WinRM. You setup the winrm service on the target system, and connect to it from the attacker system remotely. T

## Description

# Description

Windows Remote Management (winrm) allows different vendor's hardware and operating systems to interoperate. You can authenticate and control a windows machine from linux, mac or bsd using WinRM.

You setup the winrm service on the target system, and connect to it from the attacker system remotely. The following will describe how to configure winrm on both systems to make them communication.

Please note the default configuration for winrm does not enable basic auth or unencrypted data for the server. And does not enable unencrypted data for the client so you have to set this up yourself.

# Instructions

Setup winrm on the target machine with a listener and connect to it from a remote machine. Then setup winrm on the attacker machine.

## Target System

1. This command will setup the default winrm config.

**Command** ([[winrm Default Config]]):

```bash
winrm quickconfig
```

2. (optional) Check to see if a listener is running and on which ports

**Command** ([[winrm display running listener with ports]]):

```bash
winrm e winrm/config/listener
```

3. Enable basic authentication

3a. Check to see if basic authentication is permitted.

**Command** ([[winrm view permissions for basic authentication]]):

```bash
winrm get winrm/config/service
```

3b. Enable basic authentication.

**Command** ([[winrm server enable basic authentication]]):

```bash
winrm set winrm/config/Service/Auth @{Basic="true"}

```

4. Allow unencrypted data transfer.

**Command** ([[winrm server enable unencrypted data transfer]]):

```bash
winrm set winrm/config/Service @{AllowUnencrypted="true"}

```

5. Change the channel binding token hardening level to relaxed or none; to accept connections that do not contain a channel binding token.

**Command** ([[winrm set channel binding token hardening level]]):

```bash
winrm set winrm/config/service/auth @{CbtHardeningLevel="relaxed"}
```

## Attacker System

1. Setup the winrm default config.

**Command** ([[winrm client default config]]):

```bash
winrm get winrm/config/client
```

2. Enable AllowUnencrypted data transfer

**Command** ([[winrm client enable unencrypted data transfer]]):

```bash
winrm set winrm/config/client @{AllowUnencrypted="true"}
```

3. (Optional) If the target machine is in an External Domain, specify the trusted host.

**Command** ([[winrm client config trusted host for external domain]]):

```bash
winrm set winrm/config/client @{TrustedHosts="host1, host2, host3"}
```

4. Test the connection to the WinRM service. 

**Command** ([[winrm test connection to winrm service]]):

```bash
winrm identify -r:http://$TARGET_IP:5985 -auth:basic -u:$USERNAME -p:$PASSWORD -encoding:utf-8
```

5. Open a PSSession using WinRM to the target system.

**Command** ([[Open interactive session with remote computer]]):

```bash
$cred = Get-Credential
Enter-PSSession -ComputerName 'winserver1' -Credential $cred -Authentication Basic

```

## Commands Used

- [[Open interactive session with remote computer]]
- [[winrm client config trusted host for external domain]]
- [[winrm client default config]]
- [[winrm client enable unencrypted data transfer]]
- [[winrm Default Config]]
- [[winrm display running listener with ports]]
- [[winrm server enable basic authentication]]
- [[winrm server enable unencrypted data transfer]]
- [[winrm set channel binding token hardening level]]
- [[winrm test connection to winrm service]]
- [[winrm view permissions for basic authentication]]
