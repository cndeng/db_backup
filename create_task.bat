:: tn: 任务名
:: ru: 用户名
:: sc: 周期
:: st: start time
:: tr: 任务路径
schtasks /create /tn db_bak /ru system /sc daily /st 08:00:00 /tr "python db_manange.py --backup /sc"