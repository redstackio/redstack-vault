---
id: b1b3c1fc-6ea6-4ccf-8456-c849b4783741
name: Clear Command History
type: technique
mitre_id: T1146
mitre_url: null
created_at: '2019-08-28T21:17:23.626441+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Clear Command History

**MITRE ID**: T1146

## Description

macOS and Linux both keep track of the commands users type in their terminal so that users can easily remember what they've done. These logs can be accessed in a few different ways. While logged in, this command history is tracked in a file pointed to by the environment variable HISTFILE. When a user logs off a system, this information is flushed to a file in the user's home directory called ~/.bash_history. The benefit of this is that it allows users to go back to commands they've used before in different sessions. Since everything typed on the command-line is saved, passwords passed in on the command line are also saved. Adversaries can abuse this by searching these files for cleartext passwords. Additionally, adversaries can use a variety of methods to prevent their own commands from appear in these logs such as unset HISTFILE, export HISTFILESIZE=0, history -c, rm ~/.bash_history.

# Detection

User authentication, especially via remote terminal services like SSH, without new entries in that user's ~/.bash_history is suspicious. Additionally, the modification of the HISTFILE and HISTFILESIZE environment variables or the removal/clearing of the ~/.bash_history file are indicators of suspicious activity.

# Mitigation

Preventing users from deleting or writing to certain files can stop adversaries from maliciously altering their ~/.bash_history files. Additionally, making these environment variables readonly can make sure that the history is preserved   [1].

# Footnotes

[1] Mathew Branwell. (2012, March 21). Securing .bash_history file. Retrieved July 8, 2017.

## Defense

Preventing users from deleting or writing to certain files can stop adversaries from maliciously altering their <code>~/.bash_history</code> files. Additionally, making these environment variables readonly can make sure that the history is preserved   (Ci

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
