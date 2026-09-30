def water_jug(jug1_cap, jug2_cap, terget):
    jug1 = 0
    jug2 = 0
    while(jug1 != terget and jug2 != terget):
        if jug1 == 0 :
            jug1 = jug1_cap
            print(f"Fill jug1 : ({jug1}, {jug2})")
        transfer = min(jug1, jug2_cap - jug2)
        jug1 -= transfer
        jug2 += transfer
        print(f"Pour jug1 --> jug2 : ({jug1}, {jug2})")
        if jug1 == terget or jug2 == terget :
            break
        if jug2 == jug2_cap :
            jug2 = 0
            print(f"Empty jug2 : ({jug1}, {jug2})")
    print("\n Goal Reached ! ")
    print(f"Final state : ({jug1}, {jug2})")
# water_jug(5,3,4) 
# water_jug(4,3,2)
jug1_capacity = int(input("Enter capacity of Jug 1: "))
jug2_capacity = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount of water: "))
if jug1_capacity == target:
    print(f"Final state : ({jug1_capacity}, {0})")
elif jug2_capacity == target :
    print(f"Final stage : ({0}, {jug2_capacity})")
else :
    water_jug(jug1_capacity, jug2_capacity, target)