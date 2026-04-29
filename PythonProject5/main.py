import pandas as pd
import os

class Flight:
    def __init__(self, flight_num, delay_time):
        self.flight_num = flight_num
        self.delay_time = delay_time

    def check_severity(self):
        if 30 <= self.delay_time <= 60:
            print("Warning: Flight moderately delayed")
        elif self.delay_time > 60:
            print("Severe Warning: Flight severely delayed")


df = pd.read_csv("arrivals.csv")

df = df.fillna(0)

filtered_df = df[df["Minutes_Delayed"] > 30]

most_delayed = filtered_df.loc[filtered_df["Minutes_Delayed"].idxmax()]

flight_obj = Flight(most_delayed["Flight_Number"], most_delayed["Minutes_Delayed"])

flight_obj.check_severity()

new_data = pd.DataFrame([{
    "Flight_Number": most_delayed["Flight_Number"],
    "Airline": most_delayed["Airline"],
    "Minutes_Delayed": most_delayed["Minutes_Delayed"]
}])

if os.path.exists("severe_delays_log.csv"):
    existing_df = pd.read_csv("severe_delays_log.csv")
    final_df = pd.concat([existing_df, new_data], ignore_index=True)
else:
    final_df = new_data

final_df.to_csv("severe_delays_log.csv", index=False)

print("Severe delay logged successfully!")