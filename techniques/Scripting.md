---
id: df9f1408-ff17-454c-a392-68a21b39d0a3
name: Scripting
type: technique
mitre_id: T1064
mitre_url: null
created_at: '2019-08-28T21:17:38.363528+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[ActiveX-Based Autorun Macro with InkPicture Control and Painted Event]]'
- '[[Akamai WAF Bypass via Common XSS Injection Attack]]'
- '[[Akamai WAF Bypass via Prompt User Input]]'
- '[[ASR Bypass Create Child Process Rule 5 and Open PowerShell from Command Prompt]]'
- '[[AWS Userdata Retrieval via Instance Metadata Service]]'
- '[[Azure Automation Account Runbook Persistence]]'
- '[[Azure Runbook Automation]]'
- '[[Backdooring Git User Configurations]]'
- '[[Blind XSS Data Exfiltration]]'
- '[[Blind XSS Hunting with XSS Payloads]]'
- '[[Bypassing XSS Filters using UTF BOM Character]]'
- '[[Client Side Template Injection using Blind XSS]]'
- '[[Cross Site Scripting Alert Bypass using Alternate Function]]'
- '[[Cross Site Scripting - Alert Parent Location Filter Bypass]]'
- '[[Cross Site Scripting - Bypassing cookie blacklist with window.cookieStore.get()
  method]]'
- '[[Cross Site Scripting - Javascript Keylogger]]'
- '[[Cross Site Scripting - Single Quote Bypass on MouseDown Event Handler]]'
- '[[Cross Site Scripting (XSS) using Burp Collaborator to Steal Cookies]]'
- '[[CSP Bypass via Unsafe Inline Script Injection]]'
- '[[CSP Bypass via XSS Injection]]'
- '[[CSRF Attack with Bypassed Referer Header Validation]]'
- '[[CSRF Attack with Bypassed Referer Header Validation]]'
- '[[Custom DL and Execution via Malicious Macro Generator]]'
- '[[Custom Metadata PHP Injection]]'
- '[[DOCM Download and Execute via PowerShell]]'
- '[[DOM Based XSS Sink Detection]]'
- '[[Execute .NET Remote Execution with Beacon Post-Exploitation Job]]'
- '[[Exotic Payloads for Bypassing Dot Filters in XSS Attacks]]'
- '[[Exotic Payloads for Bypassing Word Blacklist and Code Evaluation]]'
- '[[Filter Bypass using UTF-7 Encoding for XSS Injection]]'
- '[[Flash-based Cross-site Scripting in SWF Files]]'
- '[[Freemarker Code Execution]]'
- '[[Git Hook Backdoor Persistence]]'
- '[[Gitlab/Github CI Command Execution]]'
- '[[HTML5 Tag Based Cross Site Scripting]]'
- '[[Identifying and Exploiting XSS Vulnerabilities]]'
- '[[Image Tragik Exploit]]'
- '[[Jinja2 Remote Code Execution via SSTI in Evil Config File]]'
- '[[JSON POST CSRF to Set Admin Role]]'
- '[[JSON POST CSRF to Set Admin Role]]'
- '[[LFI to RCE via FindFirstFile]]'
- '[[Linux - Text Hiding and Payload Creation]]'
- '[[Macro Delivery of Meterpreter Shellcode]]'
- '[[Malicious Macro-enabled Excel Documents with Macrome]]'
- '[[Metasploit Scripting with Meterpreter Reverse HTTPS Payload]]'
- '[[MSSQL Server Python Script Execution]]'
- '[[MSSQL Server R Command Execution]]'
- '[[Multi-Platform Reverse Shell Payload]]'
- '[[Mutated XSS with HTML Tag Recreation and DOMPurify Bypass]]'
- '[[Office VBA Wscript Execution]]'
- '[[Office Word Macro Payload Delivery with Metasploit]]'
- '[[Polyglot XSS Attack using SVG Image Injection]]'
- '[[Python Reverse Shell Cheat Sheet]]'
- '[[Reflection Method with WMF5 Autologging Bypass]]'
- '[[Ruby Reverse Shell Cheat Sheet]]'
- '[[Safe Script Tag Injection via Django Templates]]'
- '[[Server-Side Request Forgery (SSRF) Exploitation via PDF Files]]'
- '[[Server Side Template Injection - Mako - OS Information Gathering]]'
- '[[VBA-AMSI Bypass]]'
- '[[VBA Purging with OfficePurge command]]'
- '[[VBA Spawning via svchost.exe using Scheduled Task - Kaspersky AV Update Task]]'
- '[[WebDAV Batch File Execution via Cmd]]'
- '[[Windows - PowerShell Constrained Language Mode Check]]'
- '[[Windows Powershell Script Block Logging]]'
- '[[XLM Excel 4.0 - PowerShell Execution]]'
- '[[XSLT Injection with Remote Code Execution]]'
- '[[XSS in Files and Markdown]]'
- '[[XSS in Files with XML Payload Injection]]'
- '[[XSS Injection via JavaScript, Data URI and VBScript]]'
- '[[XSS in SVG Triangle with JavaScript Alert]]'
- '[[XSS Payload Injection]]'
- '[[XSS through PostMessage Button Click]]'
---

# Scripting

**MITRE ID**: T1064

## Description

Adversaries may use scripts to aid in operations and perform multiple actions that would otherwise be manual. Scripting is useful for speeding up operational tasks and reducing the time required to gain access to critical resources. Some scripting languages may be used to bypass process monitoring mechanisms by directly interacting with the operating system at an API level instead of calling other programs. Common scripting languages for Windows include VBScript and PowerShell but could also be in the form of command-line batch scripts.Scripts can be embedded inside Office documents as macros that can be set to execute when files used in Spearphishing Attachment and other types of spearphishing are opened. Malicious embedded macros are an alternative means of execution than software exploitation through Exploitation for Client Execution, where adversaries will rely on macros being allowed or that the user will accept to activate them.Many popular offensive frameworks exist which use forms of scripting for security testers and adversaries alike. [1] [1],  [2] [2], and PowerSploit [3] are three examples that are popular among penetration testers for exploit and post-compromise operations and include many features for evading defenses. Some adversaries are known to use PowerShell. [4]

# Detection

Scripting may be common on admin, developer, or power user systems, depending on job function. If scripting is restricted for normal users, then any attempts to enable scripts running on a system would be considered suspicious. If scripts are not commonly used on a system, but enabled, scripts running out of cycle from patching or other administrator functions are suspicious. Scripts should be captured from the file system when possible to determine their actions and intent.

Scripts are likely to perform actions with various effects on a system that may generate events, depending on the types of monitoring used. Monitor processes and command-line arguments for script execution and subsequent behavior. Actions may be related to network and system information Discovery, Collection, or other scriptable post-compromise behaviors and could be used as indicators of detection leading back to the source script.

Analyze Office file attachments for potentially malicious macros. Execution of macros may create suspicious process trees depending on what the macro is designed to do. Office processes, such as winword.exe, spawning instances of cmd.exe, script application like wscript.exe or powershell.exe, or other suspicious processes may indicate malicious activity. [103]

# Mitigation

Turn off unused features or restrict access to scripting engines such as VBScript or scriptable administration frameworks such as PowerShell.

Configure Office security settings enable Protected View, to execute within a sandbox environment, and to block macros through Group Policy. [101] Other types of virtualization and application microsegmentation may also mitigate the impact of compromise. The risks of additional exploits and weaknesses in implementation may still exist. [102]

# Footnotes

[1] Metasploit. (n.d.). Retrieved December 4, 2014.

[2] Veil Framework. (n.d.). Retrieved December 4, 2014.

[3] PowerSploit. (n.d.). Retrieved December 4, 2014.

[4] Alperovitch, D. (2014, July 7). Deep in Thought: Chinese Targeting of National Security Think Tanks. Retrieved November 12, 2014.

[5] Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.

[6] Ahl, I. (2017, June 06). Privileges and Credentials: Phished at the Request of Counsel. Retrieved May 17, 2018.

[7] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[8] Mercer, W., et al. (2017, October 22). "Cyber Conflict" Decoy Document Used in Real Cyber Conflict. Retrieved November 2, 2018.

[9] Symantec Security Response. (2015, July 13). “Forkmeiamfamous”: Seaduke, latest weapon in the Duke armory. Retrieved July 22, 2015.

[10] Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved October 4, 2016.

[11] Moran, N., et al. (2014, November 21). Operation Double Tap. Retrieved January 14, 2016.

[12] Dahan, A. (2017, May 24). OPERATION COBALT KITTY: A LARGE-SCALE APT IN ASIA CARRIED OUT BY THE OCEANLOTUS GROUP. Retrieved November 5, 2018.

[13] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[14] Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.

[15] Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.

[16] Doaty, J., Garrett, P.. (2018, September 10). We’re Seeing a Resurgence of the Demonic Astaroth WMIC Trojan. Retrieved April 17, 2019.

[17] Hayashi, K., Ray, V. (2018, July 31). Bisonal Malware Used in Attacks Against Russia and South Korea. Retrieved August 7, 2018.

[18] Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.

[19] Lee, T., Hanzlik, D., Ahl, I. (2013, August 7). Breaking Down the China Chopper Web Shell - Part I. Retrieved March 27, 2015.

[20] Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.

[21] Positive Technologies. (2017, August 16). Cobalt Strikes Back: An Evolving Multinational Threat to Finance. Retrieved September 5, 2018.

[22] Matveeva, V. (2017, August 15). Secrets of Cobalt. Retrieved October 10, 2018.

[23] Gorelik, M. (2018, October 08). Cobalt Group 2.0. Retrieved November 5, 2018.

[24] Unit 42. (2018, October 25). New Techniques to Uncover and Attribute Financial actors Commodity Builders and Infrastructure Revealed. Retrieved December 11, 2018.

[25] Giagone, R., Bermejo, L., and Yarochkin, F. (2017, November 20). Cobalt Strikes Again: Spam Runs Use Macros and CVE-2017-8759 Exploit Against Russian Banks. Retrieved March 7, 2019.

[26] Cobalt Strike. (2017, December 8). Tactics, Techniques, and Procedures. Retrieved December 20, 2017.

[27] Thomas Reed. (2018, October 29). Mac cryptocurrency ticker app installs backdoors. Retrieved April 23, 2019.

[28] Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.

[29] Blaich, A., et al. (2018, January 18). Dark Caracal: Cyber-espionage at a Global Scale. Retrieved April 11, 2018.

[30] Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.

[31] Kaspersky Lab's Global Research & Analysis Team. (2015, August 10). Darkhotel's attacks in 2015. Retrieved November 2, 2018.

[32] Falcone, R. (2018, March 15). Sofacy Uses DealersChoice to Target European Government Agency. Retrieved June 4, 2018.

[33] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[34] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[35] Symantec. (2018, July 18). The Evolution of Emotet: From Banking Trojan to Threat Distributor. Retrieved March 25, 2019.

[36] Brumaghin, E.. (2019, January 15). Emotet re-emerges after the holidays. Retrieved March 25, 2019.

[37] Trend Micro. (2019, January 16). Exploring Emotet's Activities . Retrieved March 25, 2019.

[38] Özarslan, S. (2018, December 21). The Christmas Card you never wanted - A new wave of Emotet is back to wreak havoc. Retrieved March 25, 2019.

[39] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[40] Cherepanov, A., Lipovsky, R. (2018, October 11). New TeleBots backdoor: First evidence linking Industroyer to NotPetya. Retrieved November 27, 2018.

[41] Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved July 31, 2018.

[42] FireEye iSIGHT Intelligence. (2017, June 16). FIN10: Anatomy of a Cyber Extortion Operation. Retrieved June 25, 2017.

[43] Vengerik, B. et al.. (2014, December 5). Hacking the Street? FIN4 Likely Playing the Market. Retrieved December 17, 2018.

[44] Vengerik, B. & Dennesen, K.. (2014, December 5). Hacking the Street?  FIN4 Likely Playing the Market. Retrieved January 15, 2019.

[45] Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.

[46] FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved June 1, 2016.

[47] McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.

[48] Carr, N., et al. (2018, August 01). On the Hunt for FIN7: Pursuing an Enigmatic and Evasive Global Criminal Operation. Retrieved August 23, 2018.

[49] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[50] Symantec Security Response. (2018, October 10). Gallmaker: New Attack Group Eschews Malware to Live off the Land. Retrieved November 27, 2018.

[51] Kasza, A. and Reichel, D.. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.

[52] Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.

[53] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[54] Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.

[55] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[56] Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.

[57] Patrick Wardle. (2017, January 1). Mac Malware of 2016. Retrieved September 21, 2018.

[58] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[59] Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.

[60] Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.

[61] Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.

[62] Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.

[63] Accenture Security. (2018, April 23). Hogfish Redleaves Campaign. Retrieved July 2, 2018.

[64] Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.

[65] Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.

[66] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

[67] Villanueva, M., Co, M. (2018, June 14). Another Potential MuddyWater Campaign uses Powershell-based PRB-Backdoor. Retrieved July 3, 2018.

[68] Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.

[69] Symantec DeepSight Adversary Intelligence Team. (2018, December 10). Seedworm: Group Compromises Government Agencies, Oil & Gas, NGOs, Telecoms, and IT Firms. Retrieved December 14, 2018.

[70] ClearSky Cyber Security. (2018, November). MuddyWater Operations in Lebanon and Oman: Using an Israeli compromised domain for a two-stage campaign. Retrieved November 29, 2018.

[71] F-Secure Labs. (2016, July). NANHAISHU RATing the South China Sea. Retrieved July 6, 2018.

[72] Patel, K. (2018, March 02). The NanoCore RAT Has Resurfaced From the Sewers. Retrieved November 9, 2018.

[73] Mercer, W., Rascagneres, P. (2018, May 31). NavRAT Uses US-North Korea Summit As Decoy For Attacks In South Korea. Retrieved June 11, 2018.

[74] Sherstobitoff, R., Malhotra, A. (2018, October 18). ‘Operation Oceansalt’ Attacks South Korea, U.S., and Canada With Source Code From Chinese Hacker Group. Retrieved November 30, 2018.

[75] Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.

[76] Falcone, R. and Lee, B. (2017, July 27). OilRig Uses ISMDoor Variant; Possibly Linked to Greenbug Threat Group. Retrieved January 8, 2018.

[77] Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.

[78] Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.

[79] Falcone, R., Wilhoit, K.. (2018, November 16). Analyzing OilRig’s Ops Tempo from Testing to Weaponization to Delivery. Retrieved April 23, 2019.

[80] Falcone, R., et al. (2018, September 04). OilRig Targets a Middle Eastern Government and Adds Evasion Techniques to OopsIE. Retrieved September 24, 2018.

[81] Horejsi, J. (2018, April 04). New MacOS Backdoor Linked to OceanLotus Found. Retrieved November 13, 2018.

[82] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[83] Meltzer, M, et al. (2018, June 07). Patchwork APT Group Targets US Think Tanks. Retrieved July 16, 2018.

[84] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[85] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[86] Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.

[87] Klijnsma, Y. (2018, January 23). Espionage Campaign Leverages Spear Phishing, RATs Against Turkish Defense Contractors. Retrieved November 6, 2018.

[88] Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.

[89] Lee, B., Falcone, R. (2019, January 18). DarkHydrus delivers new Trojan that can use Google Drive for C2 communications. Retrieved April 17, 2019.

[90] Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.

[91] Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.

[92]  Palotay, D. and Mackenzie, P. (2018, April). SamSam Ransomware Chooses Its Targets Carefully. Retrieved April 15, 2019.

[93] Hasherezade. (2016, September 12). Smoke Loader – downloader with a smokescreen still alive. Retrieved March 20, 2018.

[94] Check Point Research. (2019, February 4). SpeakUp: A New Undetected Backdoor Linux Trojan. Retrieved April 17, 2019.

[95] Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.

[96] Axel F. (2017, April 27). APT Targets Financial Analysts with CVE-2017-0199. Retrieved February 15, 2018.

[97] Llimos, N., Pascual, C.. (2019, February 12). Trickbot Adds Remote Application Credential-Grabbing Capabilities to Its Repertoire. Retrieved March 12, 2019.

[98] US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.

[99] Xiao, C. (2018, September 17). Xbash Combines Botnet, Ransomware, Coinmining in Worm that Targets Linux and Windows. Retrieved November 14, 2018.

[100] Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.

[101] Windows Defender Research. (2016, March 22). New feature in Office 2016 can block macros and help prevent infection. Retrieved April 11, 2018.

[102] Goodin, D. (2017, March 17). Virtual machine escape fetches $105,000 at Pwn2Own hacking contest - updated. Retrieved March 12, 2018.

[103] Felix. (2016, September). Analyzing Malicious Office Documents. Retrieved April 11, 2018.

## Defense

Turn off unused features or restrict access to scripting engines such as VBScript or scriptable administration frameworks such as PowerShell.

Configure Office security settings enable Protected View, to execute within a sandbox environment, and to block 

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (72)

- [[ActiveX-Based Autorun Macro with InkPicture Control and Painted Event]]
- [[Akamai WAF Bypass via Common XSS Injection Attack]]
- [[Akamai WAF Bypass via Prompt User Input]]
- [[ASR Bypass Create Child Process Rule 5 and Open PowerShell from Command Prompt]]
- [[AWS Userdata Retrieval via Instance Metadata Service]]
- [[Azure Automation Account Runbook Persistence]]
- [[Azure Runbook Automation]]
- [[Backdooring Git User Configurations]]
- [[Blind XSS Data Exfiltration]]
- [[Blind XSS Hunting with XSS Payloads]]
- [[Bypassing XSS Filters using UTF BOM Character]]
- [[Client Side Template Injection using Blind XSS]]
- [[Cross Site Scripting Alert Bypass using Alternate Function]]
- [[Cross Site Scripting - Alert Parent Location Filter Bypass]]
- [[Cross Site Scripting - Bypassing cookie blacklist with window.cookieStore.get() method]]
- [[Cross Site Scripting - Javascript Keylogger]]
- [[Cross Site Scripting - Single Quote Bypass on MouseDown Event Handler]]
- [[Cross Site Scripting (XSS) using Burp Collaborator to Steal Cookies]]
- [[CSP Bypass via Unsafe Inline Script Injection]]
- [[CSP Bypass via XSS Injection]]

*...and 52 more*
