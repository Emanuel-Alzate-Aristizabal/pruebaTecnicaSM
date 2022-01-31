import pandas as pd
import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            db = 'foodCom'
        )

        self.cursor = self.connection.cursor()

    def extractionCSVfile(self, path):
        print("Extrallendo datos")
        return pd.read_csv(path)

    def loadData1(self, dataframe):

        for r in range(0, len(dataframe)):
            try:
                self.cursor.execute(
                    f"INSERT INTO interactions_test(user_id,recipe_id,date,rating,u,i) VALUES({dataframe[r][0]}, {dataframe[r][1]}, {dataframe[r][2]}, {dataframe[r][3]},{dataframe[r][4]}, {dataframe[r][5]})")
                self.connection.commit()

            except ValueError:
                print("Error")
                print(ValueError)


    def loadData2(self, dataframe):

        for r in range(0,len(dataframe)):
            try:
                self.cursor.execute(f"INSERT INTO pp_users(u,techniques,items,n_items,ratings,n_ratings) VALUES({dataframe[r][0]}, {dataframe[r][1]}, {dataframe[r][2]}, {dataframe[r][3]},{dataframe[r][4]}, {dataframe[r][5]})")
                self.connection.commit()

            except ValueError:
                print("Error")
                print(ValueError)

    def loadData3(self, dataframe):

        for r in range(0, len(dataframe)):
            try:
                self.cursor.execute(
                    f"INSERT INTO pp_recipes(id,i,name_tokens,ingredient_tokens,steps_tokens,techniques,calorie_level,ingredient_ids) VALUES({dataframe[r][0]}, {dataframe[r][1]}, {dataframe[r][2]}, {dataframe[r][3]},{dataframe[r][4]}, {dataframe[r][5]}, {dataframe[r][6]}, {dataframe[r][7]})")
                self.connection.commit()

            except ValueError:
                print("Error")
                print(ValueError)

database = DataBase()
df1 = database.extractionCSVfile('interactions_test.csv')
df2 = database.extractionCSVfile('pp_users.csv')
df3 = database.extractionCSVfile('pp_recipes.csv')

database.loadData1(df1)
database.loadData2(df2)
database.loadData3(df3)


