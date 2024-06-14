{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "215549fd",
   "metadata": {
    "height": 285
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[*********************100%%**********************]  2 of 2 completed\n"
     ]
    }
   ],
   "source": [
    "from functions import get_stock_prices, plot_stock_prices\n",
    "import pandas as pd\n",
    "\n",
    "# Set the stock symbols and date range\n",
    "stock_symbols = ['NVDA', 'TSLA']\n",
    "start_date = '2024-01-01'\n",
    "end_date = '2024-06-14'\n",
    "\n",
    "# Fetch the stock prices\n",
    "stock_prices = get_stock_prices(stock_symbols, start_date, end_date)\n",
    "\n",
    "# Plot the stock prices and save to file\n",
    "plot_stock_prices(stock_prices, 'stock_prices_YTD_plot.png')\n",
    "\n",
    "# Notify the user that the process is complete and the file is saved\n",
    "print(\"Stock price plot saved as 'stock_cssprices_YTD_plot.png'.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
