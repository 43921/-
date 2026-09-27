# 1
class Employee:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def print_info(self):
        print(f"员工名字:{self.name},工号:{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, age, id, monthly_salary):
        super().__init__(name, age, id)  # 子类构造方法里，初始化父类的属性
        self.monthly_salary = monthly_salary

    def calculate_monthly_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, age, id, daily_salary, work_days):
        super().__init__(name, age, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_salary(self):
        return self.daily_salary * self.work_days


zhangsan = FullTimeEmployee("zhangsan", 21, 21, 100)
lisi = PartTimeEmployee("lisi", 21, 21, 100, 22)
lisi.print_info()
zhangsan.print_info()
print(zhangsan.calculate_monthly_salary())
print(lisi.calculate_monthly_salary())


# 2
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name}（学号：{self.student_id}）的成绩为：")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}分")


chen = Student("小陈", "100618")
chen.set_grade("语文", 92)
chen.set_grade("数学", 94)
chen.print_grades()


class Shape:
    def __init__(self, shape, name):
        self.shape = shape
        self.name = name

    def get_area(self):
        print("图形面积")


class Circle(Shape):
    def __init__(self, shape, name, radius):
        super().__init__(shape, name)
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


c = Circle("圆形", "圆", 2)
print(c.get_area())
s1 = Shape("图形", "基础图形")
c1 = Circle("圆形", "圆", 3)

s1.get_area()
c1.get_area()
# 多态：多个对象调用同名方法，执行不同代码这个效果
