def water_jug(jug1_cap, jug2_cap, target) :
    jug1 = 0
    jug2 = 0
    while jug1 != target and jug2 != target :
        if jug1 == 0 :
            jug1 = jug1_cap
            print(f"Fill jug1 : ({jug1}, {jug2})")
        transfer = min(jug1, jug2_cap - jug2)
        jug1 -= transfer
        jug2 += transfer
        print(f"Pour jug1 --> jug2 : ({jug1}, {jug2})")
        if jug1 == target or jug2 == target :
            break
        if jug2 == jug2_cap :
            jug2 = 0
            print(f"Empty jug2 : ({jug1}, {jug2})")
    print("\n Goal reached !")
    print(f"Final stage : ({jug1}, {jug2})")
jug1_capacity = int(input("Enter capacity of jug1 : "))
jug2_capacity = int(input("Enter capacity of jug2 : "))
target = int(input("Enter target amount of water : "))
water_jug(jug1_capacity, jug2_capacity, target)