class Answers:
    def __init__(self, timestamp, name, email, phone, date_of_birth, age, city, sectors, notice, full_part_time, salary, entrepreneur, why_entrepreneur, rejection, money, progression, fun, communication, confidence, adaptability, leadership, describe):
        self.timestamp = timestamp
        self.name = name
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.age = age
        self.city = city
        self.sectors = sectors
        self.notice = notice
        self.full_part_time = full_part_time
        self.salary = salary
        self.entrepreneur = entrepreneur
        self.why_entrepreneur = why_entrepreneur
        self.rejection = rejection
        self.money = money
        self.progression = progression
        self.fun = fun
        self.communication = communication
        self.confidence = confidence
        self.adaptability = adaptability
        self.leadership = leadership
        self.describe = describe

#Defines the class so it can print a full description of the individual
    def __repr__(self):
        return f"""
        {self.name}, {self.email}, {self.phone}, {self.date_of_birth} -> {self.age} years old
        Applied at {self.timestamp}
        Commute to Birmingham is easy ({self.city})
        Interested in {self.sectors}
        Notice period is {self.notice}
        They are looking for a {self.full_part_time} role
        Expected salary of {self.salary}
        Consider themselves entrepreneur ({self.entrepreneur}) because {self.why_entrepreneur}
        Handle rejection at {self.rejection}
        Rank importance as: {self.money} Money
                            {self.progression} Progression
                            {self.fun} Fun
        Rank their communication as {self.communication}
        Rank their confidence as {self.confidence}
        Rank their adaptability as {self.adaptability}
        Rank their leadership as {self.leadership}
        Describe themselves as "{self.describe}"
        """

# class Filter:
#     def __init__ (self, name, email, age, commute, availability, entrepreneur):
#         self.name = name
#         self.email = email
#         self.age = age
#         self.commute = commute
#         self.availability = availability
#         self.entrepreneur = entrepreneur
    
#     def __repr__(self): return f"""
#         {self.name}, {self.age}, {self.availability}, {self.entrepreneur}"""