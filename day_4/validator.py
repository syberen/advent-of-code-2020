import re


class PassportValidator():
    def __init__(self, file_path):
        self.hcl_re = re.compile('^#([0-9]|[a-f]){6}$')
        self.pid_re = re.compile('^[0-9]{9}$')

        self.passports = self._parse_passports(file_path)

    def _parse_passports(self, file_path):
        with open(file_path, 'r') as input:
            passport_chunks = input.read().split('\n\n')
            inline_chunk_strings = [chunk.replace(
                '\n', ' ') for chunk in passport_chunks]
            lines_with_separate_fields = [line.split(
                ' ') for line in inline_chunk_strings]

            all_passports = []

            for line in lines_with_separate_fields:
                passport = {}

                for field in line:
                    split_line = field.split(':')

                    passport[split_line[0]] = split_line[1]

                all_passports.append(passport)

            return all_passports

    def _keys_are_valid(self, passport):
        key_set = set(passport.keys())
        valid_passport_fields = {'byr', 'iyr',
                                 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

        return valid_passport_fields.issubset(key_set)

    def _validate_field(self, key, value):
        if key == 'byr':
            return 1920 <= int(value) <= 2002
        elif key == 'iyr':
            return 2010 <= int(value) <= 2020
        elif key == 'eyr':
            return 2020 <= int(value) <= 2030
        elif key == 'hgt':
            unit = value[-2:]
            height_value = value[:-2]

            if unit == 'cm':
                return 150 <= int(height_value) <= 193
            elif unit == 'in':
                return 59 <= int(height_value) <= 76
            else:
                return False
        elif key == 'hcl':

            return bool(re.match(self.hcl_re, value))
        elif key == 'ecl':
            valid_values = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

            return value in valid_values
        elif key == 'pid':

            return bool(re.match(self.pid_re, value))
        elif key == 'cid':
            return True

    def _passport_values_are_valid(self, passport):
        for key, value in passport.items():
            if self._validate_field(key, value) == False:
                return False

        return True

    def count_valid_passports_by_fields_present(self):
        valid_count = 0

        for passport in self.passports:
            if self._keys_are_valid(passport):
                valid_count += 1

        return valid_count

    def count_valid_passports_with_value_validation(self):
        valid_count = 0

        for passport in self.passports:
            if not self._keys_are_valid(passport):
                continue

            if self._passport_values_are_valid(passport) == True:
                valid_count += 1

        return valid_count
