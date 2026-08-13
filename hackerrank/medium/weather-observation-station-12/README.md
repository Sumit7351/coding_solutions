# Weather Observation Station 11

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Query the list of *CITY* names from **STATION** that *do not start* with vowels and *do not end* with vowels. Your result cannot contain duplicates.


**Input Format**

The **STATION** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" title="Station.jpg" />

where *LAT\_N* is the northern latitude and *LONG\_W* is the western longitude. 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T10:53:21.074Z  

```sql
/*
Enter your query here.
*/SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^AEIOU]'
    OR CITY REGEXP '[^AEIOU]$';

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-12/problem)