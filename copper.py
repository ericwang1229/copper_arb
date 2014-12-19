import pandas as pd
hg_trades = pd.read_csv(r"C:\Copper\HG ##-##.Last.txt", names=["DatetimeStr", "Price", "Qty"], delimiter=";", parse_dates=True)
hg_trades["Datetime"] = pd.to_datetime(hg_trades["DatetimeStr"],"%Y%m%d %H%M%S")
#hg_trades = hg_trades.set_index("Datetime")
hg_trades["Symbol"] = 1
scf_trades = pd.read_csv(r"C:\Copper\SCF ##-##.Last.txt", names=["DatetimeStr", "Price", "Qty"], delimiter=";", parse_dates=True)
scf_trades["Datetime"] = pd.to_datetime(scf_trades["DatetimeStr"],"%Y%m%d %H%M%S")
#scf_trades = scf_trades.set_index("Datetime")
scf_trades["Symbol"] = 2
print hg_trades.shape
hg_trades.head() 
print scf_trades.shape
scf_trades.head()
total_trades = pd.concat([scf_trades, hg_trades])
total_px = total_trades.drop("Qty", 1)
total_px = total_trades.drop("DatetimeStr", 1)
total_px = total_px.sort("Datetime")
total_px = total_px.drop_duplicates()
total_copy = total_px.copy()
total_copy.index = total_copy.index+1
total_px = pd.merge(total_px, total_copy)
