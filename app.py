from flask import Flask,request,jsonify

app=Flask(__name__)

class NoInput(Exception):
    status_code = 400

    def __init__(self, status_code, message):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

@app.route("/reverse",methods=['GET'],strict_slashes=False)
def reverse():
    try:
        s=request.args.get("s")
    except:
        raise NoInput(status_code=400,message="No valid string provided")
    if request.args.get("s"):
        s=request.args.get("s")
        s=s[::-1]
        data={
            "reversed_string":s
        }
    else:
        data={
            "reversed_string":""
        }
    
    return jsonify(data)


@app.errorhandler(Exception)
def handle_error(err):
    if isinstance(err,NoInput):
        return jsonify(
            error=err.__class__.__name__, message=err.message
        ), err.status_code