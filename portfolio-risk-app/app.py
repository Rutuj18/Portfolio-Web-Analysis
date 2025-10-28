from flask import Flask, render_template, request, jsonify
from utils.portfolio_analysis import analyze_portfolio

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    tickers = data.get('tickers', [])
    allocations = data.get('allocations', [])
    
    result = analyze_portfolio(tickers, allocations)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
