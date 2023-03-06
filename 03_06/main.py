from flask import Flask, render_template, request

app = Flask(
  __name__,
  template_folder='templates'
)

@app.route("/")
def home() :
  return render_template('home.html')

@app.route('/result', methods=['Post'])
def rusult() :
  n1 = float(request.form['num1'])
  n2 = float(request.form['num2'])
  operator = request.form['operator']

  result = calc(n1, n2, operator)
  return render_template('result.html', fin_result=result)

def calc(n1, n2, operator) :
  if operator == '+' :
    result = n1 + n2
  elif operator == '-' :
    result = n1 - n2
  elif operator == '*' :
    result = n1 * n2
  elif operator == '/' :
    result = n1 / n2
  return result



if __name__ == '__main__' :
  app.run(
    host='0.0.0.0',
    port=8080,
    debug=True
  )
