# Employee Salaries

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Query the total population of all cities in **CITY** where *District* is **California**. 

**Input Format**

The **CITY** table is described as follows:
<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" title="CITY.jpg" />

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T11:00:18.812Z  

```sql
/*
Enter your query here.
*/SELECT name FROM EMPLOYEE 
WHERE salary>2000 AND months<10
ORDER BY employee_id ASC;

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/revising-aggregations-sum/problem)