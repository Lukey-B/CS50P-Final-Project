import sys

class RetirementCalculator:
    def __init__(self,current_age, retirement_age, retirement_income, risk_tolerance, current_savings, years_to_retirement):

        self.current_age = current_age
        self.retirement_age = retirement_age
        self.retirement_income = retirement_income
        self.risk_tolerance = risk_tolerance
        self.current_savings = current_savings
        self.years_to_retirement = years_to_retirement

    # define FV needed to support desired monthly income during retirement, discounting back to start of retirement
    #FV = PMT x (((1 + r)^n - 1) / r) x (1 + r)
    #PV = FV lump sum/(1+r)^n

    def funds_required_in_retirement(self):
        annual_amount = self.retirement_income * 12
        years_in_retirement = 95 - self.retirement_age
        FV_annuitydue = annual_amount * ((1.04 ** (years_in_retirement) - 1) / .04) * 1.04
        inflation_adj_return = (1.04/1.03)
        PV_funds_required = (FV_annuitydue / (inflation_adj_return ** years_in_retirement))
        return PV_funds_required


    # define amount needed to be invested per month in order to meet the amount required for retirment income objective
    # Calc pmt required for FV annuity (FV of annuity will be funds required in retirement)
    #P = FV * (r / ((1 + r)^n - 1))

    def funds_required_for_retirement(self):
        risk_tolerance = self.risk_tolerance
        FV_currentsavings = self.current_savings * (1 + ROR(risk_tolerance)) ** self.years_to_retirement
        FV_required = self.funds_required_in_retirement() - FV_currentsavings
        months_till_retirement = (self.retirement_age - self.current_age) * 12
        expected_return = ROR(risk_tolerance) / 12
        pac = FV_required * (expected_return / ((1 + expected_return) ** months_till_retirement -1))
        return pac

    # assign rate of return based off risk tolerance

def ROR(risk_tolerance):
    if risk_tolerance == "low":
        return 0.04
    elif risk_tolerance == "medium":
        return 0.07
    elif risk_tolerance == "high":
        return 0.09

def formatted_dollar(pac):
    dollar_amount = float(round(pac))
    return "${:,.0f}".format(round(dollar_amount))


#function outside of class used to validate our input for each one of our questions
def get_input(prompt,condition,error_message):
    i = 0
    while i < 5:
        try:
            i += 1
            value = input(prompt)
            if not condition(value):
                raise ValueError(error_message)
            return value
        except ValueError:
            if i == 5:
                sys.exit("Too many wrong attempts")


def main():

    current_age = int(get_input("how old are you? ", lambda x: x.isnumeric() and int(x) >= 0, "Please enter a valid age"))
    retirement_age = int(get_input("When would you like to retire? ", lambda x: x.isnumeric() and int(x) >= current_age, "Retirement age cannot be less than current age"))
    retirement_income = int(get_input("how much would you like to spend per month in retirement? ", lambda x: x.isnumeric() and int(x) > 0, "Retirement income must be greater than 0"))
    risk_tolerance_options = ["low", "medium", "high"]
    risk_tolerance = get_input("When it comes to investing, would you prefer to take a low, medium, or high risk approach? ", lambda x: x.lower() in risk_tolerance_options, 'Risk tolerance must be "low", "medium", or "high"')
    current_savings = int(get_input("how much do you currently have invested? ", lambda x: x.isnumeric() and int(x) >= 0, "Please enter a valid investment amount"))
    years_to_retirement = retirement_age - current_age
    retirement_calculator = RetirementCalculator(current_age, retirement_age, retirement_income, risk_tolerance, current_savings, years_to_retirement)
    pac = formatted_dollar(retirement_calculator.funds_required_for_retirement())
    print(f"You need to save {pac} per month to achieve your retirement objective")

if __name__ == "__main__":
    main()

