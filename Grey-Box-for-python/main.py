from flask import Flask, render_template


app = Flask('app')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/Plurality')
def Plurality():
		return render_template("Plurality.html")
VOTES = ["Dima", "Dima", "Gabby",]
Pcandidates = [
        {
            "name": "Dima",
            "votes": 0,
        },
        {
            "name": "Jack",
            "votes": 0,
        },
        {
            "name": "Gabby",
            "votes": 0,
        },
    ]
for x in Pcandidates:
	
	if x["name"] == VOTES[1]:
		x["votes"] += 1
		max = 0
for y in Pcandidates:
	if y["votes"] > max:
		max = y["votes"]
for z in Pcandidates:
	if z["votes"] == max:
		print(z["name"])
		


@app.route('/Runoff')
def Runoff():
	return render_template("Runoff.html")
	Rcandidates = [
        {
            "name": "Eren",
            "votes": 0,
        },
        {
            "name": "Okabe",
            "votes": 0,
        },
        {
            "name": "Kurisu",
            "votes": 0,
        },
    ]



@app.route('/Approval')
def Approval():
	return render_template("Approval.html")
	Acandidates = [
        {
            "name": "Joe",
            "votes": 0,
        },
        {
            "name": "Falco",
            "votes": 0,
        },
        {
            "name": "Sheik",
            "votes": 0,
        },
    ]


app.run(host='0.0.0.0', port=8080)

#https://stackoverflow.com/questions/55456752/taking-user-input-from-html-form-as-a-variable-for-python-script
