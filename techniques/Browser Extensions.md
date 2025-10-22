---
id: 3ab88c3c-2e0e-4c66-bf45-18e5d4dd6fd6
name: Browser Extensions
type: technique
mitre_id: T1176
mitre_url: null
created_at: '2019-08-28T21:17:44.336957+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Browser Extensions

**MITRE ID**: T1176

## Description

Browser extensions or plugins are small programs that can add functionality and customize aspects of internet browsers. They can be installed directly or through a browser's app store. Extensions generally have access and permissions to everything that the browser can access. [1] [2]Malicious extensions can be installed into a browser through malicious app store downloads masquerading as legitimate extensions, through social engineering, or by an adversary that has already compromised a system. Security can be limited on browser app stores so may not be difficult for malicious extensions to defeat automated scanners and be uploaded. [3] Once the extension is installed, it can browse to websites in the background, [4] [5] steal all information that a user enters into a browser, to include credentials, [6] [7] and be used as an installer for a RAT for persistence. There have been instances of botnets using a persistent backdoor through malicious Chrome extensions. [8] There have also been similar examples of extensions being used for command & control  [9].

# Detection

Inventory and monitor browser extension installations that deviate from normal, expected, and benign extensions. Process and network monitoring can be used to detect browsers communicating with a C2 server. However, this may prove to be a difficult way of initially detecting a malicious extension depending on the nature and volume of the traffic it generates.

Monitor for any new items written to the Registry or PE files written to disk. That may correlate with browser extension installation.

# Mitigation

Only install browser extensions from trusted sources that can be verified. Ensure extensions that are installed are the intended ones as many malicious extensions will masquerade as legitimate ones.

Browser extensions for some browsers can be controlled through Group Policy. Set a browser extension white or black list as appropriate for your security policy. [11]

Change settings to prevent the browser from installing extensions without sufficient permissions.

Close out all browser sessions when finished using them.

# Footnotes

[1] Wikipedia. (2017, October 8). Browser Extension. Retrieved January 11, 2018.

[2] Chrome. (n.d.). What are Extensions?. Retrieved November 16, 2017.

[3] Jagpal, N., et al. (2015, August). Trends and Lessons from Three Years Fighting Malicious Extensions. Retrieved November 17, 2017.

[4] Brinkmann, M. (2017, September 19). First Chrome extension with JavaScript Crypto Miner detected. Retrieved November 16, 2017.

[5] De Tore, M., Warner, J. (2018, January 15). MALICIOUS CHROME EXTENSIONS ENABLE CRIMINALS TO IMPACT OVER HALF A MILLION USERS AND GLOBAL BUSINESSES. Retrieved January 17, 2018.

[6] Marinho, R. (n.d.). (Banker(GoogleChromeExtension)).targeting. Retrieved November 18, 2017.

[7] Marinho, R. (n.d.). "Catch-All" Google Chrome Malicious Extension Steals All Posted Data. Retrieved November 16, 2017.

[8] Vachon, F., Faou, M. (2017, July 20). Stantinko: A massive adware campaign operating covertly since 2012. Retrieved November 16, 2017.

[9] Kjaer, M. (2016, July 18). Malware in the browser: how you might get hacked by a Chrome extension. Retrieved November 22, 2017.

[10] ASERT team. (2018, December 5). STOLEN PENCIL Campaign Targets Academia. Retrieved February 5, 2019.

[11] Mohta, A. (n.d.). Block Chrome Extensions using Google Chrome Group Policy Settings. Retrieved January 10, 2018.

## Defense

Only install browser extensions from trusted sources that can be verified. Ensure extensions that are installed are the intended ones as many malicious extensions will masquerade as legitimate ones.

Browser extensions for some browsers can be controlled 

## Tactics

- [[Persistence|TA0003 - Persistence]]
