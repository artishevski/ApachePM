class ViginereExtended:
    def __init__(self, code):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюяФБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ()!@#$%^&*?№;:-+-.,`~\'_'
        self.alphabet_length = len(self.alphabet)
        self.code = list(code)
        self.code_length = len(self.code)
        self.current_index = 0

    def encode(self, text):
        encrypted_text = ''
        for symb in text:
            symb_index = self.alphabet.find(symb)
            symb_index = (symb_index + int(self.code[self.current_index])) % self.alphabet_length
            encrypted_text += self.alphabet[symb_index]
            self.current_index = (self.current_index + 1) % self.code_length
        return encrypted_text.replace(' ', '_')

    def decode(self, text):
        decrypted_text = ''
        for symb in text:
            symb_index = self.alphabet.find(symb)
            symb_index = (symb_index + self.alphabet_length - int(self.code[self.current_index])) % self.alphabet_length
            decrypted_text += self.alphabet[symb_index]
            self.current_index = (self.current_index + 1) % self.code_length
        return decrypted_text.replace('_', ' ')
