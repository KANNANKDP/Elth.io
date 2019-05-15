import json
import sys

def chat_bot(file_json):
    #open the input file for the chatbot
    input_file=file_json
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
                    final_res[stage]={}
                    final_res[stage]['Bot Says:']=[]
                else:
                    stage='stage'+str(stage_no)
                keys=[]
                for key in question:
                    keys.append(key)
    
                if('instruction' in keys):
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
                        final_res[stage]['Bot Says:'].append(response)
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
                                        final_res[stage]['User Says']=age
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
                    final_res[stage]['Bot Says:'].append(response)
                    
                    if('var' in keys):
                        if question['var'] == 'first_name':
                            first_name = input()
                            final_res[stage]['User Says']=first_name
                            stage_no+=1
                        elif question['var'] == 'last_name':
                            last_name = input()
                            userAnswer.append(last_name)
                            final_res[stage]['User Says']=last_name
                            stage_no+=1
                        elif question['var'] == 'gender':
                            gender = input()
                            userAnswer.append(gender)
                            final_res[stage]['User Says']=gender
                            stage_no+=1
                        elif question['var'] == 'age':
                            age = input()
                            userAnswer.append(age)
                            final_res[stage]['User Says']=age
                            stage_no+=1
                            
                            
    print(final_res)
    with open('my_assignment_1_response_series_1.json','w') as res:
        json.dump(final_res,res)


if __name__== "__main__":
    fileName=sys.argv[1]
    chat_bot(fileName)
    