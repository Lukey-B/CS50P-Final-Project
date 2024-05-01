# Retirement Calculator
---

## General Overview of the Program

The purpose of this program is to serve as a retirement calculator.
It attempts to answer this question - how much do I need to save to for my retirement given my current age, savings, retirement income objective, Investment risk tolerance, and anticipated age at which I will retire?


## Validating and Gathering User Information

I created a RetirementCalculator() class as way to be able to easily store and access the attributes (eg. current_age, retirement_age, retirement_income, risk_tolerance, current_savings, years_to_retirement) which are the inputs required to perform the time value of money calculations needed to answer our question. I orginally had created a function that returned these values but quickly realized that to be able to access these values in other functionswould become cumbersome. By creating an instance of the class these values could be accessed easily anywhere in the class with the "self.attribute" functionailty of classes.

The main() function is where we define the assigment for the attributes of the class. However, before that assignement is made it must flow through the get_input() function which acts both as the call for user input and the data validation mechanism. The get_input function accepts 3 parameters. prompt, condition and error_message. The prompt asks the question for example - "how old are you? ", we then pass a condition that must be met by the user in order for the attribute to be assigned and if that condition is not met we have an error_message that will display. If the conditon is not met a value error is raised and a while loop is used to give the user 5 tries to enter a valid input before the program exits and prompts the user with "Too many wrong attempts".

The conditions for each attribute were passed to the get_input function using lambda which was a great feature to utilize as these conditions are specific to each attribute and do not need to be reused at any other point. Originally I had seperate while loops with condition and if statements used for data validation but it made the code long and reduntant. The implementation of the get_input function made the code much shorter and more logical.

The RetirementClass(), main(), and get_input functions work together to obtain, validate, and access the variables needed to perform our calculations.

## Crunching the numbers

Here we have three main functions that work together to complete the calculations required to answer the question. funds_required_in_retirement(self), funds_required_for_retirement(self), and ROR(risk_tolerance).


#### How much money do we need?
The first step is to find out - based of what the user said they would like to spend per month in retirement and when they want to retire, how much money is required? This calculation is relatively straight forward. First to make the calculation more simple the monthly amount is converted to an annual amount. In the next line our years in retirement is defined as 95 minus retirement age. It is standard practice to plan retirement till age 95. What must be done next is calculate the FV of an annuity due to determine the future value of the funds with the stated retirement income objective. We choose an annuity due in this case as we are making the assumption that we need the funds at the beggining of the year as opposed to the end as with a regular annuity. we then dicount this FV lump sum back to the age of retirement. In other words discounting the future value lump sum at age 95 back to say 65. The discount factor used is adjusted for inflation which is estimated at 3% as per historical norms and assumes a 4% rate of return during retirement which is a reasonable expected return when investing in less risky assets such as fixed income. The FV of the annuity due is also estimated at a 4% rate of return. In essence we are assuming that this person is going to reduce there risk while in retirement in favour of more stability in the value of there investments while still trying to keep up with or slighlty out pace inflation. Finally the function returns the amount required at the start of retirement to meet our monthly retirement income goal.

#### How much money should we be saving now?

The next step is to determine how much we need to be saving in order to have the funds required at the start of retirement as defined by funds_required_in_retirement function. The funds_required_for_retirement function completes this calculation. The first thing it does is define risk_tolerance in the function as the attribute we defined in the Retirement calculator class. We need this risk_tolerance variable as we will be using this to determine our expected rates of return. The next line of this function calculates the FV of any savings we might currently have invested. ROR(risk_tolerance) function is called in this calculation as this function returns the rate of return based off our risk tolerance.

for a "low" risk tolerance we are assuming a 4% rate of return, again typical of fixed income. "medium" returns 7% and "high" returns 9%. While it is true that a medium fund could return 9% or even higher and the returns of the high risk fund could be much higher than 9%, we want to be conservative in our estimates for planning and not rely too heavily on investment performance as it is never guaranteed. Of course these returns vary widely by investments. But using Mutual funds with asset allocations that fall into these risk profiles, these returns are reasonable and slightly conservative.

After determing the FV of current savings we define the future value of funds required by calling funds_required_in_retirement() and subtracting the FV of our current savings. Now we have the amount required at retirement factoring in our curent savings and there growth. Finally we are ready to calculate the monthly amount needed to be saved to reach the users goal. The rate of return is converted to a monthly rate of return and we use the formula - P = FV * (r / ((1 + r)^n - 1) to solve what monthly savings are required to meet the amount needed, based of our return and the number of months until retirement. We can call this amount our pre-authorized contribution or PAC for short. The funds_required_for_retirement function returns this amount as a float.

## Formatting the PAC and presenting it to the user

The last step is to return the actual amount to the user. in the main() function we create an instance of the class. Then create a "pac" variable. Calling the funds_required_for_retirement() and nested by the formatted_dollar() function. The ladder function takes the float, rounds it, then adds the dollar symbol and seperates amounts by the comma. For example 1000.50 becomes $1,000. The final statement prints to the user just as an example "You need to save $1000 per month to achieve your retirement objective".

## Testing project.py

the test file has 5 total functions. The first is test_ROR(). this just checks if the ROR() function is returning the appropriate values when low, meduim, or high risk_tolerance is passed as an argument. test_formatted_dollar is very similar in that it checks if we pass numbers to the formatted_dollar() function if it is correctly formatting those numbers. The following four test functions are all testing the get_input() but in different ways. Here because user input is required for this function as per input() we must mock this input in order to complete the test. We can use the patch method and "builtins.input" to return a value for the 1st parameter of the get_input() function. Using these features different inputs can now be tested to see how get_input() will respond. the first test_get_input() tests to see if a valid input returns that valid value. The others all pass Invalid inputs to one of our attributes (eg. questions we are asking) and checks to see if we have a system exit once we have exceeded the permitted number of attempts.


## Final comments and Program limitations

One major limitation in the program in terms of it's ability to provide an accurate savings amount for retirement is that taxes have not been factored into the calculation. Of course, taxes could make have a huge impact on the amount required for retirement and how much actually needs to be saved per month. It also does not have the abiltiy to differentiate between non taxable and taxable savings as well as assumes the same investment returns across all savings that any users may have, which typically may very well not be the case.These are some elements that could added to provide a more robust answer.

In terms of the programming itself i think data validation could be further improved more potential user inputs. For example if the user put $3,000 into how much do you want to spend in retirement? or currently have saved? It would be reasonable for the user to input these figures and the program should be able to handle it. Additonaly i think it may make sense to take all the questions and attribute assginment out of the main() function and into its own seperate function leaving the main() function as simple as possible.

I would also like to see more robust testing. It was difficult to try and learn about mock testing as the course did not go into this at all. The two functions that perform calculations I have not tested at all. With that being said these are all mainly math operations tha have essentially been hard coded, therefore I think the testing of these functions is not as important as by the time these variables have reached these functions they have already been vaildated.

These are some of the things I would look at improving in this program. At this point I have met the requirements of the project and due to time constraints and many already need to have it submitted. Thank you CS50P for an excellent course and looking forward to continuing my coding education!


## Video Demo:  <https://youtu.be/yQGDIH964n4>




