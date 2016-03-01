#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: TempletePattern.py
@time: 2016/2/29 20:00
"""


# class CaffeineBeverage:
#     def prepareRecipe(self):
#         self.boilWater()
#         self.brew()
#         self.pourInCup()
#         if self.customWantsCondiments():
#             self.addCondiments()
#     def boilWater(self):
#         print("Boiling water")
#     def brew(self):
#         pass
#     def pourInCup(self):
#         print("Pouring into cup")
#     def addCondiments(self):
#         pass
#     def customWantsCondiments(self):
#         return True
#
#
# class Tea(CaffeineBeverage):
#     def brew(self):
#         print("Steeping the tea")
#     def addCondiments(self):
#         print("Adding Lemon")
#
# class Coffee(CaffeineBeverage):
#     def brew(self):
#         print("Dripping Coffee through filter")
#     def addCondiments(self):
#         print("Adding Sugar and Milk")
#     def customWantsCondiments(self):
#         answer = self.getUserInput()
#         if answer == "Y":
#             return True
#         else:
#             return False
#     def getUserInput(self):
#         answer = input("Would you like milk and sugar with your coffee (Y/N)? ")
#         return answer
#
# def main():
#     myTea = Tea()
#     myTea.prepareRecipe()
#     print("==========================================")
#     myCoffee = Coffee()
#     myCoffee.prepareRecipe()
# if __name__ == '__main__':
#     main()

import sqlite3

# conn = sqlite3.connect("sales.db")
# conn.execute("CREATE TABLE Sales" "(salesperson text, amt currenct, year integer, model text, new boolean)")
# conn.execute("INSERT INTO Sales VALUES " "('Tim', 16000, 2010, 'Honda Fit', 'true')")
# conn.execute("INSERT INTO Sales VALUES " "('Tim', 9000, 2006, 'Ford Focus', 'false')")
# conn.execute("INSERT INTO Sales VALUES " "('Gayle', 8000, 2004, 'Dodge Neon', 'false')")
# conn.execute("INSERT INTO Sales VALUES " "('Gayle', 28000, 2009, 'Honda Mustang', 'true')")
# conn.execute("INSERT INTO Sales VALUES " "('Gayle', 50000, 2010, 'Lincoln Navigator', 'true')")
# conn.execute("INSERT INTO Sales VALUES " "('Don', 20000, 2008, 'Toyota Prius', 'false')")
# conn.commit()
# conn.close()

class QueryTemplete:
    def connect(self):
        self.conn = sqlite3.connect("sales.db")
    def construct_query(self):
        raise NotImplementedError()
    def do_query(self):
        result = self.conn.execute(self.query)
        self.result = result.fetchall()
    def format_result(self):
        output = []
        for row in self.result:
            row = [str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)
    def output_result(self):
        raise NotImplementedError()
    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_result()
        self.output_result()

class NewVehiclesQuery(QueryTemplete):
    def construct_query(self):
        self.query = "SELECT * FROM Sales WHERE new='true' "
    def output_result(self):
        print(self.formatted_results)

q = NewVehiclesQuery()
q.process_format()
