---
id: eff84f15-287a-4ccc-ae6c-d381829299cb
name: SSH Hijacking
type: technique
mitre_id: T1184
mitre_url: null
created_at: '2019-08-28T21:17:33.403167+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Cross-Site Request Forgery with File Upload]]'
- '[[Cross-Site Request Forgery with File Upload]]'
- '[[Docker API Port Scanning and Container Management]]'
- '[[SSH-Agent Forwarding Hijack]]'
- '[[Windows SSH with Kerberos Authentication]]'
---

# SSH Hijacking

**MITRE ID**: T1184

## Description

Secure Shell (SSH) is a standard means of remote access on Linux and macOS systems. It allows a user to connect to another system via an encrypted tunnel, commonly authenticating through a password, certificate or the use of an asymmetric encryption key pair.In order to move laterally from a compromised host, adversaries may take advantage of trust relationships established with other systems via public key authentication in active SSH sessions by hijacking an existing connection to another system. This may occur through compromising the SSH agent itself or by having access to the agent's socket. If an adversary is able to obtain root access, then hijacking SSH sessions is likely trivial. [1] [2] [3] Compromising the SSH agent also provides access to intercept SSH credentials. [4]SSH Hijacking differs from use of Remote Services because it injects into an existing SSH session rather than creating a new session using Valid Accounts.

# Detection

Use of SSH may be legitimate, depending upon the network environment and how it is used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior with SSH. Monitor for user accounts logged into systems they would not normally access or access patterns to multiple systems over a relatively short period of time. Also monitor user SSH-agent socket files being used by different users.

# Mitigation

Ensure SSH key pairs have strong passwords and refrain from using key-store technologies such as ssh-agent unless they are properly protected. Ensure that all private keys are stored securely in locations where only the legitimate owner has access to with strong passwords and are rotated frequently. Ensure proper file permissions are set and harden system to prevent root privilege escalation opportunities. Do not allow remote access via SSH as root or other privileged accounts. Ensure that agent forwarding is disabled on systems that do not explicitly require this feature to prevent misuse. [6]

# Footnotes

[1] Duarte, H., Morrison, B. (2012). (Mis)trusting and (ab)using ssh. Retrieved January 8, 2018.

[2] Adam Boileau. (2005, August 5). Trust Transience:  Post Intrusion SSH Hijacking. Retrieved December 19, 2017.

[3] Beuchler, B. (2012, September 28). SSH Agent Hijacking. Retrieved December 20, 2017.

[4] M.Léveillé, M. (2014, February 21). An In-depth Analysis of Linux/Ebury. Retrieved January 8, 2018.

[5] M.Léveillé, M.. (2014, February 21). An In-depth Analysis of Linux/Ebury. Retrieved April 19, 2019.

[6] Hatch, B. (2004, November 22). SSH and ssh-agent. Retrieved January 8, 2018.

## Defense

Ensure SSH key pairs have strong passwords and refrain from using key-store technologies such as ssh-agent unless they are properly protected. Ensure that all private keys are stored securely in locations where only the legitimate owner has access to with

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (5)

- [[Cross-Site Request Forgery with File Upload]]
- [[Cross-Site Request Forgery with File Upload]]
- [[Docker API Port Scanning and Container Management]]
- [[SSH-Agent Forwarding Hijack]]
- [[Windows SSH with Kerberos Authentication]]
