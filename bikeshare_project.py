#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.xlsx',
              'new york city': 'new_york_city.xlsx',
              'washington': 'washington.xlsx' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
cities = list(CITY_DATA.keys())

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("What city would you like to see data for: Chicago, New York City, or Washington? \n").lower()
            if city in cities:
                break
            else:
                print("\nInvalid choice. Please enter a city name from the list of cities provided.")

        except ValueError:
            print("\n That's not a valid entry. Please try again")
    
        except KeyboardInterrupt:
            print("\n Attempted input. However keyboard interruption detected")

      
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Which month would you like to see data for?\n(January, February, March, April, May, June, or All)? \n").lower()
            if month in months:
                break
            else:
                print("\nInvalid choice. Please enter a selection from the list below")
        except ValueError:
            print("\nThat's not a valid entry. Please try again")
    
        except KeyboardInterrupt:
            print("\nAttempted input. However keyboard interruption detected")       
        

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Which day? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?) \n").lower()
            if day in days:
                break
            else:
                print("\nInvalid choice. Please enter a selection from the list below")
        except ValueError:
            print("\nThat's not a valid entry. Please try again")
    
        except KeyboardInterrupt:
            print("\nAttempted input. However keyboard interruption detected")


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
    # TO DO: First we start by loading the data from the CSV file into a dataframe
    df = pd.read_excel(CITY_DATA[city])
    
    # Next we convert the Start Time Column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #TO DO: Then we filter according to the month and day requested by the user
    # We start by extracting month and day of the week from the Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # I also want to extract the hour from Start Time to create an hour column, as this would be useful later on
    df['hour'] = df['Start Time'].dt.hour
    
    # Now we can filter by month if that was what the user requested
    if month != 'all':
        # use the index of the months list we already created above in line 9, in order to get the corresponding integer
        month = months.index(month) + 1
        
        # we create the new dataframe after filtering by month
        df = df[df['month'] == month]
        
    # If the user requested for specific day in the month, then the code below will filter by day
    if day != 'all':
        # we create the new dataframe after filtering by day
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month is:", popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]    
    print("The most common day of the week is:", popular_day)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]      
    print("The most common start hour is: {}:00".format(popular_hour))
    #Alternatively, I could have also used: most_common_hour = df['hour'].value_counts().idxmax() for the most popular hour.    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is:", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip   
    start_and_end_combination = (df['Start Station'] +' to '+ df['End Station']).mode()[0]
    print("The most frequent combination of start station to end station trip is:", start_and_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print("The total traveling time spent by all users is:", total_trip_duration)


    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print("The mean travel time is:", mean_trip_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print("The counts for User Type is:\n", user_types_counts)


    if 'Gender' in df.columns and 'Birth Year' in df.columns:
        
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print("The counts for all Gender is:", gender_counts)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        popular_birth_year = df['Birth Year'].value_counts().idxmax()
        
    else:
        print("\nSorry, {} does not have a Gender or Birth Year column.".format(city.title()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """ 
    Ask users if they want to see the first 5 rows of data. 
    And then Displays raw data at user's request, based on input received
    
    """    
    
    print('\nChecking to see if you need raw data displayed...\n')
    start_time = time.time()
    
    options_list = ['yes', 'no']
    
    show_raw_data = input("Would you like to see 5 lines of raw data? Enter 'yes' or 'no'\n").lower()
    if show_raw_data in options_list and show_raw_data == 'yes':
        print(df.head())
        
    elif show_raw_data in options_list and show_raw_data == 'no':
        print("Goodbye.")
        return
    
    
    lines = 0
    
    while True:
        ask_input = input("\nWould you like to see 5 more rows of raw data? Enter 'yes' or 'no'\n").lower()
        if ask_input == 'yes':
            lines += 5
            print(df.iloc[lines:lines + 5,:])
        
        else:
            break
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Have a wonderful day, goodbye!")
            break


if __name__ == "__main__":
    main()

