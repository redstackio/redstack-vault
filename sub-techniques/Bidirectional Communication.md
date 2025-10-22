---
id: d04fb65e-3599-4b5e-930b-c8e1d50b20c7
name: Bidirectional Communication
type: sub-technique
mitre_id: T1102.002
mitre_url: null
created_at: '2023-04-06T00:31:26.835987+00:00'
updated_at: '2023-04-06T00:31:26.835987+00:00'
parent_technique: '[[Web Service|T1102 - Web Service]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Bidirectional Communication

**MITRE ID**: T1102.002

**Parent Technique**: [[Web Service|T1102 - Web Service]]

This is a sub-technique of T1102 - Web Service.

## Summary

Adversaries may use an existing, legitimate external Web service as a means for sending commands to and receiving output from a compromised system over the Web service channel. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those inf

## Description

Adversaries may use an existing, legitimate external Web service as a means for sending commands to and receiving output from a compromised system over the Web service channel. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those infected systems can then send the output from those commands back over that Web service channel. The return traffic may occur in a variety of ways, depending on the Web service being utilized. For example, the return traffic may take the form of the compromised system posting a comment on a forum, issuing a pull request to development project, updating a document hosted on a Web service, or by sending a Tweet. 

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection. 

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
