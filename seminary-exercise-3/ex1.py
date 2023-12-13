class Employee:
    def __init__(self, i_num, fname, lname, work_experience, education_level, salary, age):
        self.i_num = i_num
        self.fname = fname
        self.lname = lname
        self.work_experience = work_experience
        self.education_level = education_level
        self.salary = salary
        self.age = age
    def display_info(self):
        print(f"num: {self.i_num},
              fname: {self.fname},
              lname: {self.lname}, work_experience: {self.work_experience}, education_level: {self.education_level}, salary: {self.salary}, age: {self.age}")
    def bonus(self):
        if(self.work_experience >= 1):
            self.salary = self.salary * (self.work_experience * 1.012)
        else:
            self.salary = self.salary
        if(self.education_level == 'visho'):
            self.salary = self.salary * 1.05
        elif(self.education_level == 'sredno'):
            self.salary = self.salary * 1.02

# God I am so lazy to code rn
    
            