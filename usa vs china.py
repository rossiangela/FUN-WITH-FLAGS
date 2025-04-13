import os
import time
import random
import sys
from threading import Thread

# Clear terminal function (works on Windows, macOS, and Linux)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art for the flags
USA_FLAG = [
    "┌───────────────┐",
    "│* * * * * * * │────────────┐",
    "│ * * * * * * *│            │",
    "│* * * * * * * │            │",
    "│ * * * * * * *│            │",
    "│───────────────────────────│",
    "│                           │",
    "│───────────────────────────│",
    "│                           │",
    "│───────────────────────────│",
    "│                           │",
    "└───────────────────────────┘"
]

CHINA_FLAG = [
    "┌───────────────────────────┐",
    "│                           │",
    "│    *                      │",
    "│  *   *   *                │",
    "│    *                      │",
    "│      *                    │",
    "│                           │",
    "│                           │",
    "│                           │",
    "│                           │",
    "│                           │",
    "└───────────────────────────┘"
]

# ASCII art for boxing gloves
LEFT_GLOVE = " (@@)"
RIGHT_GLOVE = "(@@) "

# Health and score tracking
usa_health = 100
china_health = 100
round_num = 1
usa_score = 0
china_score = 0

# Animation frames for punches
def usa_punch_animation():
    global china_health
    
    frames = []
    # Initial position
    for i in range(5):
        frame = []
        frame.append("╔═════════════════════════════════════════════════════════════╗")
        frame.append("║                       BOXING RING                           ║")
        frame.append("╟─────────────────────────────────────────────────────────────╢")
        
        # Health bars
        health_bar = f"║  USA {usa_health:3d}/100 [{'█' * (usa_health // 5)}{' ' * (20 - usa_health // 5)}]"
        health_bar += f" │ CHINA {china_health:3d}/100 [{'█' * (china_health // 5)}{' ' * (20 - china_health // 5)}]  ║"
        frame.append(health_bar)
        
        frame.append("║                                                             ║")
        for j in range(len(USA_FLAG)):
            if j < len(USA_FLAG) and j < len(CHINA_FLAG):
                # Add spacing based on frame number to show punch movement
                spacing = " " * (30 - i * 4) 
                line = f"║  {USA_FLAG[j]}{spacing}{CHINA_FLAG[j]}  ║"
                frame.append(line)
        
        frame.append("║                                                             ║")
        frame.append(f"║                      ROUND {round_num:2d}                             ║")
        frame.append("╚═════════════════════════════════════════════════════════════╝")
        frames.append(frame)
    
    # Punch frames
    for i in range(4):
        frame = []
        frame.append("╔═════════════════════════════════════════════════════════════╗")
        frame.append("║                       BOXING RING                           ║")
        frame.append("╟─────────────────────────────────────────────────────────────╢")
        
        health_bar = f"║  USA {usa_health:3d}/100 [{'█' * (usa_health // 5)}{' ' * (20 - usa_health // 5)}]"
        health_bar += f" │ CHINA {china_health:3d}/100 [{'█' * (china_health // 5)}{' ' * (20 - china_health // 5)}]  ║"
        frame.append(health_bar)
        
        frame.append("║                                                             ║")
        for j in range(len(USA_FLAG)):
            if j < len(USA_FLAG) and j < len(CHINA_FLAG):
                if j == 5:  # Position for the glove
                    spacing = " " * (25 - i * 6)
                    line = f"║  {USA_FLAG[j]}{RIGHT_GLOVE}{spacing}{CHINA_FLAG[j]}  ║"
                else:
                    spacing = " " * (30 - i * 4)
                    line = f"║  {USA_FLAG[j]}{spacing}{CHINA_FLAG[j]}  ║"
                frame.append(line)
        
        frame.append("║                                                             ║")
        frame.append(f"║                      ROUND {round_num:2d}                             ║")
        frame.append("╚═════════════════════════════════════════════════════════════╝")
        frames.append(frame)
    
    # Hit frame
    frame = []
    frame.append("╔═════════════════════════════════════════════════════════════╗")
    frame.append("║                       BOXING RING                           ║")
    frame.append("╟─────────────────────────────────────────────────────────────╢")
    
    # Reduce China's health
    damage = random.randint(5, 15)
    china_health -= damage
    if china_health < 0:
        china_health = 0
    
    health_bar = f"║  USA {usa_health:3d}/100 [{'█' * (usa_health // 5)}{' ' * (20 - usa_health // 5)}]"
    health_bar += f" │ CHINA {china_health:3d}/100 [{'█' * (china_health // 5)}{' ' * (20 - china_health // 5)}]  ║"
    frame.append(health_bar)
    
    frame.append("║                                                             ║")
    for j in range(len(USA_FLAG)):
        if j < len(USA_FLAG) and j < len(CHINA_FLAG):
            if j == 5:  # Position for the glove at impact
                line = f"║  {USA_FLAG[j]}{RIGHT_GLOVE}POW!{CHINA_FLAG[j]}  ║"
            else:
                line = f"║  {USA_FLAG[j]}     {CHINA_FLAG[j]}  ║"
            frame.append(line)
    
    frame.append("║                                                             ║")
    frame.append(f"║                      ROUND {round_num:2d}                             ║")
    frame.append("╚═════════════════════════════════════════════════════════════╝")
    frames.append(frame)
    
    # Reset frames
    for i in range(3):
        frame = []
        frame.append("╔═════════════════════════════════════════════════════════════╗")
        frame.append("║                       BOXING RING                           ║")
        frame.append("╟─────────────────────────────────────────────────────────────╢")
        
        health_bar = f"║  USA {usa_health:3d}/100 [{'█' * (usa_health // 5)}{' ' * (20 - usa_health // 5)}]"
        health_bar += f" │ CHINA {china_health:3d}/100 [{'█' * (china_health // 5)}{' ' * (20 - china_health // 5)}]  ║"
        frame.append(health_bar)
        
        frame.append("║                                                             ║")
        for j in range(len(USA_FLAG)):
            if j < len(USA_FLAG) and j < len(CHINA_FLAG):
                spacing = " " * 10
                line = f"║  {USA_FLAG[j]}{spacing}{CHINA_FLAG[j]}  ║"
                frame.append(line)
        
        frame.append("║                                                             ║")
        frame.append(f"║                      ROUND {round_num:2d}                             ║")
        frame.append("╚═════════════════════════════════════════════════════════════╝")
        frames.append(frame)
    
    return frames

def china_punch_animation():
    global usa_health
    
    frames = []
    # Initial position
    for i in range(5):
        frame = []
        frame.append("╔═════════════════════════════════════════════════════════════╗")
        frame.append("║                       BOXING RING                           ║")
        frame.append("╟─────────────────────────────────────────────────────────────╢")
        
        health_bar = f"║  USA {usa_health:3d}/100 [{'█' * (usa_health // 5)}{' ' * (20 - usa_health // 5)}]"
        health_bar += f" │ CHINA {china_health:3d}/100 [{'█' * (china_health // 5)}{' ' * (20 - china_health // 5)}]  ║"
        frame.append(health_bar)
        
        frame.append("║                                                             ║")
        for j in range(len(USA_FLAG)):
            if j < len(USA_FLAG) and j < len(CHINA_FLAG):
                # Add spacing based on frame number to show punch movement
                spacing = " " * (10 + i * 2)
                line = f"║  {USA_FLAG[j]}{spacing}{CHINA_FLAG[j]}  ║"
                frame.append(line)
        
        frame.append("║                                                             ║")
        frame.append(f"║                      ROUND {round_num:2d}                             ║")
        frame.append("╚═════════════════════════════════════════════════════════════╝")
        frames.append(frame)
    
    # Punch frames
    for i in range(4):
        frame = []
        frame.append("╔═════════════════════════════════════════════════════════════╗")
        frame.append("║                       BOXING RING                           ║")
        frame.append("╟─────────────────────────────────────────────────────────────╢")
        
        health_bar = f"║  USA {usa_health:3d}/100 [{'█' * (usa_health // 5)}{' ' * (20 - usa_health // 5)}]"
        health_bar += f" │ CHINA {china_health:3d}/100 [{'█' * (china_health // 5)}{' ' * (20 - china_health // 5)}]  ║"
        frame.append(health_bar)
        
        frame.append("║                                                             ║")
        for j in range(len(USA_FLAG)):
            if j < len(USA_FLAG) and j < len(CHINA_FLAG):
                if j == 5:  # Position for the glove
                    spacing = " " * (15 - i * 3)
                    line = f"║  {USA_FLAG[j]}{spacing}{LEFT_GLOVE}{CHINA_FLAG[j]}  ║"
                else:
                    spacing = " " * (20 - i * 2)
                    line = f"║  {USA_FLAG[j]}{spacing}{CHINA_FLAG[j]}  ║"
                frame.append(line)
        
        frame.append("║                                                             ║")
        frame.append(f"║                      ROUND {round_num:2d}                             ║")
        frame.append("╚═════════════════════════════════════════════════════════════╝")
        frames.append(frame)
    
    # Hit frame
    frame = []
    frame.append("╔═════════════════════════════════════════════════════════════╗")
    frame.append("║                       BOXING RING                           ║")
    frame.append("╟─────────────────────────────────────────────────────────────╢")
    
    # Reduce USA's health
    damage = random.randint(5, 15)
    usa_health -= damage
    if usa_health < 0:
        usa_health = 0
    
    health_bar = f"║  USA {usa_health:3d}/100 [{'█' * (usa_health // 5)}{' ' * (20 - usa_health // 5)}]"
    health_bar += f" │ CHINA {china_health:3d}/100 [{'█' * (china_health // 5)}{' ' * (20 - china_health // 5)}]  ║"
    frame.append(health_bar)
    
    frame.append("║                                                             ║")
    for j in range(len(USA_FLAG)):
        if j < len(USA_FLAG) and j < len(CHINA_FLAG):
            if j == 5:  # Position for the glove at impact
                line = f"║  {USA_FLAG[j]}POW!{LEFT_GLOVE}{CHINA_FLAG[j]}  ║"
            else:
                line = f"║  {USA_FLAG[j]}     {CHINA_FLAG[j]}  ║"
            frame.append(line)
    
    frame.append("║                                                             ║")
    frame.append(f"║                      ROUND {round_num:2d}                             ║")
    frame.append("╚═════════════════════════════════════════════════════════════╝")
    frames.append(frame)
    
    # Reset frames
    for i in range(3):
        frame = []
        frame.append("╔═════════════════════════════════════════════════════════════╗")
        frame.append("║                       BOXING RING                           ║")
        frame.append("╟─────────────────────────────────────────────────────────────╢")
        
        health_bar = f"║  USA {usa_health:3d}/100 [{'█' * (usa_health // 5)}{' ' * (20 - usa_health // 5)}]"
        health_bar += f" │ CHINA {china_health:3d}/100 [{'█' * (china_health // 5)}{' * ' * (20 - china_health // 5)}]  ║"
        frame.append(health_bar)
        
        frame.append("║                                                             ║")
        for j in range(len(USA_FLAG)):
            if j < len(USA_FLAG) and j < len(CHINA_FLAG):
                spacing = " " * 10
                line = f"║  {USA_FLAG[j]}{spacing}{CHINA_FLAG[j]}  ║"
                frame.append(line)
        
        frame.append("║                                                             ║")
        frame.append(f"║                      ROUND {round_num:2d}                             ║")
        frame.append("╚═════════════════════════════════════════════════════════════╝")
        frames.append(frame)
    
    return frames

def show_animation(frames):
    for frame in frames:
        clear_terminal()
        for line in frame:
            print(line)
        time.sleep(0.2)

def check_round_end():
    global usa_health, china_health, round_num, usa_score, china_score
    
    if usa_health <= 0 or china_health <= 0:
        # Determine winner
        if usa_health > china_health:
            winner = "USA"
            usa_score += 1
        elif china_health > usa_health:
            winner = "CHINA"
            china_score += 1
        else:
            winner = "DRAW"
        
        # Display round result
        clear_terminal()
        print("╔═════════════════════════════════════════════════════════════╗")
        print("║                       BOXING RING                           ║")
        print("╟─────────────────────────────────────────────────────────────╢")
        print(f"║  USA {usa_health:3d}/100 [{'█' * (usa_health // 5)}{' ' * (20 - usa_health // 5)}]"
              f" │ CHINA {china_health:3d}/100 [{'█' * (china_health // 5)}{' ' * (20 - china_health // 5)}]  ║")
        print("║                                                             ║")
        print(f"║                   {winner} WINS ROUND {round_num}!                     ║")
        print("║                                                             ║")
        print(f"║              SCORE: USA {usa_score} - {china_score} CHINA                      ║")
        print("║                                                             ║")
        print("╚═════════════════════════════════════════════════════════════╝")
        time.sleep(3)
        
        # Start new round
        round_num += 1
        usa_health = 100
        china_health = 100
        return True
    return False

def handle_user_input():
    global running
    while running:
        try:
            key = input()
            if key.lower() == 'q':
                running = False
                print("\nExiting game... Press Enter to continue")
                break
        except:
            pass

def main():
    global running, usa_health, china_health, round_num, usa_score, china_score
    
    # Welcome screen
    clear_terminal()
    print("╔═════════════════════════════════════════════════════════════╗")
    print("║                                                             ║")
    print("║             USA vs CHINA FLAG BOXING MATCH                  ║")
    print("║                                                             ║")
    print("║             Press Enter to start the match                  ║")
    print("║             Press 'q' at any time to quit                   ║")
    print("║                                                             ║")
    print("╚═════════════════════════════════════════════════════════════╝")
    input()
    
    # Start input thread
    global running
    running = True
    input_thread = Thread(target=handle_user_input)
    input_thread.daemon = True
    input_thread.start()
    
    # Main game loop
    while running and round_num <= 5:  # 5 rounds total
        # Alternating attacks
        if random.random() > 0.5:
            # USA attacks first
            show_animation(usa_punch_animation())
            if check_round_end():
                continue
            time.sleep(random.uniform(0.5, 1.5))
            show_animation(china_punch_animation())
            check_round_end()
        else:
            # China attacks first
            show_animation(china_punch_animation())
            if check_round_end():
                continue
            time.sleep(random.uniform(0.5, 1.5))
            show_animation(usa_punch_animation())
            check_round_end()
        
        time.sleep(random.uniform(0.5, 1.5))
    
    # Final results
    clear_terminal()
    print("╔═════════════════════════════════════════════════════════════╗")
    print("║                                                             ║")
    print("║                    MATCH COMPLETE!                          ║")
    print("║                                                             ║")
    if usa_score > china_score:
        print("║                     USA WINS!                               ║")
    elif china_score > usa_score:
        print("║                     CHINA WINS!                             ║")
    else:
        print("║                       DRAW!                                 ║")
    print("║                                                             ║")
    print(f"║              FINAL SCORE: USA {usa_score} - {china_score} CHINA                  ║")
    print("║                                                             ║")
    print("║               Press Enter to exit                           ║")
    print("╚═════════════════════════════════════════════════════════════╝")
    
    running = False
    input_thread.join(timeout=0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_terminal()
        print("Game terminated.")
        sys.exit(0)