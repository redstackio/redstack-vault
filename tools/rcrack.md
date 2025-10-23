---
id: 1eb8d348-1442-493a-bfdb-eaa5f01966c7
name: rcrack
type: tool
verified: false
created_at: '2019-08-28T21:17:22.248652+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# rcrack

## Overview

RainbowCrack is a general propose implementation of Philippe Oechslin’s faster time-memory trade-off technique. It crack hashes with rainbow tables.RainbowCrack uses time-memory tradeoff algorithm to crack hashes. It differs from brute force hash crackers.A brute force hash cracker generate all pos

## Description

RainbowCrack is a general propose implementation of Philippe Oechslin’s faster time-memory trade-off technique. It crack hashes with rainbow tables.RainbowCrack uses time-memory tradeoff algorithm to crack hashes. It differs from brute force hash crackers.A brute force hash cracker generate all possible plaintexts and compute the corresponding hashes on the fly, then compare the hashes with the hash to be cracked. Once a match is found, the plaintext is found. If all possible plaintexts are tested and no match is found, the plaintext is not found. With this type of hash cracking, all intermediate computation results are discarded.A time-memory tradeoff hash cracker need a pre-computation stage, at the time all plaintext/hash pairs within the selected hash algorithm, charset, plaintext length are computed and results are stored in files called rainbow table. It is time consuming to do this kind of computation. But once the one time pre-computation is finished, hashes stored in the table can be cracked with much better performance than a brute force cracker.






