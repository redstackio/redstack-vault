---
id: 651b5cc7-6d21-46f3-81bb-5dc8f722ae98
name: Plist File Modification
type: technique
mitre_id: T1647
mitre_url: null
created_at: '2023-04-06T00:31:26.423401+00:00'
updated_at: '2023-04-06T00:31:27.832342+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Plist File Modification

**MITRE ID**: T1647

## Description

Adversaries may modify property list files (plist files) to enable other malicious activity, while also potentially evading and bypassing system defenses. macOS applications use plist files, such as the <code>info.plist</code> file, to store properties and configuration settings that inform the operating system how to handle the application at runtime. Plist files are structured metadata in key-value pairs formatted in XML based on Apple's Core Foundation DTD. Plist files can be saved in text or binary format.(Citation: fileinfo plist file description) 

Adversaries can modify key-value pairs in plist files to influence system behaviors, such as hiding the execution of an application (i.e. [Hidden Window](https://attack.mitre.org/techniques/T1564/003)) or running additional commands for persistence (ex: [Launch Agent](https://attack.mitre.org/techniques/T1543/001)/[Launch Daemon](https://attack.mitre.org/techniques/T1543/004) or [Re-opened Applications](https://attack.mitre.org/techniques/T1547/007)).

For example, adversaries can add a malicious application path to the `~/Library/Preferences/com.apple.dock.plist` file, which controls apps that appear in the Dock. Adversaries can also modify the <code>LSUIElement</code> key in an application’s <code>info.plist</code> file  to run the app in the background. Adversaries can also insert key-value pairs to insert environment variables, such as <code>LSEnvironment</code>, to enable persistence via [Dynamic Linker Hijacking](https://attack.mitre.org/techniques/T1574/006).(Citation: wardle chp2 persistence)(Citation: eset_osx_flashback)

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
