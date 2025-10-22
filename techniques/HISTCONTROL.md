---
id: 74b56234-a649-4e76-b72e-3c6133ad9533
name: HISTCONTROL
type: technique
mitre_id: T1148
mitre_url: null
created_at: '2019-08-28T21:17:43.665544+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# HISTCONTROL

**MITRE ID**: T1148

## Description

The HISTCONTROL environment variable keeps track of what should be saved by the history command and eventually into the ~/.bash_history file when a user logs out. This setting can be configured to ignore commands that start with a space by simply setting it to "ignorespace". HISTCONTROL can also be set to ignore duplicate commands by setting it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples. This means that " ls" will not be saved, but "ls" would be saved by history. HISTCONTROL does not exist by default on macOS, but can be set by the user and will be respected. Adversaries can use this to operate without leaving traces by simply prepending a space to all of their terminal commands.

# Detection

Correlating a user session with a distinct lack of new commands in their .bash_history can be a clue to suspicious behavior. Additionally, users checking or changing their HISTCONTROL environment variable is also suspicious.

# Mitigation

Prevent users from changing the HISTCONTROL environment variable [1]. Also, make sure that the HISTCONTROL environment variable is set to "ignoredup" instead of "ignoreboth" or "ignorespace".

# Footnotes

[1] Mathew Branwell. (2012, March 21). Securing .bash_history file. Retrieved July 8, 2017.

## Defense

Prevent users from changing the <code>HISTCONTROL</code> environment variable (Citation: Securing bash history). Also, make sure that the <code>HISTCONTROL</code> environment variable is set to “ignoredup” instead of “ignoreboth” or “ignorespace”.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
