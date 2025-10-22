---
id: cc52887d-3655-43e5-a8a8-d2188c0ff820
name: Plist Modification
type: sub-technique
mitre_id: T1547.011
mitre_url: null
created_at: '2023-04-06T00:31:26.267153+00:00'
updated_at: '2023-04-06T00:31:26.267153+00:00'
parent_technique: '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart
  Execution]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Plist Modification

**MITRE ID**: T1547.011

**Parent Technique**: [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]

This is a sub-technique of T1547 - Boot or Logon Autostart Execution.

## Summary

Adversaries can modify property list files (plist files) to execute their code as part of establishing persistence. Plist files are used by macOS applications to store properties and configuration settings for applications and services. Applications use information plist files, <code>Info.plist</cod

## Description

Adversaries can modify property list files (plist files) to execute their code as part of establishing persistence. Plist files are used by macOS applications to store properties and configuration settings for applications and services. Applications use information plist files, <code>Info.plist</code>, to tell the operating system how to handle the application at runtime using structured metadata in the form of keys and values. Plist files are formatted in XML and based on Apple's Core Foundation DTD and can be saved in text or binary format.(Citation: fileinfo plist file description) 

Adversaries can modify paths to executed binaries, add command line arguments, and insert key/pair values to plist files in auto-run locations which execute upon user logon or system startup. Through modifying plist files in these locations, adversaries can also execute a malicious dynamic library (dylib) by adding a dictionary containing the <code>DYLD_INSERT_LIBRARIES</code> key combined with a path to a malicious dylib under the <code>EnvironmentVariables</code> key in a plist file. Upon user logon, the plist is called for execution and the malicious dylib is executed within the process space. Persistence can also be achieved by modifying the <code>LSEnvironment</code> key in the application's <code>Info.plist</code> file.(Citation: wardle artofmalware volume1)

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
