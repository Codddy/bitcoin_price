import tkinter as tk
import requests

class BitcoinPriceApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bitcoin Price Tracker')
        
        self.price_label = tk.Label(root, text='Bitcoin price: Waiting...')
        self.price_label.pack(pady=20)
        
        self.update_price()
        
    def update_price(self):
        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
            data = response.json()
            price_in_usd = data['bpi']['USD']['rate']
            self.price_label.config(text=f'Bitcoin price: {price_in_usd} USD')
        except Exception as e:
            self.price_label.config(text='Price cannot be updated.')
        
        self.root.after(600000, self.update_price)

if __name__ == '__main__':
    root = tk.Tk()
    app = BitcoinPriceApp(root)
    root.mainloop()
