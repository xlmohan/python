# Function overriding
class Management:
    def WorkingHrs(self):
        self.hrs=40
        
    def PrintHrs(self):
        print(f"From Management: {self.hrs}")
        
class Employee(Management):
    def WorkingHrs(self):
        self.hrs=40
        
    def PrintHrs(self):
        super().PrintHrs()
        print(f"Working hours: {self.hrs}")

class Trainee(Employee):
    def WorkingHrs(self):
        self.hrs=45  # Overriding the method to set different working hours for Trainee
        
    # After completing the training, employee should permenantly work as Employee
    def resetHrs(self):
        super().WorkingHrs()  # Calling the parent class method to reset hours to Employee's hours
        
employee=Employee()
employee.WorkingHrs()
employee.PrintHrs()

trainee=Trainee()
trainee.WorkingHrs()
trainee.PrintHrs()
trainee.resetHrs()
trainee.PrintHrs()