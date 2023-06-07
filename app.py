from flask import Flask, render_template, request

app = Flask(__name__)

# Define a list of health conditions and severities
health_conditions = [
    'Cardiology Department',
    'Obstetrics and Gynecology Department',
    'Neurology Department',
    # Add more conditions as needed
]

severities = [
    'regular health check-up',
    
    'Emergency',
    # Add more severities as needed
]

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        condition = request.form.get('condition')
        severity = request.form.get('severity')
        # Perform any necessary actions based on the selected condition and severity
        if severity=='Emergency':
            print('vigiting time is 9-5')
            chatbot_response=f"we are provide 24*7 service at Emergency\n please contact 011-**123\n"
            return render_template('chat.html', response=chatbot_response ,conditions=health_conditions, severities=severities)
        else:
            chatbot_response='Doctor’s Visits Timing 8:00 AM '
            return render_template('chat.html', response=chatbot_response ,conditions=health_conditions, severities=severities)
            

    return render_template('chat.html', conditions=health_conditions, severities=severities)

if __name__ == '__main__':
    app.run(debug=True)
