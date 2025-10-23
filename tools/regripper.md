---
id: 837d921c-c0de-41cb-9d85-bfd0d03f3470
name: regripper
type: tool
verified: false
created_at: '2019-08-28T21:17:39.481617+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# regripper

## Overview

RegRipper is an open source tool, written in Perl, for extracting/parsing information (keys, values, data) from the Registry and presenting it for analysis.RegRipper consists of two basic tools, both of which provide similar capability. The RegRipper GUI allows the analyst to select a hive to parse

## Description

RegRipper is an open source tool, written in Perl, for extracting/parsing information (keys, values, data) from the Registry and presenting it for analysis.RegRipper consists of two basic tools, both of which provide similar capability. The RegRipper GUI allows the analyst to select a hive to parse, an output file for the results, and a profile (list of plugins) to run against the hive. When the analyst launches the tool against the hive, the results go to the file that the analyst designated. If the analyst chooses to parse the System hive, they might also choose to send the results to system.txt. The GUI tool will also create a log of it’s activity in the same directory as the output file, using the same file name but using the .log extension (i.e., if the output is written to system.txt, the log will be written to system.log).RegRipper also includes a command line (CLI) tool called rip. Rip can be pointed against to a hive and can run either a profile (a list of plugins) or an individual plugin against that hive, with the results being sent to STDOUT. Rip can be included in batch files, using the redirection operators to send the output to a file. Rip does not write a log of it’s activity.RegRipper is similar to tools such as Nessus, in that the application itself is simply an engine that runs plugins. The plugins are individual Perl scripts that each perform a specific function. Plugins can locate specific keys, and list all subkeys, as well as values and data, or they can locate specific values. Plugins are extremely valuable in the sense that they can be written to parse data in a manner that is useful to individual analysts.Note: Plugins also serve as a means of retaining corporate knowledge, in that an analyst finds something, creates a plugin, and adds that plugin to a repository that other analysts can access. When the plugin is shared, this has the effect of being a force multiplier, in that all analysts know have access to the knowledge and experience of one analyst. In addition, plugins remain long after analysts leave an organization, allowing for retention of knowledge.






