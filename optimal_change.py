# Write your solution here!
def optimal_change(item_cost, amount_paid):
  
    if type(item_cost) == str or type(amount_paid) == str:
        return ('invalid input')
    if item_cost > amount_paid:
        return 'You did not pay enough for the Item!'
    if item_cost < 0 or amount_paid < 0:
        return 'Invalid Input'
    list_of_bills = []
    return_change_counter = {}
    change_dictionary = {
        '$100 bill' : 10000,
        '$50 bill' : 5000,
        '$20 bill' : 2000,
        '$10 bill' : 1000,
        '$5 bill' : 500,
        '$1 bill' : 100,
        'quarter' : 25,
        'dime' : 10,
        'nickel' : 5,
        'penny' : 1
    }
    total_change = amount_paid - item_cost
    total_change_to_pennies = round(float(total_change * 100))
    for denomination in change_dictionary:
        while total_change_to_pennies >= change_dictionary[denomination]:
            list_of_bills.append(denomination)
            total_change_to_pennies = total_change_to_pennies - change_dictionary[denomination]
            if total_change_to_pennies == 0:
                break 
    if len(list_of_bills) == 0:
       return f'The optimal change for an item that costs {item_cost} with an amount paid of {amount_paid} is no change is required.'        
    for bill in list_of_bills:
        return_change_counter[bill] = 0
    for bill in list_of_bills:
        return_change_counter[bill] += 1
    retured_change_string = ''
    the_key = ''
    for bill_type in return_change_counter:
        the_key = bill_type
        if return_change_counter[bill_type] != 1:
            the_key = the_key + 's'
        if the_key == 'pennys':
            the_key = 'pennies'  
        retured_change_string += (f'{return_change_counter[bill_type]} {the_key}'+ ', ')
    corrected_string = retured_change_string[:-2]
    correct_change = (f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is {corrected_string}.")
    reversed_string = correct_change[::-1].replace(",", 'dna ,', 1)
    correct_change =reversed_string[::-1]
    return correct_change

