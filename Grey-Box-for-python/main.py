from flask import Flask, render_template, request
import Plurality_Code, Approval_Code


app = Flask('app')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/Plurality')
def Plurality():
		return render_template("Plurality.html")

@app.route('/Approval', methods=['POST'])
def Approve():
		ACandidateOne = request.form['AcandidateOne']
		ACandidateTwo = request.form['AcandidateTwo']
		AVoterOne = request.form['AvoterOne']
		AVoterTwo = request.form['AvoterTwo']
		AVoterThree = request.form['AvoterThree']
		results = Approval_Code.Start_Approval(ACandidateOne, ACandidateTwo, AVoterOne, AVoterTwo, AVoterThree)
		return render_template("Approval.html", a = results[0], p = results[1])

@app.route('/Runoff')
def Runoff():
		return render_template("Runoff.html")



@app.route('/Approval')
def Approval():
		return render_template("Approval.html")


@app.route('/Plurality', methods=['POST'])
def Questions():
		CandidateOne = request.form['candidateOne']
		CandidateTwo = request.form['candidateTwo']
		VoterOne = request.form['voterOne']
		VoterTwo = request.form['voterTwo']
		VoterThree = request.form['voterThree']
		
		
		winner = Plurality_Code.Start_Pluraility(CandidateOne,CandidateTwo,VoterOne,VoterTwo,VoterThree)
		
		return render_template("Plurality.html",v = winner[0],l = winner[1])

    

app.run(host='0.0.0.0', port=8080)

#https://stackoverflow.com/questions/55456752/taking-user-input-from-html-form-as-a-variable-for-python-script
