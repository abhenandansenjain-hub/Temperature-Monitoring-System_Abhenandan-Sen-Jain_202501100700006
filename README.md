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


