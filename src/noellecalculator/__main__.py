from noellecalculator.app import main


if __name__ == '__main__':
    app = main()
    try:
        app.main_loop()
    except:
        pass
    
