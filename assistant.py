import json

#open the input file for the chatbot
input_file='test.json'
with open(input_file) as chatbot_input:
    chatbot_inputs = json.load(chatbot_input)


stage_no=0
final_res={}
userAnswer=[]
for key,value in chatbot_inputs.items():
    if(key=='questions'):
        for question in value:
            stage_no+=1
            stage='stage'+str(stage_no)
            final_res[stage]={}
            final_res[stage]['Bot Says:']=[]
            final_res[stage]['User Says:']=''
            keys=[]
            for key in question:
                keys.append(key)

            if('instruction' in keys):
                if('instruction_var' in keys):
                    ins_var=question['instruction_var'][0]
                    ins='print("'+str(question['instruction'])+'"%'+str(ins_var)+')'
                    exec(ins) 
                else:
                    print(question['instruction'])
                    

            elif('conditions' in keys):
                for condition in question['conditions']:
                    for cond in condition:
                        if eval(cond):
                            if('text' in keys):
                                print(question['text'])
                            if('var' in keys):
                                var_name=question['var']
                                if(var_name=='age'):
                                    age = input()
                continue
            elif('text' in keys):
                print(question['text'])
                if('options' in keys):
                    for option in question['options']:
                        print(option, end=" ")
                if('var' in keys):
                    if question['var'] == 'first_name':
                        first_name = input()
                    elif question['var'] == 'last_name':
                        last_name = input()
                        userAnswer.append(last_name)
                    elif question['var'] == 'gender':
                        genderResponse = input()
                        userAnswer.append(genderResponse)
                    elif question['var'] == 'age':
                        age = input()
                        userAnswer.append(age)
                    elif question['var']=='rows[0]':
                            numbers = list(map(int, input().split()))
                            rows[0].append(numbers)
                    elif question['var']=='rows[1]':
                            numbers = list(map(int, input().split()))
                            rows[1].append(numbers)
                    elif question['var']=='rows[2]':
                            numbers = list(map(int, input().split()))
                            rows[2].append(numbers)
                        

            elif('calculated_variable' in keys):
                if(question['calculated_variable']=='True'):
                    print('ok')
                    var_name=question['var']
                    formula=question['formula']
                    if(var_name=='full_name'):
                        full_name= eval(formula)
                        print(full_name)
                    elif(var_name=='rows'):
                        rows=[]
                        for i in range(0,3):
                            rows.append([])