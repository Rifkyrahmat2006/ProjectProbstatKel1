from flask import Flask, render_template, request, jsonify
import math
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def poisson_probability(lambda_val, k):
    return (math.exp(-lambda_val) * (lambda_val ** k)) / factorial(k)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        lambda_val = float(request.form['lambda'])
        x_max = float(request.form['x_max'])
        
        if lambda_val <= 0 or x_max < 0:
            return jsonify({'error': 'Invalid input values'}), 400
            
        # Calculate probabilities manually
        x_values = []
        probabilities = []
        # Convert x_max to integer for range, but keep original float value
        x_max_int = int(x_max)
        for k in range(x_max_int + 1):
            prob = poisson_probability(lambda_val, k)
            x_values.append(float(k))
            probabilities.append(prob)
        
        # Create histogram using matplotlib
        plt.figure(figsize=(10, 6))
        plt.bar(x_values, probabilities, alpha=0.7)
        plt.title(f'Distribusi Poisson (λ = {lambda_val})')
        plt.xlabel('Jumlah Kejadian (k)')
        plt.ylabel('Probabilitas P(X = k)')
        plt.grid(True, alpha=0.3)
        
        # Save plot to base64 string
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        
        # Prepare results
        results = [{'k': k, 'probability': prob} for k, prob in zip(x_values, probabilities)]
        
        return jsonify({
            'plot': plot_url,
            'results': results
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 