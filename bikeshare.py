import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(" Would you like to see data for Chicago - New York City - Washington ?").lower()
    while city not in CITY_DATA.keys():
        print("Invalid Input - Please Insert a Valid City Name.")
        city = input("Would you like to see data for Chicago - New York City - Washington ?").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months_list = [ 'January', 'February', 'March', 'April', 'May', 'June', 'All']
    month = input(" Which month? - All, January, February, ... , June?").title()
    while month not in months_list:
        print("Invalid Input - Please Insert a Valid Month.")
        month = input(" Which month? - All, January, February, ... , June?").title()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
    day = input(" Which day? All - Monday, ... , Sunday?").title()
    while day not in days_list:
        print("Invaid Input - Please Insert a Valid day.")
        day = input(" Which day? All - Monday, ... , Sunday?").title()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city]) 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month    
    df['day'] = df['Start Time'].dt.day_name() 
    
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June' ]
        month = months.index(month)+1
        df = df[df["month"] == month] 
    
    if day != 'All':
         df = df[df["day"] == day.title()]  

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months_list = ['Januray', 'February' , 'March' , 'April', 'May' , 'June' ]
    most_common_month = df["month"].mode()[0]
    print(f"The most common month is {months_list[most_common_month-1]}.")
    
    # TO DO: display the most common day of week
    most_common_day = df["day"].mode()[0]
    print(f"The most common day is {most_common_day}.")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df["hour"].mode()[0]
    print(f"The most common hour is {most_common_hour}.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start_station = df["Start Station"].mode()[0]
    print(f"The most popular start station is {most_popular_start_station}.")

    # TO DO: display most commonly used end station
    most_popular_end_station = df["End Station"].mode()[0]
    print(f"The most popular end station is {most_popular_end_station}.")

    # TO DO: display most frequent combination of start station and end station trip
    trip_combination = df["Start Station"] + " to " + df["End Station"]
    most_popular_combination = trip_combination.mode()[0]
    print(f"The most frequent combination of Start and End stations is from {most_popular_combination}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df["Trip Duration"].sum()
    tot_travel_time_hr = tot_travel_time //3600
    tot_travel_time_min = tot_travel_time % 3600 // 60
    tot_travel_time_sec = tot_travel_time % 3600 % 60
    print("Total travel time is {} hours, {} minutes, and {} seconds.".format(tot_travel_time_hr,tot_travel_time_min,tot_travel_time_sec))
    
    # TO DO: display mean travel time
    avg_travel_time = df["Trip Duration"].mean()
    avg_travel_time_hr = avg_travel_time //3600
    avg_travel_time_min = avg_travel_time % 3600 // 60
    avg_travel_time_sec = avg_travel_time % 3600 % 60
    print("Average travel time is {} hours, {} minutes, and {} seconds.".format(avg_travel_time_hr,avg_travel_time_min,avg_travel_time_sec))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df["User Type"].value_counts())
    print("\n")
    # TO DO: Display counts of gender
    if city != 'washington':
        print(df["Gender"].value_counts())
        print("\n")
        
    # TO    DO: Display earliest, most recent, and most common year of birth 
        earliest_year = df["Birth Year"].min()
        print("The earliest year of birth is {}.".format(earliest_year))
        most_recent = df["Birth Year"].max()
        print("The most recent year of birth is {}.".format(most_recent))
        most_common = df["Birth Year"].mode()[0]
        print("The most common year of birth is {}.".format(most_common))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_loc = 0
        while (view_data == 'yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
