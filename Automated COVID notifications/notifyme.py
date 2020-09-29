from plyer import notification as n
import pandas as pd
import time

def notifyMe(title, msg):
    n.notify(
        title=title,
        message=msg,
        timeout = 10
    )

if __name__ == '__main__':
    
    data = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv', header=0, usecols=[0, 1,2,3,4,5])
    
    states=["Maharashtra", "Gujarat", "Rajasthan"]
    
    for index, row in data.iterrows():
        if row['State'] in states:
            title = f"COVID19 Case Updates for {row['State']}"
            msg = f"Active: {row['Active']}\nRecovered: {row['Recovered']}\nDeaths: {row['Deaths']}\nConfirmed: {row['Confirmed']}\n"
            notifyMe(title, msg)
            time.sleep(2)
