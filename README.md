Problem Statement:

1. Build a Python code to display messages according to the temperature received from an assumed IoT system.
2. Accept max and min limit temperature.
3. Generate random values for temperature at every 2 second interval.
4. Compare with the limits to display appropriate value.


Approach:

The program first takes three inputs from the user:
Maximum temperature
Minimum temperature
Total runtime of the program
A loop runs for runtime ÷ 2 iterations because each temperature reading is generated after 2 seconds.
In every iteration:
A random temperature value between the minimum and maximum limits is generated using random.randint().
The temperature reading is displayed on the screen.
Each generated value is added to a variable to compute the mean temperature.
The program pauses for 2 seconds between readings using time.sleep(2) to simulate periodic sensor data.
After all readings are completed, the program calculates and displays the experimental mean temperature.


Sample Output:

Enter maximum temperature in Celcius : 35
Enter minimum temperature in Celcius : 20
Enter runtime : 10

READING 0 : The temperature is : 28.0 C
READING 1 : The temperature is : 24.0 C
READING 2 : The temperature is : 31.0 C
READING 3 : The temperature is : 26.0 C
READING 4 : The temperature is : 29.0 C

Experimental value obtained : 27.6 C
