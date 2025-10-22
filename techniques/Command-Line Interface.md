---
id: 31bdd15f-31e1-4b1c-a3aa-a56623e105cc
name: Command-Line Interface
type: technique
mitre_id: T1059
mitre_url: null
created_at: '2019-08-28T21:17:25.387326+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Abuse GPO with PowerView to Push Empire Stager]]'
- '[[Advanced XSS in Angular and AngularJS]]'
- '[[Akamai WAF Bypass via Prompt User Input]]'
- '[[Argument Injection - Find Files]]'
- '[[ASP Razor Server Side Template Injection with C# Command Execution]]'
- '[[Automatic Sanitization Bypass in Angular and AngularJS]]'
- '[[Azure VM RunCommand Execution]]'
- '[[Backgrounding Long Running Commands]]'
- '[[Bash TCP Reverse Shell Connection]]'
- '[[Basic Command Injection Exploitation]]'
- '[[Basic LFI Filter Bypass]]'
- '[[Basic LFI via UTF-8 encoding]]'
- '[[Basic LFI with Path Truncation]]'
- '[[Basic RFI with Double Encoding]]'
- '[[Bypassing XSS Filters using UTF BOM Character]]'
- '[[Cloudflare XSS Bypass via Common WAF and HTML Injection]]'
- '[[Command Execution via xp_cmdshell - MSSQL Server]]'
- '[[Command Injection - Chaining Commands]]'
- '[[Command Injection Filter Bypass with $() and variable expansion]]'
- '[[Command Injection Filter Bypass with Backslash and Slash]]'
- '[[Command Injection - Filter Bypass with Backslash Newline]]'
- '[[Command Injection Filter Bypass with PowerShell]]'
- '[[Command Injection - Reading /etc/passwd]]'
- '[[Command Injection - Time Based Data Exfiltration]]'
- '[[Command Injection via Curl Arguments]]'
- '[[Command Injection with $@]]'
- '[[Command Injection with $() Filter Bypass]]'
- '[[Command Injection with Double Quote Bypass]]'
- '[[Command Injection with Filter Bypass using Line Return]]'
- '[[Command Injection with Filter Bypass using Single Quote]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[C Reverse Shell]]'
- '[[Cross Site Scripting Alert Bypass using Alternate Function]]'
- '[[CSP Bypass via XSS Injection]]'
- '[[CSV Injection - Exploit]]'
- '[[CURL Argument Injection]]'
- '[[CVE-2021-44228 Log4Shell Remote Command Execution]]'
- '[[CVE-2021-44228 Log4Shell Remote Command Execution]]'
- '[[CVE-2021-44228 Log4Shell Remote Command Execution]]'
- '[[Dart Reverse PowerShell Shell]]'
- '[[ECMAScript6 Filter Bypass Script Injection]]'
- '[[Execution of xp_cmdshell on Linked Database]]'
- '[[Exotic Payloads for Bypassing Filters in JavaScript]]'
- '[[Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks]]'
- '[[FFmpeg HLS Playlist Injection]]'
- '[[Filter Bypass using UTF-7 Encoding for XSS Injection]]'
- '[[Gitlab/Github CI Command Execution]]'
- '[[Groovy Server Side Template Injection with Command Execution]]'
- '[[Hex-encoded Path Traversal]]'
- '[[Hidden Input XSS Attack]]'
- '[[HTML5 Tag Based Cross Site Scripting]]'
- '[[Java Reverse Shell]]'
- '[[Java Reverse Shell Thread]]'
- '[[Java RMI Server RCE using Metasploit]]'
- '[[Jinja2 Config Information Extraction]]'
- '[[Jinja2 Server Side Template Injection with os.popen().read()]]'
- '[[Jinja2 Server Side Template Injection with Remote Code Execution]]'
- '[[Jinja2 SSTI Remote Code Execution via subprocess.Popen]]'
- '[[Jinja2 SSTI with Popen Remote Code Execution]]'
- '[[Jinja2 Template Injection - Server Side Template Injection]]'
- '[[Jinjava Command Execution]]'
- '[[Lessjs Command Execution via Server Side Template Injection]]'
- '[[LFI/RFI using php://filter wrapper]]'
- '[[LFI to RCE via Apache and Nginx Log Files]]'
- '[[LFI to RCE via /proc/self/environ]]'
- '[[LFI to RCE via Upload Race]]'
- '[[Linux Bash Command Injection with Filter Bypass]]'
- '[[Linux Staged Reverse TCP Meterpreter Shell]]'
- '[[Log4Shell Exploitation via Docker]]'
- '[[Log4Shell Exploitation via Docker]]'
- '[[Log4Shell Exploitation via Docker]]'
- '[[Macro Delivery of Meterpreter Shellcode]]'
- '[[Mako Server Side Template Injection to Retrieve User ID]]'
- '[[Malicious Macro-enabled Excel Documents with Macrome]]'
- '[[Metasploit Reverse Shell Handler]]'
- '[[Metasploit Scripting with Meterpreter Reverse HTTPS Payload]]'
- '[[MSSQL CLR Assembly Command Execution]]'
- '[[MSSQL Command Execution via xp_cmdshell]]'
- '[[MSSQL OLE Automation Command Execution]]'
- '[[MSSQL Server Command Execution via xp_cmdshell with Invoke-SQLOSCmd]]'
- '[[MSSQL Server External Script Execution]]'
- '[[MultiBrowser RPO Attack and XSS Injection Prevention]]'
- '[[MYSQL Injection - Write Shell using Outfile Method]]'
- '[[MYSQL Time-Based Injection via Conditional Statements]]'
- '[[Netcat OpenBSD Bind Shell]]'
- '[[Netcat Reverse Shell Cheat Sheet]]'
- '[[Netcat Traditional Bind Shell]]'
- '[[NodeJS Reverse Shell Cheat Sheet]]'
- '[[Office Word Macro Payload Delivery with Metasploit]]'
- '[[Oracle Java Class OS Command Execution]]'
- '[[Perl Bind Shell]]'
- '[[PHP Filter LFI/RFI]]'
- '[[Polyglot Command Injection for DNS Data Exfiltration]]'
- '[[PostgreSQL Command Execution using libc.so.6]]'
- '[[PostgreSQL XML Data Exfiltration]]'
- '[[Python Reverse Shell Cheat Sheet]]'
- '[[Reflective Assembly Loading with Powershell]]'
---

# Command-Line Interface

**MITRE ID**: T1059

## Description

Command-line interfaces provide a way of interacting with computer systems and is a common feature across many types of operating system platforms. [1] One example command-line interface on Windows systems is cmd, which can be used to perform a number of tasks including execution of other software. Command-line interfaces can be interacted with locally or remotely via a remote desktop application, reverse shell session, etc. Commands that are executed run with the current permission level of the command-line interface process unless the command includes process invocation that changes permissions context for that execution (e.g. Scheduled Task).Adversaries may use command-line interfaces to interact with systems and execute other software during the course of an operation.

# Detection

Command-line interface activities can be captured through proper logging of process execution with command-line arguments. This information can be useful in gaining additional insight to adversaries' actions through how they use native processes or custom tools.

# Mitigation

Audit and/or block command-line interpreters by using whitelisting [148] tools, like AppLocker, [149] [150] or Software Restriction Policies [151] where appropriate. [152]

# Footnotes

[1] Wikipedia. (2016, June 26). Command-line interface. Retrieved June 27, 2016.

[2] Crowdstrike Global Intelligence Team. (2014, June 9). CrowdStrike Intelligence Report: Putter Panda. Retrieved January 22, 2016.

[3] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[4] FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.

[5] ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.

[6] Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.

[7] Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.

[8] Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved November 15, 2018.

[9] Shelmire, A. (2015, July 06). Evasive Maneuvers by the Wekby group with custom ROP-packing and DNS covert channels. Retrieved November 15, 2018.

[10] Lee, B., Falcone, R. (2018, June 06). Sofacy Group’s Parallel Attacks. Retrieved June 18, 2018.

[11] Moran, N., et al. (2014, November 21). Operation Double Tap. Retrieved January 14, 2016.

[12] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[13] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[14] FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved March 1, 2018.

[15] Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.

[16] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[17] Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.

[18] Trend Micro. (2018, November 20). Lazarus Continues Heists, Mounts Attacks on Financial Organizations in Latin America. Retrieved December 3, 2018.

[19] FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved May 1, 2015.

[20] Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.

[21] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[22] Galperin, E., Et al.. (2016, August). I Got a Letter From the Government the Other Day.... Retrieved April 25, 2018.

[23] Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.

[24] US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.

[25] Mandiant. (n.d.). Appendix C (Digital) - The Malware Arsenal. Retrieved July 18, 2016.

[26] Hayashi, K., Ray, V. (2018, July 31). Bisonal Malware Used in Attacks Against Russia and South Korea. Retrieved August 7, 2018.

[27] FireEye Labs/FireEye Threat Intelligence. (2015, May 14). Hiding in Plain Sight: FireEye and Microsoft Expose Obfuscation Tactic. Retrieved January 22, 2016.

[28] Wilhoit, K. and Falcone, R. (2018, September 12). OilRig Uses Updated BONDUPDATER to Target Middle Eastern Government. Retrieved February 18, 2019.

[29] Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.

[30] Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.

[31] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[32] Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.

[33] Sebastian Feldmann. (2018, February 14). Chaos: a Stolen Backdoor Rising Again. Retrieved March 5, 2018.

[34] Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.

[35] Lee, T., Hanzlik, D., Ahl, I. (2013, August 7). Breaking Down the China Chopper Web Shell - Part I. Retrieved March 27, 2015.

[36] The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.

[37] Alperovitch, D.. (2016, June 15). Bears in the Midst: Intrusion into the Democratic National Committee. Retrieved August 3, 2016.

[38] Microsoft. (n.d.). Cmd. Retrieved April 18, 2016.

[39] Gorelik, M. (2018, October 08). Cobalt Group 2.0. Retrieved November 5, 2018.

[40] Cobalt Strike. (2017, December 8). Tactics, Techniques, and Procedures. Retrieved December 20, 2017.

[41] Yadav, A., et al. (2017, August 31). Cobian RAT – A backdoored RAT. Retrieved November 13, 2018.

[42] Thomas Reed. (2018, October 29). Mac cryptocurrency ticker app installs backdoors. Retrieved April 23, 2019.

[43] F-Secure Labs. (2015, April 22). CozyDuke: Malware Analysis. Retrieved December 10, 2015.

[44] Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.

[45] Chen, J. and Hsieh, M. (2017, November 7). REDBALDKNIGHT/BRONZE BUTLER’s Daserf Backdoor Now Using Steganography. Retrieved December 27, 2017.

[46] Dahan, A. (2017, May 24). OPERATION COBALT KITTY: A LARGE-SCALE APT IN ASIA CARRIED OUT BY THE OCEANLOTUS GROUP. Retrieved November 5, 2018.

[47] Fidelis Cybersecurity. (2016, February 29). The Turbo Campaign, Featuring Derusbi for 64-bit Linux. Retrieved March 2, 2016.

[48] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[49] ClearSky Cyber Security. (2017, December). Charming Kitten. Retrieved December 27, 2017.

[50] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[51] Falcone, R. and Miller-Osborn, J.. (2015, December 18). Attack on French Diplomat Linked to Operation Lotus Blossom. Retrieved February 15, 2016.

[52] Özarslan, S. (2018, December 21). The Christmas Card you never wanted - A new wave of Emotet is back to wreak havoc. Retrieved March 25, 2019.

[53] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[54] Cherepanov, A., Lipovsky, R. (2018, October 11). New TeleBots backdoor: First evidence linking Industroyer to NotPetya. Retrieved November 27, 2018.

[55] Somerville, L. and Toro, A. (2017, March 30). Playing Cat & Mouse: Introducing the Felismus Malware. Retrieved November 16, 2017.

[56] Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved July 31, 2018.

[57] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[58] Carr, N., et al. (2018, August 01). On the Hunt for FIN7: Pursuing an Enigmatic and Evasive Global Criminal Operation. Retrieved August 23, 2018.

[59] Bohannon, D. & Carr N. (2017, June 30). Obfuscation in the Wild: Targeted Attackers Lead the Way in Evasion Techniques. Retrieved February 12, 2018.

[60] FireEye Threat Intelligence. (2015, July 13). Demonstrating Hustle, Chinese APT Groups Quickly Use Zero-Day Vulnerability (CVE-2015-5119) Following Hacking Team Leak. Retrieved January 25, 2016.

[61] Pantazopoulos, N. (2018, April 17). Decoding network data from a Gh0st RAT variant. Retrieved November 2, 2018.

[62] Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.

[63] Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.

[64] Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.

[65] Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved September 26, 2016.

[66] US-CERT. (2018, February 05). Malware Analysis Report (MAR) - 10135536-F. Retrieved June 11, 2018.

[67] Carvey, H.. (2014, September 2). Where you AT?: Indicators of lateral movement using at.exe on Windows 7 systems. Retrieved January 25, 2016.

[68] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[69] Fidelis Cybersecurity. (2015, December 16). Fidelis Threat Advisory #1020: Dissecting the Malware Involved in the INOCNATION Campaign. Retrieved March 24, 2016.

[70] Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.

[71] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[72] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.

[73] ASERT Team. (2018, April 04). Innaput Actors Utilize Remote Access Trojan Since 2016, Presumably Targeting Victim Files. Retrieved July 9, 2018.

[74] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[75] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[76] Yadav, A., et al. (2016, January 29). Malicious Office files dropping Kasidet and Dridex. Retrieved March 24, 2016.

[77] Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.

[78] Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.

[79] Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.

[80] US-CERT. (2018, August 09). MAR-10135536-17 – North Korean Trojan: KEYMARBLE. Retrieved August 16, 2018.

[81] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[82] Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.

[83] Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.

[84] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[85] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved March 2, 2016.

[86] Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.

[87] US-CERT. (2018, March 09). Malware Analysis Report (MAR) - 10135536.11.WHITE. Retrieved June 13, 2018.

[88] Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.

[89] Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.

[90] ClearSky Cyber Security and Trend Micro. (2017, July). Operation Wilted Tulip: Exposing a cyber espionage apparatus. Retrieved August 21, 2017.

[91] PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.

[92] PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.

[93] Twi1ight. (2015, July 11). AD-Pentest-Script - wmiexec.vbs. Retrieved June 29, 2017.

[94] Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.

[95] Rosenberg, J. (2018, June 14). MirageFox: APT15 Resurfaces With New Tools Based On Old Ones. Retrieved September 21, 2018.

[96] Gross, J. (2016, February 23). Operation Dust Storm. Retrieved September 19, 2017.

[97] Stama, D.. (2015, February 6). Backdoor.Mivast. Retrieved February 15, 2016.

[98] Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.

[99] ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.

[100] Symantec DeepSight Adversary Intelligence Team. (2018, December 10). Seedworm: Group Compromises Government Agencies, Oil & Gas, NGOs, Telecoms, and IT Firms. Retrieved December 14, 2018.

[101] Kasza, A., Halfpop, T. (2016, February 09). NanoCoreRAT Behind an Increase in Tax-Themed Phishing E-mails. Retrieved November 9, 2018.

[102] Mercer, W., Rascagneres, P. (2018, May 31). NavRAT Uses US-North Korea Summit As Decoy For Attacks In South Korea. Retrieved June 11, 2018.

[103] Sherstobitoff, R., Malhotra, A. (2018, October 18). ‘Operation Oceansalt’ Attacks South Korea, U.S., and Canada With Source Code From Chinese Hacker Group. Retrieved November 30, 2018.

[104] Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.

[105] Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.

[106] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[107] Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.

[108] Falcone, R., et al. (2018, September 04). OilRig Targets a Middle Eastern Government and Adds Evasion Techniques to OopsIE. Retrieved September 24, 2018.

[109] Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.

[110] Horejsi, J. (2018, April 04). New MacOS Backdoor Linked to OceanLotus Found. Retrieved November 13, 2018.

[111] Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved August 3, 2016.

[112] Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved August 17, 2016.

[113] Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.

[114] Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.

[115] Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.

[116] Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.

[117] Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.

[118] Kasza, A. and Reichel, D.. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.

[119] Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.

[120] MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.

[121] Lei, C., et al. (2018, January 24). Lazarus Campaign Targeting Cryptocurrencies Reveals Remote Controller Tool, an Evolved RATANKBA, and More. Retrieved May 22, 2018.

[122] Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.

[123] FireEye iSIGHT Intelligence. (2017, April 6). APT10 (MenuPass Group): New Tools, Global Campaign Latest Manifestation of Longstanding Threat. Retrieved June 29, 2017.

[124] Bacurio, F., Salvio, J. (2017, February 14). REMCOS: A New RAT In The Wild. Retrieved November 6, 2018.

[125] Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.

[126] Falcone, R. (2018, January 25). OilRig uses RGDoor IIS Backdoor on Targets in the Middle East. Retrieved July 6, 2018.

[127] Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.

[128] Faou, M. and Boutin, J.. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.

[129] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, July 30). Sakula Malware Family. Retrieved January 26, 2016.

[130] Grunzweig, J.. (2015, July 14). Unit 42 Technical Analysis: Seaduke. Retrieved August 3, 2016.

[131] Symantec Security Response. (2017, November 7). Sowbug: Cyber espionage group targets South American and Southeast Asian governments. Retrieved November 16, 2017.

[132] Cylance SPEAR Team. (2017, February 9). Shell Crew Variants Continue to Fly Under Big AV’s Radar. Retrieved February 15, 2017.

[133] DiMaggio, J.. (2016, May 17). Indian organizations targeted in Suckfly attacks. Retrieved August 3, 2016.

[134] Miller, S., et al. (2017, March 7). FIN7 Spear Phishing Campaign Targets Personnel Involved in SEC Filings. Retrieved March 8, 2017.

[135] Brumaghin, E. and Grady, C.. (2017, March 2). Covert Channels and Poor Decisions: The Tale of DNSMessenger. Retrieved March 8, 2017.

[136] Dell SecureWorks Counter Threat Unit Special Operations Team. (2015, May 28). Living off the Land. Retrieved January 26, 2016.

[137] Cylance. (2014, December). Operation Cleaver. Retrieved September 14, 2017.

[138] O'Leary, J., et al. (2017, September 20). Insights into Iranian Cyber Espionage: APT33 Targets Aerospace and Energy Sectors and has Ties to Destructive Malware. Retrieved February 15, 2018.

[139] US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.

[140] Hayashi, K. (2017, November 28). UBoatRAT Navigates East Asia. Retrieved January 12, 2018.

[141] Fernando Mercês. (2016, September 5). Pokémon-themed Umbreon Linux Rootkit Hits x86, ARM Systems. Retrieved March 5, 2018.

[142] Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.

[143] US-CERT. (2017, November 22). Alert (TA17-318B): HIDDEN COBRA – North Korean Trojan: Volgmer. Retrieved December 7, 2017.

[144] US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.

[145] Zhou, R. (2012, May 15). Backdoor.Wiarp. Retrieved February 22, 2018.

[146] Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.

[147] McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.

[148] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[149] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[150] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[151] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[152] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Audit and/or block command-line interpreters by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Commands JPCERT) (Citation: NSA MS AppLocker) or Software Restriction Policies (Citation: Corio 2008) where appropriate. 

## Tactics

- [[Execution|TA0002 - Execution]]

## Related Procedures (100)

- [[Abuse GPO with PowerView to Push Empire Stager]]
- [[Advanced XSS in Angular and AngularJS]]
- [[Akamai WAF Bypass via Prompt User Input]]
- [[Argument Injection - Find Files]]
- [[ASP Razor Server Side Template Injection with C# Command Execution]]
- [[Automatic Sanitization Bypass in Angular and AngularJS]]
- [[Azure VM RunCommand Execution]]
- [[Backgrounding Long Running Commands]]
- [[Bash TCP Reverse Shell Connection]]
- [[Basic Command Injection Exploitation]]
- [[Basic LFI Filter Bypass]]
- [[Basic LFI via UTF-8 encoding]]
- [[Basic LFI with Path Truncation]]
- [[Basic RFI with Double Encoding]]
- [[Bypassing XSS Filters using UTF BOM Character]]
- [[Cloudflare XSS Bypass via Common WAF and HTML Injection]]
- [[Command Execution via xp_cmdshell - MSSQL Server]]
- [[Command Injection - Chaining Commands]]
- [[Command Injection Filter Bypass with $() and variable expansion]]
- [[Command Injection Filter Bypass with Backslash and Slash]]

*...and 80 more*
