select Nodeid,GROUP_CONCAT(alarm," | ") as "alarmObject"
from
(select Nodeid,STRFTIME('%Y-%m-%d %H:%M:%S', "dateid","localtime")||"  "||c."全量告警"||"("||"Alarmobject"||")" as "alarm"
from
(select * from
(
select replace("Network Element","NetworkElement=","") AS "Nodeid",
substr("Event Time",-4,4)||"-"||
case 
when substr("Event Time",5,3)="Jan" then "01"
when substr("Event Time",5,3)="Feb" then "02"
when substr("Event Time",5,3)="Mar" then "03"
when substr("Event Time",5,3)="Apr" then "04"
when substr("Event Time",5,3)="May" then "05"
when substr("Event Time",5,3)="Jun" then "06"
when substr("Event Time",5,3)="Jul" then "07"
when substr("Event Time",5,3)="Aug" then "08"
when substr("Event Time",5,3)="Sep" then "09"
when substr("Event Time",5,3)="Oct" then "10"
when substr("Event Time",5,3)="Nov" then "11"
when substr("Event Time",5,3)="Dec" then "12"
END ||"-"||
substr("Event Time",-20,2)||
substr("Event Time",-8,-10) as "dateid",
"Specific Problem",
replace("Alarming Object","EUtranCellFDD=","") as "Alarmobject"
from Alarm_FDD_Cause
) as a
LEFT JOIN
(select "告警英文","全量告警" from Alarm_Standard) as b
on a."Specific Problem"=b."告警英文"
where b."告警英文" is not null
) as c
) as d
GROUP BY Nodeid