from flask import Flask, render_template, request
from gramformer import Gramformer
import torch

def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

set_seed(1212)

gf = Gramformer(models=1, use_gpu=False) # 1=corrector, 2=detector

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/correct', methods=['GET', 'POST'])
def correct():
    if request.method == 'POST':
        try:
            text = request.form['input_sentence']
            corrected_text = gf.correct(text, max_candidates=1)
            return render_template('index1.html', input_sentence=text, corrected_text=corrected_text)
        except:
            error_message = "An error occurred while processing your request. Please try again later."
            return render_template('index1.html', error_message=error_message)
    else:
        return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)
