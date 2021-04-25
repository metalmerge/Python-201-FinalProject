from flask import Flask, render_template, request
import Plurality_Code


app = Flask('app')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/Plurality')
def Plurality():
		return render_template("Plurality.html")

#@app.route('/Plurality_Input', methods=['POST'])
#def Amount():
		#Candidate_Count = int(request.form['candidate_count'])
		#Voter_Count = int(request.form['voter_count'])
		#for i in range(Candidate_Count):
			
		#return render_template("Plurality.html")


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
		
		return render_template("Plurality.html",v = winner)

    

app.run(host='0.0.0.0', port=8080)

#https://stackoverflow.com/questions/55456752/taking-user-input-from-html-form-as-a-variable-for-python-script
