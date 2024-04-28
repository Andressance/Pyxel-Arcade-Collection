


class ForceManager:
    def __init__(self,force:int, MAX_FORCE:int):
        self.force = force
        self.MAX_FORCE = MAX_FORCE

        self.frame_count = 0

    def update(self, force:int):
        self.force = force
        self.manage_force()
        return self.force
    
    def manage_force(self):
        self.frame_count += 1

        if self.frame_count > 120:
            self.force += 5
            self.frame_count = 0

        if self.force < 0:
            self.force = 0

        if self.force > self.MAX_FORCE:
            self.force = self.MAX_FORCE