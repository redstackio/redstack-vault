---
id: f8a742e5-d525-4b69-86e8-f9cab336724b
name: Man in the Browser
type: technique
mitre_id: T1185
mitre_url: null
created_at: '2019-08-28T21:17:17.808518+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Man in the Browser

**MITRE ID**: T1185

## Description

Adversaries can take advantage of security vulnerabilities and inherent functionality in browser software to change content, modify behavior, and intercept information as part of various man in the browser techniques. [1]A specific example is when an adversary injects software into a browser that allows an them to inherit cookies, HTTP sessions, and SSL client certificates of a user and use the browser as a way to pivot into an authenticated intranet. [2] [3]Browser pivoting requires the SeDebugPrivilege and a high-integrity process to execute. Browser traffic is pivoted from the adversary's browser through the user's browser by setting up an HTTP proxy which will redirect any HTTP and HTTPS traffic. This does not alter the user's traffic in any way. The proxy connection is severed as soon as the browser is closed. Whichever browser process the proxy is injected into, the adversary assumes the security context of that process. Browsers typically create a new process for each tab that is opened and permissions and certificates are separated accordingly. With these permissions, an adversary could browse to any resource on an intranet that is accessible through the browser and which the browser has sufficient permissions, such as Sharepoint or webmail. Browser pivoting also eliminates the security provided by 2-factor authentication. [4]

# Detection

This is a difficult technique to detect because adversary traffic would be masked by normal user traffic. No new processes are created and no additional software touches disk. Authentication logs can be used to audit logins to specific web applications, but determining malicious logins versus benign logins may be difficult if activity matches typical user behavior. Monitor for process injection against browser applications

# Mitigation

Since browser pivoting requires a high integrity process to launch from, restricting user permissions and addressing Privilege Escalation and Bypass User Account Control opportunities can limit the exposure to this technique. 

Close all browser sessions regularly and when they are no longer needed.

# Footnotes

[1] Wikipedia. (2017, October 28). Man-in-the-browser. Retrieved January 10, 2018.

[2] Mudge, R. (n.d.). Browser Pivoting. Retrieved January 10, 2018.

[3] De Tore, M., Warner, J. (2018, January 15). MALICIOUS CHROME EXTENSIONS ENABLE CRIMINALS TO IMPACT OVER HALF A MILLION USERS AND GLOBAL BUSINESSES. Retrieved January 17, 2018.

[4] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[5] Reaves, J. (2016, October 15). TrickBot: We Missed you, Dyre. Retrieved August 2, 2018.

[6] Keshet, L. (2016, November 09). Tricks of the Trade: A Deeper Look Into TrickBot’s Machinations. Retrieved August 2, 2018.

[7] Pornasdoro, A. (2017, October 12). Trojan:Win32/Totbrick. Retrieved September 14, 2018.

[8] Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.

## Defense

Since browser pivoting requires a high integrity process to launch from, restricting user permissions and addressing Privilege Escalation and [Bypass User Account Control](https://attack.mitre.org/techniques/T1088) opportunities can limit the exposure to 

## Tactics

- [[Collection|TA0009 - Collection]]
