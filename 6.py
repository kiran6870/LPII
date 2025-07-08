
def evaluate_employee():
    print("==Employee performance evaluation system==")
    name=input("enter the employee name:")
    punctuality=input("is the employee punctual(yes or no):").lower()
    project_complition=int(input("enter the no of project completed(out of 5):"))
    peer_feedback=input("enter the peer feedback(good/average/poor):").lower()
    manager_feedback=input("enter the managers feedback(good/average/poor):").lower()
    training_attended=int(input("no of taining a attended this year(out of 5):"))
    score=0

    # rule 1: regarding punctuality
    if(punctuality=='yes'):
        score+=2

    # rule 2: regarding project completion
    if(project_complition==5):
        score+=4
    elif(project_complition>=3):
        score+=2
    
    # rule 3: regarding the peer_feedback
    if(peer_feedback=='good'):
        score+=2
    elif(peer_feedback=='average'):
        score+=1

    # rule 4: regarding the manager_feedback
    if(manager_feedback=='good'):
        score+=2
    elif(manager_feedback=='average'):
        score+=1

    # rule 5: regarding the traning session attended
    if(training_attended>=3):
        score+=2
    elif(training_attended>=1):
        score+=1
    
    print(f"\n performance evaluation Report for{name}:")
    print(f"total score:{score}/13")

    if(score>=11):
        rating="Excellent"
    elif(score>=8):
        rating="Good"
    elif(score>=5):
        rating='Satisfactory'
    else:
        rating="Need Improvement"
    
    print(f"performance rating:{rating}")
evaluate_employee()