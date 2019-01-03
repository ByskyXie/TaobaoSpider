import time
from typing import Any


class Commodity:
    __item_url = ''
    __item_title = ''
    __item_name = ''
    item_type = None
    __store_name = ''
    __store_url = ''

    def __init__(self) -> None:
        super().__init__()

    @property
    def item_url(self) -> str:
        return self.__item_url

    @item_url.setter
    def item_url(self, value: str):
        self.__item_url = str(value).strip()

    @property
    def item_title(self) -> str:
        return self.__item_title

    @item_title.setter
    def item_title(self, value: str):
        self.__item_title = str(value).strip()

    @property
    def item_name(self) -> str:
        return self.__item_name

    @item_name.setter
    def item_name(self, value: str):
        self.__item_name = str(value).strip()

    @property
    def store_name(self) -> str:
        return self.__store_name

    @store_name.setter
    def store_name(self, value: str):
        self.__store_name = str(value).strip()

    @property
    def store_url(self) -> str:
        return self.__store_url

    @store_url.setter
    def store_url(self, value: str):
        self.__store_url = str(value).strip()

    @item_name.setter
    def item_name(self, value: str):
        self.__item_name = str(value).strip()

    def __str__(self) -> str:
        return '[Title]:' + self.item_title + '\n[Url]:' + self.item_url + \
               '\n[Store]:' + self.store_name + '\n[Url]:' + self.store_url


class Item:
    __item_url = ''
    __item_price = -1.0
    __plus_price = -1.0
    __ticket = ''
    inventory = None
    __data_date = time.time()
    __sales_amount = ''
    __transport_fare = None
    __all_specification = ''
    __spec1 = None
    __spec2 = None
    spec3 = None
    spec4 = None
    spec5 = None
    spec_other = None

    def __init__(self):
        pass

    def generate_all_specification(self):
        all_str = ''
        if self.spec1 is not None and len(self.spec1.strip()) > 0:
            all_str += self.spec1.strip()
        if self.spec2 is not None and len(self.spec2.strip()) > 0:
            all_str += '\n' + self.spec2.strip()
        if self.spec3 is not None and len(self.spec3.strip()) > 0:
            all_str += '\n' + self.spec3.strip()
        if self.spec4 is not None and len(self.spec4.strip()) > 0:
            all_str += '\n' + self.spec4.strip()
        if self.spec5 is not None and len(self.spec5.strip()) > 0:
            all_str += '\n' + self.spec5.strip()
        if self.spec_other is not None and len(self.spec_other.strip()) > 0:
            all_str += '\n' + self.spec_other.strip()
        self.__all_specification = all_str

    @property
    def url(self) -> str:
        return self.__item_url

    @url.setter
    def url(self, value: str):
        self.__item_url = str(value).strip()

    @property
    def price(self) -> float:
        return self.__item_price

    @price.setter
    def price(self, value: float):
        if type(value) == float or type(value) == int:
            self.__item_price = float(value)
        return

    @property
    def plus_price(self) -> float:
        return self.__plus_price

    @plus_price.setter
    def plus_price(self, value: float):
        if type(value) == float or type(value) == int:
            self.__plus_price = float(value)
        return

    @property
    def ticket(self):
        return self.__ticket

    @ticket.setter
    def ticket(self, value: str):
        if type(value) != str:
            return
        self.__ticket = value.strip()

    @property
    def data_date(self) -> time:
        return self.__data_date

    @data_date.setter
    def data_date(self, value: time):
        if type(value) != float:
            return
        self.__data_date = value

    @property
    def sales_amount(self) -> str:
        return self.__sales_amount

    @sales_amount.setter
    def sales_amount(self, value: str):
        self.__sales_amount = str(value).strip()

    @property
    def transport_fare(self) -> float:
        return self.__transport_fare

    @transport_fare.setter
    def transport_fare(self, value: float):
        if type(value) != float and type(value) != int:
            return
        self.__transport_fare = float(value)

    @property
    def all_specification(self) -> str:
        return self.__all_specification

    @property
    def spec1(self) -> str:
        return self.__spec1

    @spec1.setter
    def spec1(self, value: str):
        if type(value) != str:
            return
        self.__spec1 = value.strip()

    @property
    def spec2(self) -> str:
        return self.__spec2

    @spec2.setter
    def spec2(self, value: str):
        if type(value) != str:
            return
        self.__spec2 = value.strip()

    def get_str_time(self):
        time_array = time.localtime(self.__data_date)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_array)

    def __str__(self) -> str:
        return self.url + '\n[price]:' + self.price.__str__() + '\t' + self.plus_price.__str__() + \
               '\n[ticket]:\n' + self.ticket + '\n[inventory]:' + self.inventory.__str__() + '\n[time]:' + \
               self.get_str_time() + '\n[sales]:' + self.sales_amount.__str__() + '\n[transport]:' + \
               self.transport_fare.__str__() + '\n[speci]:' + self.all_specification
