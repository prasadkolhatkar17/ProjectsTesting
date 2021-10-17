class Functions:

    def __init__(self, driver):
        self.driver = driver

    def new_window(self, parentwin):
        chdwin = self.driver.window_handles
        for w in chdwin:
            if w != parentwin:
                self.win_switch(w)
                break

    def win_switch(self, new_win):
        new = self.driver.switch_to.window(new_win)
