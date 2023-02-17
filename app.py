from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"]=True

@app.route('/', methods=['GET', 'POST'])
def main():
   try:
      if "opt" in request.args and "v1" in request.args and "v2" in request.args:
         result = eval(request.args["v1"]+request.args["opt"]+request.args["v2"] )
         response = {"operation": request.args, "result": result}
         return jsonify({'status': 'succes',
                         'code': 200,
                         'message': response})
      else:
         return jsonify({'status': 'Error',
                         'code' : 400,
                         'message': 'Calculation Error : Invalid operation parameters'})
   except Exception as e:
      return jsonify({'status': 'Error',
                         'code' : 400,
                         'message': str(e)})




