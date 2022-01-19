import math

while True:

    a = input("amaliat mored nazar ra vared kon:")
    e = float(input("lotfa add dovom ra vared kon:"))
    w = float(input("lotfa add aval ra vared kon:"))

    if a == "+":
        result = w + e

    if a == "-":
        result = w - e

    if a == "*":
        result = w * e

    if a == "/":
        if a != 0 :
            result = w / e
        else:
            result = ("can not divide by zero!!")
    
    if a == "quit":
        break

    print(result)
