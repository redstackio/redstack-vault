---
id: bf80551e-0e6b-4a03-b97d-c1dab559de0b
name: One-Way Communication
type: sub-technique
mitre_id: T1102.003
mitre_url: null
created_at: '2023-04-06T00:31:26.619962+00:00'
updated_at: '2023-04-06T00:31:26.619962+00:00'
parent_technique: '[[Web Service|T1102 - Web Service]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# One-Way Communication

**MITRE ID**: T1102.003

**Parent Technique**: [[Web Service|T1102 - Web Service]]

This is a sub-technique of T1102 - Web Service.

## Summary

Adversaries may use an existing, legitimate external Web service as a means for sending commands to a compromised system without receiving return output over the Web service channel. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Tho

## Description

Adversaries may use an existing, legitimate external Web service as a means for sending commands to a compromised system without receiving return output over the Web service channel. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those infected systems may opt to send the output from those commands back over a different C2 channel, including to another distinct Web service. Alternatively, compromised systems may return no output at all in cases where adversaries want to send instructions to systems and do not want a response.

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
