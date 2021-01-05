from runner.test_runner import TestRunner

class Main:
    
    def start(self):
        TestRunner().runner()

if __name__ == "__main__":
    '''整个自动化代码的入口'''
    Main().start()