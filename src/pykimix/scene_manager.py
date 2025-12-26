class Scene:
    def update(self, dt):
        pass

    def render(self, canvas):
        pass

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def set_scene(self, name):
        self.current = self.scenes.get(name)

    def run_tick(self, canvas, dt):
        if self.current:
            self.current.update(dt)
            self.current.render(canvas)