class Driver:
    def __init__(self, salary, quali_place, bonus):
        self.salary = salary
        self.quali_place = quali_place
        self.bonus = bonus

class TeamPrincipal:
    def __init__(self, salary):
        self.salary = salary


class Accountant:

    def calculate_principal_payment(self, team_principal, driver):
        if(driver.quali_place == 1):
            final_salary = eval(team_principal.salary) * 1.10
            return final_salary




