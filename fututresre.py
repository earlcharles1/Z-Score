import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Data_and_Plots:
	def __init__(self):
		self.ticker = yf.Ticker('XLM-USD')
		self.data = yf.download(tickers=('XLM-USD'), 
			period = '1d', 
			interval = '1m',
			group_by ='ticker', 
			auto_adjust = True, 
			prepost = False)
		self.df = pd.DataFrame(self.data)
		self.returns = 100 * np.log(self.df['Close'] / self.df['Close'].shift(1)) 
		#self.returns1 = np.log(self.df['VXX','Close'] / self.df['VXX','Close'].shift(1))
		# self.returns2 = np.log(self.df['KKR','Close'] / self.df['KKR','Close'].shift(1))
		# self.returns3 = np.log(self.df['VXX','Close'] / self.df['VXX','Close'].shift(1))
		# self.Return_Deviation = np.std(self.returns)
		#self.Price_Deviation = np.std(self.df['UVXY','Close'])

	def histogram(self):
		plt.hist(self.returns)
		plt.title('Histogram of Daily Returns')
		plt.show()
	def return_plot(self):
		plt.plot(self.returns)
		plt.show()
		#self.cumu = np.cumsum(self.returns)
		#self.cumu1 = np.cumsum(self.returns1)
	def bell_curve(self):
		"""This uses the numpy random distribution function, 
			it takes the parameters loc, scale, size. loc = mean,
			scale= standard deviation, and size = length of dataframe
			."""
		distribution = np.random.normal(
			self.df['Close'].mean(),
			np.std(self.df['Close']),
			len(self.df['Close']))
		plt.hist(distribution), #bins = 3)
		plt.show()

	def z_score_single(self):
		mean = self.df['Close'].mean()
		z_from_mean = (self.df['Close'].tail(1) - mean) / np.std(self.df['Close'])
		print(self.df['Close'].tail(1))
		print(z_from_mean)
	def new_hmm(self):
		self.df['Close'].plot()
		plt.show()


class MultiTickerStuff:
	def __init__(self):
		self.ticker = yf.Tickers('BTC-USD')
		self.ticker1 = yf.Tickers('ETH-USD')
		# self.ticker2 = yf.Tickers('BNB-USD')
		# self.ticker3 = yf.Tickers('DOGE-USD')
		# self.ticker4 = yf.Tickers('XRP-USD')
		self.data = yf.download(tickers=('BTC-USD'),period='1y',interval='1d',group_by='ticker',auto_adjust=True,prepost=False)
		self.data1 = yf.download(tickers=('ETH-USD'),period='7d',interval='1m',group_by='ticker',auto_adjust=True,prepost=False)
		# self.data2 = yf.download(tickers=('BNB-USD'),period='7d',interval='1m',group_by='ticker',auto_adjust=True,prepost=False)
		# self.data3 = yf.download(tickers=('DOGE-USD'),period='7d',interval='1m',group_by='ticker',auto_adjust=True,prepost=False)
		# self.data4 = yf.download(tickers=('XRP-USD'),period='7d',interval='1m',group_by='ticker',auto_adjust=True,prepost=False)
		self.df = pd.DataFrame(self.data)
		self.df1 = pd.DataFrame(self.data1)
		# self.df2 = pd.DataFrame(self.data2)
		# self.df3 = pd.DataFrame(self.data3)
		# self.df4 = pd.DataFrame(self.data4)
		print(self.df.tail(1))
		print(self.df1.tail(1))
		# print(self.df2.tail())
		# print(self.df3.tail())
		# print(self.df4.tail())




	def find_z(self):
		mean = self.df['Close'].mean()
		mean1 = self.df1['Close'].mean()
		# mean2 = self.df2['Close'].mean()
		# mean3 = self.df3['Close'].mean()
		# mean4 = self.df4['Close'].mean()
		z_from_mean = (self.df['Close'].tail(1) - mean) / np.std(self.df['Close'])
		z_from_mean1 = (self.df1['Close'].tail(1) - mean1) / np.std(self.df1['Close'])
		# z_from_mean2 = (self.df2['Close'].tail(1) - mean2) / np.std(self.df2['Close'])
		# z_from_mean3 = (self.df3['Close'].tail(1) - mean3) / np.std(self.df3['Close'])
		# z_from_mean4 = (self.df4['Close'].tail(1) - mean4) / np.std(self.df4['Close'])
		print("BTC-USD",self.df['Close'].tail(1),z_from_mean)
		print("ETH-USD",self.df1['Close'].tail(1),z_from_mean1)
		# print("BNB-USD",self.df2['Close'].tail(1),z_from_mean2)
		# print("DOGE-USD",self.df3['Close'].tail(1),z_from_mean3)
		# print("XRP-USD",self.df4['Close'].tail(1),z_from_mean4)




# DnP= Data_and_Plots()
# Datafeed = DnP.df
MTS = MultiTickerStuff()
MDF = MTS.df
MTS.find_z()
