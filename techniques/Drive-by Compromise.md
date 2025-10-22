---
id: 3d55b3c9-12c1-4f37-8cf0-685242403521
name: Drive-by Compromise
type: technique
mitre_id: T1189
mitre_url: null
created_at: '2019-08-28T21:17:20.016702+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
procedures:
- '[[ASCII Conversion XSS Filter Bypass]]'
- '[[Custom DL and Execution via Malicious Macro Generator]]'
- '[[CVE-2014-6271 Shellshock Remote Code Execution]]'
- '[[CVE-2014-6271 Shellshock Remote Code Execution]]'
- '[[Linux Privilege Escalation via LXC/LXD Alpine Image]]'
- '[[Open URL Redirection via Injection Parameters]]'
- '[[Remote JavaScript Injection via SVG Onload Fetch Command]]'
- '[[SCF and URL File Attack Against Writable Share via Windows Search Connectors
  Files]]'
- '[[SCF and URL File Attack Against Writeable Share]]'
- '[[SCF and URL File Attack Against Writeable Share]]'
- '[[SSRF Exploiting URL Parser Bypass]]'
- '[[Windows - Download and execute via WebDAV]]'
- '[[XSS in SWF Flash Application]]'
---

# Drive-by Compromise

**MITRE ID**: T1189

## Description

A drive-by compromise is when an adversary gains access to a system through a user visiting a website over the normal course of browsing. With this technique, the user's web browser is targeted for exploitation.Multiple ways of delivering exploit code to a browser exist, including:A legitimate website is compromised where adversaries have injected some form of malicious code such as JavaScript, iFrames, cross-site scripting.Malicious ads are paid for and served through legitimate ad providers.Built-in web application interfaces are leveraged for the insertion of any other kind of object that can be used to display web content or contain a script that executes on the visiting client (e.g. forum posts, comments, and other user controllable web content).Often the website used by an adversary is one visited by a specific community, such as government, a particular industry, or region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted attack is referred to a strategic web compromise or watering hole attack. There are several known examples of this occurring. [1]Typical drive-by compromise process:A user visits a website that is used to host the adversary controlled content.Scripts automatically execute, typically searching versions of the browser and plugins for a potentially vulnerable version. The user may be required to assist in this process by enabling scripting or active website components and ignoring warning dialog boxes.Upon finding a vulnerable version, exploit code is delivered to the browser.If exploitation is successful, then it will give the adversary code execution on the user's system unless other protections are in place.In some cases a second visit to the website after the initial scan is required before exploit code is delivered.Unlike Exploit Public-Facing Application, the focus of this technique is to exploit software on a client endpoint upon visiting a website. This will commonly give an adversary access to systems on the internal network instead of external systems that may be in a DMZ.

# Detection

Firewalls and proxies can inspect URLs for potentially known-bad domains or parameters. They can also do reputation-based analytics on websites and their requested resources such as how old a domain is, who it's registered to, if it's on a known bad list, or how many other users have connected to it before.

Network intrusion detection systems, sometimes with SSL/TLS MITM inspection, can be used to look for known malicious scripts (recon, heap spray, and browser identification scripts have been frequently reused), common script obfuscation, and exploit code.

Detecting compromise based on the drive-by exploit from a legitimate website may be difficult. Also look for behavior on the endpoint system that might indicate successful compromise, such as abnormal behavior of browser processes. This could include suspicious files written to disk, evidence of Process Injection for attempts to hide execution, evidence of Discovery, or other unusual network traffic that may indicate additional tools transferred to the system.

# Mitigation

Drive-by compromise relies on there being a vulnerable piece of software on the client end systems. Use modern browsers with security features turned on. Ensure all browsers and plugins kept updated can help prevent the exploit phase of this technique.

For malicious code served up through ads, adblockers can help prevent that code from executing in the first place. Script blocking extensions can help prevent the execution of JavaScript that may commonly be used during the exploitation process.

Browser sandboxes can be used to mitigate some of the impact of exploitation, but sandbox escapes may still exist. [20] [21]

Other types of virtualization and application microsegmentation may also mitigate the impact of client-side exploitation. The risks of additional exploits and weaknesses in implementation may still exist. [21]

Security applications that look for behavior used during exploitation such as Windows Defender Exploit Guard (WDEG) and the Enhanced Mitigation Experience Toolkit (EMET) can be used to mitigate some exploitation behavior. [22] Control flow integrity checking is another way to potentially identify and stop a software exploit from occurring. [23] Many of these protections depend on the architecture and target application binary for compatibility.

# Footnotes

[1] Adair, S., Moran, N. (2012, May 15). Cyber Espionage & Strategic Web Compromises – Trusted Websites Serving Dangerous Results. Retrieved March 13, 2018.

[2] Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.

[3] Foltýn, T. (2018, March 13). OceanLotus ships new backdoor using old tricks. Retrieved May 22, 2018.

[4] Raiu, C., and Ivanov, A. (2016, June 17). Operation Daybreak. Retrieved February 15, 2018.

[5] FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved March 1, 2018.

[6] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[7] DiMaggio, J. (2016, April 28). Tick cyberespionage group zeros in on Japan. Retrieved July 16, 2018.

[8] Blaich, A., et al. (2018, January 18). Dark Caracal: Cyber-espionage at a Global Scale. Retrieved April 11, 2018.

[9] Kaspersky Lab's Global Research and Analysis Team. (2014, November). The Darkhotel APT A Story of Unusual Hospitality. Retrieved November 12, 2014.

[10] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[11] O'Gorman, G., and McDonald, G.. (2012, September 6). The Elderwood Project. Retrieved February 15, 2018.

[12] Clayton, M.. (2012, September 14). Stealing US business secrets: Experts ID two huge cyber 'gangs' in China. Retrieved February 15, 2018.

[13] Paganini, P. (2012, September 9). Elderwood project, who is behind Op. Aurora and ongoing attacks?. Retrieved February 13, 2018.

[14] Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.

[15] Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.

[16] Hamada, J.. (2016, July 25). Patchwork cyberespionage group expands targets from governments to wide range of industries. Retrieved August 17, 2016.

[17] Meltzer, M, et al. (2018, June 07). Patchwork APT Group Targets US Think Tanks. Retrieved July 16, 2018.

[18] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.

[19] Legezo, D. (2018, June 13). LuckyMouse hits national data center to organize country-level waterholing campaign. Retrieved August 18, 2018.

[20] Cowan, C. (2017, March 23). Strengthening the Microsoft Edge Sandbox. Retrieved March 12, 2018.

[21] Goodin, D. (2017, March 17). Virtual machine escape fetches $105,000 at Pwn2Own hacking contest - updated. Retrieved March 12, 2018.

[22] Nunez, N. (2017, August 9). Moving Beyond EMET II – Windows Defender Exploit Guard. Retrieved March 12, 2018.

[23] Wikipedia. (2018, January 11). Control-flow integrity. Retrieved March 12, 2018.

## Defense

Drive-by compromise relies on there being a vulnerable piece of software on the client end systems. Use modern browsers with security features turned on. Ensure all browsers and plugins kept updated can help prevent the exploit phase of this technique.

F

## Tactics

- [[Initial Access|TA0001 - Initial Access]]

## Related Procedures (13)

- [[ASCII Conversion XSS Filter Bypass]]
- [[Custom DL and Execution via Malicious Macro Generator]]
- [[CVE-2014-6271 Shellshock Remote Code Execution]]
- [[CVE-2014-6271 Shellshock Remote Code Execution]]
- [[Linux Privilege Escalation via LXC/LXD Alpine Image]]
- [[Open URL Redirection via Injection Parameters]]
- [[Remote JavaScript Injection via SVG Onload Fetch Command]]
- [[SCF and URL File Attack Against Writable Share via Windows Search Connectors Files]]
- [[SCF and URL File Attack Against Writeable Share]]
- [[SCF and URL File Attack Against Writeable Share]]
- [[SSRF Exploiting URL Parser Bypass]]
- [[Windows - Download and execute via WebDAV]]
- [[XSS in SWF Flash Application]]
