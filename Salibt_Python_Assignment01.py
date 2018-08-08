# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 13:34:32 2018

@author: salibt
"""


######################get number of Moves################################
#########################################################################  
def nb_of_move() :
    """ Function to read number of move, function accept positive integer only and return positive integer  """
    while True:
        try:
            n_move = input("enter number of move: ")
            n_move = int(n_move)
            if n_move > 0:
                break
        except ValueError:
            print ("Something went wrong, would you please enter a positive integer number ")
        except KeyboardInterrupt:
            print("User Exit")
            n_move = "q"
            break
    
    
    return n_move            
#########################################################################
#########################################################################            

#########################Read Game Level and Next move ##################
######################################################################### 
# Create a function to read player input
def player_input(mylist,msg) :
    """ Function to capture player move , Accept only 0, or 1 or q to exit , return 0, or  1 or q  """
    #mylist = ("0","1","q")
    #msg=varstr
    list1=mylist
    while True:
        try:
           
            p_input = input(msg)
            if str(p_input) in list1:
                break
        except ValueError:
            print ("Something went wrong, would you please enter a binary number ")
        except KeyboardInterrupt:
            print("User Exit")
            p_input = "q"
            break
       
    return p_input
#########################################################################
######################################################################### 




######################### PRINT SCORE for every iteration ###############
#########################################################################
def print_score (c_move,p_move) :
    """ Function to calculate computer bet, print result and return computer bet  """  
    global glb_comp_res
    global glb_player_res
    
    if c_move == 0 :
   
        if p_move == 0 :
            print("player = " + str(p_move) + " machine = " + str(c_move) + " – Computer wins!")
            glb_comp_res= glb_comp_res + 1 
        else  :
            print("player = " + str(p_move) + " machine = " + str(c_move) + " – Player wins!")
            glb_player_res= glb_player_res + 1
        
    elif c_move == 1 :
        
        if p_move == 1 :
            print("player = " + str(p_move) + " machine = " + str(c_move) + " – Computer wins!")
            glb_comp_res= glb_comp_res + 1 
        else  :
            print("player = " + str(p_move) + " machine = " + str(c_move) + " – Player wins!")
            glb_player_res= glb_player_res + 1 
    else :
        pass
    
    p_msg=''
    p_msg='*' * glb_player_res
    p_msg='PLAYER: ' + p_msg
    c_msg=''
    c_msg='*' * glb_comp_res
    c_msg='COMPUTER: ' + c_msg
    print(p_msg)
    print(c_msg)
    print("---")
    
    
             

#########################################################################
######################################################################### 

######################### Print Final Score #############################
#########################################################################
def print_final (l_msg,g_p_res,g_c_res):
    """ Print Final Score for one game, input level message, player win count and computer win count, return nothing """
    l_msg = l_msg +  "player " + str(g_p_res) + " - " + str(g_c_res) + " computer - "
    if g_p_res > g_c_res :
        l_msg = l_msg + "You Won!"
    elif g_p_res == g_c_res :
        l_msg = l_msg + "TIE!!"  
    else:
        l_msg = l_msg + "You Lost!"
    print(l_msg)

#########################################################################
######################################################################### 
    
    
    
######################### DIFF LEVEL ####################################
#########################################################################
def diff_level (p_list,c_move) :
    pre_move = p_list[-1]
    
    if pre_move == 0 :
        throw00 = p_list.count(0)
        throw10 = p_list.count(1)
         #sum(1 for i in range(len(user_list)) if user_list[i:i+2]==[0,0])
        
        if throw10 > throw00 :
            comp = 1
        elif throw10 < throw00:
            comp = 0
        else :
            comp=c_move
            
    else :
        throw01 = p_list.count(0)
        throw11 = p_list.count(1)
        if throw11 > throw01 :
            comp = 1
        elif throw11 < throw01:
            comp = 0
        else :
             comp=c_move
    
    return comp 

#########################################################################
#########################################################################



###########################MAIN PROGRAM START HERE ######################
######################################################################### 

# Import Packages and files section
import lnr_cong as cme

# Import Packages
import ie_mbdbl2018_salibt as lc
#import matplotlib.pyplot as plt
#import numpy as np


""" Variable Declaration section """
#Declare Input List
move_list = ("0","1")
level_list = ("1","2")
x0 = 123 #seed Value
## Print Welcome Message
print ("Welcome to Human Behavior Prediction by Tarek Saliba")

## Start Infinite Loop
while True :
    #Initialize Varialble for every round
    #x0 = 123 #seed Value
    
    #Global Variable that count player and computer Wins
    glb_player_res=0
    glb_comp_res=0
    
    result =-1
    inc=1
    
    player_move = ""
    level_msg =""
    #initialize list used to store user and computer result
    player_response= []
    comp_response = []

    #Print message for user to chose level
    level_msg = "Choose the type of game (1: Easy; 2: Difficult):"
    level=player_input(level_list,level_msg)
    #Exit program f user kill the program
    if level == "q" :
        exit()
    
    #Print message for user to chose number of rounds
    nb_move = nb_of_move()
    #Exit program f user kill the program
    if nb_move == "q" :
        exit()
    
    level = int(level)
    print("---")
    
    
    #Start Game
    while player_move != "q" and inc <= nb_move:
        #Print Message for user to select his bet
        move_msg = "Choose your move number " + str(inc) + " (0 or 1)"    
        player_move=player_input(move_list,move_msg)
        
        #Calculate Linear Congruence value
        x0,comp_move=lc.linear_congruence_random_generator(x0)
        #Exit Program if user kill the program, and print result for this game
        if player_move == "q" :
            player_move = -1
            comp_move = -1
            print_score(comp_move,player_move)
            exit()
        #check winner based on game level
        else :
            player_move = int(player_move)
            #easy level
            if level == 1 :
                print_score(comp_move,player_move)
            #Difficult level
            else :
                 
                if inc == 1 :
                    print_score(comp_move,player_move)
                else:
                    comp_move = diff_level(player_response,comp_move)            
                    print_score (comp_move,player_move)
                
           
            player_response.extend([player_move])
            comp_response.extend([comp_move]) 
    
        inc = inc + 1
    #Print Game result
    if level == 1  :
        level1_msg = "Easy game is over, final score: " 
        print_final(level1_msg,glb_player_res,glb_comp_res)
    else:
        level2_msg = "Difficult game is over, final score: " 
        print_final(level2_msg,glb_player_res,glb_comp_res)




##result_graph1 = ["Player","Machine"]
##result_graph2 = [glb_player_res,glb_comp_res]
##y_pos = np.arange((len(result_graph1)))
##plt.bar(y_pos ,result_graph2 , align='center', alpha=0.5,color=['b','g'])
##plt.xticks(y_pos, result_graph1)
##plt.ylabel('Score')
##plt.title('')
##plt.show()




  
    
    
    
    