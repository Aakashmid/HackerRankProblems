from datetime import datetime as dt
# Complete the time_delta function below.
def time_delta(t1, t2):
    time_format="%a %d %b %Y %H:%M:%S %z" #for Sun 10 May 2015 13:54:36 -0000
    dt1=dt.strptime(t1,time_format)
    dt2=dt.strptime(t2,time_format)
    return str(int((dt1-dt2).total_seconds()))