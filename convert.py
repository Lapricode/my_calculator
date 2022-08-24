import math as m

#cartesian to polar
def catop():
    IN = complex(input(": ")) #input format: "x+yj"
    x = IN.real
    y = IN.imag

    A = m.sqrt(x**2 + y**2)
    θ = m.atan2(y, x)
    print (IN, f"= {round(A,3)}∠{round(m.degrees(θ),3)}°")

#polar to cartesian
def potoc():
    IN = input(": ") #input format: "A/θ"
    I = IN.split("/")
    A = float(I[0])
    θ = m.radians(float(I[1]))

    x = A*m.cos(θ)
    y = A*m.sin(θ)
    if y >= 0:
        print(IN, f" = {round(x,3)}+{round(y,3)}j")
    else:
        print(IN, f" = {round(x,3)}{round(y,3)}j")