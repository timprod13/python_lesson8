class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def extract(cls, d_m_y):
        my_date = []
        for i in d_m_y.split():
            if i != '-':
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Everything is okay'
                else:
                    return f'Wrong year {year}!'
            else:
                return f'Wrong month {month}!'
        else:
            return f'Wrong day {day}!'

    def __str__(self):
        return f'Today is {Data.extract(self.d_m_y)}'


today = Data('31 - 10 - 2020')
print(today)
print(Data.validation(-5, 5, 5))
print(today.validation(15, 13, 2033))
print(Data.extract('18 - 12 - 1966'))
print(today.extract('11 - 09 - 2001'))
print(Data.validation(1, 11, 2))
