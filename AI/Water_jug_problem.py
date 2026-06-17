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
water_jug(5,3,4) 