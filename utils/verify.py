import ddddocr

class getcode():

    def __init__(self,res):
        self.res = res
    
    def get_photo(self):
        try:
            with open('./img/verify.png', 'wb') as f:
                f.write(self.res)
            return True

        except Exception as e:
            print(e)
            return False

    def parse(self):
        ocr = ddddocr.DdddOcr(show_ad=False,old=True)
        with open('./img/verify.png', 'rb') as f:
            image = f.read()
        res = ocr.classification(image)
        print('验证码识别结果：',res)
        return res
    
    def main(self):
        if self.get_photo():
            return self.parse()
        else:
            return False


if __name__ == '__main__':
    getcode().main()