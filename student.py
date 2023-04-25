class student:
    #phương thức của đối tượng
    def __init__(self, name, age, gender, res):
        self.name = name
        self.age = age
        self.gender = gender
        self.residence = res
        print('Đối tượng đã khởi tạo thành công')
    def run(self):
        print('student can run')
    def info(self):
        print(f'name = {self.name}, age = {self.age},\ gender = {self.gender}, residence = {self.residence}')
    def study(self):
        print('student can study...')
