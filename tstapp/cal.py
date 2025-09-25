def calculate_bmi(weight, height):
    height = height/100
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return("You are underweight.",bmi)
    elif 18.5 <= bmi < 24.9:
        return("You have a normal weight.",bmi)
    elif 25 <= bmi < 29.9:
        return("You are overweight.",bmi)
    else:
        return("You are obese.",bmi)
    
def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        # BMR formula for males
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        return bmr
    elif gender == 'female':
        # BMR formula for females
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return bmr

def calculate_calorie_intake(bmr, activity_level):
    # different activity levels
    calorie_intake = bmr * activity_level
    return (calorie_intake)

def calculate_ibw(height, gender):
    # Convert height from meters to inches (1 meter = 39.37 inches)
    height_in_inches = height * 39.37/100
    
    if gender == 'male':
        # Devine formula for males
        if height_in_inches > 60:
            ibw = 50 + 2.3 * (height_in_inches - 60)
        else:
            ibw = 50  # Default for height less than or equal to 60 inches
    elif gender == 'female':
        # Devine formula for females
        if height_in_inches > 60:
            ibw = 45.5 + 2.3 * (height_in_inches - 60)
        else:
            ibw = 45.5  # Default for height less than or equal to 60 inches
    
    return(ibw)

def calculate_water_intake(weight, activity_level):
    var = 0
    if activity_level=="Sedentary":
        # 35 mL of water per kg for sedentary individuals 
        var = 35
    
    if activity_level=="Active":
         # 40 mL of water per kg for active individuals 
         var = 40
    water_intake_ml = var * weight  
    
    # Convert water intake from mL to liters
    water_intake_liters = water_intake_ml / 1000
    return water_intake_liters    
