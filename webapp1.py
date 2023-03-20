from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def peso():
    return render_template("webapp.html") 

@app.route('/imc')
def IMC():
    peso = int(request.args.get('kg'))
    altezza = int(request.args.get('cm'))
    imc = round((peso/(altezza/100)**2), 2)
    if imc < 18.5:
        stato = 'SOTTOPESO'
        immagine = 'static/images/sottopeso.jpg'
    elif imc > 18.5 and imc < 25:
        stato = 'NORMOPESO'
        immagine = 'static/images/normopeso.jpg'
    elif imc > 25:    
        stato = 'SOVRAPPESO'
        immagine = 'static/images/sovrappeso.jpg'
    return render_template("imc.html", imc = imc, stato = stato, immagine = immagine) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
