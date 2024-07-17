from manim import *


class Besizer(Scene):

    def dot(self, arr:tuple[float, float, float], label: str):
        g = Group()
        p = Dot(arr, stroke_width=10).set_color(BLACK)
        l = MathTex(label).set_color(BLACK)
        l.next_to(p, RIGHT)
        g.add(p)
        g.add(l)
        return g

    def construct(self):
        self.camera.background_color = WHITE
        count = 15
        self.camera.frame_center = [2, 2, 0]
        pts1 = [np.array([-2, 3.5]), np.array([0.5, 0.5]), np.array([5, 0.5])]
        for i, it in enumerate(pts1):
            self.play(FadeIn(self.dot([it[0], it[1], 0], 'P_{'+str(i+1)+'}')))
        self.wait(1)
        group = Group()
        origin = self.dot([0, 0, 0], 'O')
        group.add(origin)
        self.play(FadeIn(origin))
        for it in pts1:
            v_obj = Vector(it).set_color(DARK_GRAY)
            group.add(v_obj)
            self.play(FadeIn(v_obj))
        pts2 = []
        for i in range(count+1):
            s = 1- i / count
            pts2.append(pts1[0]*s+pts1[1]*(1-s))
        for it in pts2:
            v_obj = Vector(it, stroke_width=1).set_color(RED_A)
            group.add(v_obj)
            self.play(FadeIn(v_obj, run_time=0.1))
        pts3 = []
        for i in range(count+1):
            s = 1-i / count
            pts3.append(pts1[1]*s+pts1[2]*(1-s))
        for it in pts3:
            v_obj = Vector(it, stroke_width=1).set_color(RED_A)
            group.add(v_obj)
            self.play(FadeIn(v_obj, run_time=0.1))
        pts4 = []
        for i in range(count+1):
            s = 1-i / count
            pts4.append(pts2[i]*s+pts3[i]*(1-s))
        pre = None
        for it in pts4:
            v_obj = Vector(it, stroke_width=1).set_color(RED_B)
            group.add(v_obj)
            self.play(FadeIn(v_obj, run_time=0.1))
            if pre:
                self.add(Line(pre, [it[0], it[1], 0]).set_color(RED))
            pre = [it[0], it[1], 0]
        self.play(FadeOut(group))
        self.wait(3)
    


            
        