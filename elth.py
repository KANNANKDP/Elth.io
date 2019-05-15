import json
import collections
with open('assignment_1_input_1.json') as json_data:
    file = json.load(json_data)
    questions = file['questions']
    userAnswer = []
    for question in questions:
    	stage = len(userAnswer)
    	print ("stage%s"%(stage))
    	ques = collections.OrderedDict(sorted(question.items()))
    	# question should appear first 
    	# normal dict arranges key based on key lenght
    	# that makes "var" appear first than "text"
    	for key in ques:
    		#print key
    		if key == 'instruction':
    			print (ques[key])
    		elif(key == 'text'):
    			print (ques[key])
    		elif(key == 'options'):
    			option = ques[key]
    		elif(key == 'conditions'):
    			if type(ques[key][0]) == list:
    				flag = "AND"
    				logic = ques[key][0]
    				string = logic[0].split(" ")
    				if string[1] == "==":
    					if string[2] == 'False':
    						varList = string[0].split(".")
    						if varList[0] == 'age' and varList[1] == "isDigit()":
    							if age.isDigit() == True:
    								continue
    								#do something
    				elif string[1] == "!=":
    					if string[2] == 'False':
    						if string[0] == False:
    							print ("not equals and False")
    						else:
    							print ("not equals and true")


    		elif(key == 'var'):
    			if ques[key] == 'first_name':
    				first_name = input()
    				#print "first name %s"%(first_name)
    				userAnswer.append(first_name)
    			elif ques[key] == 'last_name':
    				last_name = input()
    				#print "last name %s"%(last_name)
    				userAnswer.append(last_name)
    			elif ques[key] == 'gender':
    				genderResponse = input()
    				#print "gender %s"%(genderResponse)
    				userAnswer.append(genderResponse)
    			elif ques[key] == 'age':
    				age = input()
    				userAnswer.append(age)

    print (userAnswer)