import requests
import pandas as pd

#https://iss.moex.com/iss/engines/stock/markets/shares/securities/RU000A0JX2B5.json
# https://iss.moex.com/iss/securities/RU000A0JX2B5.json
# https://iss.moex.com/iss/securities/RU000A0JX2B5/bondization.json?iss.only=coupons",
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
        self.__df_coupons = self.__get_coupons()

    def __get_coupons(self):
        resp = requests.get(
            url=f"https://iss.moex.com/iss/securities/{self.__secid}/bondization.json",
            params={
                "iss.only": "coupons",
                "coupons.columns": "coupondate,initialfacevalue,facevalue,value,valueprc,value_rub"
            }
        )
        jsn = resp.json()["coupons"]
        print(resp.url)
        return pd.DataFrame(columns=jsn["columns"], data=jsn["data"])


    def get_coupons_dates(self):
        return self.__df_coupons["coupondate"].values.tolist()

    def get_coupons_values(self):
        return self.__df_coupons["value"].values.tolist()

    def get_current_yield(self, current_price: float, accin: float = 0.0):
        return float(self.__couponvalue) * float(self.__couponfrequency) / (current_price / 100 * float(self.__facevalue)) * 100


    def print_params(self):
        print(type(self.__couponvalue))
        print(type(self.__couponfrequency))
        print(type(self.__facevalue))








sec = Bonds("RU000A106A86")
sec.print_params()
print(sec.get_current_yield(88.48))