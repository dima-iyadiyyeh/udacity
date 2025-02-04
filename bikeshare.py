import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ["January", "February", "March", "April", "May", "June", "all"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "all"]

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
    while True:
        city = input(f"Enter the name of the city from the following list:\n{', '.join(CITY_DATA.keys())}\n> ").lower().strip()
        if city in CITY_DATA:
            print(f"You selected: {city.title()}")
            break
        else:
            print("Invalid city name, please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(f"Please choose a month from the following list:\n{', '.join(MONTHS)}\n> ").strip().capitalize()
        if month in MONTHS:
            break
        else:
            print("Invalid month name, please try again.")
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(f"Please choose a day of the week from the following list:\n{', '.join(DAYS)}\n> ").strip().capitalize()
        if day in DAYS:
            break
        else:
            print("Invalid day name, please try again.")

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
    #To Do: Load data
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != "all":
        month_index = MONTHS.index(month)  # Get month index
        df = df[df['Start Time'].dt.month == month_index]

    if day != "all":
        df = df[df['Start Time'].dt.day_name() == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_common_month = df['Start Time'].dt.month.mode()[0]
    print(f"Most common month: {MONTHS[most_common_month - 1]}")

   # TO DO: display the most common day of week
    most_common_day = df['Start Time'].dt.day_name().mode()[0]
    print(f"Most common day of the week: {most_common_day}")

   # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {most_common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: {most_common_start_station}")

   # TO DO: display most commonly used end station

    most_common_end_station = df['End Station'].mode()[0]
    print(f"Most commonly used end station: {most_common_end_station}")

   # TO DO: display most frequent combination of start station and end station trip

    most_common_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print(f"Most frequent trip: {most_common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Counts of user types:\n{user_types}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f"Counts of gender:\n{gender_counts}")
    else:
        print("Gender data not available.")

     # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"Earliest year of birth: {earliest_birth_year}")
        print(f"Most recent year of birth: {most_recent_birth_year}")
        print(f"Most common year of birth: {most_common_birth_year}")
    else:
        print("Birth year data not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    def display_raw_data(df):
    row_index = 0  
    while True:
        raw_data_request = input("\nWould you like to see 5 lines of raw data? Enter yes or no.\n").lower().strip()
        
        if raw_data_request == 'yes':
            print(df.iloc[row_index:row_index + 5]) 
            row_index += 5  
            if row_index >= len(df):
                print("\nNo more raw data to display.")
                break
        elif raw_data_request == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if _name_ == "_main_":
    main()