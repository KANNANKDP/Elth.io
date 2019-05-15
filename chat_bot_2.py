import json
import sys
from io import StringIO 

if __name__== "__main__":
    fileName=sys.argv[1]
    input_file=fileName
    print(input_file)
    with open(input_file) as chatbot_input:
        chatbot_inputs = json.load(chatbot_input)

    stage_nos=[]
    stage_no=1
    final_res={}
    userAnswer=[]
    for key,value in chatbot_inputs.items():
        if(key=='questions'):
            for question in value:
                if(stage_no not in stage_nos):
                    stage='stage'+str(stage_no)
                    stage_nos.append(stage_no)
                    final_res[stage]=[]
                else:
                    stage='stage'+str(stage_no)
                keys=[]
                for key in question:
                    keys.append(key)

                if('instruction' in keys and 'list_length' not in keys):
                    if('instruction_var' in keys):
                        ins_var=question['instruction_var'][0]
                        ins='print("'+str(question['instruction'])+'"%'+str(ins_var)+')'
                        exec(ins) 
                    else:
                        response={
                            'message':{
                                'text':question['instruction']       
                            }        
                        }
                        final_res[stage].append(response)
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
                                        stage_no+=1
                    continue
                elif('text' in keys):
                    print(question['text'])
                    response={
                        'message':{
                            'text':question['text']       
                        }
                    }
                    if('options' in keys):
                        response['message']["quick_replies"]=[]
                        for option in question['options']:
                            print(option, end=" ")
                            response['message']["quick_replies"].append(
                                {
                                "content_type": 'text',
                                "title": option,
                                "payload": option.lower()
                                }
                            )
                    final_res[stage].append(response)
                    
                    if('var' in keys):
                        if question['var'] == 'first_name':
                            first_name = input()
                            stage_no+=1
                        elif question['var'] == 'last_name':
                            last_name = input()
                            userAnswer.append(last_name)
                            stage_no+=1
                        elif question['var'] == 'gender':
                            gender = input()
                            userAnswer.append(gender)
                            stage_no+=1
                        elif question['var'] == 'age':
                            age = input()
                            userAnswer.append(age)
                            stage_no+=1
                        elif question['var']=='rows[0]':
                                numbers = input()
                                rows.append(numbers)
                                stage_no+=1
                        elif question['var']=='rows[1]':
                                numbers = input()
                                rows.append(numbers)
                                stage_no+=1
                        elif question['var']=='rows[2]':
                                numbers = input()
                                rows.append(numbers)
                                stage_no+=1
                            

                elif('calculated_variable' in keys):
                    if(question['calculated_variable']=='True'):
                        var_name=question['var']
                        formula=question['formula']
                        if(var_name=='full_name'):
                            full_name= eval(formula)
                            print(full_name)
                        elif(var_name=='rows'):
                            rows=[]
                        elif(var_name=='matrix'):
                            matrix=eval(formula)
                        elif(var_name=='t_matrix'):
                            t_matrix=eval(formula)
                            
                elif('list_var' in keys):
                    list_length=int(question['list_length'])
                    for i in range(0,list_length):
                        old_stdout = sys.stdout
                        result = StringIO()
                        sys.stdout = result
                        ins_var1=question['instruction_var'][0]
                        ins_var2=question['instruction_var'][1]
                        ins='print("'+str(question['instruction'])+'"%(('+str(ins_var1)+'),'+str(ins_var2)+')'+')'
                        exec(ins)
                        result_string = result.getvalue()
                        sys.stdout = old_stdout
                        res=result_string.split('\n')[0]
                        response={
                            'message':{
                                'text':res
                            }        
                        }
                        final_res[stage].append(response)
                        
                            
    print(final_res)
    with open('my_assignment_1_response_series_2.json','w') as res:
        json.dump(final_res,res)