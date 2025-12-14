# Crypto Dashboard
A real-time cryptocurrency dashboard built with Python and Tkinter. Displays live market data from Binance platform, including price tickers, volume, order book, recent trades, and candlestick/line charts. Supports multiple cryptocurrencies with toggleable panels.

## Project Structure

```bash
├── libs/ # Panels and utilities
│ ├── lib_data.py # Store class to get the value of api end point
│ ├── lib_socket.py # Store class to initiate socket
│ ├── matplot_lib.py # Store class to create matplot graph
│ └── widget_lib.py # Store class to create custom widgets
├── picture/ # Assets
│ ├── ui_from_figma.png # Figma UI Design
│ └── real_ui.png # Figma UI Design 
├── test/ # To test code before put inside the main program
│ ├── crypto_price.py # Test simple api endpoint
│ ├── hide.py # Test hide widget button
│ ├── loop_crypto.py # Check of socket is working fine
│ └── test_sys.py # Check if the api endpoint is valid
├── main.py # Main code
├── requirement.txt # All required libraries
└── README.md # You are here !
```

## Features
### Core Features
- Real-time price tracking for multiple cryptocurrencies (BTC, ETH, BNB, XRP, SOL, ADA)
- Color-coded price changes (green for increase, red for decrease)
- 24-hour price change display
- Clean, organized, professional GUI
- Toggle buttons to show/hide panels
- Responsive layout that adapts to window resizing
- Persistent settings (last selected symbol and panel visibility)

### Advanced Features
- 24-hour volume display
- Order book showing top 10 bids and asks
- Recent trades feed
- Candlestick chart with volume using Matplotlib
- Line chart volume that reset every 1 minutes using Matploadlib
- Multiple panels displaying different market information
- Efficient use of screen space

## Installation
### Requirements
- Python 3.7+

### Dependencies
Install via pip:
```bash
pip install -r requirement.txt
```

## How to run
Type this on terminal
```bash
python main.py
```

## Project Requirements & Grading Rubric
### Core Requirements
#### Basic Features
- ✅ Application launches without errors
- ✅ Clean OOP design with classes
- ✅ Proper event handling
- ✅ Graceful shutdown (closes WebSockets, no errors)

#### Price Tickers
- ✅ At least 3 cryptocurrency tickers (BTC, ETH, SOL)
- ✅ Real-time price updates via WebSocket
- ✅ Color-coded price changes (green/red)
- ✅ Display 24h change and percentage

#### User Interface
- ✅ Professional, organized layout
- ✅ Toggle buttons to show/hide panels
- ✅ Responsive to window resizing
- ✅ Clear labeling and readability

### Advanced Features
#### Additional Data Streams
- ✅ 24-Hour Volume display
- ✅ Order Book (top 10 bids/asks)
- ✅ Recent Trades feed
- ✅ Candlestick chart with Matplotlib

#### Multiple Assets & Toggles
- ✅ Support for 5+ cryptocurrencies
- ✅ Individual toggle buttons for each asset
- ❌ Saved preferences (remember which panels are visible)

#### Information Density
- ✅ Displays comprehensive market data
- ✅ Multiple panels with different information types
- ✅ Efficient use of screen space

## Youtube video: https://youtu.be/gQZSQlRQmyc