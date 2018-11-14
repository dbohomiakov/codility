def solution(A, B):
    fishes = zip(A, B)
    
    fish_stack = []
    fish_alive = 0
    
    for fish in fishes:
        size, direct = fish
        add_fish_stack = True

        while fish_alive:
            last_size, last_direct = fish_stack[-1]
            
            if last_direct == 1 and direct == 0:
                if size > last_size:
                    fish_stack.pop()
                    fish_alive -= 1
                    continue

                add_fish_stack = False
            break

        if add_fish_stack:
            fish_stack.append(fish)
            fish_alive += 1

    return fish_alive

