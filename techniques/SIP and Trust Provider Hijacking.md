---
id: df5d04b5-0bf0-4940-895d-845767531213
name: SIP and Trust Provider Hijacking
type: technique
mitre_id: T1198
mitre_url: null
created_at: '2019-08-28T21:17:21.010579+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# SIP and Trust Provider Hijacking

**MITRE ID**: T1198

## Description

In user mode, Windows Authenticode [1] digital signatures are used to verify a file's origin and integrity, variables that may be used to establish trust in signed code (ex: a driver with a valid Microsoft signature may be handled as safe). The signature validation process is handled via the WinVerifyTrust application programming interface (API) function,  [2] which accepts an inquiry and coordinates with the appropriate trust provider, which is responsible for validating parameters of a signature. [3]Because of the varying executable file types and corresponding signature formats, Microsoft created software components called Subject Interface Packages (SIPs) [4] to provide a layer of abstraction between API functions and files. SIPs are responsible for enabling API functions to create, retrieve, calculate, and verify signatures. Unique SIPs exist for most file formats (Executable, PowerShell, Installer, etc., with catalog signing providing a catch-all  [5]) and are identified by globally unique identifiers (GUIDs). [3]Similar to Code Signing, adversaries may abuse this architecture to subvert trust controls and bypass security policies that allow only legitimately signed code to execute on a system. Adversaries may hijack SIP and trust provider components to mislead operating system and whitelisting tools to classify malicious (or any) code as signed by: [3]Modifying the Dll and FuncName Registry values in HKLM\SOFTWARE[\WOW6432Node]Microsoft\Cryptography\OID\EncodingType 0\CryptSIPDllGetSignedDataMsg{SIP_GUID} that point to the dynamic link library (DLL) providing a SIP’s CryptSIPDllGetSignedDataMsg function, which retrieves an encoded digital certificate from a signed file. By pointing to a maliciously-crafted DLL with an exported function that always returns a known good signature value (ex: a Microsoft signature for Portable Executables) rather than the file’s real signature, an adversary can apply an acceptable signature value all files using that SIP [6] (although a hash mismatch will likely occur, invalidating the signature, since the hash returned by the function will not match the value computed from the file).Modifying the Dll and FuncName Registry values in HKLM\SOFTWARE[WOW6432Node]Microsoft\Cryptography\OID\EncodingType 0\CryptSIPDllVerifyIndirectData{SIP_GUID} that point to the DLL providing a SIP’s CryptSIPDllVerifyIndirectData function, which validates a file’s computed hash against the signed hash value. By pointing to a maliciously-crafted DLL with an exported function that always returns TRUE (indicating that the validation was successful), an adversary can successfully validate any file (with a legitimate signature) using that SIP [6] (with or without hijacking the previously mentioned CryptSIPDllGetSignedDataMsg function). This Registry value could also be redirected to a suitable exported function from an already present DLL, avoiding the requirement to drop and execute a new file on disk.Modifying the DLL and Function Registry values in HKLM\SOFTWARE[WOW6432Node]Microsoft\Cryptography\Providers\Trust\FinalPolicy{trust provider GUID} that point to the DLL providing a trust provider’s FinalPolicy function, which is where the decoded and parsed signature is checked and the majority of trust decisions are made. Similar to hijacking SIP’s CryptSIPDllVerifyIndirectData function, this value can be redirected to a suitable exported function from an already present DLL or a maliciously-crafted DLL (though the implementation of a trust provider is complex).Note: The above hijacks are also possible without modifying the Registry via DLL Search Order Hijacking.Hijacking SIP or trust provider components can also enable persistent code execution, since these malicious components may be invoked by any application that performs code signing or signature validation. [3]

# Detection

Periodically baseline registered SIPs and trust providers (Registry entries and files on disk), specifically looking for new, modified, or non-Microsoft entries. [3]

Enable CryptoAPI v2 (CAPI) event logging [7] to monitor and analyze error events related to failed trust validation (Event ID 81, though this event can be subverted by hijacked trust provider components) as well as any other provided information events (ex: successful validations). Code Integrity event logging may also provide valuable indicators of malicious SIP or trust provider loads, since protected processes that attempt to load a maliciously-crafted trust validation component will likely fail (Event ID 3033). [3]

Utilize Sysmon detection rules and/or enable the Registry (Global Object Access Auditing) [8] setting in the Advanced Security Audit policy to apply a global system access control list (SACL) and event auditing on modifications to Registry values (sub)keys related to SIPs and trust providers: [9]

HKLM\SOFTWARE\Microsoft\Cryptography\OIDHKLM\SOFTWARE\WOW6432Node\Microsoft\Cryptography\OIDHKLM\SOFTWARE\Microsoft\Cryptography\Providers\TrustHKLM\SOFTWARE\WOW6432Node\Microsoft\Cryptography\Providers\Trust

Note: As part of this technique, adversaries may attempt to manually edit these Registry keys (ex: Regedit) or utilize the legitimate registration process using Regsvr32. [3]

Analyze Autoruns data for oddities and anomalies, specifically malicious files attempting persistent execution by hiding within auto-starting locations. Autoruns will hide entries signed by Microsoft or Windows by default, so ensure "Hide Microsoft Entries" and "Hide Windows Entries" are both deselected. [3]

# Mitigation

Ensure proper permissions are set for Registry hives to prevent users from modifying keys related to SIP and trust provider components. Also ensure that these values contain their full path to prevent DLL Search Order Hijacking. [3]

Consider removing unnecessary and/or stale SIPs. [3]

Restrict storage and execution of SIP DLLs to protected directories, such as C:\Windows, rather than user directories.

Enable whitelisting solutions such as AppLocker and/or Device Guard to block the loading of malicious SIP DLLs. Components may still be able to be hijacked to suitable functions already present on disk if malicious modifications to Registry keys are not prevented.

# Footnotes

[1] Microsoft. (n.d.). Authenticode. Retrieved January 31, 2018.

[2] Microsoft. (n.d.). WinVerifyTrust function. Retrieved January 31, 2018.

[3] Graeber, M. (2017, September). Subverting Trust in Windows. Retrieved January 31, 2018.

[4] Navarro, E. (2008, July 11). SIP’s (Subject Interface Package) and Authenticode. Retrieved January 31, 2018.

[5] Hudek, T. (2017, April 20). Catalog Files and Digital Signatures. Retrieved January 31, 2018.

[6] Graeber, M. (2017, September 14). PoCSubjectInterfacePackage. Retrieved January 31, 2018.

[7] Entrust Datacard. (2017, August 16). How do I enable CAPI 2.0 logging in Windows Vista, Windows 7 and Windows 2008 Server?. Retrieved January 31, 2018.

[8] Microsoft. (2016, August 31). Registry (Global Object Access Auditing). Retrieved January 31, 2018.

[9] Microsoft. (2012, July 2). Audit Registry. Retrieved January 31, 2018.

## Defense

Ensure proper permissions are set for Registry hives to prevent users from modifying keys related to SIP and trust provider components. Also ensure that these values contain their full path to prevent [DLL Search Order Hijacking](https://attack.mitre.org/

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
