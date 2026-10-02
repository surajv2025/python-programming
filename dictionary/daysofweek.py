def get_dayofweek(day_number):
    days_dict={
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return days_dict.get(day_number,"Invalid Input")#get() dictionary ke andar key search karta hai.

print(get_dayofweek(7))