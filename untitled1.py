import investpy
import datetime as dt

start = '1/5/2022'
end = dt.datetime.now().strftime("%d/%m/%Y")

search_result = investpy.get_stocks_list(country='VietNam')

df = search_result.get_stock_historical_data(start, end)
dfmack=pd.read_csv("C:\\Users\\HOANG\\Desktop\\Python\\Ma CK Viet Nam.csv")
dfmack=pd.DataFrame(dfmack)
dfmack=dfmack.loc[dfmack['SAN']=='HNX']
listck=dfmack['Ma CK'].values.tolist()