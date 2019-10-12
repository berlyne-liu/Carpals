SELECT TestA.day,TestA.Area,"" as "GSM流量",FDD_Traffic_GB as "FDD流量",TDD_Traffic_GB as "TDD流量",FDD_Traffic_GB+TDD_Traffic_GB as "LTE流量","" as "GSM话务",FDD_VoiceTraffic_Erl as "FDD话务",TDD_VoiceTraffic_Erl as "TDD话务",FDD_VoiceTraffic_Erl+TDD_VoiceTraffic_Erl as "LTE话务",NBTraffic as "NB流量",
CASE 
WHEN TestA.Area="清远" THEN 1
WHEN TestA.Area="清新" THEN 2
WHEN TestA.Area="佛冈" THEN 3
WHEN TestA.Area="英德" THEN 4
WHEN TestA.Area="连州" THEN 5
WHEN TestA.Area="阳山" THEN 6
WHEN TestA.Area="连南" THEN 7
WHEN TestA.Area="连山" THEN 8
WHEN TestA.Area="合计" THEN 9
ELSE "无"
END AS "顺序"
FROM
(SELECT TMPA.day,TMPA.Area,TDD_Traffic_GB,TDD_VoiceTraffic_Erl,FDD_Traffic_GB,FDD_VoiceTraffic_Erl
FROM 
(
SELECT day,Area,sum(DataTraffic) AS "TDD_Traffic_GB",sum(VoiceTraffic) as "TDD_VoiceTraffic_Erl" FROM
(
SELECT day,
CASE
WHEN substr(site,3,2)="QY" THEN "清远"
WHEN substr(site,3,2)="QX" THEN "清新"
WHEN substr(site,3,2)="FG" THEN "佛冈"
WHEN substr(site,3,2)="YD" THEN "英德"
WHEN substr(site,3,2)="YS" THEN "阳山"
WHEN substr(site,3,2)="LS" THEN "连山"
WHEN substr(site,3,2)="LN" THEN "连南"
WHEN substr(site,3,2)="LZ" THEN "连州"
WHEN substr(site,3,2)="GQ" THEN "清远"
END as "Area", 
case  
WHEN substr(site,-3,3) in ("ELH","ELW","ELR")THEN "TDD"																										 
WHEN substr(site,-3,3) in ("EFH","EFW","EFR") THEN "FDD"
ELSE "TDD"
END AS "Type",
"空口总业务量GB" AS "DataTraffic",
"VoLTE语音话务量（Erl）" as "VoiceTraffic"
FROM "LTE_Traffic"
) as A
where Type="TDD"
GROUP BY day,Area
)TMPA
LEFT JOIN
(
SELECT day,Area,sum(DataTraffic) AS "FDD_Traffic_GB",sum(VoiceTraffic) as "FDD_VoiceTraffic_Erl" FROM
(
SELECT day,
CASE
WHEN substr(site,3,2)="QY" THEN "清远"
WHEN substr(site,3,2)="QX" THEN "清新"
WHEN substr(site,3,2)="FG" THEN "佛冈"
WHEN substr(site,3,2)="YD" THEN "英德"
WHEN substr(site,3,2)="YS" THEN "阳山"
WHEN substr(site,3,2)="LS" THEN "连山"
WHEN substr(site,3,2)="LN" THEN "连南"
WHEN substr(site,3,2)="LZ" THEN "连州"
WHEN substr(site,3,2)="GQ" THEN "清远"
END as "Area",
case  
WHEN substr(site,-3,3) in ("ELH","ELW","ELR")THEN "TDD"																										 
WHEN substr(site,-3,3) in ("EFH","EFW","EFR") THEN "FDD"
ELSE "TDD"
END AS "Type",
"空口总业务量GB" AS "DataTraffic",
"VoLTE语音话务量（Erl）" as "VoiceTraffic"
FROM "LTE_Traffic"
) as B
where Type="FDD"
GROUP BY day,Area
)TMPB
ON TMPB.day=TMPA.day and TMPB.Area=TMPA.Area

UNION

SELECT TMPC.day,"合计" as "AREA",TDD_Traffic_GB,TDD_VoiceTraffic_Erl,FDD_Traffic_GB,FDD_VoiceTraffic_Erl
FROM 
(
SELECT day,sum(DataTraffic) AS "TDD_Traffic_GB",sum(VoiceTraffic) as "TDD_VoiceTraffic_Erl" FROM
(
SELECT day, 
case  
WHEN substr(site,-3,3) in ("ELH","ELW","ELR")THEN "TDD"																										 
WHEN substr(site,-3,3) in ("EFH","EFW","EFR") THEN "FDD"
ELSE "TDD"
END AS "Type",
"空口总业务量GB" AS "DataTraffic",
"VoLTE语音话务量（Erl）" as "VoiceTraffic"
FROM "LTE_Traffic"
) as C
where Type="TDD"
GROUP BY day
)TMPC
LEFT JOIN
(
SELECT day,sum(DataTraffic) AS "FDD_Traffic_GB",sum(VoiceTraffic) as "FDD_VoiceTraffic_Erl" FROM
(
SELECT day, 
case  
WHEN substr(site,-3,3) in ("ELH","ELW","ELR")THEN "TDD"																										 
WHEN substr(site,-3,3) in ("EFH","EFW","EFR") THEN "FDD"
ELSE "TDD"
END AS "Type",
"空口总业务量GB" AS "DataTraffic",
"VoLTE语音话务量（Erl）" as "VoiceTraffic"
FROM "LTE_Traffic"
) as D
where Type="FDD"
GROUP BY day
)TMPD
ON TMPC.day=TMPD.day
) TestA
LEFT JOIN
(
SELECT day,Area,NBTraffic
FROM 
(
SELECT TmpA.day,TmpA.Area,sum(NBTraffic) as NBTraffic from
(
SELECT day,site,location,
CASE
WHEN substr(site,3,2)="QY" THEN "清远"
WHEN substr(site,3,2)="QX" THEN "清新"
WHEN substr(site,3,2)="FG" THEN "佛冈"
WHEN substr(site,3,2)="YD" THEN "英德"
WHEN substr(site,3,2)="YS" THEN "阳山"
WHEN substr(site,3,2)="LS" THEN "连山"
WHEN substr(site,3,2)="LN" THEN "连南"
WHEN substr(site,3,2)="LZ" THEN "连州"
WHEN substr(site,3,2)="GQ" THEN "清远"
END as "Area", 
"NB上行流量(KB)"+"NB下行流量(KB)" AS "NBTraffic"
FROM "NB_Traffic"
) as TmpA
GROUP BY day,Area

union

SELECT TmpB.day,TmpB.Area,sum(NBTraffic) as NBTraffic from
(
SELECT day,site,location,"合计" as "Area",
"NB上行流量(KB)"+"NB下行流量(KB)" AS "NBTraffic"
FROM "NB_Traffic"
) as TmpB
GROUP BY day,Area
) as TmpC
) TestB
ON TestB.day=TestA.day and TestB.Area=TestA.Area