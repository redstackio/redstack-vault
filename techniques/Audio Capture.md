---
id: 36e2a495-9127-4696-bcb5-e3dfaafab2a9
name: Audio Capture
type: technique
mitre_id: T1123
mitre_url: null
created_at: '2019-08-28T21:17:25.134602+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Audio Capture

**MITRE ID**: T1123

## Description

An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

# Detection

Detection of this technique may be difficult due to the various APIs that may be used. Telemetry data regarding API use may not be useful depending on how a system is normally used, but may provide context to other potentially malicious activity occurring on a system.

Behavior that could indicate technique use include an unknown or unusual process accessing APIs associated with devices or software that interact with the microphone, recording devices, or recording software, and a process periodically writing files to disk that contain audio data.

# Mitigation

Mitigating this technique specifically may be difficult as it requires fine-grained API control. Efforts should be focused on preventing unwanted or unknown code from executing on a system.

Identify and block potentially malicious software that may be used to record audio by using whitelisting [25] tools, like AppLocker, [26] [27] or Software Restriction Policies [28] where appropriate. [29]

# Footnotes

[1] FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved March 1, 2018.

[2] Galperin, E., Et al.. (2016, August). I Got a Letter From the Government the Other Day.... Retrieved April 25, 2018.

[3] Yadav, A., et al. (2017, August 31). Cobian RAT – A backdoored RAT. Retrieved November 13, 2018.

[4] TrendMicro. (2014, September 03). DARKCOMET. Retrieved November 6, 2018.

[5] Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.

[6] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[7] Grunzweig, J. (2018, October 01). NOKKI Almost Ties the Knot with DOGCALL: Reaper Group Uses New Malware to Deploy RAT. Retrieved November 5, 2018.

[8] PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.

[9] Gostev, A. (2012, May 28). The Flame: Questions and Answers. Retrieved March 1, 2017.

[10] Gostev, A. (2012, May 30). Flame: Bunny, Frog, Munch and BeetleJuice…. Retrieved March 1, 2017.

[11] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[12] Brod. (2013, July 15). Signed Mac Malware Using Right-to-Left Override Trick. Retrieved July 17, 2017.

[13] Thomas. (2013, July 15). New signed malware called Janicab. Retrieved July 17, 2017.

[14] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[15] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[16] Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.

[17] The DigiTrust Group. (2017, January 01). NanoCore Is Not Your Average RAT. Retrieved November 9, 2018.

[18] Kasza, A., Halfpop, T. (2016, February 09). NanoCoreRAT Behind an Increase in Tax-Themed Phishing E-mails. Retrieved November 9, 2018.

[19] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[20] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[21] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[22] Bacurio, F., Salvio, J. (2017, February 14). REMCOS: A New RAT In The Wild. Retrieved November 6, 2018.

[23] Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.

[24] Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.

[25] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[26] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[27] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[28] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[29] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Mitigating this technique specifically may be difficult as it requires fine-grained API control. Efforts should be focused on preventing unwanted or unknown code from executing on a system.

Identify and block potentially malicious software that may be us

## Tactics

- [[Collection|TA0009 - Collection]]
