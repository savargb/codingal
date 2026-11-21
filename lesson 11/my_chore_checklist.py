#Step 1: Set total_chores to 4, store it as original_count, and print how many chores are on today's list.

total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today. \n")

#Step 2: Set up a completed_count counter starting at 0 and a chore_num counter starting at 1.

completed_count = 0
chore_num = 1


#Step 3: Start a while loop that keeps running as long as chore_num is less than or equal to total_chores.

while chore_num <= total_chores:

#Step 4: Inside the loop, work out the current chore's name from chore_num, then ask if it has been finished.

    if chore_num == 1: 
        next_chore = "Make your bed"
    
    elif chore_num == 2: 
        next_chore = "Feed the pet"
    
    elif chore_num == 3: 
        next_chore = "Take out the trash"
            
    else: 
        next_chore = "Wash the dishes"
            
    answer = input(f"Have you finished: {next_chore}? (yes/no): ").lower
    
#Step 5: If the answer is yes, increase completed_count and chore_num by 1; otherwise, print a message and let the loop ask about the same chore again.

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed. ")
    else:
        print("Okay. Finish it and check again!")

#Step 6: Once the while loop ends, print the completion message, then safely demonstrate an infinite loop's condition, using a break to stop it after 3 rounds.

    print("Chores remaining:",  total_chores - completed_count)
    print()
#Step 7: Print the final chore checklist summary showing chores assigned, completed, and remaining.

print("==========ALL CHORES COMPLETED!===============")
print("Great Job finishing all your chores!")