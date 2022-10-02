def valid_input(vaule, vaule_type):
    try:
        vaule = int(vaule)
        if vaule > 0:
            if vaule_type == "apartment_type" and vaule <= 3:
                return True
            elif vaule_type == "apartment_area" and 33 <= vaule <= 125:
                return True
            elif vaule_type == "floor" and 1 <= vaule <= 9:
                return True
            elif vaule_type == "first_payment" and 1 <= vaule <= 200000:
                return True
            elif vaule_type == "period" and 12 <= vaule <= 60:
                return True
    except:
        pass
    return False


def correct_input(input_messege, vaule_type):
    valid = False

    while not valid:
        answer = input(input_messege)
        valid = valid_input(answer, vaule_type)
    return int(answer)


answer_type = correct_input("Please, choice the apartment type, 1, 2, 3 rooms: ", "apartment_type")

type_rooms = [1, 2, 3]
floor_rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9]

type_1_room = [33, 40, 42, 44, 55, 56]
type_2_room = [52, 55, 66, 68, 75, 80]
type_3_room = [70, 82, 90, 97, 110, 125]

# Вартість за квадратний метер квартири: 1-кім - 1400, 2-кім - 1300, 3-кім - 1250
m2_1 = 1400
m2_2 = 1300
m2_3 = 1250

k_floor = {1: 0.9, 2: 0.9, 3: 0.9, 4: 1.1, 5: 1.1, 6: 1.1, 7: 1.15, 8: 1.15, 9: 1.20 }

if answer_type == 1:
    print(type_1_room)
    answer_m2 = correct_input("Please, choice apartment area: ", "apartment_area" )
    result_m2 = answer_m2 * m2_1
elif answer_type == 2:
    print(type_2_room)
    answer_m2 = correct_input("Please, choice apartment area: ", "apartment_area" )
    result_m2 = answer_m2 * m2_2
elif answer_type == 3:
    print(type_3_room)
    answer_m2 = correct_input("Please, choice apartment area: ", "apartment_area" )
    result_m2 = answer_m2 * m2_3

print(floor_rooms)
answer_floor = correct_input("Please, choice the floor of the apartment, 1 - 9 floor: ", "floor")

vaule = k_floor[answer_floor]
total_result = vaule * result_m2
first_payment = total_result * 0.3

first_payment = correct_input(f"Please enter the amount of the first installment, your payment cannot be less $ {first_payment} ", "first_payment" )

period_of_payment= correct_input("Please choose the payment schedule, specify the number of months ", "period")


loan_amount = total_result - first_payment
monthly_payment = (total_result - first_payment)/period_of_payment

for i in range(period_of_payment):
    one_pay = monthly_payment + loan_amount * 0.1/12
    loan_amount = loan_amount - monthly_payment
    print(i+1,  round(one_pay,2))


