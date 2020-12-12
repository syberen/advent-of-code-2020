from validator import PassportValidator

validator = PassportValidator('input.txt')

# Part 1 solution
print(validator.count_valid_passports_by_fields_present())

# Part 2 solution
print(validator.count_valid_passports_with_value_validation())
