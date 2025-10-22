---
id: 0d8e924b-2baf-4174-9337-f9bca16c1708
name: Source
type: technique
mitre_id: T1153
mitre_url: null
created_at: '2019-08-28T21:17:32.483930+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Reflected XSS Attack Prevention]]'
---

# Source

**MITRE ID**: T1153

## Description

The source command loads functions into the current shell or executes files in the current context. This built-in command can be run in two different ways source /path/to/filename [arguments] or . /path/to/filename [arguments]. Take note of the space after the ".". Without a space, a new shell is created that runs the program instead of running the program within the current context. This is often used to make certain features or functions available to a shell or to update a specific shell's environment. Adversaries can abuse this functionality to execute programs. The file executed with this technique does not need to be marked executable beforehand.

# Detection

Monitor for command shell execution of source and subsequent processes that are started as a result of being executed by a source command. Adversaries must also drop a file to disk in order to execute it with source, and these files can also detected by file monitoring.

# Mitigation

Due to potential legitimate uses of source commands, it's may be difficult to mitigate use of this technique.

# Footnotes

## Defense

Due to potential legitimate uses of source commands, it's may be difficult to mitigate use of this technique.

## Tactics

- [[Execution|TA0002 - Execution]]

## Related Procedures (1)

- [[Reflected XSS Attack Prevention]]
