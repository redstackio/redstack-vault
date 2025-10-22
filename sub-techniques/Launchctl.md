---
id: e154f8be-838d-4e9e-84fe-f413080795c3
name: Launchctl
type: sub-technique
mitre_id: T1569.001
mitre_url: null
created_at: '2023-04-06T00:31:26.480332+00:00'
updated_at: '2023-04-06T00:31:26.480332+00:00'
parent_technique: '[[System Services|T1569 - System Services]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
---

# Launchctl

**MITRE ID**: T1569.001

**Parent Technique**: [[System Services|T1569 - System Services]]

This is a sub-technique of T1569 - System Services.

## Summary

Adversaries may abuse launchctl to execute commands or programs. Launchctl interfaces with launchd, the service management framework for macOS. Launchctl supports taking subcommands on the command-line, interactively, or even redirected from standard input.(Citation: Launchctl Man)

Adversaries use 

## Description

Adversaries may abuse launchctl to execute commands or programs. Launchctl interfaces with launchd, the service management framework for macOS. Launchctl supports taking subcommands on the command-line, interactively, or even redirected from standard input.(Citation: Launchctl Man)

Adversaries use launchctl to execute commands and programs as [Launch Agent](https://attack.mitre.org/techniques/T1543/001)s or [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)s. Common subcommands include: <code>launchctl load</code>,<code>launchctl unload</code>, and <code>launchctl start</code>. Adversaries can use scripts or manually run the commands <code>launchctl load -w "%s/Library/LaunchAgents/%s"</code> or <code>/bin/launchctl load</code> to execute [Launch Agent](https://attack.mitre.org/techniques/T1543/001)s or [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)s.(Citation: Sofacy Komplex Trojan)(Citation: 20 macOS Common Tools and Techniques)

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]
