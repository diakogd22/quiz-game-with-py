import time
from colorama import Fore, Style, init

init(autoreset=True)

def show_loading_animation():
    """Show loading animation"""
    print("Loading", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def calculate_rank(score, total_questions):
    """Calculate rank based on score"""
    percentage = (score / total_questions) * 100
    
    if percentage == 100:
        return {
            "rank": " Computer Master!",
            "emoji": "👑",
            "color": Fore.YELLOW,
            "message": "You're a genius! All answers were correct!"
        }
    elif percentage >= 80:
        return {
            "rank": " Excellent!",
            "emoji": "🌟",
            "color": Fore.GREEN,
            "message": "You're very good! Almost perfect!"
        }
    elif percentage >= 60:
        return {
            "rank": " Good!",
            "emoji": "👍",
            "color": Fore.CYAN,
            "message": "You have good knowledge, keep going!"
        }
    elif percentage >= 40:
        return {
            "rank": " Beginner",
            "emoji": "📝",
            "color": Fore.BLUE,
            "message": "You're learning, great job!"
        }
    elif percentage >= 20:
        return {
            "rank": " Newbie",
            "emoji": "🌱",
            "color": Fore.MAGENTA,
            "message": "You just started, need more practice!"
        }
    else:
        return {
            "rank": " Need serious practice!",
            "emoji": "💪",
            "color": Fore.RED,
            "message": "Don't worry! You'll succeed with more practice!"
        }

def ask_question_with_timer(question, correct_answer, time_limit=10):
    """Ask a question with a timer"""
    print(f"\n⏱️ You have {time_limit} seconds to answer!")
    print(question)
    print("Your answer: ", end="", flush=True)
    
    start_time = time.time()
    
    user_answer = input()
    time_taken = time.time() - start_time
    
    # Check if time is up
    if time_taken > time_limit:
        print(Fore.RED + f"⏰ Time's up! You took {time_taken:.1f}s" + Style.RESET_ALL)
    
    # Check if answer is correct
    is_correct = user_answer.lower() == correct_answer.lower()
    
    return is_correct, time_taken, user_answer

def show_score_with_animation(score, total_questions, rank_info):
    """Show score with animation"""
    print("\n" + "=" * 50)
    print(f"{rank_info['color']}📊 Final Result:{Style.RESET_ALL}")
    print("=" * 50)
    
    # Score counting animation
    print("Calculating score...", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")
    
    # Display score with graphics
    percentage = (score / total_questions) * 100
    bar_length = 20
    filled = int((score / total_questions) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    
    print(f"{rank_info['color']}{rank_info['emoji']} Your Rank: {rank_info['rank']}{Style.RESET_ALL}")
    print(f"{rank_info['color']}Score: {score}/{total_questions} ({percentage:.1f}%){Style.RESET_ALL}")
    print(f"{rank_info['color']}[{bar}] {percentage:.1f}%{Style.RESET_ALL}")
    print(f"\n💬 {rank_info['message']}")
    print("=" * 50)

def main():
    # Main variables
    score = 0
    total_questions = 7
    total_time_taken = 0
    
    # Start game
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
    print(Fore.YELLOW + "🎮 Welcome to the Computer Quiz Game! 🎮" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
    print()
    
    playing = input("Do you want to play? (yes/no): ")
    
    if playing.lower() == "yes":
        show_loading_animation()
        
        print(Fore.GREEN + "Game is starting!..." + Style.RESET_ALL)
        x = 3
        while x > 0:
            print(Fore.YELLOW + str(x) + Style.RESET_ALL)
            x -= 1
            time.sleep(1)
        print(Fore.GREEN + "Go! 🚀" + Style.RESET_ALL)
        print()
        
        # Question 1: CPU
        print(f"{Fore.CYAN}Question 1 of {total_questions}{Style.RESET_ALL}")
        is_correct, time_taken, user_answer = ask_question_with_timer(
            "What does CPU stand for?", 
            "central processing unit",
            time_limit=10
        )
        if is_correct:
            print(Fore.GREEN + f"✅ Correct! ({time_taken:.1f}s)" + Style.RESET_ALL)
            score += 1
        else:
            if user_answer:
                print(Fore.RED + f"❌ Incorrect! ({time_taken:.1f}s)" + Style.RESET_ALL)
            print("The correct answer is central processing unit")
        total_time_taken += time_taken
        
        print()
        print("-" * 30)
        
        # Question 2: GPU
        print(f"{Fore.CYAN}Question 2 of {total_questions}{Style.RESET_ALL}")
        is_correct, time_taken, user_answer = ask_question_with_timer(
            "What does GPU stand for?", 
            "graphical processing unit",
            time_limit=10
        )
        if is_correct:
            print(Fore.GREEN + f"✅ Correct! ({time_taken:.1f}s)" + Style.RESET_ALL)
            score += 1
        else:
            if user_answer:
                print(Fore.RED + f"❌ Incorrect! ({time_taken:.1f}s)" + Style.RESET_ALL)
            print("The correct answer is graphical processing unit")
        total_time_taken += time_taken
        
        print()
        print("-" * 30)
        
        # Question 3: RAM
        print(f"{Fore.CYAN}Question 3 of {total_questions}{Style.RESET_ALL}")
        is_correct, time_taken, user_answer = ask_question_with_timer(
            "What does RAM stand for?", 
            "random access memory",
            time_limit=10
        )
        if is_correct:
            print(Fore.GREEN + f"✅ Correct! ({time_taken:.1f}s)" + Style.RESET_ALL)
            score += 1
        else:
            if user_answer:
                print(Fore.RED + f"❌ Incorrect! ({time_taken:.1f}s)" + Style.RESET_ALL)
            print("The correct answer is random access memory")
        total_time_taken += time_taken
        
        print()
        print("-" * 30)
        
        # Question 4: PSU 
        print(f"{Fore.CYAN}Question 4 of {total_questions}{Style.RESET_ALL}")
        is_correct, time_taken, user_answer = ask_question_with_timer(
            "What does PSU stand for?", 
            "power supply unit",
            time_limit=10
        )
        if is_correct:
            print(Fore.GREEN + f"✅ Correct! ({time_taken:.1f}s)" + Style.RESET_ALL)
            score += 1
        else:
            if user_answer:
                print(Fore.RED + f"❌ Incorrect! ({time_taken:.1f}s)" + Style.RESET_ALL)
            print("The correct answer is power supply unit")
        total_time_taken += time_taken
        
        print()
        print("-" * 30)
        
        # Question 5: SSD 
        print(f"{Fore.CYAN}Question 5 of {total_questions}{Style.RESET_ALL}")
        is_correct, time_taken, user_answer = ask_question_with_timer(
            "What does SSD stand for?", 
            "solid state drive",
            time_limit=10
        )
        if is_correct:
            print(Fore.GREEN + f"✅ Correct! ({time_taken:.1f}s)" + Style.RESET_ALL)
            score += 1
        else:
            if user_answer:
                print(Fore.RED + f"❌ Incorrect! ({time_taken:.1f}s)" + Style.RESET_ALL)
            print("The correct answer is Solid State Drive")
        total_time_taken += time_taken
        
        print()
        print("-" * 30)
        
        # Question 6: HDD 
        print(f"{Fore.CYAN}Question 6 of {total_questions}{Style.RESET_ALL}")
        is_correct, time_taken, user_answer = ask_question_with_timer(
            "What does HDD stand for?", 
            "hard disk drive", 
            time_limit=10
        )
        if is_correct:
            print(Fore.GREEN + f"✅ Correct! ({time_taken:.1f}s)" + Style.RESET_ALL)
            score += 1
        else:
            if user_answer:
                print(Fore.RED + f"❌ Incorrect! ({time_taken:.1f}s)" + Style.RESET_ALL)
            print("The correct answer is Hard Disk Drive")
        total_time_taken += time_taken
        
        print()
        print("-" * 30)
        
        # Question 7: HTML (FIXED)
        print(f"{Fore.CYAN}Question 7 of {total_questions}{Style.RESET_ALL}")
        is_correct, time_taken, user_answer = ask_question_with_timer(
            "What does HTML stand for?", 
            "hypertext markup language",
            time_limit=10
        )
        if is_correct:
            print(Fore.GREEN + f"✅ Correct! ({time_taken:.1f}s)" + Style.RESET_ALL)
            score += 1
        else:
            if user_answer:
                print(Fore.RED + f"❌ Incorrect! ({time_taken:.1f}s)" + Style.RESET_ALL)
            print("The correct answer is Hypertext Markup Language")
        total_time_taken += time_taken
        
        print()
        print("-" * 30)
        
        # Calculate rank and show final result
        rank_info = calculate_rank(score, total_questions)
        show_score_with_animation(score, total_questions, rank_info)
        
        # Show question summary
        print("\n📝 Question Summary:")
        print(f"✅ Correct: {score}")
        print(f"❌ Incorrect: {total_questions - score}")
        print(f"⏱️ Total time taken: {total_time_taken:.1f} seconds")
        print(f"⏱️ Average time per question: {total_time_taken/total_questions:.1f} seconds")
        
        # Replay suggestion
        print("\n" + "=" * 50)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            print(Fore.CYAN + "\n🔄 Restarting game..." + Style.RESET_ALL)
            time.sleep(1)
            main()  # Restart the game
        else:
            print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
            
    elif playing.lower() == "no":
        print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
        quit()
    else:
        print(Fore.RED + "❌ Invalid input! Please enter yes or no." + Style.RESET_ALL)

# Run the program
if __name__ == "__main__":
    main()