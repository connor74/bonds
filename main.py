import requests
import pandas as pd

#https://iss.moex.com/iss/engines/stock/markets/shares/securities/RU000A0JSGV0.json
# https://iss.moex.com/iss/securities/RU000A0JX2B5.json
class Bonds:
    def __init__(self, secid: str):
        self.__secid = secid
        resp = requests.get(
            url=f"https://iss.moex.com/iss/securities/{self.__secid}.json",
            params={
                "iss.only": "description",
            }
        )
        self.__data = resp.json()["description"]["data"]
        self.__name = self.__data[1][2]
        self.__shortname = self.__data[2][2]
        self.__issuedate = self.__data[5][2]
        self.__matdate = self.__data[6][2]
        self.__initialfacevalue = self.__data[7][2]
        self.__faceunit = self.__data[8][2]
        self.__facevalue = self.__data[15][2]
        self.__couponfrequency = self.__data[17][2]
        self.__couponvalue = self.__data[20][2]

    def get_coupons(self):
        pass

    def print_params(self):
        print(self.__name)
        print(self.__shortname)
        print(self.__issuedate)






sec = Bonds("RU000A0JX2B5")
sec.print_params()