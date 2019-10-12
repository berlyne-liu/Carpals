select 
day,
sum("空口总业务量GB") as "总业务量GB" 
FROM LTE_Traffic 
GROUP BY day
ORDER BY day
