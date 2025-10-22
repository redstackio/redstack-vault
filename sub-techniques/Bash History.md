---
id: 32d5ba99-c750-41af-9bf4-aedd95e599fb
name: Bash History
type: sub-technique
mitre_id: T1552.003
mitre_url: null
created_at: '2023-04-06T00:31:26.487392+00:00'
updated_at: '2023-04-06T00:31:26.487392+00:00'
parent_technique: '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[AWS CLI Configuration]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
---

# Bash History

**MITRE ID**: T1552.003

**Parent Technique**: [[Unsecured Credentials|T1552 - Unsecured Credentials]]

This is a sub-technique of T1552 - Unsecured Credentials.

## Summary

Adversaries may search the bash command history on compromised systems for insecurely stored credentials. Bash keeps track of the commands users type on the command-line with the "history" utility. Once a user logs out, the history is flushed to the user’s <code>.bash_history</code> file. For each u

## Description

Adversaries may search the bash command history on compromised systems for insecurely stored credentials. Bash keeps track of the commands users type on the command-line with the "history" utility. Once a user logs out, the history is flushed to the user’s <code>.bash_history</code> file. For each user, this file resides at the same location: <code>~/.bash_history</code>. Typically, this file keeps track of the user’s last 500 commands. Users often type usernames and passwords on the command-line as parameters to programs, which then get saved to this file when they log out. Adversaries can abuse this by looking through the file for potential credentials. (Citation: External to DA, the OS X Way)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 4 procedures using this sub-technique:

- [[AWS CLI Configuration]]
- [[Twitter API Key Leak Exploitation]]
- [[Twitter API Key Leak Exploitation]]
- [[Twitter API Key Leak Exploitation]]
