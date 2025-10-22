---
id: 69f5c355-991c-4eb8-8c39-550a6cf1faef
name: Subvert Trust Controls
type: technique
mitre_id: T1553
mitre_url: null
created_at: '2023-04-06T00:31:26.796034+00:00'
updated_at: '2023-04-06T03:56:42.267030+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[AWS API Gateway Resource Enumeration]]'
- '[[AWS Lambda Function Enumeration]]'
- '[[CRLF Injection and Cookie Stealing]]'
- '[[CRLF Injection and Cookie Stealing]]'
- '[[CRLF Injection and Cookie Stealing]]'
- '[[CSRF AutoSubmit HTML POST]]'
- '[[CSRF AutoSubmit HTML POST]]'
- '[[Kubernetes Pentest with BishopFox BadPods]]'
- '[[Kubernetes Service Account Token Theft]]'
- '[[Log4Shell Scanning Procedure]]'
- '[[Log4Shell Scanning Procedure]]'
- '[[Log4Shell Scanning Procedure]]'
- '[[Mutated XSS with HTML Tag Recreation and DOMPurify Bypass]]'
- '[[Open URL Redirection Filter Bypass]]'
- '[[PHP Juggling Type and Magic Hashes]]'
- '[[Subdomain Enumeration and Takeover with tko-subs]]'
---

# Subvert Trust Controls

**MITRE ID**: T1553

## Description

Adversaries may undermine security controls that will either warn users of untrusted activity or prevent execution of untrusted programs. Operating systems and security products may contain mechanisms to identify programs or websites as possessing some level of trust. Examples of such features would include a program being allowed to run because it is signed by a valid code signing certificate, a program prompting the user with a warning because it has an attribute set from being downloaded from the Internet, or getting an indication that you are about to connect to an untrusted site.

Adversaries may attempt to subvert these trust mechanisms. The method adversaries use will depend on the specific mechanism they seek to subvert. Adversaries may conduct [File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222) or [Modify Registry](https://attack.mitre.org/techniques/T1112) in support of subverting these controls.(Citation: SpectorOps Subverting Trust Sept 2017) Adversaries may also create or steal code signing certificates to acquire trust on target systems.(Citation: Securelist Digital Certificates)(Citation: Symantec Digital Certificates) 

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (16)

- [[AWS API Gateway Resource Enumeration]]
- [[AWS Lambda Function Enumeration]]
- [[CRLF Injection and Cookie Stealing]]
- [[CRLF Injection and Cookie Stealing]]
- [[CRLF Injection and Cookie Stealing]]
- [[CSRF AutoSubmit HTML POST]]
- [[CSRF AutoSubmit HTML POST]]
- [[Kubernetes Pentest with BishopFox BadPods]]
- [[Kubernetes Service Account Token Theft]]
- [[Log4Shell Scanning Procedure]]
- [[Log4Shell Scanning Procedure]]
- [[Log4Shell Scanning Procedure]]
- [[Mutated XSS with HTML Tag Recreation and DOMPurify Bypass]]
- [[Open URL Redirection Filter Bypass]]
- [[PHP Juggling Type and Magic Hashes]]
- [[Subdomain Enumeration and Takeover with tko-subs]]
