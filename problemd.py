# (c) Kristoff Getes and Angeline Peseral
# D. Load Distribution on a Beam

def main ():
    w = float(input("Enter the value of uniform load (N/m): "))
    L = float(input("Enter the value of length (m): "))
  
    
    F = w * L
    
    print(f"So, the total load acting on the beam is {F} N. ")
    
if __name__ == "__main__":
 main()