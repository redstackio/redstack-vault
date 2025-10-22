---
id: f1889df3-0714-46bb-8a39-65b3c70f5ddb
name: Install Root Certificate
type: technique
mitre_id: T1130
mitre_url: null
created_at: '2019-08-28T21:17:35.422507+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[AWS SSH Key Persistence]]'
- '[[AWS SSH Persistence using Public Key]]'
- '[[Filter Bypass with Exotic Payloads for Cross Site Scripting]]'
---

# Install Root Certificate

**MITRE ID**: T1130

## Description

Root certificates are used in public key cryptography to identify a root certificate authority (CA). When a root certificate is installed, the system or application will trust certificates in the root's chain of trust that have been signed by the root certificate. [1] Certificates are commonly used for establishing secure TLS/SSL communications within a web browser. When a user attempts to browse a website that presents a certificate that is not trusted an error message will be displayed to warn the user of the security risk. Depending on the security settings, the browser may not allow the user to establish a connection to the website.Installation of a root certificate on a compromised system would give an adversary a way to degrade the security of that system. Adversaries have used this technique to avoid security warnings prompting users when compromised systems connect over HTTPS to adversary controlled web servers that spoof legitimate websites in order to collect login credentials. [2]Atypical root certificates have also been pre-installed on systems by the manufacturer or in the software supply chain and were used in conjunction with malware/adware to provide a man-in-the-middle capability for intercepting information transmitted over secure TLS/SSL communications. [3]Root certificates (and their associated chains) can also be cloned and reinstalled. Cloned certificate chains will carry many of the same metadata characteristics of the source and can be used to sign malicious code that may then bypass signature validation tools (ex: Sysinternals, antivirus, etc.) used to block execution and/or uncover artifacts of Persistence. [4]In macOS, the Ay MaMi malware uses /usr/bin/security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /path/to/malicious/cert to install a malicious certificate as a trusted root certificate into the system keychain. [5]

# Detection

A system's root certificates are unlikely to change frequently. Monitor new certificates installed on a system that could be due to malicious activity. [4] Check pre-installed certificates on new systems to ensure unnecessary or suspicious certificates are not present. Microsoft provides a list of trustworthy root certificates online and through authroot.stl. [4] The Sysinternals Sigcheck utility can also be used (sigcheck[64].exe -tuv) to dump the contents of the certificate store and list valid certificates not rooted to the Microsoft Certificate Trust List. [10]

Installed root certificates are located in the Registry under HKLM\SOFTWARE\Microsoft\EnterpriseCertificates\Root\Certificates\ and [HKLM or HKCU]\Software[\Policies]\Microsoft\SystemCertificates\Root\Certificates\. There are a subset of root certificates that are consistent across Windows systems and can be used for comparison: [11]

18F7C1FCC3090203FD5BAA2F861A754976C8DD25245C97DF7514E7CF2DF8BE72AE957B9E04741E853B1EFD3A66EA28B16697394703A72CA340A05BD57F88CD7223F3C813818C994614A89C99FA3B52478F43288AD272F3103B6FB1428485EA3014C0BCFEA43489159A520F0D93D032CCAF37E7FE20A8B419BE36A4562FB2EE05DBB3D32323ADF445084ED656CDD4EEAE6000AC7F40C3802C171E30148030C072

# Mitigation

HTTP Public Key Pinning (HPKP) is one method to mitigate potential man-in-the-middle situations where and adversary uses a mis-issued or fraudulent certificate to intercept encrypted communications by enforcing use of an expected certificate. [9]

Windows Group Policy can be used to manage root certificates and the Flags value of HKLM\SOFTWARE\Policies\Microsoft\SystemCertificates\Root\ProtectedRoots can be set to 1 to prevent non-administrator users from making further root installations into their own HKCU certificate store. [4]

# Footnotes

[1] Wikipedia. (2016, December 6). Root certificate. Retrieved February 20, 2017.

[2] Sancho, D., Hacquebord, F., Link, R. (2014, July 22). Finding Holes Operation Emmental. Retrieved February 9, 2016.

[3] Onuma. (2015, February 24). Superfish: Adware Preinstalled on Lenovo Laptops. Retrieved February 20, 2017.

[4] Graeber, M. (2017, December 22). Code Signing Certificate Cloning Attacks and Defenses. Retrieved April 3, 2018.

[5] Patrick Wardle. (2018, January 11). Ay MaMi. Retrieved March 19, 2018.

[6] Levene, B., Falcone, R., Grunzweig, J., Lee, B., Olson, R. (2015, August 20). Retefe Banking Trojan Targets Sweden, Switzerland and Japan. Retrieved July 3, 2017.

[7] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[8] Faou, M. and Boutin, J.. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.

[9] Wikipedia. (2017, February 28). HTTP Public Key Pinning. Retrieved March 31, 2017.

[10] Russinovich, M. et al.. (2017, May 22). Sigcheck. Retrieved April 3, 2018.

[11] Smith, T. (2016, October 27). AppUNBlocker: Bypassing AppLocker. Retrieved December 19, 2017.

## Defense

HTTP Public Key Pinning (HPKP) is one method to mitigate potential man-in-the-middle situations where and adversary uses a mis-issued or fraudulent certificate to intercept encrypted communications by enforcing use of an expected certificate. (Citation: W

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (3)

- [[AWS SSH Key Persistence]]
- [[AWS SSH Persistence using Public Key]]
- [[Filter Bypass with Exotic Payloads for Cross Site Scripting]]
