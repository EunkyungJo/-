import re


class PhoneNumberValidator(object):
    PATTERN = r'^01[016789]\d{7,8}$'

    def get_pattern(self):
        return self.PATTERN

    def __call__(self, value):
        if re.match(self.get_pattern(), value) is None:
            print('유효성 검사 실패')


validator = PhoneNumberValidator()
validator('01029970828')


def phone_number_validator(value):
    PATTERN = r'^01[016789]\d{7,8}$'
    if re.match(PATTERN, value) is None:
        print('유효성 검사 실패')


phone_number_validator('01029970828')
