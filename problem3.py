# (c) Kristoff Getes and Angeline Peseral
# E. Slope of a Road

def main ():
    Rise = float(input("Enter the value of rise (m): "))
    Run = float(input("Enter the value of horizontal distance (m): "))
  
    
    S = (Rise/Run) * 100
    
    print(f"So, the slope of the road is {S} %. ")
    
if __name__ == "__main__":
 main()