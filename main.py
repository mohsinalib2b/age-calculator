from tkinter import *
from tkinter import ttk
from datetime import date
from tkinter import messagebox

class Age_Calculator:
    def __init__(self, root):
        self.window = root
        self.window.title("Age Calculator")
        self.window.geometry("640x240+0+0")
        self.month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        # Getting today's date
        todays = date.today()

        self.label1 = Label(self.window, text="Date of Birth", font=("times new roman", 20, "bold")).place(x=90, y=30)
        self.label2 = Label(self.window, text="Age at the date of", font=("times new roman", 20, "bold")).place(x=40, y=80)

        # Taking the Birth Month
        self.month1 = StringVar()
        self.month_combo = ttk.Combobox(self.window, width=10, textvariable=self.month1)
        self.month_combo['values'] = self.month_list
        self.month_combo.current(0)
        self.month_combo.place(x=250, y=35)

        # Birth Date
        self.date1 = StringVar()
        self.date_entry = Entry(self.window, textvariable=self.date1, width=10)
        self.date_entry.insert(0, "1")
        self.date_entry.place(x=360, y=35)

        # Birth Year
        self.year1 = StringVar()
        self.year_entry = Entry(self.window, textvariable=self.year1, width=10)
        self.year_entry.insert(0, "2000")
        self.year_entry.place(x=470, y=35)

        # Taking the Current Month
        self.month2 = StringVar()
        self.month2_combo = ttk.Combobox(self.window, width=10, textvariable=self.month2)
        self.month2_combo['values'] = self.month_list
        self.month2_combo.current(todays.month - 1)
        self.month2_combo.place(x=250, y=87)

        # Current Date
        self.date2 = StringVar()
        self.date2_entry = Entry(self.window, textvariable=self.date2, width=10)
        self.date2_entry.insert(0, todays.day)
        self.date2_entry.place(x=360, y=87)

        # Current Year
        self.year2 = StringVar()
        self.year2_entry = Entry(self.window, textvariable=self.year2, width=10)
        self.year2_entry.insert(0, todays.year)
        self.year2_entry.place(x=470, y=87)

        self.calculate_button = Button(self.window, text="Calculate Age", bg="green", fg="white", font=("times new roman", 12, "bold"), command=self.calculate_age)
        self.calculate_button.place(x=270, y=150)

    def is_leap_year(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def calculate_age(self):
        self.months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        self.month_dict = {
            "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
        }

        try:
            day1 = int(self.date1.get())
            mon1 = int(self.month_dict[self.month_combo.get()])
            year1 = int(self.year1.get())

            day2 = int(self.date2.get())
            mon2 = int(self.month_dict[self.month2_combo.get()])
            year2 = int(self.year2.get())

            date1 = date(year1, mon1, day1)
            date2 = date(year2, mon2, day2)

            # Difference between two dates
            TotalDays = (date2 - date1).days

            if year1 == year2:
                month = TotalDays / 30
                day = TotalDays % 30
                year = 0
            else:
                year = TotalDays / 365
                month = (TotalDays % 365) / 30

                if self.is_leap_year(year2):
                    self.months[2] = 29

                if day2 >= day1:
                    day = day2 - day1
                elif mon2 == 2 and (self.is_leap_year(year2) or not self.is_leap_year(year2)):
                    year = year
                    month = 11

                    if mon2 == 1:
                        prevMonth = self.months[mon2]
                    else:
                        prevMonth = self.months[mon2 - 1]
                    days = prevMonth - day1 + day2
                    day = days
                else:
                    if mon2 == 1:
                        prevMonth = self.months[mon2]
                    else:
                        prevMonth = self.months[mon2 - 1]

                        if self.is_leap_year(year1) & (mon1 == 2) & (mon2 == 3):
                            days = prevMonth - day1 + day2 + 1
                        else:
                            days = prevMonth - day1 + day2
                    day = days
                    month = month

            day = int(day)
            month = int(month)
            year = int(year)

            # Printing the result
            messagebox.showinfo("Age", f"{year} years {month} months {day} days")

        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")


if __name__ == "__main__":
    root = Tk()
    obj = Age_Calculator(root)
    root.mainloop()
