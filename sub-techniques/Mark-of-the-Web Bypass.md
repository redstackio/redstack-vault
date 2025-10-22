---
id: 2ffde1d5-a05c-43c2-a8e9-16a4f3cff968
name: Mark-of-the-Web Bypass
type: sub-technique
mitre_id: T1553.005
mitre_url: null
created_at: '2023-04-06T00:31:26.452248+00:00'
updated_at: '2023-04-06T00:31:26.452248+00:00'
parent_technique: '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Mark-of-the-Web Bypass

**MITRE ID**: T1553.005

**Parent Technique**: [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

This is a sub-technique of T1553 - Subvert Trust Controls.

## Summary

Adversaries may abuse specific file formats to subvert Mark-of-the-Web (MOTW) controls. In Windows, when files are downloaded from the Internet, they are tagged with a hidden NTFS Alternate Data Stream (ADS) named <code>Zone.Identifier</code> with a specific value known as the MOTW.(Citation: Micros

## Description

Adversaries may abuse specific file formats to subvert Mark-of-the-Web (MOTW) controls. In Windows, when files are downloaded from the Internet, they are tagged with a hidden NTFS Alternate Data Stream (ADS) named <code>Zone.Identifier</code> with a specific value known as the MOTW.(Citation: Microsoft Zone.Identifier 2020) Files that are tagged with MOTW are protected and cannot perform certain actions. For example, starting in MS Office 10, if a MS Office file has the MOTW, it will open in Protected View. Executables tagged with the MOTW will be processed by Windows Defender SmartScreen that compares files with an allowlist of well-known executables. If the file in not known/trusted, SmartScreen will prevent the execution and warn the user not to run it.(Citation: Beek Use of VHD Dec 2020)(Citation: Outflank MotW 2020)(Citation: Intezer Russian APT Dec 2020)

Adversaries may abuse container files such as compressed/archive (.arj, .gzip) and/or disk image (.iso, .vhd) file formats to deliver malicious payloads that may not be tagged with MOTW. Container files downloaded from the Internet will be marked with MOTW but the files within may not inherit the MOTW after the container files are extracted and/or mounted. MOTW is a NTFS feature and many container files do not support NTFS alternative data streams. After a container file is extracted and/or mounted, the files contained within them may be treated as local files on disk and run without protections.(Citation: Beek Use of VHD Dec 2020)(Citation: Outflank MotW 2020)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
